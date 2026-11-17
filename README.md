# MedRec — Medical Recommendation System

An end-to-end machine learning web application that predicts a probable disease from a set of user-selected symptoms and returns structured guidance: a description of the condition, recommended medications, precautions, dietary advice, and suggested workouts.

> **Final solo college project — 2025.**

---

## Overview

MedRec combines a **Supervised Machine Learning** model (Support Vector Classifier) with a **Flask REST API** and a **Vue 3** single-page front end. The user selects symptoms, the front end sends them to the API, and the API returns a predicted condition along with supporting medical guidance sourced from curated datasets.

The system is built as a full stack project: model training and serving on the backend, a responsive and accessible interface on the frontend.

---

## Features

- **Symptom-based prediction** across **41 diseases** using **132 binary symptom features**.
- **Quick-select common symptoms** plus full searchable symptom list.
- **Structured results**: description, medications, precautions, diet, and workout recommendations.
- **REST API** (`/recommend`) for programmatic access, consumed by the Vue frontend.
- **Server-rendered fallback UI** (Flask + Jinja templates) with optional **speech recognition** input for symptoms.
- **Animated analysis progress** and a clean, responsive interface.
- **Standalone authentication pages** (login / register) included as UI templates.

---

## Tech Stack

**Backend**
- Python 3
- Flask & Flask-CORS
- pandas, NumPy
- scikit-learn (Support Vector Classifier)

**Frontend**
- Vue 3 (Composition API) + Vite
- Element Plus
- Axios
- Pinia & Vue Router (available in dependencies)

**Machine Learning**
- scikit-learn `SVC(kernel='linear')`
- `LabelEncoder` for disease labels
- Persisted with `pickle`

---

## Project Structure

```
.
├── main.py                                  # Flask application & prediction API
├── Medicine Recommendation System.ipynb     # Model training & experimentation notebook
├── datasets/                                # Symptom, disease & recommendation data (CSV)
│   ├── Training.csv                         # 4,920 symptom–disease records (132 features)
│   ├── Training_cleaned.csv                 # Cleaned subset (304 records)
│   ├── Symptom-severity.csv                 # Symptom severity weights (133 rows)
│   ├── description.csv                      # Disease descriptions (41)
│   ├── medications.csv                      # Medications per disease (41)
│   ├── precautions_df.csv                   # Precautions per disease (41)
│   ├── diets.csv                            # Diet recommendations (41)
│   ├── workout_df.csv                       # Diet tips & workouts
│   └── symptoms_df.csv                      # Symptom listings per disease
├── models/
│   ├── svc.pkl                              # Trained Support Vector Classifier
│   └── label_encoder.pkl                    # Fitted LabelEncoder (41 classes)
├── templates/                               # Jinja2 templates (server-rendered UI)
│   ├── index.html                           # Symptom input & results page
│   ├── about.html  blog.html  contact.html  developer.html  result.html
├── static/                                  # Static assets (CSS, images)
├── frontend/                                # Vue 3 + Vite single-page application
│   ├── src/
│   │   ├── App.vue                          # Root component & page routing
│   │   ├── main.js                          # App bootstrap
│   │   ├── components/                      # Header, footer, symptom selector, results
│   │   └── views/                           # Home, About, How It Works, Contact
│   ├── index.html
│   └── package.json
├── login.html  register.html  styles.css    # Standalone auth UI templates
├── mypy.ini                                 # Static type-checking configuration
└── medicine-recommendation-system.code-workspace
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 18+ and npm

### 1. Backend (Flask API)

From the project root:

```bash
python -m pip install flask flask-cors pandas numpy scikit-learn
python main.py
```

The API runs at **http://localhost:5000**.

### 2. Frontend (Vue SPA)

```bash
cd frontend
npm install
npm run dev
```

The app runs at **http://localhost:5173** and communicates with the backend at `http://localhost:5000`.

> Both servers must run at the same time for the full experience.

---

## API Reference

| Method | Endpoint     | Description                                       |
|--------|--------------|---------------------------------------------------|
| `GET`  | `/`          | Server-rendered home page (symptom input).        |
| `POST` | `/predict`   | Form-based prediction; renders results in the page. |
| `POST` | `/recommend` | JSON API used by the frontend.                    |
| `GET`  | `/about`     | About page.                                       |
| `GET`  | `/contact`   | Contact page.                                     |
| `GET`  | `/developer` | Developer page.                                   |
| `GET`  | `/blog`      | Blog page.                                        |

### Example — `POST /recommend`

**Request**

```json
{
  "symptoms": "itching, skin_rash, nodal_skin_eruptions"
}
```

**Response**

```json
{
  "disease": "Fungal infection",
  "description": "Fungal infection is a common skin condition caused by fungi.",
  "precautions": ["bath twice", "use detol or neem in bathing water", "keep infected area dry", "use clean cloths"],
  "recommendations": [
    {
      "name": "Antifungal Cream",
      "dosage": "Consult your doctor for proper dosage",
      "side_effects": "Consult your doctor for potential side effects",
      "precautions": "Consult your doctor for specific precautions"
    }
  ],
  "diet": ["Consume probiotics", "Stay hydrated", "Consume green tea"],
  "workout": ["Light stretching", "Yoga for relaxation"]
}
```

---

## How It Works

1. **Data preparation** — Raw symptom–disease records (`datasets/Training.csv`, 132 symptom features) are cleaned and encoded.
2. **Training** — Disease labels are encoded with `LabelEncoder`; a linear-kernel `SVC` is trained to map a 132-dimensional binary symptom vector to one of 41 diseases. The full pipeline is documented in `Medicine Recommendation System.ipynb`.
3. **Serving** — The trained model and label encoder are persisted to `models/` and loaded by the Flask app.
4. **Inference** — For each request, a 132-length binary vector is constructed from the user's symptoms and passed to the model; the predicted class is mapped back to a disease name.
5. **Recommendation lookup** — The predicted disease is used to join the description, medications, precautions, diet, and workout datasets, which are returned to the client.

> The training notebook reports **100% accuracy on the held-out split of the provided dataset**. As the dataset is limited in size and scope, this figure should be interpreted as dataset-specific and is **not** a measure of clinical performance.

---

## Disclaimer

This project is developed for **educational purposes only**. It is not a medical device and must not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider regarding any medical condition. Medication dosage, side effects, and precautions are intentionally left for a physician to determine.

---

## Author

**Pramish Sharma**
GitHub: [@spramish](https://github.com/spramish)

---

## License

Developed as an academic project. Please credit the author if you reuse or reference this work.
