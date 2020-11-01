from typing import Dict, Optional


class FakeRiot:
    """Fakes the riot API for the purposes of testing"""

    def __init__(self, key: str):
        self.key = key

    def region(self, region: str):
        return self

    def get_player_from_name(self, summoner_name: str, nrows: int = None) -> dict:
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

    def get_mastery(
        self, summoner_id: str, nchamps: Optional[int] = None
    ) -> Dict[str, int]:
        response = {
            "Pyke": 9851,
            "Ryze": 4699,
            "Wukong": 4048,
            "LeBlanc": 3826,
            "Xayah": 3403,
            "Morgana": 3171,
            "Akali": 3137,
            "Ezreal": 3132,
            "Corki": 2826,
            "Lucian": 2539,
            "Ashe": 2486,
            "Irelia": 2270,
            "Caitlyn": 2246,
            "Viktor": 2225,
            "Brand": 2148,
            "Shen": 2118,
            "Gangplank": 2091,
            "Vladimir": 1984,
            "Nautilus": 1691,
            "Azir": 1689,
            "Galio": 1674,
            "Annie": 1645,
            "Shyvana": 1642,
            "Twitch": 1624,
            "Vayne": 1549,
            "Diana": 1538,
            "Taliyah": 1516,
            "Karma": 1510,
            "Swain": 1486,
            "Aatrox": 1474,
            "Kog'Maw": 1460,
            "Lux": 1419,
            "Yasuo": 1415,
            "Zed": 1324,
            "Darius": 1159,
            "Zac": 1080,
            "Kassadin": 1074,
            "Heimerdinger": 1054,
            "Cho'Gath": 1050,
            "Jhin": 1022,
            "Talon": 997,
            "DrMundo": 971,
            "Urgot": 958,
            "Sion": 898,
            "Yorick": 872,
            "Fiddlesticks": 871,
            "Varus": 849,
            "Mordekaiser": 842,
            "Kennen": 838,
            "Teemo": 815,
            "TwistedFate": 812,
            "Soraka": 748,
            "Neeko": 745,
            "Nidalee": 737,
            "Nocturne": 733,
            "Maokai": 731,
            "Rakan": 720,
            "Lulu": 718,
            "Jinx": 718,
            "Zoe": 717,
            "Amumu": 701,
            "Sivir": 651,
            "Orianna": 635,
            "MissFortune": 627,
            "Fiora": 617,
            "Taric": 616,
            "Sylas": 601,
            "Ahri": 560,
            "Graves": 519,
            "Nami": 496,
            "Malzahar": 473,
            "Shaco": 419,
            "Ornn": 334,
            "Veigar": 275,
            "Kalista": 185,
            "Fizz": 171,
            "Rumble": 155,
            "Karthus": 149,
            "Evelynn": 138,
            "Trundle": 137,
            "Elise": 120,
            "Qiyana": 118,
            "Hecarim": 116,
            "Skarner": 115,
            "Kha'Zix": 104,
            "Braum": 103,
            "Poppy": 102,
            "Sona": 100,
            "Ekko": 100,
            "Renekton": 96,
            "Kled": 94,
        }
        if nchamps is not None:
            response = dict(list(response.items())[:nchamps])
        return response

    def get_history(self):
        # TODO
        pass
