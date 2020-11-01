"""Defines API classes"""

import logging
import time
from typing import Dict, Optional

import requests

from .constants import champion_names

logger = logging.getLogger(__name__)


class API:
    @staticmethod
    def _call(url: str) -> requests.Response:
        """Gets a reponse from the API and handles not ok response codes.

        Parameters
        ----------
        url : str
            url to request

        Returns
        -------
        requests.Response
            A response object from the requests library
        """

        attempts = 0
        while attempts < 3:
            try:
                response = requests.get(url)
                response.raise_for_status()
                break
            except requests.HTTPError:
                logger.debug(
                    f"{url} gives status code:"
                    f" {response.status_code}, attempt: {attempts + 1}"
                )
                attempts += 1
                time.sleep(5)
        return response


class Riot(API):
    """Connector for the Riot API"""

    def __init__(self, key: str):
        self.key = key
        self._champions = None

    def region(self, region: str):
        self.base_url = f"https://{region}.api.riotgames.com/lol/"
        return self

    def get_player_from_name(self, summoner_name: str) -> dict:
        end_point = f"summoner/v4/summoners/by-name/{summoner_name}?api_key={self.key}"
        data = self._call(self.base_url + end_point).json()
        return data

    def get_role(self):
        # TODO
        pass

    def get_rank(self):
        # TODO
        pass

    def get_mastery(
        self, summoner_id: str, nchamps: Optional[int] = None
    ) -> Dict[str, int]:
        """Request mastery points by champion for the given summoner.

        Parameters
        ----------
        summoner_id : str
            Summoner ID associated with the player
        nchamps : int, optional
            Number of champions to return, by default all champions are returned.

        Returns
        -------
        Dict[str, int]
            Masteries for the given summoner sorted by mastery points descending
            the key is the champion name and the value is the mastery points.
        """
        end_point = f"{self.base_url}champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}?api_key={self.key}"
        response = self._call(end_point).json()

        if nchamps is not None:
            response = response[:nchamps]

        masteries = {
            champion_names.get(row["championId"]): row["championPoints"]
            for row in response
        }
        return masteries

    def get_history(self):
        # TODO
        pass
