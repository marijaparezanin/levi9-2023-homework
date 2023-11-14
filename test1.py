import unittest
from main import load_CSV, calculate_player_stats, players_App

class TestPlayerStats(unittest.TestCase):

    def setUp(self):
        self.app = players_App.test_client()

    def test_load_CSV(self):
        result = load_CSV("files/L9HomeworkChallengePlayersInput.csv")
        self.assertIsInstance(result, dict)
        # Add more assertions based on your specific requirements

    def test_calculate_player_stats(self):
        # Write test cases for the calculate_player_stats function
        # Ensure that the function returns the expected results for different input scenarios
        players = load_CSV("files/L9HomeworkChallengePlayersInput.csv")

        player_name = "Tunde Nathi"
        result = calculate_player_stats(players[player_name])
        '''expected = {
            "advanced": {
                "effectiveFieldGoalPercentage": 93.75,
                "hollingerAssistRatio": 5.843681519357195,
                "trueShootingPercentage": 90.67579127459366,
                "valorization": 28.5
            },
            "gamesPlayed": 2,
            "playerName": "Tunde Nathi",
            "traditional": {
                "assists": 1.0,
                "blocks": 1.5,
                "freeThrows": {
                    "attempts": 5.5,
                    "made": 4.0,
                    "shootingPercentage": 72.72727272727273
                },
                "points": 26.5,
                "rebounds": 5.5,
                "steals": 0.0,
                "threePoints": [
                    {
                        "attempts": 6.0,
                        "made": 4.5,
                        "shootingPercentage": 75.0
                    }
                ],
                "turnovers": 1.5,
                "twoPoints": [
                    {
                        "attempts": 6.0,
                        "made": 4.5,
                        "shootingPercentage": 75.0
                    }
                ]
            }
        }'''
        expected = {}
        #self.assertIsInstance(result, expected)
        # Add more assertions based on your specific requirements

    def test_get_player_stats(self):
        # Write test cases for the get_player_stats route
        # Ensure that the endpoint returns the expected JSON response for different scenarios
        response = self.app.get('/stats/player/Nkosinathi Cyprian')
        self.assertEqual(response.status_code, 200)
        #self.assertIsInstance(response.json, dict)
        # Add more assertions based on your specific requirements

    def test_get_player_stats_not_found(self):
        # Write a test case for the scenario where the player is not found
        response = self.app.get('/stats/player/Nonexistent Player')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['error'], 'Player not found')

if __name__ == '__main__':
    unittest.main()
