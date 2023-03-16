from flask import jsonify
import pytest
import json

from flaskr import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "DATABASE": 'mock'
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_get_survey_template_1(client):
  expected = b'{"questions":[{"question":"test question one","type":"freetext"},{"answer_choices":["test answer one","test answer two","test answer three"],"question":"test question two","type":"singleselect"}],"title":"test_template_one"}\n'

  response = client.get("/get-survey-template?title=test_template_one")

  assert response.status_code == 200
  assert response.data == expected

def test_get_survey_template_2(client):
  expected = b'{"questions":[{"question":"Do you know the muffin man?","type":"freetext"},{"answer_choices":["Cinderella","Snow White","Princess Fiona"],"question":"The best bacholerettes are:","type":"multiselect"}],"title":"test_template_two"}\n'

  response = client.get("/get-survey-template?title=test_template_two")

  assert response.status_code == 200
  assert response.data == expected

def test_get_incomplete_survey(client):
  expected = b'{"questions":[{"answer":"test answer one","question":"test question one","type":"freetext"},{"answer_choices":["test answer one","test answer two","test answer three"],"question":"test question two","selected_answer":"test answer one","type":"singleselect"}],"submitted":false,"title":"test_incomplete_survey"}\n'

  response = client.get("/get-survey?username=test_username&title=test_incomplete_survey")

  assert response.status_code == 200
  assert response.data == expected

def test_get_submitted_survey(client):
    expected = b'{"questions":[{"answer":"test answer one","question":"test question one","type":"freetext"},{"answer_choices":["test answer one","test answer two","test answer three"],"question":"test question two","selected_answer":"test answer one","type":"singleselect"}],"submitted":true,"title":"test_submitted_survey"}\n'

    response = client.get("/get-survey?username=test_username&title=test_submitted_survey")

    assert response.status_code == 200
    assert response.data == expected

def test_create_survey_template(client):
  expected = b'{"questions":[{"question":"test question one","type":"freetext"},{"answer_choices":["test answer one","test answer two","test answer three"],"question":"test question two","type":"singleselect"}],"title":"test_created_template"}\n'

  headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  },

  data = {
    "questions": [
      {
        "question": "test question one",
        "type": "freetext"
      },
      {
        "answer_choices": [
          "test answer one",
          "test answer two",
          "test answer three"
        ],
        "question": "test question two",
        "type": "singleselect"
      }
    ],
    "title": "test_created_template"
  }

  create_response = client.post("/create-survey-template", data=json.dumps(data), headers=headers)
  get_response = client.get("/get-survey-template?title=test_created_template")

  assert create_response.status_code == 200
  assert create_response.data == b'{"message":"Data processed successfully"}\n'
  assert get_response.status_code == 200
  assert get_response.data == expected

def test_edit_survey(client):
  expected = b'{"questions":[{"answer":"test edited answer","question":"test question one","type":"freetext"},{"answer_choices":["test answer one","test answer two","test answer three"],"question":"test question two","selected_answer":"test answer two","type":"singleselect"}],"submitted":false,"title":"test_incomplete_survey"}\n'

  headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  },

  data = {
    "questions": [
      {
          "type": "freetext",
          "question": "test question one",
          "answer": "test edited answer"
      },
      {
          "type": "singleselect",
          "question": "test question two",
          "answer_choices": [
              "test answer one",
              "test answer two",
              "test answer three"
          ],
          "selected_answer": "test answer two"
      },
    ],
  }

  edit_response = client.post("/edit-survey?username=test_username&title=test_incomplete_survey", data=json.dumps(data), headers=headers)
  get_response = client.get("/get-survey?username=test_username&title=test_incomplete_survey")

  assert edit_response.status_code == 200
  assert edit_response.data == b'{"message":"Data processed successfully"}\n'
  assert get_response.status_code == 200
  assert get_response.data == expected