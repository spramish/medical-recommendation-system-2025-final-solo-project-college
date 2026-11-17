<script setup>
import { ref, computed, watch } from 'vue'
import { ElTag, ElInput, ElAutocomplete, ElDivider } from 'element-plus'

const props = defineProps({
  allSymptoms: {
    type: Array,
    required: true
  },
  commonSymptoms: {
    type: Array,
    required: true
  },
  selectedSymptoms: {
    type: Array,
    required: true
  },
  loading: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['update:selected-symptoms'])

const searchInput = ref('')
const filteredSymptoms = computed(() => {
  if (!searchInput.value) return []
  
  const search = searchInput.value.toLowerCase()
  return props.allSymptoms
    .filter(symptom => 
      symptom.label.toLowerCase().includes(search) && 
      !props.selectedSymptoms.includes(symptom.value)
    )
    .slice(0, 10)
})

const handleSelect = (item) => {
  if (item && item.value) {
    addSymptom(item.value)
  }
}

const addSymptom = (symptom) => {
  if (!props.selectedSymptoms.includes(symptom)) {
    const newSelectedSymptoms = [...props.selectedSymptoms, symptom]
    emit('update:selected-symptoms', newSelectedSymptoms)
  }
  searchInput.value = ''
}

const removeSymptom = (symptom) => {
  const newSelectedSymptoms = props.selectedSymptoms.filter(s => s !== symptom)
  emit('update:selected-symptoms', newSelectedSymptoms)
}

const formatSymptomName = (symptom) => {
  return symptom.replace(/_/g, ' ')
}

const groupedCommonSymptoms = computed(() => {
  // Group common symptoms into categories for better organization
  const categories = {
    'Pain & Discomfort': ['headache', 'joint_pain', 'back_pain', 'chest_pain', 'abdominal_pain', 'muscle_pain'],
    'Respiratory': ['cough', 'breathlessness', 'continuous_sneezing'],
    'Digestive': ['nausea', 'vomiting', 'diarrhoea', 'constipation', 'loss_of_appetite'],
    'General': ['fatigue', 'fever', 'weight_loss', 'weight_gain', 'dizziness'],
    'Skin': ['itching', 'skin_rash'],
    'Mental': ['anxiety', 'depression']
  }
  
  const result = {}
  for (const [category, symptoms] of Object.entries(categories)) {
    result[category] = symptoms.filter(s => props.commonSymptoms.includes(s))
  }
  
  return result
})

// Icons for categories
const categoryIcons = {
  'Pain & Discomfort': `<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 11h8v2H8z"></path><circle cx="12" cy="12" r="10"></circle></svg>`,
  'Respiratory': `<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22a9 9 0 0 0 9-9c0-4-2-5-3-6s.5-4-3-8.5C13.5 2 12 2 12 2s-1.5 0-3 .5C5.5 7 6 8 5 9S2 9 2 13a9 9 0 0 0 9 9Z"></path></svg>`,
  'Digestive': `<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 11c0-2-2-3-2-3s2-1 2-3c0-1.667-1-3-3-3s-3 1.333-3 3c0 2 2 3 2 3s-2 1-2 3c0 1.667 1 3 3 3s3-1.333 3-3Z"></path><path d="M10.5 7.5C10.5 5.833 9.5 4.5 7.5 4.5s-3 1.333-3 3C4.5 9.5 6.5 10 6.5 10S4.5 11.5 4.5 13.5c0 1.667 1 3 3 3s3-1.333 3-3c0-2-2-2.5-2-2.5s2-1 2-3.5Z"></path><path d="M20 19c0-2-2-3-2-3s2-1 2-3c0-1.667-1-3-3-3s-3 1.333-3 3c0 2 2 3 2 3s-2 1-2 3c0 1.667 1 3 3 3s3-1.333 3-3Z"></path></svg>`,
  'General': `<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="m4.93 4.93 14.14 14.14"></path></svg>`,
  'Skin': `<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.24 12.24a6 6 0 0 0-8.49-8.49L5 10.5V19h8.5z"></path><line x1="16" y1="8" x2="2" y2="22"></line><line x1="17.5" y1="15" x2="9" y2="15"></line></svg>`,
  'Mental': `<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M8 14s1.5 2 4 2 4-2 4-2"></path><line x1="9" y1="9" x2="9.01" y2="9"></line><line x1="15" y1="9" x2="15.01" y2="9"></line></svg>`
}
</script>

<template>
  <div id="symptom-selector" class="symptom-selector">
    <h3>Select Your Symptoms</h3>
    
    <!-- Search and add symptoms -->
    <div class="search-container">
      <el-autocomplete
        v-model="searchInput"
        :fetch-suggestions="(query, cb) => cb(filteredSymptoms)"
        placeholder="Search for symptoms..."
        :trigger-on-focus="false"
        :loading="loading"
        @select="handleSelect"
        class="symptom-search"
        popper-class="symptom-popper"
        value-key="value"
      >
        <template #default="{ item }">
          <div class="suggestion-item" @click="addSymptom(item.value)">
            {{ item.label }}
          </div>
        </template>
        <template #suffix>
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="search-icon">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
        </template>
      </el-autocomplete>
    </div>
    
    <!-- Selected symptoms -->
    <div v-if="selectedSymptoms.length > 0" class="selected-symptoms">
      <h4>Your Selected Symptoms</h4>
      <div class="tags-container">
        <el-tag
          v-for="symptom in selectedSymptoms"
          :key="symptom"
          closable
          @close="removeSymptom(symptom)"
          class="symptom-tag"
          type="primary"
          effect="light"
        >
          {{ formatSymptomName(symptom) }}
        </el-tag>
      </div>
    </div>
    
    <el-divider>
      <span class="divider-content">Common Symptoms</span>
    </el-divider>
    
    <!-- Common symptoms by category -->
    <div class="common-symptoms">
      <div v-for="(symptoms, category) in groupedCommonSymptoms" :key="category" class="symptom-category">
        <h4>
          <span class="category-icon" v-html="categoryIcons[category]"></span>
          {{ category }}
        </h4>
        <div class="category-symptoms">
          <el-tag
            v-for="symptom in symptoms"
            :key="symptom"
            @click="addSymptom(symptom)"
            class="symptom-tag clickable"
            :type="selectedSymptoms.includes(symptom) ? 'primary' : 'info'"
            :effect="selectedSymptoms.includes(symptom) ? 'dark' : 'plain'"
          >
            {{ formatSymptomName(symptom) }}
          </el-tag>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.symptom-selector {
  width: 100%;
}

.symptom-selector h3 {
  margin-bottom: 1.5rem;
  color: var(--primary-dark);
  text-align: center;
  font-size: 1.5rem;
  position: relative;
  display: inline-block;
  left: 50%;
  transform: translateX(-50%);
}

.symptom-selector h3::after {
  content: '';
  position: absolute;
  bottom: -8px;
  left: 0;
  width: 50px;
  height: 3px;
  background: linear-gradient(to right, var(--primary-color), var(--secondary-color));
  border-radius: 3px;
}

.search-container {
  margin-bottom: 2rem;
  position: relative;
}

.symptom-search {
  width: 100%;
}

.search-icon {
  color: var(--text-light);
}

.suggestion-item {
  padding: 0.75rem;
  transition: background-color 0.2s ease;
  cursor: pointer;
}

.suggestion-item:hover {
  background-color: var(--primary-light);
}

.selected-symptoms {
  margin-bottom: 2rem;
  background-color: var(--primary-light);
  border-radius: 10px;
  padding: 1.25rem;
  border: 1px dashed var(--primary-color);
  animation: fadeIn 0.5s ease-out;
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

.selected-symptoms h4 {
  margin-bottom: 1rem;
  color: var(--primary-dark);
  font-size: 1.1rem;
  display: flex;
  align-items: center;
}

.selected-symptoms h4::before {
  content: '';
  display: inline-block;
  width: 18px;
  height: 18px;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='18' height='18' viewBox='0 0 24 24' fill='none' stroke='%233a86ff' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M22 11.08V12a10 10 0 1 1-5.93-9.14'%3E%3C/path%3E%3Cpolyline points='22 4 12 14.01 9 11.01'%3E%3C/polyline%3E%3C/svg%3E");
  background-repeat: no-repeat;
  margin-right: 8px;
}

.tags-container {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.symptom-tag {
  margin-right: 0;
  margin-bottom: 0;
  text-transform: capitalize;
  border-radius: 6px;
  padding: 8px 12px;
  font-size: 0.9rem;
  transition: all 0.3s ease;
}

.symptom-tag.clickable {
  cursor: pointer;
  transition: all 0.2s ease;
}

.symptom-tag.clickable:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.divider-content {
  font-size: 0.9rem;
  color: var(--text-light);
  font-weight: 500;
}

.common-symptoms {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 2rem;
}

.symptom-category {
  background-color: var(--card-color);
  border-radius: 10px;
  padding: 1.25rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  border: 1px solid var(--border-color);
  transition: all 0.3s ease;
}

.symptom-category:hover {
  box-shadow: 0 10px 15px rgba(0, 0, 0, 0.05);
  transform: translateY(-5px);
}

.symptom-category h4 {
  margin-bottom: 1rem;
  color: var(--text-color);
  font-size: 1.1rem;
  display: flex;
  align-items: center;
}

.category-icon {
  display: inline-flex;
  margin-right: 8px;
  color: var(--primary-color);
}

.category-symptoms {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}

@media (max-width: 768px) {
  .common-symptoms {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
  .symptom-category {
    padding: 1rem;
  }
}
</style>

<style>
/* Global styles for the autocomplete dropdown */
.symptom-popper .el-scrollbar__view {
  padding: 5px 0;
}

.symptom-popper .el-autocomplete-suggestion__list {
  margin: 0;
  padding: 0;
}

.symptom-popper .el-autocomplete-suggestion__wrap {
  max-height: 280px;
}

.symptom-popper .el-autocomplete-suggestion li {
  line-height: 1.5;
  padding: 0;
  cursor: pointer;
}

.symptom-popper .el-autocomplete-suggestion li:hover {
  background-color: var(--primary-light);
}
</style>
