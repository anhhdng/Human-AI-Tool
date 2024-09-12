
Project structure 
Sent_Annot
App Server -- Flask application
├── app.py  # Flask application|
├── static/
│   └── style.css  # CSS for the Flask frontend
├── templates/
│   └── index.html  # HTML template for the Flask frontend
Backend Server -- fast api applicaiton
backend_server/
│   ├── main.py  # FastAPI application
│   └── utils.py  # Utility functions for sentence segmentation
├── requirements.txt  # Project dependencies
└── README.md  # Project documentation



create virtual environment and then from terminal install 
pip install -r requirements.txt

activate your virtual environment

Run the backend server Applications
$uvicorn main:app --reload


Run flask front end
Flask frontend
python app.py

Test the Application
http://127.0.0.1:5000/





Summary: 
Flask serves as the frontend UI for user interactions.
FastAPI is the backend API for processing text data.
The application segments sentences and highlights them in the UI.

multiline -deselect highlight does not work properly.
select and deselect works only on sameline.

Testing the Updated Functionality

    Highlight Multiline Text: Drag to select text across multiple lines, ensuring the entire selection is highlighted.

    Deselect Text: Click the "Deselect" button located at the end of the highlighted text to remove the highlight.

    Navigate Files: Use the "Next" and "Previous" buttons to navigate between files and ensure that the content loads correctly with highlighted text maintained.



Logging Actions:

    Added the logAction function to record user interactions, such as highlighting or deselecting text, with a timestamp and details.

Highlight and Deselect:

    When highlighting text, logAction is called to record the action.
    When deselecting text, the deselectBtn click handler logs the action and updates the state.

Submit Annotation:

    The submit-annotation button now includes actions in the data sent to the server, capturing a history of user interactions.



Testing

    Provide Feedback: Check that user comments are captured and stored.
    Track Actions: Verify that user actions are logged correctly.
    Review Logs: Inspect the user_actions.csv and user_feedback.csv files to ensure data is recorded accurately.