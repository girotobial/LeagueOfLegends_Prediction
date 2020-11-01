import unittest.mock as mock

import pytest
import requests


@pytest.fixture
def mock_get(monkeypatch) -> mock.MagicMock:
    with monkeypatch.context() as m:
        mock_req = mock.MagicMock()
        m.setattr("requests.get", mock_req)
        m.setattr("requests.Response.raise_for_status", mock_req)

        yield mock_req


class MockResponse:
    def __init__(self, status_pass: bool):
        self.status_pass = status_pass

    def raise_for_status(self):
        if not self.status_pass:
            raise requests.HTTPError

    @staticmethod
    def json():
        return [
            {
                "summonerId": 1,
                "championId": 1,
                "championPoints": 1,
            }
        ]


@pytest.fixture
def mock_response_ok(monkeypatch):
    """
    Requests.get() mocked to return
    {
        "summonerId": 1,
        "championId": 1,
        "championPoints": 1,
    }
    """

    def mock_get(*args, **kwargs):
        return MockResponse(True)

    monkeypatch.setattr("requests.get", mock_get)


@pytest.fixture
def mock_response_fail(monkeypatch):
    """Requests.get() mocked to return response with failed status"""

    def mock_get(*args, **kwargs):
        return MockResponse(False)

    monkeypatch.setattr("request.get", mock_get)


class MockAPI:
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
