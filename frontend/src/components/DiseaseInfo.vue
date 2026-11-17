<script setup>
import { computed } from 'vue'

const props = defineProps({
  diseaseInfo: {
    type: Object,
    required: true
  }
})

const hasDiet = computed(() => {
  return props.diseaseInfo.diet && props.diseaseInfo.diet.length > 0 && 
    !props.diseaseInfo.diet.every(item => item.includes('No dietary recommendations'))
})

const hasWorkout = computed(() => {
  return props.diseaseInfo.workout && props.diseaseInfo.workout.length > 0 && 
    !props.diseaseInfo.workout.every(item => item.includes('No workout recommendations'))
})
</script>

<template>
  <div class="disease-info">
    <div class="disease-header">
      <div class="disease-icon">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M8 2h8a2 2 0 0 1 2 2v16a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2Z"></path>
          <path d="M12 6v12"></path>
          <path d="M6 12h12"></path>
        </svg>
      </div>
      <div class="disease-title">
        <h3>{{ diseaseInfo.name }}</h3>
        <div class="confidence-badge">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
          </svg>
          AI-Powered Diagnosis
        </div>
      </div>
    </div>
    
    <div class="disease-content">
      <div class="info-section">
        <h4>
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="12" y1="16" x2="12" y2="12"></line>
            <line x1="12" y1="8" x2="12.01" y2="8"></line>
          </svg>
          Description
        </h4>
        <div class="description-card">
          <p>{{ diseaseInfo.description }}</p>
        </div>
      </div>
      
      <div v-if="diseaseInfo.precautions && diseaseInfo.precautions.length > 0" class="info-section">
        <h4>
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
          </svg>
          Precautions
        </h4>
        <div class="recommendations-grid">
          <div v-for="(precaution, index) in diseaseInfo.precautions" :key="index" class="recommendation-card">
            <div class="card-icon">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
              </svg>
            </div>
            <p>{{ precaution }}</p>
          </div>
        </div>
      </div>
      
      <div v-if="diseaseInfo.diet && diseaseInfo.diet.length > 0" class="info-section">
        <h4>
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M18 8h1a4 4 0 0 1 0 8h-1"></path>
            <path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"></path>
            <line x1="6" y1="1" x2="6" y2="4"></line>
            <line x1="10" y1="1" x2="10" y2="4"></line>
            <line x1="14" y1="1" x2="14" y2="4"></line>
          </svg>
          Dietary Recommendations
        </h4>
        <div class="recommendations-grid">
          <div v-for="(diet, index) in diseaseInfo.diet" :key="index" class="recommendation-card">
            <div class="card-icon">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M18 8h1a4 4 0 0 1 0 8h-1"></path>
                <path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"></path>
                <line x1="6" y1="1" x2="6" y2="4"></line>
                <line x1="10" y1="1" x2="10" y2="4"></line>
                <line x1="14" y1="1" x2="14" y2="4"></line>
              </svg>
            </div>
            <p>{{ diet }}</p>
          </div>
        </div>
      </div>
      
      <div v-if="diseaseInfo.workout && diseaseInfo.workout.length > 0" class="info-section">
        <h4>
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M18 8h1a4 4 0 0 1 0 8h-1"></path>
            <path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"></path>
            <line x1="6" y1="1" x2="6" y2="4"></line>
            <line x1="10" y1="1" x2="10" y2="4"></line>
            <line x1="14" y1="1" x2="14" y2="4"></line>
          </svg>
          Exercise Recommendations
        </h4>
        <div class="recommendations-grid">
          <div v-for="(workout, index) in diseaseInfo.workout" :key="index" class="recommendation-card">
            <div class="card-icon">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M18 8h1a4 4 0 0 1 0 8h-1"></path>
                <path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"></path>
                <line x1="6" y1="1" x2="6" y2="4"></line>
                <line x1="10" y1="1" x2="10" y2="4"></line>
                <line x1="14" y1="1" x2="14" y2="4"></line>
              </svg>
            </div>
            <p>{{ workout }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.disease-info {
  background-color: var(--card-color);
  border-radius: var(--border-radius);
  box-shadow: var(--shadow);
  overflow: hidden;
  height: 100%;
  display: flex;
  flex-direction: column;
  transition: all 0.3s ease;
  border: 1px solid var(--border-color);
}

.disease-info:hover {
  box-shadow: var(--shadow-hover);
  transform: translateY(-5px);
}

.disease-header {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
  padding: 1.5rem;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.disease-icon {
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.disease-title {
  flex: 1;
}

.disease-header h3 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 600;
}

.confidence-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background-color: rgba(255, 255, 255, 0.2);
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.875rem;
  margin-top: 0.5rem;
}

.disease-content {
  padding: 1.5rem;
  flex: 1;
}

.info-section {
  margin-bottom: 2rem;
  animation: fadeIn 0.5s ease-out;
}

.info-section:last-child {
  margin-bottom: 0;
}

.info-section h4 {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--primary-dark);
  margin-bottom: 1rem;
  font-size: 1.1rem;
}

.description-card {
  background-color: var(--background-color);
  padding: 1.25rem;
  border-radius: 8px;
  border: 1px solid var(--border-color);
}

.description-card p {
  margin: 0;
  line-height: 1.6;
  color: var(--text-color);
}

.recommendations-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1rem;
}

.recommendation-card {
  background-color: var(--background-color);
  padding: 1rem;
  border-radius: 8px;
  border: 1px solid var(--border-color);
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  transition: all 0.3s ease;
}

.recommendation-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  border-color: var(--primary-color);
}

.card-icon {
  color: var(--primary-color);
  flex-shrink: 0;
}

.recommendation-card p {
  margin: 0;
  line-height: 1.5;
  color: var(--text-color);
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 768px) {
  .recommendations-grid {
    grid-template-columns: 1fr;
  }
  
  .disease-header {
    padding: 1.25rem;
  }
  
  .disease-content {
    padding: 1.25rem;
  }
}
</style>
