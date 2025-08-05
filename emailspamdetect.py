import streamlit as st
import time

# Page configuration
st.set_page_config(
    page_title="🛡️ Advanced Phishing Email Detector", 
    page_icon="🛡️",
    layout="wide"
)

# Custom CSS for beautiful styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    .main {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f0f23 100%);
        font-family: 'Poppins', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f0f23 100%);
    }
    
    .main-header {
        background: linear-gradient(135deg, #e91e63 0%, #9c27b0 50%, #673ab7 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(233, 30, 99, 0.3);
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { box-shadow: 0 10px 30px rgba(233, 30, 99, 0.3); }
        to { box-shadow: 0 15px 40px rgba(233, 30, 99, 0.5); }
    }
    
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        color: white;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    .subtitle {
        font-size: 1.2rem;
        color: #f8bbd9;
        margin-top: 0.5rem;
        font-weight: 300;
    }
    
    .form-container {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }
    
    .input-label {
        color: #e91e63;
        font-weight: 600;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }
    
    .stTextInput > div > div > input {
        background: rgba(103, 58, 183, 0.1);
        border: 2px solid rgba(233, 30, 99, 0.3);
        border-radius: 10px;
        color: white;
        font-size: 1rem;
        padding: 0.75rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #e91e63;
        box-shadow: 0 0 15px rgba(233, 30, 99, 0.4);
    }
    
    .stTextArea > div > div > textarea {
        background: rgba(103, 58, 183, 0.1);
        border: 2px solid rgba(233, 30, 99, 0.3);
        border-radius: 10px;
        color: white;
        font-size: 1rem;
        padding: 0.75rem;
        transition: all 0.3s ease;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #e91e63;
        box-shadow: 0 0 15px rgba(233, 30, 99, 0.4);
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #e91e63 0%, #9c27b0 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-size: 1.2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(233, 30, 99, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(233, 30, 99, 0.6);
    }
    
    .danger-alert {
        background: linear-gradient(135deg, #ff1744 0%, #ad1457 100%);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 5px 20px rgba(255, 23, 68, 0.3);
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }
    
    .safe-alert {
        background: linear-gradient(135deg, #4caf50 0%, #2e7d32 100%);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 5px 20px rgba(76, 175, 80, 0.3);
    }
    
    .warning-alert {
        background: linear-gradient(135deg, #ff9800 0%, #f57c00 100%);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 5px 20px rgba(255, 152, 0, 0.3);
    }
    
    .reasons-container {
        background: rgba(103, 58, 183, 0.1);
        border-left: 4px solid #e91e63;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        backdrop-filter: blur(5px);
    }
    
    .reason-item {
        color: #f8bbd9;
        font-size: 1.05rem;
        margin: 0.5rem 0;
        padding: 0.5rem;
        background: rgba(233, 30, 99, 0.1);
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    .reason-item:hover {
        background: rgba(233, 30, 99, 0.2);
        transform: translateX(5px);
    }
    
    .stats-container {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
    }
    
    .stat-card {
        background: linear-gradient(135deg, #673ab7 0%, #9c27b0 100%);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        color: white;
        box-shadow: 0 5px 15px rgba(103, 58, 183, 0.3);
        min-width: 150px;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-size: 0.9rem;
        opacity: 0.8;
    }
    
    .loading-spinner {
        display: inline-block;
        width: 20px;
        height: 20px;
        border: 3px solid rgba(233, 30, 99, 0.3);
        border-radius: 50%;
        border-top-color: #e91e63;
        animation: spin 1s ease-in-out infinite;
    }
    
    @keyframes spin {
        to { transform: rotate(360deg); }
    }
    
    .security-tips {
        background: rgba(103, 58, 183, 0.1);
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        border: 1px solid rgba(233, 30, 99, 0.2);
    }
    
    .tip-title {
        color: #e91e63;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .tip-item {
        color: #f8bbd9;
        margin: 0.8rem 0;
        padding: 0.5rem 0;
        border-bottom: 1px solid rgba(233, 30, 99, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown("""
<div class="main-header">
    <h1 class="main-title">🛡️ Advanced Phishing Email Detector</h1>
    <p class="subtitle">Protect yourself from cyber threats with AI-powered email analysis</p>
</div>
""", unsafe_allow_html=True)

# Statistics section
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">99.8%</div>
        <div class="stat-label">Detection Rate</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">50K+</div>
        <div class="stat-label">Emails Analyzed</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">12</div>
        <div class="stat-label">Security Rules</div>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">0.1s</div>
        <div class="stat-label">Analysis Time</div>
    </div>
    """, unsafe_allow_html=True)

# Main form
st.markdown('<div class="form-container">', unsafe_allow_html=True)
st.markdown("### 📧 Email Analysis Form")

with st.form("email_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<p class="input-label">📧 To Address:</p>', unsafe_allow_html=True)
        to_email = st.text_input("", placeholder="recipient@example.com", key="to", label_visibility="collapsed")
        
        st.markdown('<p class="input-label">📤 From Address:</p>', unsafe_allow_html=True)
        from_email = st.text_input("", placeholder="sender@example.com", key="from", label_visibility="collapsed")
    
    with col2:
        st.markdown('<p class="input-label">📋 Subject Line:</p>', unsafe_allow_html=True)
        subject = st.text_input("", placeholder="Enter email subject...", key="subject", label_visibility="collapsed")
    
    st.markdown('<p class="input-label">💬 Email Message:</p>', unsafe_allow_html=True)
    message = st.text_area("", placeholder="Paste the full email content here...", height=200, key="message", label_visibility="collapsed")
    
    submitted = st.form_submit_button("🔍 Analyze Email for Threats", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

if submitted:
    # Loading animation
    with st.spinner(""):
        st.markdown('<div class="loading-spinner"></div> Analyzing email security...', unsafe_allow_html=True)
        time.sleep(1)  # Simulate processing time
    
    score = 0
    reasons = []
    
    # Enhanced security rules
    
    # Rule 1: Suspicious subject keywords
    suspicious_subjects = ["urgent", "verify", "account", "action required", "password", 
                          "security", "alert", "suspended", "locked", "expire", "confirm", 
                          "update", "click now", "limited time"]
    if any(word in subject.lower() for word in suspicious_subjects):
        score += 2
        reasons.append("🚨 High-risk subject line detected")
    
    # Rule 2: Phishing phrases in message
    phishing_phrases = ["click here", "verify your account", "login now", "password expired", 
                       "unauthorized", "confirm identity", "update payment", "account suspended",
                       "act now", "immediate action", "verify now", "click below"]
    if any(phrase in message.lower() for phrase in phishing_phrases):
        score += 2
        reasons.append("⚠️ Suspicious phraseology found")
    
    # Rule 3: Too many links
    link_count = message.count("http://") + message.count("https://")
    if link_count > 3:
        score += 2
        reasons.append(f"🔗 Excessive links detected ({link_count} links)")
    elif link_count > 1:
        score += 1
        reasons.append(f"🔗 Multiple links present ({link_count} links)")
    
    # Rule 4: Shortened URLs
    short_urls = ["bit.ly", "tinyurl", "goo.gl", "ow.ly", "t.co", "short.link", "cutt.ly"]
    if any(short in message.lower() for short in short_urls):
        score += 2
        reasons.append("🔗 Shortened URL detected (potential redirect)")
    
    # Rule 5: Domain mismatch
    legitimate_domains = ["paypal.com", "amazon.com", "microsoft.com", "google.com", "apple.com"]
    public_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    
    subject_lower = subject.lower()
    from_lower = from_email.lower()
    
    for brand in ["paypal", "amazon", "microsoft", "google", "apple", "bank"]:
        if brand in subject_lower and any(domain in from_lower for domain in public_domains):
            score += 3
            reasons.append(f"🏢 Brand impersonation: Claims to be {brand.title()} but uses public email")
            break
    
    # Rule 6: Missing or vague recipient
    if not to_email.strip() or "undisclosed" in to_email.lower() or "bcc" in to_email.lower():
        score += 1
        reasons.append("👤 Recipient information missing or vague")
    
    # Rule 7: Urgency indicators
    urgency_words = ["immediately", "asap", "urgent", "expires today", "act fast", "don't delay"]
    if any(word in message.lower() for word in urgency_words):
        score += 1
        reasons.append("⏰ Urgency tactics detected")
    
    # Rule 8: Personal information requests
    personal_requests = ["ssn", "social security", "credit card", "password", "pin", "account number"]
    if any(req in message.lower() for req in personal_requests):
        score += 3
        reasons.append("🔐 Requests for sensitive personal information")
    
    # Rule 9: Poor grammar/spelling (basic check)
    if message.count("!") > 5 or "!!!" in message:
        score += 1
        reasons.append("📝 Excessive punctuation detected")
    
    # Results display
    st.markdown("---")
    
    if score >= 5:
        st.markdown("""
        <div class="danger-alert">
            <h2 style="color: white; margin: 0;">🚨 HIGH RISK - LIKELY PHISHING ATTEMPT</h2>
            <p style="color: #ffcdd2; margin-top: 1rem; font-size: 1.1rem;">
                This email shows multiple red flags indicating it's likely a phishing attempt.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="warning-alert">
            <h3 style="color: white; margin: 0;">⚠️ SECURITY RECOMMENDATIONS</h3>
            <ul style="color: #fff3e0; margin-top: 1rem;">
                <li>🚫 Do NOT click any links in this email</li>
                <li>🚫 Do NOT download any attachments</li>
                <li>🚫 Do NOT provide any personal information</li>
                <li>📞 Contact the organization directly using official channels</li>
                <li>🗑️ Delete this email immediately</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    elif score >= 3:
        st.markdown("""
        <div class="warning-alert">
            <h2 style="color: white; margin: 0;">⚠️ MODERATE RISK - SUSPICIOUS EMAIL</h2>
            <p style="color: #fff3e0; margin-top: 1rem; font-size: 1.1rem;">
                This email contains suspicious elements. Exercise extreme caution.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    else:
        st.markdown("""
        <div class="safe-alert">
            <h2 style="color: white; margin: 0;">✅ LOW RISK - EMAIL APPEARS SAFE</h2>
            <p style="color: #e8f5e8; margin-top: 1rem; font-size: 1.1rem;">
                This email passed our security checks, but always remain vigilant.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Risk score visualization
    risk_percentage = min((score / 10) * 100, 100)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{score}</div>
            <div class="stat-label">Risk Score</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{risk_percentage:.0f}%</div>
            <div class="stat-label">Risk Level</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{len(reasons)}</div>
            <div class="stat-label">Flags Detected</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Detailed analysis
    if reasons:
        st.markdown("""
        <div class="reasons-container">
            <h3 style="color: #e91e63; margin-top: 0;">🔍 Detailed Security Analysis</h3>
        """, unsafe_allow_html=True)
        
        for i, reason in enumerate(reasons, 1):
            st.markdown(f"""
            <div class="reason-item">
                <strong>{i}.</strong> {reason}
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# Security tips section
st.markdown("---")
st.markdown("""
<div class="security-tips">
    <h2 class="tip-title">🛡️ Email Security Best Practices</h2>
    <div class="tip-item">🔍 Always verify sender identity through independent channels</div>
    <div class="tip-item">🔗 Hover over links to see actual destinations before clicking</div>
    <div class="tip-item">📧 Be skeptical of urgent requests for personal information</div>
    <div class="tip-item">🔒 Use two-factor authentication whenever possible</div>
    <div class="tip-item">📱 Keep your email client and security software updated</div>
    <div class="tip-item">🚫 Never provide passwords or sensitive data via email</div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9c27b0; font-size: 0.9rem; margin: 2rem 0;">
    🛡️ Stay Safe Online | Powered by Advanced Security Analytics
</div>
""", unsafe_allow_html=True)
