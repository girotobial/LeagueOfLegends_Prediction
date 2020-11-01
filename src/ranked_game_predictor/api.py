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
        self.base_url = f"https://{region}.api.riotgames.com/lol/"
        return self

    def get_player_from_name(self, summoner_name: str) -> dict:
        end_point = (
            f"summoner/v4/summoners/by-name/{summoner_name}" f"?api_key={self.key}"
        )
        data = self._call(self.base_url + end_point).json()
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

    def __init__(self, key: str):
        self.key = key

    def region(self, region: str):
        return self

    def get_player_from_name(self, summoner_name: str) -> dict:
        response = dict(
            accountId="0" * 56,
            profileIconId=1,
            revisionDate=1604187079,
            name=summoner_name,
            id="1" * 63,
            puuid="2" * 78,
            summonerLevel=30,
        )
        return response

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
