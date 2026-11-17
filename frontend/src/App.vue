<script setup>
import { ref, reactive, onMounted, computed } from 'vue'
import axios from 'axios'
import { ElMessage, ElLoading } from 'element-plus'
import AppHeader from './components/AppHeader.vue'
import AppFooter from './components/AppFooter.vue'
import SymptomSelector from './components/SymptomSelector.vue'
import DiseaseInfo from './components/DiseaseInfo.vue'
import MedicationList from './components/MedicationList.vue'
import About from './views/About.vue'
import HowItWorks from './views/HowItWorks.vue'
import Contact from './views/Contact.vue'

// Simple navigation system without Vue Router
const currentPage = ref('home')
const setCurrentPage = (page) => {
  currentPage.value = page
}

const API_BASE_URL = 'http://localhost:5000'
const loading = ref(false)
const recommendations = ref([])
const diseaseInfo = ref(null)
const showResults = ref(false)
const selectedSymptoms = ref([])
const analysisStage = ref(0) // 0: not started, 1: analyzing, 2: completed
const analysisProgress = ref(0)
const analysisMessages = [
  "Analyzing symptoms...",
  "Matching patterns in medical database...",
  "Identifying potential conditions...",
  "Determining recommended medications...",
  "Generating personalized health advice..."
]
const currentAnalysisMessage = ref(analysisMessages[0])

// Get all available symptoms from the backend
const allSymptoms = ref([])
const loadingSymptoms = ref(false)

onMounted(async () => {
  try {
    // In a real app, you would fetch this from an endpoint
    // For now, we'll use the symptoms from the Python code
    allSymptoms.value = Object.keys(symptoms_dict).map(symptom => ({
      value: symptom,
      label: symptom.replace(/_/g, ' ')
    }))
  } catch (error) {
    console.error('Error loading symptoms:', error)
    ElMessage.error('Failed to load symptoms list')
  } finally {
    loadingSymptoms.value = false
  }
})

// Symptoms dictionary from the Python code
const symptoms_dict = {
  'itching': 0, 'skin_rash': 1, 'nodal_skin_eruptions': 2,
  'continuous_sneezing': 3, 'shivering': 4, 'chills': 5, 'joint_pain': 6,
  'stomach_pain': 7, 'acidity': 8, 'ulcers_on_tongue': 9,
  'muscle_wasting': 10, 'vomiting': 11, 'burning_micturition': 12,
  'spotting_urination': 13, 'fatigue': 14, 'weight_gain': 15,
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
  'bladder_discomfort': 89, 'foul_smell_of_urine': 90,
  'continuous_feel_of_urine': 91, 'passage_of_gases': 92,
  'internal_itching': 93, 'toxic_look_(typhos)': 94, 'depression': 95,
  'irritability': 96, 'muscle_pain': 97, 'altered_sensorium': 98,
  'red_spots_over_body': 99, 'belly_pain': 100,
  'abnormal_menstruation': 101, 'dischromic_patches': 102,
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

// Common symptoms for quick selection
const commonSymptoms = [
  'itching', 'skin_rash', 'fever', 'headache', 'cough',
  'fatigue', 'nausea', 'dizziness', 'chest_pain', 'back_pain',
  'joint_pain', 'muscle_pain', 'abdominal_pain', 'vomiting',
  'diarrhoea', 'constipation', 'loss_of_appetite', 'weight_loss',
  'weight_gain', 'anxiety', 'depression', 'breathlessness'
]

const updateSelectedSymptoms = (symptoms) => {
  selectedSymptoms.value = symptoms
}

// For preview purposes, let's add a mock function that returns data without making an actual API call
const getMockRecommendations = () => {
  return {
    disease: "Common Cold",
    description: "The common cold is a viral infection of your nose and throat (upper respiratory tract). It's usually harmless, although it might not feel that way. Many types of viruses can cause a common cold.",
    recommendations: [
      {
        name: "Acetaminophen (Tylenol)",
        dosage: "325-650 mg every 4-6 hours as needed",
        side_effects: "Rare when taken as directed. May include nausea, stomach pain.",
        precautions: "Do not exceed 3,000 mg in 24 hours. Avoid alcohol."
      },
      {
        name: "Dextromethorphan (Robitussin)",
        dosage: "10-20 mg every 4 hours or 30 mg every 6-8 hours",
        side_effects: "Drowsiness, dizziness, mild stomach discomfort.",
        precautions: "Do not use with MAO inhibitors. Avoid alcohol."
      }
    ],
    diet: [
      "Stay hydrated with water, clear broths, and herbal tea",
      "Consume vitamin C rich foods like citrus fruits",
      "Eat honey to soothe sore throat (not for children under 1 year)",
      "Consume warm soups like chicken soup"
    ],
    workout: [
      "Rest is recommended during acute symptoms",
      "Light walking when feeling better",
      "Avoid strenuous exercise until fully recovered",
      "Gentle stretching may help relieve muscle tension"
    ]
  }
}

const runAnalysisAnimation = async () => {
  analysisStage.value = 1
  analysisProgress.value = 0
  
  // Simulate the analysis process with progress updates
  for (let i = 0; i <= 100; i += 5) {
    analysisProgress.value = i
    
    // Update the message at certain progress points
    if (i === 0) currentAnalysisMessage.value = analysisMessages[0]
    else if (i === 25) currentAnalysisMessage.value = analysisMessages[1]
    else if (i === 50) currentAnalysisMessage.value = analysisMessages[2]
    else if (i === 75) currentAnalysisMessage.value = analysisMessages[3]
    else if (i === 95) currentAnalysisMessage.value = analysisMessages[4]
    
    await new Promise(resolve => setTimeout(resolve, 100))
  }
  
  analysisStage.value = 2
}

const getRecommendations = async () => {
  if (selectedSymptoms.value.length === 0) {
    ElMessage.warning('Please select at least one symptom')
    return
  }

  loading.value = true
  
  try {
    // Run the analysis animation
    await runAnalysisAnimation()
    
    // Make the actual API call to the backend
    const response = await axios.post(`${API_BASE_URL}/recommend`, {
      symptoms: selectedSymptoms.value.join(', ')
    })
    
    if (response.data) {
      console.log('Backend response:', response.data) // Debug log
      
      // Process workout data to remove disease name and clean up formatting
      const processedWorkout = response.data.workout ? response.data.workout.map(item => {
        // Remove disease name and any leading/trailing whitespace
        const diseaseName = response.data.disease || '';
        return item.replace(new RegExp(`^${diseaseName}:\\s*`, 'i'), '')
                  .replace(new RegExp(`^${diseaseName}\\s*:\\s*`, 'i'), '')
                  .replace(new RegExp(`^${diseaseName}\\s*`, 'i'), '')
                  .replace(/^,\s*/, '') // Remove leading comma and any following whitespace
                  .trim();
      }) : [];

      // Debug log for precautions
      console.log('Raw precautions from backend:', response.data.precautions);

      // Update disease info with all available data
      diseaseInfo.value = {
        name: response.data.disease || 'Unknown',
        description: response.data.description || 'No description available',
        precautions: Array.isArray(response.data.precautions) ? response.data.precautions : [],
        diet: response.data.diet || [],
        workout: processedWorkout
      }

      // Debug log for processed disease info
      console.log('Processed disease info:', diseaseInfo.value);

      // Update recommendations with medications
      recommendations.value = response.data.recommendations ? response.data.recommendations.map(med => ({
        name: med.name || med,
        dosage: med.dosage || 'Consult your doctor for proper dosage',
        side_effects: med.side_effects || 'Consult your doctor for potential side effects',
        precautions: med.precautions || 'Consult your doctor for specific precautions'
      })) : [];

      showResults.value = true
      
      // Scroll to results
      setTimeout(() => {
        const resultsElement = document.getElementById('results-section')
        if (resultsElement) {
          resultsElement.scrollIntoView({ behavior: 'smooth' })
        }
      }, 100)
    } else {
      throw new Error('No data received from the server')
    }
  } catch (error) {
    console.error('Error getting recommendations:', error)
    ElMessage.error(error.response?.data?.error || 'Error analyzing symptoms. Please try again.')
  } finally {
    loading.value = false
  }
}

const resetForm = () => {
  selectedSymptoms.value = []
  recommendations.value = []
  diseaseInfo.value = null
  showResults.value = false
  analysisStage.value = 0
  analysisProgress.value = 0
}
</script>

<template>
  <div class="app-container">
    <AppHeader :current-page="currentPage" @navigate="setCurrentPage" />
    
    <main class="main-content">
      <!-- Home Page -->
      <div v-if="currentPage === 'home'">
        <div class="container">
          <!-- Symptom Selection Section -->
          <section class="section symptom-section">
            <div class="section-header">
              <h2>Symptom Analysis</h2>
              <p class="section-description">
                Select your symptoms to get personalized medical recommendations
              </p>
            </div>
            
            <div class="card">
              <SymptomSelector 
                :all-symptoms="allSymptoms" 
                :common-symptoms="commonSymptoms"
                :selected-symptoms="selectedSymptoms"
                :loading="loadingSymptoms"
                @update:selected-symptoms="updateSelectedSymptoms"
              />
              
              <div class="action-buttons">
                <el-button 
                  type="primary" 
                  size="large" 
                  @click="getRecommendations" 
                  :loading="loading"
                  :disabled="selectedSymptoms.length === 0"
                  class="analyze-button"
                >
                  <span class="button-icon">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path>
                      <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>
                    </svg>
                  </span>
                  Analyze Symptoms
                </el-button>
                <el-button 
                  type="default" 
                  size="large" 
                  @click="resetForm"
                  :disabled="selectedSymptoms.length === 0"
                  class="reset-button"
                >
                  <span class="button-icon">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"></path>
                      <path d="M3 3v5h5"></path>
                    </svg>
                  </span>
                  Reset
                </el-button>
              </div>
            </div>
          </section>
          
          <!-- Analysis Progress Section -->
          <section v-if="analysisStage === 1" class="section analysis-section">
            <div class="analysis-container">
              <div class="analysis-content">
                <div class="analysis-icon">
                  <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="analysis-pulse">
                    <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
                  </svg>
                </div>
                <h3>{{ currentAnalysisMessage }}</h3>
                <div class="progress-container">
                  <div class="progress-bar">
                    <div class="progress-fill" :style="{ width: `${analysisProgress}%` }"></div>
                  </div>
                  <div class="progress-text">{{ analysisProgress }}%</div>
                </div>
              </div>
            </div>
          </section>
          
          <!-- Results Section -->
          <section v-if="showResults" id="results-section" class="section results-section">
            <div class="section-header">
              <h2>Analysis Results</h2>
              <p class="section-description">
                Based on your symptoms, we've identified the following condition and recommendations
              </p>
            </div>
            
            <div class="results-container">
              <DiseaseInfo 
                v-if="diseaseInfo" 
                :disease-info="diseaseInfo" 
              />
              
              <MedicationList 
                v-if="recommendations.length > 0" 
                :medications="recommendations" 
              />
            </div>
            
            <div class="results-actions">
              <el-button type="primary" class="action-button">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                  <polyline points="7 10 12 15 17 10"></polyline>
                  <line x1="12" y1="15" x2="12" y2="3"></line>
                </svg>
                Download Report
              </el-button>
              <el-button type="default" class="action-button">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                  <circle cx="9" cy="7" r="4"></circle>
                  <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                  <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                </svg>
                Share with Doctor
              </el-button>
              <el-button type="success" class="action-button">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                  <line x1="8" y1="12" x2="16" y2="12"></line>
                  <line x1="12" y1="8" x2="12" y2="16"></line>
                </svg>
                Book Appointment
              </el-button>
            </div>
            
            <div class="disclaimer">
              <el-alert
                title="Medical Disclaimer"
                type="warning"
                description="This information is provided for educational purposes only and is not intended to be a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition."
                show-icon
                :closable="false"
              />
            </div>
          </section>
        </div>
      </div>
      
      <!-- About Page -->
      <About v-else-if="currentPage === 'about'" />
      
      <!-- How It Works Page -->
      <HowItWorks v-else-if="currentPage === 'how-it-works'" />
      
      <!-- Contact Page -->
      <Contact v-else-if="currentPage === 'contact'" />
    </main>
    
    <AppFooter />
  </div>
</template>

<style>
:root {
  --primary-color: #3a86ff;
  --primary-light: #e0ecff;
  --primary-dark: #2667cc;
  --secondary-color: #00b4d8;
  --secondary-light: #e3faff;
  --secondary-dark: #0096b2;
  --accent-color: #ff6b6b;
  --accent-light: #ffebeb;
  --text-color: #2d3748;
  --text-light: #718096;
  --background-color: #f7fafc;
  --card-color: #ffffff;
  --border-color: #e2e8f0;
  --shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.03);
  --shadow-hover: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
  --border-radius: 12px;
  --transition: all 0.3s ease;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  color: var(--text-color);
  background-color: var(--background-color);
  line-height: 1.6;
}

.app-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.main-content {
  flex: 1;
  padding: 3rem 0;
  background-image: linear-gradient(to bottom, #f7fafc, #edf2f7);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

.section {
  margin-bottom: 4rem;
  animation: fadeIn 0.8s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.section-header {
  margin-bottom: 2rem;
  text-align: center;
}

.section-header h2 {
  font-size: 2.25rem;
  color: var(--primary-dark);
  margin-bottom: 0.75rem;
  position: relative;
  display: inline-block;
}

.section-header h2::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 60px;
  height: 3px;
  background: linear-gradient(to right, var(--primary-color), var(--secondary-color));
  border-radius: 3px;
}

.section-description {
  color: var(--text-light);
  font-size: 1.1rem;
  max-width: 700px;
  margin: 0 auto;
}

.card {
  background-color: var(--card-color);
  border-radius: var(--border-radius);
  box-shadow: var(--shadow);
  padding: 2.5rem;
  margin-bottom: 2rem;
  transition: var(--transition);
  border: 1px solid var(--border-color);
}

.card:hover {
  box-shadow: var(--shadow-hover);
  transform: translateY(-5px);
}

.action-buttons {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  margin-top: 2.5rem;
}

.analyze-button, .reset-button {
  padding: 12px 24px;
  font-weight: 600;
  border-radius: 8px;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 8px;
}

.analyze-button {
  background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));
  border: none;
}

.analyze-button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 7px 14px rgba(50, 50, 93, 0.1), 0 3px 6px rgba(0, 0, 0, 0.08);
}

.reset-button:hover:not(:disabled) {
  transform: translateY(-2px);
}

.button-icon {
  display: flex;
  align-items: center;
  justify-content: center;
}

.results-container {
  display: flex;
  flex-direction: column;
  gap: 0;
  max-width: 900px;
  margin: 0 auto;
}

.results-actions {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin: 2rem 0;
  flex-wrap: wrap;
}

.action-button {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  border-radius: 8px;
  font-weight: 600;
  transition: all 0.3s ease;
}

.action-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.disclaimer {
  margin-top: 2.5rem;
}

/* Analysis section styles */
.analysis-section {
  margin: 2rem 0;
}

.analysis-container {
  background-color: var(--card-color);
  border-radius: var(--border-radius);
  box-shadow: var(--shadow);
  padding: 2.5rem;
  text-align: center;
  max-width: 700px;
  margin: 0 auto;
  border: 1px solid var(--border-color);
}

.analysis-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
}

.analysis-icon {
  color: var(--primary-color);
}

.analysis-pulse {
  animation: pulse 1.5s infinite;
}

@keyframes pulse {
  0% {
    transform: scale(0.95);
    opacity: 0.7;
  }
  50% {
    transform: scale(1.05);
    opacity: 1;
  }
  100% {
    transform: scale(0.95);
    opacity: 0.7;
  }
}

.analysis-content h3 {
  color: var(--primary-dark);
  font-size: 1.5rem;
  margin: 0;
}

.progress-container {
  width: 100%;
  max-width: 500px;
}

.progress-bar {
  height: 10px;
  background-color: var(--primary-light);
  border-radius: 5px;
  overflow: hidden;
  margin-bottom: 0.5rem;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(to right, var(--primary-color), var(--secondary-color));
  border-radius: 5px;
  transition: width 0.3s ease;
}

.progress-text {
  text-align: right;
  font-weight: 600;
  color: var(--primary-dark);
}

@media (min-width: 768px) {
  .results-container {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 767px) {
  .section-header h2 {
    font-size: 1.75rem;
  }
  
  .card {
    padding: 1.5rem;
  }
  
  .action-buttons {
    flex-direction: column;
  }
  
  .results-actions {
    flex-direction: column;
  }
}
</style>
