"""Defines API classes"""

import logging
import time

import requests

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

    def region(self, region: str):
        self.base_url = f"https://{region}.api.riotgames.com/lol/league/v4"
        return self

    def get_player_from_name(self, summoner_name: str) -> dict:
        end_point = f"/lol/summoner/v4/summoners/by-name/{summoner_name}"
        data = self._call(end_point).json()
        return data

    def get_role(self):
        # TODO
        pass

    def get_rank(self):
        # TODO
        pass

    def get_mastery(self):
        # TODO
        pass

    def get_history(self):
        # TODO
        pass


class FakeRiot(API):
    """Fakes the riot API for the purposes of testing"""

    # TODO

    def get_historic_soloq(self):
        # TODO
        pass

    def get_side(self):
        # TODO
        pass

    def get_role(self):
        # TODO
        pass

    def get_rank(self):
        # TODO
        pass

    def get_history(self):
        # TODO
        pass
