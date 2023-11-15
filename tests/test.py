import unittest, sys, os
#because the folder is above
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import players_App

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = players_App.test_client()

    def test_player_found(self):
        response = self.app.get('/stats/player/Nkosinathi Cyprian')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['playerName'], 'Nkosinathi Cyprian')

    def test_player_not_found(self):
        response = self.app.get('/stats/player/Nonexistent_Player')
        data = response.get_json()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['error'], 'Player not found')

    def test_player_advanced(self):
        response = self.app.get('/stats/player/Nkosinathi Cyprian')
        data = response.get_json()

        expected_advanced = {'effectiveFieldGoalPercentage': 23.8, 
                             'hollingerAssistRatio': 6.6, 
                             'trueShootingPercentage': 25.7, 
                             'valorization': 2.0}
        self.assertEqual(data['advanced'], expected_advanced)

    def test_player_traditional(self):
        response = self.app.get('/stats/player/Jawara Mekonnen')
        data = response.get_json()

        expected_traditional = {'assists': 2.5, 
                             'blocks': 0.5, 
                             'freeThrows': {'attempts': 1.5, 
                                            'made': 1.5, 
                                            'shootingPercentage': 100.0}, 
                            'points': 13.0, 
                            'rebounds': 0.0, 
                            'steals': 1.0, 
                            'threePoints': [{'attempts': 1.5, 
                                             'made': 1.5, 
                                             'shootingPercentage': 100.0}], 
                            'turnovers': 0.5, 
                            'twoPoints':[{'attempts': 4.0, 
                                          'made': 3.5, 
                                          'shootingPercentage': 87.5}]}
        self.assertEqual(data['traditional'], expected_traditional)

    def test_player_games(self):
        response = self.app.get('/stats/player/Sifiso Abdalla')
        data = response.get_json()

        expected_games = 3
        self.assertEqual(data['gamesPlayed'], expected_games)


if __name__ == '__main__':
    unittest.main()
