<template>
  <div class="tecbridge-home">
    <!-- Hero Section -->
    <section class="hero">
      <div class="container">
        <div class="hero-content">
          <img src="@/assets/logo.png" alt="TEC-Bridge Logo" class="logo">
          <div>
            <h1>TEC-Bridge AI</h1>
            <p>Serving in Technology, Education, and Culture</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Our Services -->
    <section class="services">
      <div class="container">
        <h2>Services</h2>
        <div class="services-grid">
          <div class="service-card">
            <h3>Education Services</h3>
            <p>At TEC-Bridge AI, we advance education with Internsthip and through AI-driven research and development. Our solutions enhance teaching, optimize learning, and foster cross-cultural communication. By integrating intelligent tools like adaptive learning systems and language translation technologies, we empower educators and students while creating a more inclusive, efficient, and engaging learning environment.</p>
          </div>
          <div class="service-card">
            <h3>Business Support</h3>
            <p>At TEC-Bridge AI, we empower businesses with advanced AI solutions, including data analytics and visualization for informed decision-making and cloud migration for seamless operations. Our services enhance cybersecurity, automate workflows using traditional, generative, and agentic AI, and support secure website development. These tools drive efficiency, innovation, and growth in a competitive digital landscape.</p>
          </div>
          <div class="service-card">
            <h3>Community Services</h3>
            <p>At TEC-Bridge AI, we foster cross-cultural connections through our community engagement program, and develop tools to promote communication such as natural language translation, we break down language barriers for seamless communication. We aim to promote cultural understanding, encouraging respect and collaboration in diverse communities. These innovations empower individuals and organizations to thrive in a globally connected world.</p>
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
            <p>Join us at TEC-Bridge AI for an exciting opportunity to apply for our internship program! Whether you're a current student or a recent graduate, we invite you to become part of a dynamic team where you can gain hands-on experience in the field of AI. This is your chance to enhance your skills, network with industry professionals, and contribute to innovative projects that are shaping the future. Don't miss the opportunity to kickstart your career—apply today!</p>
          </div>
          <div class="program-card">
            <h3>Research & Development</h3>
            <p>While we are developing our own apps and platforms, we invite business operators to partner with us in developing AI-based apps, APIs, or agents tailored to your unique needs. Our research and development specializes in creating innovative solutions that can enhance your operations elevate customer experiences. Let us help you streamline your processes and drive growth in your business. Join us in transforming your ideas into powerful digital that will set you apart in the market.</p>
          </div>
          <div class="program-card">
            <h3>Community Engagement</h3>
            <p>TEC-Bridge AI is committed to fostering cross-cultural connections and enriching communities through our support of diverse cultural and artistic initiatives. We actively engage in partnerships with events such as the Lion's Music Scholarship Competition, International Children's Festivals, Asian Festivals, and Spring Festivals. By supporting these events, we contribute to cultural appreciation, inclusivity, and the empowerment of future generations through music, arts, and community collaboration.</p>
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

    <!-- About -->
    <section class="about">
      <div class="container">
        <h2>About Us</h2>
        <p>We are TEC-Bridge—a collective of individuals from diverse fields, united by a shared vision. Our team includes experienced IT professional and professor, innovative music artist and teacher, dynamic business performers, and ambitious college graduates, all driven by a singular goal: harnessing the transformative power of artificial intelligence to uplift and strengthen our community. By bridging the gap between cutting-edge technology and real-world impact, we aim to create solutions that foster connection, efficiency, and progress. TEC-Bridge AI stands at the crossroads of expertise and aspiration, working together to shape a smarter, more inclusive future.</p>
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