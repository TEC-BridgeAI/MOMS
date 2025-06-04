<template>
  <div class="tecbridge-home">
    <!-- Hero Section -->
    <section class="hero">
      <div class="container">
        <div class="hero-content">
          <img src="@/assets/logo.png" alt="TEC-Bridge Logo" class="logo">
          <div>
            <h1>TEC-Bridge AI</h1>
            <p>Bridging Technology, Education, and Culture with AI</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Our Services -->
    <section class="services">
      <div class="container">
        <h2>Our Services</h2>
        <div class="services-grid">
          <div class="service-card">
            <h3>Internship</h3>
            <p>Gain practical experience and professional skills through our structured internship programs in technology and business fields.</p>
          </div>
          <div class="service-card">
            <h3>Education Services</h3>
            <p>Access quality education resources and programs designed to enhance learning outcomes and develop critical skills.</p>
          </div>
          <div class="service-card">
            <h3>Business Support</h3>
            <p>Receive comprehensive assistance for business development, including technology integration, strategy, and operational improvements.</p>
          </div>
          <div class="service-card">
            <h3>Cross-Cultural Connection</h3>
            <p>Bridge cultural gaps through programs that foster understanding, collaboration, and global perspective development.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Why Choose Us -->
    <section class="why-choose">
      <div class="container">
        <h2>Why Choose TEC-Bridge AI</h2>
        <div class="reasons-grid">
          <div class="reason-card">
            <h3>Expertise</h3>
            <p>Team of AI and technology experts</p>
          </div>
          <div class="reason-card">
            <h3>Innovation</h3>
            <p>Cutting-edge solutions for modern challenges</p>
          </div>
          <div class="reason-card">
            <h3>Results</h3>
            <p>Proven track record of successful implementations</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Programs -->
    <section class="programs">
      <div class="container">
        <h2>Programs</h2>
        <div class="programs-grid">
          <div class="program-card">
            <h3>Student Internship</h3>
            <p>Offering valuable work experience and mentorship opportunities for students in various fields of technology and business.</p>
          </div>
          <div class="program-card">
            <h3>Research & Development</h3>
            <p>Conducting innovative research projects that advance technology solutions and address real-world challenges.</p>
          </div>
          <div class="program-card">
            <h3>Community Services</h3>
            <p>Supporting communities through technology education, digital literacy programs, and accessible tech solutions.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- About -->
    <section class="about">
      <div class="container">
        <h2>About TEC-Bridge AI</h2>
        <p>TEC-Bridge AI is dedicated to bridging the gap between technology, education, and culture with AI solutions that drive real results for organizations of all sizes.</p>
        <p>Our mission is to make advanced AI technology accessible and beneficial for businesses across industries.</p>
      </div>
    </section>

    <!-- Footer -->
    <footer>
      <div class="container">
        <p>&copy; 2025 TEC-Bridge AI. All rights reserved.</p>
        <div class="footer-links">
          <router-link to="/login">Login</router-link>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'TecBridgeHome'
}
</script>

<style scoped>
.tecbridge-home {
  font-family: 'Arial', sans-serif;
  color: #333;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.hero {
  background-color: #0066cc;
  color: white;
  padding: 80px 0;
}

.hero-content {
  display: flex;
  align-items: center;
  justify-content: center;
}

.logo {
  width: 100px;
  height: auto;
  margin-right: 20px;
}

.hero h1 {
  font-size: 3rem;
  margin: 0;
}

section {
  padding: 60px 0;
}

section h2 {
  text-align: center;
  margin-bottom: 40px;
  color: #0066cc;
}

.services-grid, .reasons-grid, .programs-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
}

.service-card, .reason-card, .program-card {
  background-color: #f5f5f5;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.about {
  background-color: #f9f9f9;
}

footer {
  background-color: #333;
  color: white;
  padding: 30px 0;
  text-align: center;
}

.footer-links {
  margin-top: 10px;
}

.footer-links a {
  color: #fff;
  text-decoration: none;
}

.footer-links a:hover {
  text-decoration: underline;
}
</style>