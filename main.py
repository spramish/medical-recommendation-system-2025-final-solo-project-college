"""Flask app for medicine recommendation based on symptoms."""

import pickle
from typing import List, Tuple

import pandas as pd
import numpy as np
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load datasets with error handling
try:
    sym_des = pd.read_csv(
        "datasets/symptoms_df.csv",
        encoding='utf-8',
        sep=',',
        skipinitialspace=True,
        on_bad_lines='skip'
    )
    precautions = pd.read_csv(
        "datasets/precautions_df.csv",
        encoding='utf-8',
        sep=',',
        skipinitialspace=True,
        on_bad_lines='skip'
    )
    workout = pd.read_csv(
        "datasets/workout_df.csv",
        header=None,
        names=['disease', 'diet_tips', 'workout'],
        encoding='utf-8',
        sep=',',
        skipinitialspace=True,
        on_bad_lines='skip'
    )
    description = pd.read_csv(
        "datasets/description.csv",
        encoding='utf-8',
        sep=',',
        skipinitialspace=True,
        on_bad_lines='skip'
    )
    medications = pd.read_csv(
        "datasets/medications.csv",
        encoding='utf-8',
        sep=',',
        skipinitialspace=True,
        on_bad_lines='skip'
    )
    diets = pd.read_csv(
        "datasets/diets.csv",
        encoding='utf-8',
        sep=',',
        skipinitialspace=True,
        on_bad_lines='skip'
    )
except FileNotFoundError as e:
    print(f"Error loading datasets: {e}")
    raise

# Load model
try:
    with open('models/svc.pkl', 'rb') as file:
        svc = pickle.load(file)
except FileNotFoundError as e:
    print(f"Error loading model: {e}")
    raise

# Define symptoms_dict and diseases_list
symptoms_dict = {
    'itching': 0, 'skin_rash': 1, 'nodal_skin_eruptions': 2,
    'continuous_sneezing': 3, 'shivering': 4, 'chills': 5, 'joint_pain': 6,
    'stomach_pain': 7, 'acidity': 8, 'ulcers_on_tongue': 9,
    'muscle_wasting': 10, 'vomiting': 11, 'burning_micturition': 12,
    'spotting_ urination': 13, 'fatigue': 14, 'weight_gain': 15,
    'anxiety': 16, 'cold_hands_and_feets': 17, 'mood_swings': 18,
    'weight_loss': 19, 'restlessness': 20, 'lethargy': 21,
    'patches_in_throat': 22, 'irregular_sugar_level': 23, 'cough': 24,
    'high_fever': 25, 'sunken_eyes': 26, 'breathlessness': 27,
    'sweating': 28, 'dehydration': 29, 'indigestion': 30, 'headache': 31,
    'yellowish_skin': 32, 'dark_urine': 33, 'nausea': 34,
    'loss_of_appetite': 35, 'pain_behind_the_eyes': 36, 'back_pain': 37,
    'constipation': 38, 'abdominal_pain': 39, 'diarrhoea': 40,
    'mild_fever': 41, 'yellow_urine': 42, 'yellowing_of_eyes': 43,
    'acute_liver_failure': 44, 'fluid_overload': 45,
    'swelling_of_stomach': 46, 'swelled_lymph_nodes': 47, 'malaise': 48,
    'blurred_and_distorted_vision': 49, 'phlegm': 50,
    'throat_irritation': 51, 'redness_of_eyes': 52, 'sinus_pressure': 53,
    'runny_nose': 54, 'congestion': 55, 'chest_pain': 56,
    'weakness_in_limbs': 57, 'fast_heart_rate': 58,
    'pain_during_bowel_movements': 59, 'pain_in_anal_region': 60,
    'bloody_stool': 61, 'irritation_in_anus': 62, 'neck_pain': 63,
    'dizziness': 64, 'cramps': 65, 'bruising': 66, 'obesity': 67,
    'swollen_legs': 68, 'swollen_blood_vessels': 69,
    'puffy_face_and_eyes': 70, 'enlarged_thyroid': 71, 'brittle_nails': 72,
    'swollen_extremeties': 73, 'excessive_hunger': 74,
    'extra_marital_contacts': 75, 'drying_and_tingling_lips': 76,
    'slurred_speech': 77, 'knee_pain': 78, 'hip_joint_pain': 79,
    'muscle_weakness': 80, 'stiff_neck': 81, 'swelling_joints': 82,
    'movement_stiffness': 83, 'spinning_movements': 84,
    'loss_of_balance': 85, 'unsteadiness': 86,
    'weakness_of_one_body_side': 87, 'loss_of_smell': 88,
    'bladder_discomfort': 89, 'foul_smell_of urine': 90,
    'continuous_feel_of_urine': 91, 'passage_of_gases': 92,
    'internal_itching': 93, 'toxic_look_(typhos)': 94, 'depression': 95,
    'irritability': 96, 'muscle_pain': 97, 'altered_sensorium': 98,
    'red_spots_over_body': 99, 'belly_pain': 100,
    'abnormal_menstruation': 101, 'dischromic _patches': 102,
    'watering_from_eyes': 103, 'increased_appetite': 104, 'polyuria': 105,
    'family_history': 106, 'mucoid_sputum': 107, 'rusty_sputum': 108,
    'lack_of_concentration': 109, 'visual_disturbances': 110,
    'receiving_blood_transfusion': 111,
    'receiving_unsterile_injections': 112, 'coma': 113,
    'stomach_bleeding': 114, 'distention_of_abdomen': 115,
    'history_of_alcohol_consumption': 116, 'fluid_overload.1': 117,
    'blood_in_sputum': 118, 'prominent_veins_on_calf': 119,
    'palpitations': 120, 'painful_walking': 121, 'pus_filled_pimples': 122,
    'blackheads': 123, 'scurring': 124, 'skin_peeling': 125,
    'silver_like_dusting': 126, 'small_dents_in_nails': 127,
    'inflammatory_nails': 128, 'blister': 129, 'red_sore_around_nose': 130,
    'yellow_crust_ooze': 131
}

diseases_list = {
    15: 'Fungal infection', 4: 'Allergy', 16: 'GERD',
    9: 'Chronic cholestasis', 14: 'Drug Reaction',
    33: 'Peptic ulcer disease', 1: 'AIDS', 12: 'Diabetes',
    17: 'Gastroenteritis', 6: 'Bronchial Asthma', 23: 'Hypertension',
    30: 'Migraine', 7: 'Cervical spondylosis',
    32: 'Paralysis (brain hemorrhage)', 28: 'Jaundice', 29: 'Malaria',
    8: 'Chicken pox', 11: 'Dengue', 37: 'Typhoid', 40: 'Hepatitis A',
    19: 'Hepatitis B', 20: 'Hepatitis C', 21: 'Hepatitis D',
    22: 'Hepatitis E', 3: 'Alcoholic hepatitis', 36: 'Tuberculosis',
    10: 'Common Cold', 34: 'Pneumonia',
    13: 'Dimorphic hemorrhoids (piles)', 18: 'Heart attack',
    39: 'Varicose veins', 26: 'Hypothyroidism', 24: 'Hyperthyroidism',
    25: 'Hypoglycemia', 31: 'Osteoarthritis', 5: 'Arthritis',
    0: '(vertigo) Paroxysmal Positional Vertigo', 2: 'Acne',
    38: 'Urinary tract infection', 35: 'Psoriasis', 27: 'Impetigo'
}

def helper(dis: str) -> Tuple[str, List[str], List[str], List[str], List[str]]:
    """Retrieve recommendations for a disease.

    Args:
        dis: Name of the predicted disease.

    Returns:
        Tuple of description, precautions, medications, diet, and workout.
    """
    try:
        print(f"Retrieving data for disease: {dis}")  # Debug log
        
        desc = description[description['Disease'] == dis]['Description'].iloc[0]
        desc = desc if pd.notna(desc) else "No description available"
        print(f"Description: {desc}")  # Debug log

        # Get precautions and filter out empty or NaN values
        pre = precautions[precautions['Disease'] == dis][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']].values
        print(f"Raw precautions: {pre}")  # Debug log
        
        if pre.size > 0:
            pre_list = [p for p in pre.tolist()[0] if pd.notna(p) and p.strip()]
            print(f"Filtered precautions: {pre_list}")  # Debug log
        else:
            pre_list = ["No precautions available"]
            print("No precautions found in database")  # Debug log

        med = medications[medications['Disease'] == dis]['Medication'].tolist()
        med = med if med else ["No medications available"]
        print(f"Medications: {med}")  # Debug log

        die = diets[diets['Disease'] == dis]['Diet'].tolist()
        die = die if die else ["No dietary recommendations available"]
        print(f"Diet: {die}")  # Debug log

        if 'diet_tips' in workout.columns:
            diet_tips = workout[workout['disease'] == dis]['diet_tips'].tolist()
            diet_tips = diet_tips if diet_tips else []
            die.extend(diet_tips)

        wrkout = workout[workout['disease'] == dis]['workout'].tolist()
        wrkout = wrkout if wrkout else ["No workout recommendations available"]
        print(f"Workout: {wrkout}")  # Debug log

        return desc, pre_list, med, die, wrkout
    except Exception as e:
        print(f"Error in helper for disease {dis}: {e}")
        return (
            "Error retrieving data",
            ["No precautions available"],
            ["No medications available"],
            ["No dietary recommendations available"],
            ["No workout recommendations available"]
        )

def get_predicted_value(patient_symptoms: List[str]) -> str:
    """Predict disease from symptoms.

    Args:
        patient_symptoms: List of user-provided symptoms.

    Returns:
        Predicted disease name or error message.
    """
    try:
        input_vector = pd.DataFrame(
            [[0] * len(symptoms_dict)],
            columns=list(symptoms_dict.keys())
        )

        valid_symptom_found = False
        for item in patient_symptoms:
            item = item.lower().strip().replace(" ", "_")  # Handle spaces in symptom names
            if item in symptoms_dict:
                input_vector[item] = 1
                valid_symptom_found = True
            else:
                print(f"Warning: Symptom '{item}' not found in symptoms_dict")

        if not valid_symptom_found:
            return (
                "Error: No valid symptoms provided. Please enter valid "
                "symptoms (e.g., itching, skin_rash)."
            )

        prediction = svc.predict(input_vector)[0]
        return diseases_list.get(prediction, "Unknown disease")
    except Exception as e:
        print(f"Error in prediction: {e}")
        return "Error predicting disease"

@app.route("/")
def index() -> str:
    """Render the home page."""
    return render_template("index.html")

@app.route('/predict', methods=['GET', 'POST'])
def home() -> str:
    """Handle symptom input and render results."""
    if request.method == 'POST':
        symptoms = request.form.get('symptoms', '')
        print("Received symptoms:", symptoms)

        # Process symptoms into a list
        user_symptoms = [s.strip() for s in symptoms.split(',') if s.strip()]
        print("Processed symptoms:", user_symptoms)

        # Check if the placeholder text "Symptoms" was submitted
        if not user_symptoms or all(s == "Symptoms" for s in user_symptoms):
            message = (
                "Error: No valid symptoms provided. Please enter valid "
                "symptoms (e.g., itching, skin_rash)."
            )
            return render_template('index.html', message=message)

        predicted_disease = get_predicted_value(user_symptoms)
        if predicted_disease in [
            "Error predicting disease",
            "Unknown disease",
            "Error: No valid symptoms provided. Please enter valid "
            "symptoms (e.g., itching, skin_rash)."
        ]:
            message = predicted_disease
            return render_template('index.html', message=message)

        dis_des, prec_list, med_list, diet_list, workout_list = helper(
            predicted_disease
        )
        valid_prec = [
            i for i in prec_list
            if pd.notna(i) and i != "No precautions available"
        ]
        valid_prec = valid_prec if valid_prec else ["No precautions available"]
        return render_template(
            'index.html',
            predicted_disease=predicted_disease,
            dis_des=dis_des,
            my_precautions=valid_prec,
            medications=med_list,
            my_diet=diet_list,
            workout=workout_list
        )
    return render_template('index.html')

@app.route('/about')
def about() -> str:
    """Render the about page."""
    return render_template("about.html")

@app.route('/contact')
def contact() -> str:
    """Render the contact page."""
    return render_template("contact.html")

@app.route('/developer')
def developer() -> str:
    """Render the developer page."""
    return render_template("developer.html")

@app.route('/blog')
def blog() -> str:
    """Render the blog page."""
    return render_template("blog.html")

@app.route('/recommend', methods=['POST'])
def recommend() -> dict:
    """API endpoint for medicine recommendations."""
    try:
        data = request.get_json()
        symptoms = data.get('symptoms', '')
        
        # Process symptoms into a list
        user_symptoms = [s.strip() for s in symptoms.split(',') if s.strip()]
        
        if not user_symptoms:
            return jsonify({
                'error': 'No symptoms provided'
            }), 400

        predicted_disease = get_predicted_value(user_symptoms)
        
        if predicted_disease.startswith('Error'):
            return jsonify({
                'error': predicted_disease
            }), 400

        desc, pre_list, med, die, wrkout = helper(predicted_disease)
        
        # Debug logging
        print("Predicted Disease:", predicted_disease)
        print("Precautions from helper:", pre_list)
        
        # Filter out empty or NaN precautions
        valid_precautions = [p for p in pre_list if pd.notna(p) and p.strip()]
        print("Valid precautions:", valid_precautions)
        
        recommendations = []
        for medication in med:
            recommendations.append({
                'name': medication,
                'dosage': 'Consult your doctor for proper dosage',
                'side_effects': 'Consult your doctor for potential side effects',
                'precautions': 'Consult your doctor for specific precautions'
            })

        response_data = {
            'disease': predicted_disease,
            'description': desc,
            'precautions': valid_precautions,
            'recommendations': recommendations,
            'diet': die,
            'workout': wrkout
        }
        
        print("Final response data:", response_data)
        return jsonify(response_data)

    except Exception as e:
        print("Error in recommend endpoint:", str(e))
        return jsonify({
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)