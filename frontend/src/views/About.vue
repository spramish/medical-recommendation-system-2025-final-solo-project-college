<template>
  <div class="container">
    <section class="section about-section">
      <div class="section-header">
        <h2>About MedRec</h2>
        <p class="section-description">
          Learn more about our mission to make healthcare more accessible
        </p>
      </div>
      
      <div class="about-content">
        <div class="about-image">
          <img src="https://img.freepik.com/free-vector/medical-team-concept-illustration_114360-1008.jpg" alt="Medical professionals" class="rounded-image" />
        </div>
        
        <div class="about-text">
          <h3>Our Mission</h3>
          <p>
            At MedRec, we believe that everyone should have access to reliable medical information. Our mission is to leverage technology to make healthcare more accessible, understandable, and personalized.
          </p>
          
          <h3>What We Do</h3>
          <p>
            MedRec is a symptom-based medical recommendation system that uses advanced algorithms to analyze your symptoms and provide personalized health insights. We combine medical knowledge with cutting-edge technology to help you understand your health better.
          </p>
          
          <h3>Our Team</h3>
          <p>
            Our team consists of healthcare professionals, data scientists, and software engineers who are passionate about improving healthcare through technology. We work closely with medical experts to ensure the accuracy and reliability of our recommendations.
          </p>
          
          <div class="values-grid">
            <div class="value-card">
              <div class="value-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                  <polyline points="22 4 12 14.01 9 11.01"></polyline>
                </svg>
              </div>
              <h4>Accuracy</h4>
              <p>We prioritize medical accuracy in all our recommendations</p>
            </div>
            
            <div class="value-card">
              <div class="value-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                </svg>
              </div>
              <h4>Privacy</h4>
              <p>Your health data is private and secure with us</p>
            </div>
            
            <div class="value-card">
              <div class="value-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="12" cy="12" r="10"></circle>
                  <path d="M12 16v-4"></path>
                  <path d="M12 8h.01"></path>
                </svg>
              </div>
              <h4>Transparency</h4>
              <p>We're clear about what our system can and cannot do</p>
            </div>
            
            <div class="value-card">
              <div class="value-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                  <circle cx="9" cy="7" r="4"></circle>
                  <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                  <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                </svg>
              </div>
              <h4>Accessibility</h4>
              <p>Making healthcare information accessible to everyone</p>
            </div>
          </div>
        </div>
      </div>
    </section>
    
    <section class="section team-section">
      <div class="section-header">
        <h2>Our Leadership Team</h2>
        <p class="section-description">
          Meet the experts behind MedRec
        </p>
      </div>
      
      <div class="team-grid">
        <div class="team-member">
          <div class="member-image">
            <img src="https://img.freepik.com/free-vector/doctor-character-avatar-illustrated_24877-60111.jpg" alt="Dr. Sarah Johnson" />
          </div>
          <h3>Dr. Sarah Johnson</h3>
          <p class="member-title">Chief Medical Officer</p>
          <p class="member-bio">Board-certified physician with over 15 years of experience in internal medicine.</p>
        </div>
        
        <div class="team-member">
          <div class="member-image">
            <img src="https://img.freepik.com/free-vector/ai-technology-brain-background-digital-transformation-concept_53876-124674.jpg" alt="Michael Chen" />
          </div>
          <h3>Michael Chen</h3>
          <p class="member-title">Chief Technology Officer</p>
          <p class="member-bio">AI specialist with a background in healthcare technology and machine learning.</p>
        </div>
        
        <div class="team-member">
          <div class="member-image">
            <img src="https://img.freepik.com/free-vector/medical-research-concept-illustration_114360-1009.jpg" alt="Dr. James Wilson" />
          </div>
          <h3>Dr. James Wilson</h3>
          <p class="member-title">Medical Research Director</p>
          <p class="member-bio">Specializes in diagnostic medicine with a focus on symptom analysis and pattern recognition.</p>
        </div>
        
        <div class="team-member">
          <div class="member-image">
            <img src="https://img.freepik.com/free-vector/user-experience-concept-illustration_114360-1010.jpg" alt="Emily Rodriguez" />
          </div>
          <h3>Emily Rodriguez</h3>
          <p class="member-title">Head of User Experience</p>
          <p class="member-bio">Expert in creating accessible and intuitive healthcare interfaces for diverse users.</p>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.about-section {
  margin-top: 2rem;
}

.about-content {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 3rem;
  margin-top: 2rem;
}

.about-image {
  display: flex;
  align-items: center;
  justify-content: center;
}

.rounded-image {
  width: 100%;
  max-width: 400px;
  border-radius: 12px;
  box-shadow: var(--shadow);
}

.about-text h3 {
  color: var(--primary-dark);
  margin-bottom: 1rem;
  font-size: 1.5rem;
}

.about-text p {
  margin-bottom: 1.5rem;
  line-height: 1.7;
}

.values-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
  margin-top: 2rem;
}

.value-card {
  background-color: var(--card-color);
  border-radius: var(--border-radius);
  padding: 1.5rem;
  box-shadow: var(--shadow);
  transition: var(--transition);
  border: 1px solid var(--border-color);
}

.value-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-hover);
}

.value-icon {
  color: var(--primary-color);
  margin-bottom: 1rem;
}

.value-card h4 {
  color: var(--text-color);
  margin-bottom: 0.5rem;
  font-size: 1.2rem;
}

.value-card p {
  color: var(--text-light);
  margin: 0;
}

.team-section {
  margin-top: 4rem;
}

.team-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;
  margin-top: 2rem;
}

.team-member {
  background-color: var(--card-color);
  border-radius: var(--border-radius);
  overflow: hidden;
  box-shadow: var(--shadow);
  transition: var(--transition);
  text-align: center;
  border: 1px solid var(--border-color);
}

.team-member:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-hover);
}

.member-image {
  width: 100%;
  height: 200px;
  overflow: hidden;
}

.member-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.team-member h3 {
  margin: 1rem 0 0.25rem;
  color: var(--text-color);
  font-size: 1.2rem;
}

.member-title {
  color: var(--primary-color);
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.member-bio {
  padding: 0 1rem 1.5rem;
  color: var(--text-light);
  font-size: 0.9rem;
}

@media (max-width: 992px) {
  .about-content {
    grid-template-columns: 1fr;
  }
  
  .about-image {
    margin-bottom: 2rem;
  }
  
  .team-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 576px) {
  .values-grid {
    grid-template-columns: 1fr;
  }
  
  .team-grid {
    grid-template-columns: 1fr;
  }
}
</style>
