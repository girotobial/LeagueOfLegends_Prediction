import unittest.mock as mock

import pytest


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.delattr("requests.sessions.Session.request")


@pytest.fixture
def mock_get(monkeypatch) -> mock.MagicMock:
    with monkeypatch.context() as m:
        mock_req = mock.MagicMock()
        m.setattr("requests.get", mock_req)
        m.setattr("requests.Response.raise_for_status", mock_req)

        yield mock_req


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
