from flask import Flask, render_template, request, jsonify
import requests
import pickle

app = Flask(__name__)

# Load the ICD-10 model (assuming it's a pre-trained model)
# with open('models/icd10_model.pkl', 'rb') as f:
#     icd10_model = pickle.load(f)

# Route to display the annotation interface
@app.route('/')
def index():
    return render_template('index_v5.html')

# Route to handle text annotation and variable capture
@app.route('/annotate', methods=['POST'])
def annotate_text():
    data = request.json
    sentences = data['sentences']
    
    annotations = []
    for sentence in sentences:
        # Here you would implement the logic to detect suicide ideation/attempt and ICD-10 code
        # icd10_code = detect_icd10_code(sentence)
        icd10_code = ''
        annotations.append({
            'sentence': sentence,
            'suicide_class': data.get('suicide_class', ''),
            'icd10_code': icd10_code,
            'team_performance': data.get('team_performance', ''),
            'individual_performance': data.get('individual_performance', ''),
            'workload': data.get('workload', ''),
            'trust': data.get('trust', ''),
            'situation_awareness': data.get('situation_awareness', ''),
            'team_coordination': data.get('team_coordination', ''),
            'individual_mental_model': data.get('individual_mental_model', ''),
            'shared_mental_model': data.get('shared_mental_model', '')
        })

    # Send annotations to FastAPI backend
    response = requests.post('http://localhost:8000/save_annotations', json=annotations)
    return jsonify(response.json())

def detect_icd10_code(sentence):
    # Use the model to predict the ICD-10 code
    icd10_code = icd10_model.predict([sentence])[0]
    return icd10_code

if __name__ == '__main__':
    app.run(debug=True)
