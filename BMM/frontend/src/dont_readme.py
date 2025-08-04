<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SocialScheduler Pro | AI-Powered Marketing Platform</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/src/App.css">
</head>
<body>
  <div id="root">
    <script type="module" src="/src/main.jsx"></script>
  <!-- Navbar -->
  <nav class="navbar">
    <div class="container navbar-container">
      <a href="#" class="logo">
        <i class="fas fa-rocket"></i>
        <span>SocialScheduler Pro</span>
      </a>
      
      <div class="nav-links">
        <a href="#" class="nav-link">Features</a>
        <a href="#" class="nav-link">Solutions</a>
        <a href="#" class="nav-link">Pricing</a>
        <a href="#" class="nav-link">Resources</a>
      </div>
      
      <div class="user-section">
        <a href="#" class="btn btn-outline">Sign In</a>
        <a href="#" class="btn btn-primary">Get Started</a>
      </div>
    </div>
  </nav>

  <!-- Hero Section -->
  <section class="hero">
    <div class="container hero-content text-center">
      <h1 class="hero-title">Automate Your Social Media Marketing</h1>
      <p class="hero-subtitle">AI-powered content creation and scheduling for businesses. Streamline your social presence with enterprise-grade tools designed for marketers.</p>
      
      <div class="flex justify-center gap-6 mt-8">
        <a href="#" class="btn btn-primary">
          Get Started Free
          <i class="fas fa-arrow-right"></i>
        </a>
        <a href="#" class="btn btn-outline">
          <i class="fas fa-play-circle"></i>
          Watch Demo
        </a>
      </div>
      
      <div class="features-grid">
        <!-- Feature 1 -->
        <div class="feature-card floating">
          <div class="feature-icon">
            <i class="fas fa-robot"></i>
          </div>
          <h3 class="feature-title">AI Content Generation</h3>
          <p class="feature-description">Create compelling posts with our AI assistant that understands your brand voice and marketing goals.</p>
        </div>
        
        <!-- Feature 2 -->
        <div class="feature-card floating" style="animation-delay: 0.5s;">
          <div class="feature-icon">
            <i class="fas fa-calendar-alt"></i>
          </div>
          <h3 class="feature-title">Smart Scheduling</h3>
          <p class="feature-description">Automate posting to multiple platforms with intelligent scheduling optimized for maximum engagement.</p>
        </div>
        
        <!-- Feature 3 -->
        <div class="feature-card floating" style="animation-delay: 1s;">
          <div class="feature-icon">
            <i class="fas fa-chart-line"></i>
          </div>
          <h3 class="feature-title">Performance Tracking</h3>
          <p class="feature-description">Monitor your content history and engagement metrics to refine your marketing strategy.</p>
        </div>
      </div>
    </div>
  </section>
  </div> 
  <script>
    // Add floating animation to feature cards
    document.querySelectorAll('.feature-card').forEach((card, index) => {
      card.style.animationDelay = `${index * 0.2}s`;
    });
    
    // Add scroll effect to navbar
    window.addEventListener('scroll', () => {
      const navbar = document.querySelector('.navbar');
      if (window.scrollY > 50) {
        navbar.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.05)';
        navbar.style.background = 'rgba(255, 255, 255, 0.95)';
      } else {
        navbar.style.boxShadow = 'none';
        navbar.style.background = 'rgba(255, 255, 255, 0.85)';
      }
    });
  </script>
</body>
</html>
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vite + React + TS</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>



@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');


:root {
  --primary: #4361ee;
  --primary-dark: #3a56d4;
  --secondary: #f72585;
  --dark: #1d3557;
  --light: #f8f9fa;
  --gray: #6c757d;
  --light-gray: #e9ecef;
  --success: #4cc9f0;
  --danger: #e63946;
  --warning: #ff9e00;
  --border-radius: 8px;
  --shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  --transition: all 0.3s ease;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Poppins', sans-serif;
  background-color: #85b6ff;
  color: #333;
  line-height: 1.6;
}

a {
  text-decoration: none;
  color: inherit;
}

button {
  cursor: pointer;
  font-family: 'Poppins', sans-serif;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Layout utilities */
.flex {
  display: flex;
}

.flex-col {
  flex-direction: column;
}

.items-center {
  align-items: center;
}

.justify-between {
  justify-content: space-between;
}

.gap-4 {
  gap: 1rem;
}

.gap-8 {
  gap: 2rem;
}

.mt-4 {
  margin-top: 1rem;
}

.mt-8 {
  margin-top: 2rem;
}

.mb-4 {
  margin-bottom: 1rem;
}

.mb-8 {
  margin-bottom: 2rem;
}

.p-4 {
  padding: 1rem;
}

.p-6 {
  padding: 1.5rem;
}

.rounded {
  border-radius: var(--border-radius);
}

.shadow {
  box-shadow: var(--shadow);
}

.bg-white {
  background-color: white;
}

.text-center {
  text-align: center;
}

/* Buttons */
.btn {
  padding: 10px 20px;
  border-radius: var(--border-radius);
  border: none;
  font-weight: 500;
  transition: var(--transition);
}

.btn-primary {
  background-color: var(--primary);
  color: white;
}

.btn-primary:hover {
  background-color: var(--primary-dark);
}

.btn-outline {
  background-color: transparent;
  border: 1px solid var(--primary);
  color: var(--primary);
}

.btn-outline:hover {
  background-color: var(--primary);
  color: white;
}

/* Forms */
.form-group {
  margin-bottom: 1.5rem;
}

.form-label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.form-input,
.form-textarea,
.form-select {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1px solid #ddd;
  border-radius: var(--border-radius);
  font-size: 1rem;
  transition: var(--transition);
}

.form-input:focus,
.form-textarea:focus,
.form-select:focus {
  outline: none;
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(67, 97, 238, 0.2);
}

.form-textarea {
  min-height: 120px;
  resize: vertical;
}

/* Dashboard */
.dashboard {
  display: grid;
  grid-template-columns: 250px 1fr;
  gap: 2rem;
  padding: 2rem 0;
}

.sidebar {
  background-color: white;
  border-radius: var(--border-radius);
  padding: 1.5rem;
  box-shadow: var(--shadow);
  height: fit-content;
}

.sidebar-nav {
  list-style: none;
}

.sidebar-link {
  display: flex;
  align-items: center;
  padding: 0.75rem 1rem;
  border-radius: var(--border-radius);
  margin-bottom: 0.5rem;
  transition: var(--transition);
}

.sidebar-link:hover,
.sidebar-link.active {
  background-color: var(--light);
  color: var(--primary);
}

.main-content {
  flex: 1;
}

.card {
  background-color: white;
  border-radius: var(--border-radius);
  padding: 1.5rem;
  box-shadow: var(--shadow);
  margin-bottom: 1.5rem;
}

.card-header {
  padding-bottom: 1rem;
  border-bottom: 1px solid var(--light-gray);
  margin-bottom: 1.5rem;
}

/* Content history */
.content-list {
  list-style: none;
}

.content-item {
  padding: 1rem;
  border-bottom: 1px solid var(--light-gray);
  transition: var(--transition);
}

.content-item:hover {
  background-color: var(--light);
}

.content-meta {
  display: flex;
  gap: 1rem;
  margin-top: 0.5rem;
  font-size: 0.875rem;
  color: var(--gray);
}

/* Platform selector */
.platform-selector {
  margin-bottom: 1.5rem;
}

.platform-options {
  display: flex;
  gap: 1.5rem;
  margin-top: 0.5rem;
}

.platform-option {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

/* Home page */
.hero {
  min-height: 80vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 4rem 1rem;
  background: linear-gradient(135deg, #f5f7fa 0%, #e4edf9 100%);
}

.hero h1 {
  font-size: 3.5rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  line-height: 1.2;
}

.hero p {
  font-size: 1.25rem;
  max-width: 700px;
  margin: 0 auto 2rem;
  color: var(--gray);
}

.cta-button {
  padding: 12px 30px;
  font-size: 1.1rem;
  border-radius: 50px;
}

.features {
  padding: 5rem 1rem;
}

.feature-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-top: 3rem;
}

.feature-card {
  background: white;
  border-radius: var(--border-radius);
  padding: 2rem;
  box-shadow: var(--shadow);
  transition: var(--transition);
  text-align: center;
}

.feature-card:hover {
  transform: translateY(-5px);
}

.feature-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
  color: var(--primary);
}

/* Login page */
.login-page {
  min-height: 100vh;
  display: flex;
}

.login-container {
  display: flex;
  width: 100%;
  min-height: 100vh;
}

.login-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 2rem;
  max-width: 500px;
  margin: 0 auto;
}

.login-image {
  flex: 1;
  background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 2rem;
  color: white;
  text-align: center;
}

.login-image h2 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.login-image p {
  max-width: 500px;
}

.clerk-signin {
  margin-top: 2rem;
  width: 100%;
}

/* Responsive */
@media (max-width: 992px) {
  .dashboard {
    grid-template-columns: 1fr;
  }
  
  .sidebar {
    display: none;
  }
}

@media (max-width: 768px) {
  .hero h1 {
    font-size: 2.5rem;
  }
  
  .login-container {
    flex-direction: column;
  }
  
  .login-image {
    padding: 3rem 1rem;
  }
}




/* Modern Professional CSS Redesign */
:root {
  --primary: #4361ee;
  --primary-dark: #3a56d4;
  --primary-light: #eef2ff;
  --secondary: #f72585;
  --accent: #4cc9f0;
  --success: #2ecc71;
  --warning: #ff9e00;
  --error: #e63946;
  --dark: #1d3557;
  --darker: #0f172a;
  --light: #f8f9fa;
  --light-gray: #e9ecef;
  --medium-gray: #94a3b8;
  --border-radius: 12px;
  --border-radius-sm: 8px;
  --shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
  --shadow-sm: 0 4px 12px rgba(0, 0, 0, 0.05);
  --transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
  --glass-bg: rgba(255, 255, 255, 0.85);
}

/* Reset and Base Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  background: linear-gradient(135deg, #f5f7fa 0%, #e4edf9 100%);
  color: var(--darker);
  line-height: 1.6;
  min-height: 100vh;
  background-attachment: fixed;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Modern Typography */
h1, h2, h3, h4, h5 {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-weight: 700;
  line-height: 1.2;
  margin-bottom: 1.5rem;
}

h1 {
  font-size: 3.5rem;
  letter-spacing: -0.03em;
}

h2 {
  font-size: 2.5rem;
  letter-spacing: -0.02em;
}

h3 {
  font-size: 1.75rem;
}

p {
  font-size: 1.125rem;
  line-height: 1.7;
  color: var(--dark);
  margin-bottom: 1.5rem;
}

/* Layout Utilities */
.container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 2rem;
}

.flex {
  display: flex;
}

.flex-col {
  flex-direction: column;
}

.items-center {
  align-items: center;
}

.justify-center {
  justify-content: center;
}

.justify-between {
  justify-content: space-between;
}

.gap-4 {
  gap: 1rem;
}

.gap-6 {
  gap: 1.5rem;
}

.gap-8 {
  gap: 2rem;
}

.gap-12 {
  gap: 3rem;
}

.mt-6 {
  margin-top: 1.5rem;
}

.mt-8 {
  margin-top: 2rem;
}

.mt-12 {
  margin-top: 3rem;
}

.mb-6 {
  margin-bottom: 1.5rem;
}

.mb-8 {
  margin-bottom: 2rem;
}

.mb-12 {
  margin-bottom: 3rem;
}

.p-6 {
  padding: 1.5rem;
}

.p-8 {
  padding: 2rem;
}

.rounded-xl {
  border-radius: var(--border-radius);
}

.rounded-lg {
  border-radius: var(--border-radius-sm);
}

.shadow-lg {
  box-shadow: var(--shadow);
}

.shadow-md {
  box-shadow: var(--shadow-sm);
}

.bg-glass {
  background: var(--glass-bg);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.5);
}

.bg-white {
  background-color: white;
}

.text-center {
  text-align: center;
}

/* Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.875rem 2rem;
  border-radius: var(--border-radius-sm);
  border: none;
  font-weight: 600;
  font-family: 'Inter', sans-serif;
  font-size: 1rem;
  transition: var(--transition);
  cursor: pointer;
  text-decoration: none;
  gap: 0.5rem;
}

.btn-primary {
  background: var(--primary);
  background: linear-gradient(90deg, var(--primary) 0%, var(--accent) 100%);
  color: white;
  box-shadow: 0 4px 12px rgba(67, 97, 238, 0.3);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(67, 97, 238, 0.4);
}

.btn-outline {
  background: transparent;
  border: 2px solid var(--primary);
  color: var(--primary);
}

.btn-outline:hover {
  background: rgba(67, 97, 238, 0.05);
}

/* Hero Section */
.hero {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  padding-top: 5rem;
  position: relative;
  overflow: hidden;
}

.hero::before {
  content: "";
  position: absolute;
  top: -50%;
  right: -10%;
  width: 800px;
  height: 800px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(67, 97, 238, 0.15) 0%, rgba(76, 201, 240, 0.05) 70%, transparent 100%);
  z-index: -1;
}

.hero-content {
  max-width: 800px;
  margin: 0 auto;
  position: relative;
  z-index: 2;
}

.hero-title {
  font-size: 3.75rem;
  line-height: 1.1;
  margin-bottom: 1.5rem;
  background: linear-gradient(90deg, var(--primary) 0%, var(--accent) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-subtitle {
  font-size: 1.5rem;
  font-weight: 400;
  color: var(--dark);
  max-width: 700px;
  margin: 0 auto 2.5rem;
}

/* Features Grid */
.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-top: 4rem;
}

.feature-card {
  background: var(--glass-bg);
  backdrop-filter: blur(12px);
  border-radius: var(--border-radius);
  padding: 2.5rem 2rem;
  border: 1px solid rgba(255, 255, 255, 0.5);
  transition: var(--transition);
  box-shadow: var(--shadow-sm);
  text-align: left;
}

.feature-card:hover {
  transform: translateY(-8px);
  box-shadow: var(--shadow);
  border-color: rgba(67, 97, 238, 0.15);
}

.feature-icon {
  width: 64px;
  height: 64px;
  background: linear-gradient(135deg, rgba(67, 97, 238, 0.1) 0%, rgba(76, 201, 240, 0.1) 100%);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.5rem;
}

.feature-icon i {
  font-size: 1.75rem;
  color: var(--primary);
}

.feature-title {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: var(--darker);
}

.feature-description {
  font-size: 1.05rem;
  color: var(--dark);
}

/* Navbar */
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  padding: 1.5rem 0;
  z-index: 100;
  background: var(--glass-bg);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.7);
  transition: var(--transition);
}

.navbar-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 1.75rem;
  font-weight: 800;
  color: var(--primary);
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.logo span {
  color: var(--darker);
}

.nav-links {
  display: flex;
  gap: 2.5rem;
  align-items: center;
}

.nav-link {
  text-decoration: none;
  color: var(--darker);
  font-weight: 500;
  transition: var(--transition);
  position: relative;
  padding: 0.25rem 0;
}

.nav-link:hover {
  color: var(--primary);
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--primary);
  transition: var(--transition);
}

.nav-link:hover::after {
  width: 100%;
}

.user-section {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

/* Responsive */
@media (max-width: 992px) {
  .navbar {
    padding: 1.25rem 0;
  }
  
  .nav-links {
    gap: 1.5rem;
  }
  
  h1 {
    font-size: 3rem;
  }
  
  h2 {
    font-size: 2.25rem;
  }
}

@media (max-width: 768px) {
  .navbar-container {
    flex-direction: column;
    gap: 1.5rem;
  }
  
  .hero-title {
    font-size: 2.75rem;
  }
  
  .hero-subtitle {
    font-size: 1.25rem;
  }
  
  .features-grid {
    grid-template-columns: 1fr;
  }
  
  .nav-links {
    flex-wrap: wrap;
    justify-content: center;
  }
  
  .container {
    padding: 0 1.5rem;
  }
}

@media (max-width: 576px) {
  .hero-title {
    font-size: 2.25rem;
  }
  
  .hero-subtitle {
    font-size: 1.1rem;
  }
  
  .btn {
    width: 100%;
  }
  
  .feature-card {
    padding: 2rem 1.5rem;
  }
}

/* Animation */
@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-12px); }
  100% { transform: translateY(0px); }
}

.floating {
  animation: float 4s ease-in-out infinite;
}