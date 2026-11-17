<script setup>
import { ref } from 'vue'

const props = defineProps({
  currentPage: {
    type: String,
    default: 'home'
  }
})

const emit = defineEmits(['navigate'])

const isMenuOpen = ref(false)

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

const closeMenu = () => {
  isMenuOpen.value = false
}

const navigateTo = (page) => {
  emit('navigate', page)
  closeMenu()
  // Scroll to top when navigating
  window.scrollTo({ top: 0, behavior: 'smooth' })
}
</script>

<template>
  <header class="app-header">
    <div class="container header-container">
      <div class="logo" @click="navigateTo('home')">
        <div class="logo-icon">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
          </svg>
        </div>
        <span class="logo-text">MedRec</span>
      </div>
      
      <button class="menu-toggle" @click="toggleMenu" aria-label="Toggle menu">
        <span></span>
        <span></span>
        <span></span>
      </button>
      
      <nav class="main-nav" :class="{ 'is-open': isMenuOpen }">
        <ul class="nav-list">
          <li><a href="#" class="nav-link" :class="{ 'active': currentPage === 'home' }" @click.prevent="navigateTo('home')">Home</a></li>
          <li><a href="#" class="nav-link" :class="{ 'active': currentPage === 'about' }" @click.prevent="navigateTo('about')">About</a></li>
          <li><a href="#" class="nav-link" :class="{ 'active': currentPage === 'how-it-works' }" @click.prevent="navigateTo('how-it-works')">How It Works</a></li>
          <li><a href="#" class="nav-link" :class="{ 'active': currentPage === 'contact' }" @click.prevent="navigateTo('contact')">Contact</a></li>
        </ul>
      </nav>
    </div>
    
    <div class="hero" v-if="currentPage === 'home'">
      <div class="container hero-container">
        <div class="hero-content">
          <h1>Medical Recommendation System</h1>
          <p>Get personalized medical recommendations based on your symptoms</p>
          <div class="hero-buttons">
            <a href="#symptom-selector" class="hero-button primary">Get Started</a>
            <a href="#" class="hero-button secondary" @click.prevent="navigateTo('how-it-works')">Learn More</a>
          </div>
        </div>
        <div class="hero-image">
          <svg xmlns="http://www.w3.org/2000/svg" width="400" height="300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" class="medical-icon">
            <path d="M8 2h8a2 2 0 0 1 2 2v16a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2Z"></path>
            <path d="M12 6v12"></path>
            <path d="M6 12h12"></path>
          </svg>
        </div>
      </div>
      <div class="wave-container">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320" class="wave">
          <path fill="#f7fafc" fill-opacity="1" d="M0,96L48,112C96,128,192,160,288,160C384,160,480,128,576,122.7C672,117,768,139,864,149.3C960,160,1056,160,1152,138.7C1248,117,1344,75,1392,53.3L1440,32L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path>
        </svg>
      </div>
    </div>
    
    <div class="page-header" v-else>
      <div class="container">
        <h1>{{ currentPage.charAt(0).toUpperCase() + currentPage.slice(1).replace(/-/g, ' ') }}</h1>
      </div>
    </div>
  </header>
</template>

<style scoped>
.app-header {
  background-color: var(--card-color);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
  position: relative;
}

.header-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.25rem 1.5rem;
  position: relative;
}

.logo {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  cursor: pointer;
}

.logo-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));
  border-radius: 10px;
  color: white;
}

.logo-text {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--primary-dark);
  letter-spacing: -0.5px;
}

.menu-toggle {
  display: none;
  flex-direction: column;
  justify-content: space-between;
  width: 2rem;
  height: 1.5rem;
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 0;
  z-index: 10;
}

.menu-toggle span {
  display: block;
  height: 2px;
  width: 100%;
  background-color: var(--text-color);
  border-radius: 2px;
  transition: all 0.3s ease;
}

.nav-list {
  display: flex;
  list-style: none;
  gap: 2.5rem;
}

.nav-link {
  color: var(--text-color);
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s ease;
  padding: 0.5rem 0;
  position: relative;
  font-size: 1.05rem;
}

.nav-link:hover, .nav-link.active {
  color: var(--primary-color);
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background-color: var(--primary-color);
  transition: width 0.3s ease;
}

.nav-link:hover::after, .nav-link.active::after {
  width: 100%;
}

.hero {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
  padding: 5rem 0 0;
  text-align: left;
  position: relative;
  overflow: hidden;
}

.hero-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  z-index: 2;
}

.hero-content {
  max-width: 600px;
}

.hero-content h1 {
  font-size: 3rem;
  margin-bottom: 1.5rem;
  line-height: 1.2;
  font-weight: 800;
}

.hero-content p {
  font-size: 1.25rem;
  margin-bottom: 2rem;
  opacity: 0.9;
  line-height: 1.6;
}

.hero-buttons {
  display: flex;
  gap: 1rem;
}

.hero-button {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.3s ease;
}

.hero-button.primary {
  background-color: white;
  color: var(--primary-dark);
}

.hero-button.primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 7px 14px rgba(0, 0, 0, 0.1), 0 3px 6px rgba(0, 0, 0, 0.08);
}

.hero-button.secondary {
  background-color: rgba(255, 255, 255, 0.1);
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.hero-button.secondary:hover {
  background-color: rgba(255, 255, 255, 0.2);
}

.hero-image {
  display: flex;
  align-items: center;
  justify-content: center;
}

.medical-icon {
  width: 300px;
  height: 300px;
  stroke: rgba(255, 255, 255, 0.8);
  stroke-width: 1;
}

.wave-container {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  overflow: hidden;
  line-height: 0;
}

.wave {
  display: block;
  width: 100%;
  height: 70px;
}

.page-header {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
  padding: 3rem 0;
  text-align: center;
}

.page-header h1 {
  font-size: 2.5rem;
  font-weight: 700;
  margin: 0;
  text-transform: capitalize;
}

@media (max-width: 992px) {
  .hero-content h1 {
    font-size: 2.5rem;
  }
  
  .hero-image {
    display: none;
  }
  
  .hero-content {
    max-width: 100%;
    text-align: center;
  }
  
  .hero-buttons {
    justify-content: center;
  }
}

@media (max-width: 768px) {
  .menu-toggle {
    display: flex;
  }
  
  .main-nav {
    position: fixed;
    top: 0;
    right: -100%;
    width: 80%;
    max-width: 300px;
    height: 100vh;
    background-color: white;
    padding: 5rem 2rem 2rem;
    box-shadow: -2px 0 5px rgba(0, 0, 0, 0.1);
    transition: right 0.3s ease;
    z-index: 5;
  }
  
  .main-nav.is-open {
    right: 0;
  }
  
  .nav-list {
    flex-direction: column;
    gap: 1.5rem;
  }
  
  .nav-link {
    display: block;
    font-size: 1.1rem;
  }
  
  .hero-content h1 {
    font-size: 2rem;
  }
  
  .hero-content p {
    font-size: 1.1rem;
  }
  
  .page-header h1 {
    font-size: 2rem;
  }
}
</style>
