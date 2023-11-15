import unittest, sys, os
#because the folder is above
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import players_App

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = players_App.test_client()

    def test_get_player_stats(self):
        response = self.app.get('/stats/player/Nkosinathi Cyprian')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['playerName'], 'Nkosinathi Cyprian')

    def test_player_not_found(self):
        response = self.app.get('/stats/player/Nonexistent_Player')
        data = response.get_json()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['error'], 'Player not found')

if __name__ == '__main__':
    unittest.main()
