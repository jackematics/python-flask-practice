from flaskr.repository.repo_factory import RepoFactory

class SurveyService:
  def __init__(self) -> None:
    repo_factory = RepoFactory()
    self.repo = repo_factory.create_db()
    pass

  def get_survey_data(self):
    return self.repo.get_survey_data()
  
  def get_survey_template(self, title: str):
    templates = self.get_survey_data()['templates']
    
    return next(
      (template for template in templates if template["title"] == title), 
      None
    )
  
  def create_survey_template(self, template):
    survey_data = self.repo.get_survey_data()
    survey_data['templates'].append(template)

    self.repo.create_survey_template(survey_data)

    return { 'message': 'Data processed successfully' }
  
  def get_survey(self, username: str, title: str):
    user_data = next(
      (user for user in self.get_survey_data()['users'] if user["username"] == username), 
      None
    )

    return next(
      (survey for survey in user_data['surveys'] if survey["title"] == title), 
      None
    )
  
  def edit_survey(self, username: str, title: str, editted_survey):
    survey_data = self.repo.get_survey_data()

    selected_user_index = next(
       (i for i, user in enumerate(survey_data['users']) if user['username'] == username), 
       None
    )
    survey_to_edit_index =  next(
       (i for i, survey in enumerate(survey_data['users'][selected_user_index]['surveys']) if survey['title'] == title), 
       None
    )
    survey_data['users'][selected_user_index]['surveys'][survey_to_edit_index]['questions'] = editted_survey['questions']

    self.repo.edit_survey(survey_data)
    
    return { 'message': 'Data processed successfully' }