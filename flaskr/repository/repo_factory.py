from flask import current_app

from flaskr.repository.repo_interface import RepoInterface
from flaskr.repository.firebase_repository import FirebaseRepository
from flaskr.repository.mock_repository import MockRepository

class RepoFactory:
    def create_db(self) -> RepoInterface:
        return MockRepository() if current_app.config['TESTING'] == True else FirebaseRepository('survey')