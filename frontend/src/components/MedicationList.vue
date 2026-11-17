<script setup>
defineProps({
  medications: {
    type: Array,
    required: true
  }
})
</script>

<template>
  <div class="medication-list">
    <div class="medication-header">
      <div class="medication-icon">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"></path>
        </svg>
      </div>
      <h3>Recommended Medications</h3>
    </div>
    
    <div class="medication-content">
      <div v-for="(medication, index) in medications" :key="index" class="medication-card">
        <div class="medication-card-header">
          <h4>{{ medication.name }}</h4>
          <div class="medication-badge">Prescription Required</div>
        </div>
        
        <div class="medication-details">
          <div class="detail-item">
            <div class="detail-icon">
              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
              </svg>
            </div>
            <div class="detail-content">
              <h5>Dosage</h5>
              <p>{{ medication.dosage }}</p>
            </div>
          </div>
          
          <div class="detail-item">
            <div class="detail-icon">
              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
              </svg>
            </div>
            <div class="detail-content">
              <h5>Side Effects</h5>
              <p>{{ medication.side_effects }}</p>
            </div>
          </div>
          
          <div class="detail-item">
            <div class="detail-icon">
              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
              </svg>
            </div>
            <div class="detail-content">
              <h5>Precautions</h5>
              <p>{{ medication.precautions }}</p>
            </div>
          </div>
        </div>
        
        <div class="medication-actions">
          <button class="action-button">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
              <polyline points="7 10 12 15 17 10"></polyline>
              <line x1="12" y1="15" x2="12" y2="3"></line>
            </svg>
            Save Info
          </button>
          <button class="action-button">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
              <circle cx="9" cy="7" r="4"></circle>
              <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
              <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
            </svg>
            Share with Doctor
          </button>
        </div>
      </div>
      
      <div v-if="medications.length === 0" class="no-medications">
        <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10"></circle>
          <line x1="12" y1="8" x2="12" y2="12"></line>
          <line x1="12" y1="16" x2="12.01" y2="16"></line>
        </svg>
        <p>No specific medications recommended. Please consult with a healthcare professional.</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.medication-list {
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

.medication-list:hover {
  box-shadow: var(--shadow-hover);
  transform: translateY(-5px);
}

.medication-header {
  background: linear-gradient(135deg, var(--accent-color) 0%, #ff8787 100%);
  color: white;
  padding: 1.5rem;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.medication-icon {
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.medication-header h3 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 600;
}

.medication-content {
  padding: 1.5rem;
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.medication-card {
  background-color: var(--background-color);
  border-radius: 12px;
  border: 1px solid var(--border-color);
  overflow: hidden;
  transition: all 0.3s ease;
}

.medication-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  border-color: var(--accent-color);
}

.medication-card-header {
  background-color: var(--accent-light);
  padding: 1rem 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid var(--border-color);
}

.medication-card-header h4 {
  margin: 0;
  color: var(--accent-color);
  font-size: 1.2rem;
  font-weight: 600;
}

.medication-badge {
  background-color: var(--accent-color);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.875rem;
}

.medication-details {
  padding: 1.5rem;
}

.detail-item {
  display: flex;
  gap: 1rem;
  margin-bottom: 1.25rem;
}

.detail-item:last-child {
  margin-bottom: 0;
}

.detail-icon {
  color: var(--accent-color);
  flex-shrink: 0;
}

.detail-content h5 {
  margin: 0 0 0.5rem 0;
  color: var(--text-color);
  font-size: 1rem;
}

.detail-content p {
  margin: 0;
  color: var(--text-light);
  line-height: 1.5;
}

.medication-actions {
  padding: 1rem 1.5rem;
  background-color: var(--background-color);
  border-top: 1px solid var(--border-color);
  display: flex;
  gap: 1rem;
}

.action-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  border: 1px solid var(--border-color);
  border-radius: 6px;
  background-color: white;
  color: var(--text-color);
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.action-button:hover {
  background-color: var(--accent-light);
  border-color: var(--accent-color);
  color: var(--accent-color);
}

.no-medications {
  text-align: center;
  color: var(--text-light);
  padding: 2rem 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

@media (max-width: 768px) {
  .medication-actions {
    flex-direction: column;
  }
  
  .action-button {
    width: 100%;
    justify-content: center;
  }
}
</style>
