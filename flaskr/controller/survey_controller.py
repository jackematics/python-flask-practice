from flask import Blueprint, request, jsonify
import json

from flaskr.service.survey_service import SurveyService

bp = Blueprint('survey', __name__, url_prefix="")

@bp.route("/get-survey-template", methods=['GET'])
def get_survey_template():
  survey_service = SurveyService()
  return jsonify(survey_service.get_survey_template(request.args.get('title'))), 200

@bp.route("/create-survey-template", methods=['POST'])
def create_survey_template():
  survey_service = SurveyService()
  response = survey_service.create_survey_template(json.loads(request.get_data()))

  return response, 200

@bp.route("/edit-survey", methods=['POST'])
def edit_survey():
  username = request.args.get('username')
  title = request.args.get('title')
  editted_survey = json.loads(request.get_data())

  survey_service = SurveyService()
  response = survey_service.edit_survey(username, title, editted_survey)

  return response, 200

@bp.route("/get-survey", methods=['GET'])
def get_survey():
  survey_service = SurveyService()
  username = request.args.get('username')
  title = request.args.get('title')

  return jsonify(survey_service.get_survey(username, title)), 200


