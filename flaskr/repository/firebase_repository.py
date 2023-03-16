from firebase_admin import credentials, firestore, initialize_app, _apps
from interface import implements

from flaskr.repository.repo_interface import RepoInterface

class FirebaseRepository(implements(RepoInterface)):
    def __init__(self, collection: str):
      if not _apps:
          cred = credentials.Certificate('key.json')
          default_app = initialize_app(cred)

      db = firestore.client()
      self.survey_ref = db.collection(collection)
      self.id = 'zScoYmb5cN1am7TpRs6S'
      pass

    def get_survey_data(self):
        return self.survey_ref.document(self.id).get().to_dict()
    
    def create_survey_template(self, survey_with_added_template):
      self.survey_ref.document(self.id).set(survey_with_added_template)
      pass

    def edit_survey(self, editted_survey_data):
      self.survey_ref.document(self.id).update(editted_survey_data)
      pass

