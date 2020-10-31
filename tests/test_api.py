import pytest
import requests

from ranked_game_predictor.api import Riot


@pytest.fixture
def riot():
    return Riot("my-fake-key")


class TestRiot:
    def test_call(self, riot, mock_get):
        fake_url = "my_fake_url"
        riot._call(fake_url)
        requests.get.assert_called_with(fake_url)

    def test_call_checks_status(self, riot, mock_get):
        riot._call("fake_url")
        requests.Response.raise_for_status.assert_called

    def test_requires_key(self):
        with pytest.raises(TypeError):
            Riot()

    def test_region_requires_value(self, riot):
        with pytest.raises(TypeError):
            riot.region()

    def test_region_change(self, riot):
        test_string = "test-string"
        riot.region(test_string)
        assert test_string in riot.base_url

    def test_get_player_from_name_response(self, riot, mock_response_ok):
        assert riot.get_player_from_name("not a player") == {
            "mock_key": "mock_response"
        }

    def test_get_mastery_response(self, riot, mock_response_ok):
        assert riot.get_mastery("not a player") == {"mock_key": "mock_response"}

    def test_get_rank_response(self, riot, mock_response_ok):
        assert riot.get_rank("not a player") == {"mock_key": "mock_response"}

    def test_get_soloq_history_response(self, riot, mock_response_ok):
        assert riot.get_soloq_history("not a player") == {"mock_key": "mock_response"}
