from flask import Flask, render_template, request
import pandas as pd
import joblib
import sqlite3 
from datetime import datetime
app = Flask(__name__)
def init_db():
    conn = sqlite3.connect('patients.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id TEXT,
            result TEXT,
            time TEXT
        )
    ''')

    conn.commit()
    conn.close()
init_db()
# Load model files
model = joblib.load("fetal_model.pkl")
scaler = joblib.load("scaler.pkl")
features = joblib.load("features.pkl")

# Store patients
patients = []

@app.route('/')
def home():
    conn = sqlite3.connect('patients.db')
    c = conn.cursor()
    c.execute("SELECT patient_id, result, time FROM patients")
    data = c.fetchall()
    conn.close()

    patients = [{"patient_id": r[0], "result": r[1], "time": r[2]} for r in data]

    return render_template(
        'index.html',
        features=features,
        patients=patients,
        input_data={},
        patient_id=""
    )

@app.route('/history')
def history():
    conn = sqlite3.connect('patients.db')
    c = conn.cursor()
    c.execute("SELECT patient_id, result, time FROM patients")
    data = c.fetchall()
    conn.close()

    patients = [{"patient_id": r[0], "result": r[1], "time": r[2]} for r in data]

    return render_template('history.html', patients=patients)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        patient_id = request.form.get('patient_id')

        input_values = []
        input_data = {}

        # Collect inputs
        for feature in features:
            value = float(request.form[feature])
            input_values.append(value)
            input_data[feature] = value  

        # Convert to DataFrame
        input_df = pd.DataFrame([input_values], columns=features)

        # Scale
        scaled_input = scaler.transform(input_df)

        # Predict
        pred = model.predict(scaled_input)[0]

        # Map result
        result_map = {0: "NORMAL", 1: "SUSPECT", 2: "PATHOLOGICAL"}
        result = result_map[pred]

        # Recommendation
        if result == "NORMAL":
            recommendation = "Routine monitoring recommended."
        elif result == "SUSPECT":
            recommendation = "Close monitoring required."
        else:
            recommendation = "Immediate medical attention required!"

        # Store patient
        conn = sqlite3.connect('patients.db')
        c = conn.cursor()

        c.execute("INSERT INTO patients (patient_id, result, time) VALUES (?, ?, ?)", 
                (patient_id, result, datetime.now().strftime("%d-%m-%Y %I:%M %p")))

        conn.commit()
        conn.close()

        return render_template(
            'index.html',
            prediction=result,
            recommendation=recommendation,
            features=features,
            patients=patients,
            input_data=input_data,   
            patient_id=patient_id   
        )

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4040, debug=True)