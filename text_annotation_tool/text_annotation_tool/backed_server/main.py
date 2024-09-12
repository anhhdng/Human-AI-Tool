from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from typing import List
import os

app = FastAPI()

# Path to the folder containing text files
TEXT_FILES_FOLDER = 'sent_annot/backed_server/text_data/'
# cwd = os.getcwd()
# print(cwd)
class TextData(BaseModel):
    filename: str
    content: str

@app.get("/files")
async def list_files():
    cwd = os.getcwd()
    print(cwd)
    data_dir = os.path.join(cwd,TEXT_FILES_FOLDER)
    files = [f for f in os.listdir(data_dir) if f.endswith('.txt')]
    return {"files": files}

@app.get("/file/{filename}", response_model=TextData)
async def get_file_content(filename: str):
    filepath = os.path.join(TEXT_FILES_FOLDER, filename)
    print(filepath)
    with open(filepath, 'r') as file:
        content = file.read()
    return {"filename": filename, "content": content}

# Example DataFrame (replace with your real data)
data = {
    'text': [
        "Patient exhibits symptoms of depression and anxiety.",
        "Diagnosed with type 2 diabetes mellitus.",
        "Severe acute respiratory syndrome.",
        "Hypertensive heart disease with heart failure.",
        "Chronic obstructive pulmonary disease with exacerbation."
    ],
    'icd10_code': [
        "F32",  # Major depressive disorder
        "E11",  # Type 2 diabetes mellitus
        "U07.1",  # COVID-19, virus identified
        "I11.0",  # Hypertensive heart disease with heart failure
        "J44.1"  # Chronic obstructive pulmonary disease
    ]
}
df = pd.DataFrame(data)

class TextData(BaseModel):
    text: str
    icd10_code: str

@app.get("/text/{index}", response_model=TextData)
async def get_text(index: int):
    if index >= len(df):
        return {"text": "", "icd10_code": ""}
    row = df.iloc[index]
    return {"text": row['text'], "icd10_code": row['icd10_code']}

class Annotation(BaseModel):
    sentence: str
    suicide_class: str
    icd10_code: str
    team_performance: str
    individual_performance: str
    workload: str
    trust: str
    situation_awareness: str
    team_coordination: str
    individual_mental_model: str
    shared_mental_model: str

class AnnotationData(BaseModel):
    sentences: list
    highlighted_text: list
    suicide_class: str
    annotated_html: str
    actions: list
    feedback: str

@app.post("/annotate")
async def annotate(data: AnnotationData):
    # Save actions and feedback to CSV
    actions_df = pd.DataFrame(data.actions)
    actions_df.to_csv('user_actions.csv', mode='a', header=False, index=False)
    
    feedback_df = pd.DataFrame([{'feedback': data.feedback}], index=[0])
    feedback_df.to_csv('user_feedback.csv', mode='a', header=False, index=False)
    
    # Further processing of annotation data
    return {"message": "Annotation data received"}

@app.post("/save_annotations/")
def save_annotations(annotations: List[Annotation]):
    # Load existing data if exists
    try:
        df = pd.read_csv('annotations.csv')
    except FileNotFoundError:
        df = pd.DataFrame()

    # Convert annotations to DataFrame and append to the existing data
    new_data = pd.DataFrame([annotation.dict() for annotation in annotations])
    df = pd.concat([df, new_data], ignore_index=True)

    # Save to CSV
    df.to_csv('annotations.csv', index=False)
    return {"message": "Annotations saved successfully"}

@app.get("/annotations/")
def get_annotations():
    try:
        df = pd.read_csv('annotations.csv')
        return df.to_dict(orient='records')
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="No annotations found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
