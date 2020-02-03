import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import app
from models import Movie, Actor


class BaseTestCase(unittest.TestCase):
    """This class represents the casting agency test case"""

    
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.executive_producer_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5rTkVNa0l4T1VNMU5UVkRSRE13UXpoRE4wVTJNMEZHUWpVM1FrVkZPRUpDTVRoR05qUTBPUSJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob29wLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMjEyNTM1Mjc0NzUyMTY4Mjg3MyIsImF1ZCI6WyJjb2ZmZWVzaG9wIiwiaHR0cHM6Ly9jb2ZmZWVzaG9vcC5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTc5NjQwNTkzLCJleHAiOjE1Nzk3MjY5OTMsImF6cCI6IjJQNGFzRlREWEsyc0liRm9xZWhabXZqS0ZkckFqZ0JjIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.l8gqXNrCkCb18EcR-PSVseTB8z8OcmRtiXlTn7SVkAf4-p3TK5XSGKMILzlVOxlk01jW64RPVWyB5ljt6zCCfauJnM0WeS93t8---f1QKfpuEHmaFZPxw4iIhckZOw7VlqlUs26ZU9V9_ff5oj-2fuWLkIQugpYQqeUYbdIyeLajy-9DbxEqSA0M-tS2aHjkpNB3m5SEyVYHmhwGhre6h4SttKQyudj-G86RLSot_R1ogTkZcRm_tYHVx7X5FR7XJ5BQaYH0TWw8Y6U_Hm2KQUd5m1AGWE9RhL-jpshCXgzo9T3ftCLqePMsoZiWRl3oUjR-MZod2gifEivxJxh1oQ'
        self.casting_director_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5rTkVNa0l4T1VNMU5UVkRSRE13UXpoRE4wVTJNMEZHUWpVM1FrVkZPRUpDTVRoR05qUTBPUSJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob29wLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExNTA3MDY4MTYyOTQ2Mzg3NzY4NSIsImF1ZCI6WyJjb2ZmZWVzaG9wIiwiaHR0cHM6Ly9jb2ZmZWVzaG9vcC5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTc5NjQyNTExLCJleHAiOjE1Nzk3Mjg5MTEsImF6cCI6IjJQNGFzRlREWEsyc0liRm9xZWhabXZqS0ZkckFqZ0JjIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.54MFTblXtVluzYcRMZpWvWHZmG3CZl1l_-TW8wf77Q_XPPvw2IuqPYRZNeIrPewKflmJIncOWHM9ROV0GIvI0yv5nk3yqlXbayEjgf72_m7VDFwvCjrkh0FRviJvfcoRdxb-VTnLG0fYViHZNajMJlB0uyJyCfHhJvSuYYBnXVrSeTvAELQkIVwbk1CUZ3x8i6fQiBsjaphzwC9Sk8XK0Z1AnEH_txHlIPNyuxOsOtxGwetegOmIGvQ8oJ8syzYpiGcrmg5b9cOrwIEqRfiJ8cZE6bIEzvT6MiOsOw2YbdfGTcdmlvtSe4rvp-ewAHh6Qisdl3cKjQMrAJJQSwPB1g'

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_create_actors_with_casting_assistant_token_success(self):
        data = {
            'name': 'jenny',
            'age': '25',
            'gender': 'female'
        }
        response = self.client().post(
            '/actors/create',
            json=data, headers={
                "Authorization":
                    "Bearer {}".format(self.casting_director_token)
            })
        self.assertEqual(response.status_code, 201)

    def test_get_actors_success(self):

        response = self.client().get(
            '/actors',
            headers={
                "Authorization":
                    "Bearer {}".format(self.casting_director_token)
            }
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        
    def test_get_movies_success(self):

        response = self.client().get(
            '/movies',
            headers={
                "Authorization":
                    "Bearer {}".format(self.casting_director_token)
            }
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        
    def test_get_actors_success(self):

        response = self.client().get(
            '/actors',
            headers={
                "Authorization":
                    "Bearer {}".format(self.executive_producer_token)
            }
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_movies_with_no_permission_fails(self):
        response = self.client().delete(
            '/movies/1',
            headers={
                "Authorization":
                    "Bearer {}".format(self.casting_director_token)
            })
        self.assertEqual(response.status_code, 401)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()