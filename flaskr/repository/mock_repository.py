from interface import implements

from flaskr.repository.repo_interface import RepoInterface
from .mock_data import mock_data

class MockRepository(implements(RepoInterface)):
  def __init__(self) -> None:
    self.document = mock_data

  def get_survey_data(self):
    return self.document

  def create_survey_template(self, survey_with_added_template):
    self.document = survey_with_added_template
    pass

  def edit_survey(self, editted_survey_data):
    self.document = editted_survey_data
    pass