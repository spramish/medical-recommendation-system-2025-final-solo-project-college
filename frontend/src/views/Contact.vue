<template>
  <div class="container">
    <section class="section contact-section">
      <div class="section-header">
        <h2>Contact Us</h2>
        <p class="section-description">
          Get in touch with our team for questions, feedback, or support
        </p>
      </div>
      
      <div class="contact-container">
        <div class="contact-info">
          <h3>Get In Touch</h3>
          <p>We'd love to hear from you. Whether you have a question about our services, need technical support, or want to provide feedback, our team is here to help.</p>
          
          <div class="contact-methods">
            <div class="contact-method">
              <div class="method-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
                </svg>
              </div>
              <div class="method-details">
                <h4>Phone</h4>
                <p>(123) 456-7890</p>
                <p class="text-light">Monday-Friday, 9am-5pm EST</p>
              </div>
            </div>
            
            <div class="contact-method">
              <div class="method-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                  <polyline points="22,6 12,13 2,6"></polyline>
                </svg>
              </div>
              <div class="method-details">
                <h4>Email</h4>
                <p>support@medrec.com</p>
                <p class="text-light">We'll respond within 24 hours</p>
              </div>
            </div>
            
            <div class="contact-method">
              <div class="method-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                  <circle cx="12" cy="10" r="3"></circle>
                </svg>
              </div>
              <div class="method-details">
                <h4>Office</h4>
                <p>123 Health Avenue, Suite 456</p>
                <p>Boston, MA 02110</p>
              </div>
            </div>
          </div>
          
          <div class="social-links">
            <h4>Connect With Us</h4>
            <div class="social-icons">
              <a href="#" class="social-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path>
                </svg>
              </a>
              <a href="#" class="social-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path>
                </svg>
              </a>
              <a href="#" class="social-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
                  <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
                  <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
                </svg>
              </a>
              <a href="#" class="social-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
                  <rect x="2" y="9" width="4" height="12"></rect>
                  <circle cx="4" cy="4" r="2"></circle>
                </svg>
              </a>
            </div>
          </div>
        </div>
        
        <div class="contact-form">
          <h3>Send Us a Message</h3>
          <form @submit.prevent="submitForm">
            <div class="form-group">
              <label for="name">Your Name</label>
              <input type="text" id="name" v-model="form.name" required>
            </div>
            
            <div class="form-group">
              <label for="email">Email Address</label>
              <input type="email" id="email" v-model="form.email" required>
            </div>
            
            <div class="form-group">
              <label for="subject">Subject</label>
              <input type="text" id="subject" v-model="form.subject" required>
            </div>
            
            <div class="form-group">
              <label for="message">Message</label>
              <textarea id="message" v-model="form.message" rows="5" required></textarea>
            </div>
            
            <button type="submit" class="submit-button" :disabled="submitting">
              <span v-if="!submitting">Send Message</span>
              <span v-else>Sending...</span>
            </button>
            
            <div v-if="formSubmitted" class="form-success">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                <polyline points="22 4 12 14.01 9 11.01"></polyline>
              </svg>
              <p>Your message has been sent successfully. We'll get back to you soon!</p>
            </div>
          </form>
        </div>
      </div>
    </section>
    
    <section class="section faq-section">
      <div class="section-header">
        <h2>Frequently Asked Questions</h2>
        <p class="section-description">
          Quick answers to common questions
        </p>
      </div>
      
      <div class="faq-grid">
        <div class="faq-card">
          <h3>How quickly will I receive a response?</h3>
          <p>We aim to respond to all inquiries within 24 hours during business days. For urgent matters, please call our support line.</p>
        </div>
        
        <div class="faq-card">
          <h3>Can I request a demo of the system?</h3>
          <p>Yes, you can request a personalized demo by contacting our sales team through the form above or by emailing sales@medrec.com.</p>
        </div>
        
        <div class="faq-card">
          <h3>Do you offer technical support?</h3>
          <p>Yes, we provide technical support for all users. You can reach our support team via email or phone during business hours.</p>
        </div>
        
        <div class="faq-card">
          <h3>How can I provide feedback?</h3>
          <p>We value your feedback! You can share your thoughts and suggestions using the contact form above or by emailing feedback@medrec.com.</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'

const form = reactive({
  name: '',
  email: '',
  subject: '',
  message: ''
})

const submitting = ref(false)
const formSubmitted = ref(false)

const submitForm = async () => {
  submitting.value = true
  
  // Simulate form submission
  await new Promise(resolve => setTimeout(resolve, 1500))
  
  // Reset form
  form.name = ''
  form.email = ''
  form.subject = ''
  form.message = ''
  
  submitting.value = false
  formSubmitted.value = true
  
  // Hide success message after 5 seconds
  setTimeout(() => {
    formSubmitted.value = false
  }, 5000)
}
</script>

<style scoped>
.contact-section {
  margin-top: 2rem;
}

.contact-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  margin-top: 2rem;
}

.contact-info, .contact-form {
  background-color: var(--card-color);
  border-radius: var(--border-radius);
  padding: 2rem;
  box-shadow: var(--shadow);
  border: 1px solid var(--border-color);
}

.contact-info h3, .contact-form h3 {
  color: var(--primary-dark);
  margin-bottom: 1.25rem;
  font-size: 1.5rem;
}

.contact-info p {
  margin-bottom: 1.5rem;
  line-height: 1.7;
}

.contact-methods {
  margin-top: 2rem;
}

.contact-method {
  display: flex;
  align-items: flex-start;
  margin-bottom: 1.5rem;
}

.method-icon {
  color: var(--primary-color);
  margin-right: 1rem;
  background-color: var(--primary-light);
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.method-details h4 {
  margin: 0 0 0.5rem;
  color: var(--text-color);
  font-size: 1.1rem;
}

.method-details p {
  margin: 0 0 0.25rem;
}

.text-light {
  color: var(--text-light);
  font-size: 0.9rem;
}

.social-links {
  margin-top: 2rem;
}

.social-links h4 {
  margin-bottom: 1rem;
  color: var(--text-color);
  font-size: 1.1rem;
}

.social-icons {
  display: flex;
  gap: 1rem;
}

.social-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background-color: var(--primary-light);
  color: var(--primary-color);
  border-radius: 50%;
  transition: all 0.3s ease;
}

.social-icon:hover {
  background-color: var(--primary-color);
  color: white;
  transform: translateY(-3px);
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: var(--text-color);
  font-weight: 500;
}

.form-group input, .form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid var(--border-color);
  border-radius: 8px;
  font-family: inherit;
  font-size: 1rem;
  transition: border-color 0.3s ease;
}

.form-group input:focus, .form-group textarea:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px var(--primary-light);
}

.submit-button {
  background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));
  color: white;
  border: none;
  border-radius: 8px;
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  width: 100%;
}

.submit-button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.submit-button:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.form-success {
  margin-top: 1.5rem;
  padding: 1rem;
  background-color: #d1fae5;
  border-radius: 8px;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  color: #065f46;
  animation: fadeIn 0.5s ease-out;
}

.form-success svg {
  color: #059669;
}

.faq-section {
  margin-top: 4rem;
}

.faq-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2rem;
  margin-top: 2rem;
}

.faq-card {
  background-color: var(--card-color);
  border-radius: var(--border-radius);
  padding: 1.5rem;
  box-shadow: var(--shadow);
  border: 1px solid var(--border-color);
  transition: var(--transition);
}

.faq-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-hover);
}

.faq-card h3 {
  color: var(--primary-dark);
  margin-bottom: 0.75rem;
  font-size: 1.1rem;
}

.faq-card p {
  color: var(--text-light);
  margin: 0;
  line-height: 1.7;
}

@media (max-width: 992px) {
  .contact-container {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  
  .faq-grid {
    grid-template-columns: 1fr;
  }
}
</style>
