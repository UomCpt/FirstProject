import React from 'react';
import './LandingPage.css';
import Image from '../assets/codingImage.png';
import Header from '../Components/Header';
import Footer from '../Components/Footer';


function LandingPage() {
  return (
    <div className="landing-page">
      
      <Header />

      {/* Hero Section */}
      <section className="hero">
        <h1>Ready to compete?</h1>
        <p>Press the button and start working on the tests!</p>
        <button className="start-button">START CODING</button>
      </section>

      {/* Info Section */}
      <section className="info-section">
        <div className="info-image">
          <img src={Image} alt="Code" />
        </div>
        <div className="info-text">
          <h2>How It Works</h2>
          <p>
            We streamline our processes to deliver you the best content services
            and make every piece of copy as effective as possible.
          </p>
          <ul>
            <li>
              <span className="number">1.</span>
              <strong> Fill Out the Form</strong><br />
              Leave your phone number or contact us directly to schedule a conversation with our manager.
            </li>
            <li>
              <span className="number">2.</span>
              <strong> Get Your Free Site Analysis</strong><br />
              We will thoroughly examine your website and prepare a full report with possible improvements.
            </li>
            <li>
              <span className="number">3.</span>
              <strong> Approve the Strategy</strong><br />
              Everything starts with a strategy. When it is approved by you, we start creating content.
            </li>
            <li>
              <span className="number">4.</span>
              <strong> Get Monthly Reports</strong><br />
              We will keep you informed about the results, engagement and conversion rates.
            </li>
          </ul>
        </div>
      </section>

      <Footer />

    </div>
  );
}

export default LandingPage;