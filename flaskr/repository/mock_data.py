mock_data = {
    "templates": [
      {
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
        "title": "test_template_one"
      },
      {
        "questions": [
          {
            "question": "Do you know the muffin man?",
            "type": "freetext"
          },
          {
            "answer_choices": [
              "Cinderella",
              "Snow White",
              "Princess Fiona"
            ],
            "question": "The best bacholerettes are:",
            "type": "multiselect"
          }
        ],
        "title": "test_template_two"
      }
    ],
    "users": [
      {
        "surveys": [
          {
            "title": "test_incomplete_survey",
            "questions": [
              {
                  "type": "freetext",
                  "question": "test question one",
                  "answer": "test answer one"
              },
              {
                  "type": "singleselect",
                  "question": "test question two",
                  "answer_choices": [
                      "test answer one",
                      "test answer two",
                      "test answer three"
                  ],
                  "selected_answer": "test answer one"
              },
            ],
            "submitted": False 
          },
          {
            "title": "test_submitted_survey",
            "questions": [
              {
                  "type": "freetext",
                  "question": "test question one",
                  "answer": "test answer one"
              },
              {
                  "type": "singleselect",
                  "question": "test question two",
                  "answer_choices": [
                      "test answer one",
                      "test answer two",
                      "test answer three"
                  ],
                  "selected_answer": "test answer one"
              },
            ],
            "submitted": True 
          }
        ],
        "username": "test_username"
      }
    ]
  }