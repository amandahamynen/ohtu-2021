import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_palauttaa_oikean_maaran_pelaajia(self):
        reader = PlayerReaderStub()
        lista_pelaajista = reader.get_players()
        self.assertAlmostEqual(5, len(lista_pelaajista))

    def test_loytaa_oikean_pelaajan_nimen_perusteella(self):
        nimi = self.statistics.search("Kurri").name
        oikea_vastaus = PlayerReaderStub().get_players()[2].name
        self.assertAlmostEqual(nimi, oikea_vastaus)

    def test_ei_loyda_pelaajaa_jota_ei_ole(self):
        nimi = self.statistics.search("EiOleOlemassa")
        self.assertAlmostEqual(nimi, None)

    def test_loytaa_saman_tiimin_pelaajat(self):
        tiimi = self.statistics.team("EDM")
        self.assertAlmostEqual(len(tiimi), 3)

    def test_loytaa_parhaimman_pelaajan(self):
        pelaaja = self.statistics.top_scorers(1)[0]
        self.assertAlmostEqual(pelaaja.name, "Gretzky")