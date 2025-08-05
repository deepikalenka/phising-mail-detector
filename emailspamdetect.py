import streamlit as st
import re

st.set_page_config(page_title="Phishing Email Detector", layout="centered", page_icon="🔐")

# Custom CSS for enhanced styling
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .detector-container {
        background: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .title-container {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(45deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        color: #6c5ce7;
        font-size: 1.2rem;
        font-weight: 500;
        margin-bottom: 1rem;
    }
    
    .feature-badge {
        display: inline-block;
        background: linear-gradient(45deg, #a29bfe, #6c5ce7);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        font-size: 0.9rem;
        margin: 0.2rem;
        font-weight: 500;
    }
    
    .input-section {
        background: #f8f9ff;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        border: 2px solid #e9ecef;
    }
    
    .analyze-button {
        background: linear-gradient(45deg, #00b894, #00cec9) !important;
        color: white !important;
        border: none !important;
        padding: 0.8rem 2rem !important;
        border-radius: 25px !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 5px 15px rgba(0,184,148,0.3) !important;
    }
    
    .analyze-button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 25px rgba(0,184,148,0.4) !important;
    }
    
    .result-safe {
        background: linear-gradient(45deg, #00b894, #55efc4);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 10px 20px rgba(0,184,148,0.2);
    }
    
    .result-danger {
        background: linear-gradient(45deg, #e84393, #fd79a8);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 10px 20px rgba(232,67,147,0.2);
    }
    
    .reason-item {
        background: rgba(255,255,255,0.9);
        padding: 0.8rem;
        margin: 0.5rem 0;
        border-radius: 10px;
        border-left: 4px solid #6c5ce7;
        color: #2d3436;
    }
    
    .footer-info {
        text-align: center;
        margin-top: 2rem;
        color: rgba(255,255,255,0.8);
        font-weight: 500;
    }
    
    .security-icons {
        text-align: center;
        font-size: 2rem;
        margin: 1rem 0;
    }
    
    .divider {
        height: 2px;
        background: linear-gradient(45deg, #667eea, #764ba2);
        border: none;
        border-radius: 2px;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
<div class="detector-container">
    <div class="title-container">
        <h1 class="main-title">🔐 Phishing Email Detector</h1>
        <p class="subtitle">Fortinet-Inspired Rule-Based Filter | Real-Time Detection</p>
        <div>
            <span class="feature-badge">AI-Free Analysis</span>
            <span class="feature-badge">Real-Time Detection</span>
            <span class="feature-badge">Case Study Ready</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# Form layout with enhanced styling
st.markdown('<div class="input-section">', unsafe_allow_html=True)
with st.form("email_form", clear_on_submit=False):
    st.markdown("### 📧 Email Analysis Form")
    
    col1, col2 = st.columns(2)
    with col1:
        to_email = st.text_input("📥 To:", placeholder="recipient@example.com")
        from_email = st.text_input("📤 From:", placeholder="sender@example.com")
    with col2:
        subject = st.text_input("📝 Subject:", placeholder="Enter email subject")
        st.write("")  # Spacing
    
    message = st.text_area("💬 Email Message:", height=200, placeholder="Paste the email content here...")
    
    st.markdown("<br>", unsafe_allow_html=True)
    submitted = st.form_submit_button("🔍 Analyze Email", use_container_width=True, type="primary")

st.markdown('</div>', unsafe_allow_html=True)

# Phishing detection function (unchanged)
def detect_phishing_email(to_email, from_email, subject, message):
    score = 0
    reasons = []

    if not all([to_email, from_email, subject, message]):
        return "Invalid Input", ["❗ Please fill in all fields."]

    from_email = from_email.lower()
    subject = subject.lower()
    message = message.lower()

    # Subject
    subject_keywords = [
        "verify your account", "account locked", "suspended", "urgent",
        "action required", "limited time", "unusual activity", "unauthorized login",
        "your account has been", "security alert", "final warning", "reset password",
        "payment failure", "bank alert", "confirm identity", "blocked"
    ]
    if any(kw in subject for kw in subject_keywords):
        score += 1
        reasons.append("⚠️ Suspicious subject line detected")

    # Message
    message_keywords = [
        "confirm your identity", "click the link", "multiple failed login",
        "restore access", "update your account", "security notice",
        "validate information", "suspend", "won a prize", "send your id",
        "bank account", "atm card", "aadhar", "passport", "urgent response",
        "reset your password", "click below", "log in here", "verify now",
        "click to continue", "account verification", "payment declined"
    ]
    if any(kw in message for kw in message_keywords):
        score += 1
        reasons.append("⚠️ Message contains phishing-style content")

    # Shortened URLs
    shortened_domains = ["bit.ly", "tinyurl.com", "shorturl.at", "rb.gy", "ow.ly", "t.co"]
    if any(url in message for url in shortened_domains):
        score += 1
        reasons.append("🔗 Shortened URL detected")

    # Personal info
    personal_info_triggers = ["aadhar", "otp", "bank details", "debit card", "password", "ssn", "cvv"]
    if any(pii in message for pii in personal_info_triggers):
        score += 1
        reasons.append("🔐 Request for sensitive personal info")

    # Brand impersonation
    fake_brands = ["paypal", "microsoft", "amazon", "facebook", "google", "apple", "netflix", "bank"]
    if any(brand in from_email for brand in fake_brands) and not any(brand + ".com" in from_email for brand in fake_brands):
        score += 1
        reasons.append("📛 Sender may be impersonating a trusted brand")

    # Domain checks
    legit_domains = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", ".edu", ".org", ".gov", ".net", ".com"]
    if not any(domain in from_email for domain in legit_domains):
        score += 1
        reasons.append("📧 Sender domain looks suspicious")

    # Urgency phrases
    urgency_phrases = ["within 24 hours", "act now", "immediately", "before it's too late", "final notice"]
    if any(phrase in message for phrase in urgency_phrases):
        score += 1
        reasons.append("⏱️ Urgent or threatening language")

    # Unknown links
    urls = re.findall(r'http[s]?://[^\s<>"]+|www\.[^\s<>"]+', message)
    if urls:
        for url in urls:
            if not re.search(r"(google|facebook|microsoft|amazon|apple|paypal)\.com", url):
                score += 1
                reasons.append("🌐 Unknown or suspicious link")
                break

    if score >= 2:
        return "Phishing", reasons
    else:
        return "Safe", reasons

# Display result with enhanced styling
if submitted:
    result, reasons = detect_phishing_email(to_email, from_email, subject, message)

    if result == "Invalid Input":
        st.markdown(f"""
        <div style="background: linear-gradient(45deg, #fdcb6e, #e17055); color: white; padding: 1.5rem; border-radius: 15px; text-align: center; margin: 1rem 0;">
            <h3>⚠️ Input Required</h3>
            <p>{reasons[0]}</p>
        </div>
        """, unsafe_allow_html=True)
    elif result == "Phishing":
        st.markdown("""
        <div class="result-danger">
            <h2>🚨 PHISHING DETECTED!</h2>
            <p style="font-size: 1.2rem; margin: 1rem 0;">This email shows multiple phishing indicators</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🔍 Detection Reasons:")
        for reason in reasons:
            st.markdown(f'<div class="reason-item">{reason}</div>', unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="result-safe">
            <h2>✅ EMAIL APPEARS SAFE</h2>
            <p style="font-size: 1.2rem; margin: 1rem 0;">No strong phishing indicators found</p>
        </div>
        """, unsafe_allow_html=True)

    # Security Tips Section
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    
    with st.expander("🛡️ Security Tips & Best Practices"):
        st.markdown("""
        **How to stay safe from phishing:**
        - 🔍 Always verify the sender's email address
        - 🌐 Hover over links before clicking to see the actual URL
        - 🔐 Never share passwords or personal info via email
        - 📞 Contact companies directly if you're unsure about an email
        - 🎯 Be suspicious of urgent or threatening language
        - 💼 Use official websites instead of email links for important accounts
        """)

# Footer
st.markdown("""
<div class="footer-info">
    🔍 AI-Free Real-Time Analysis | Built for Case Studies & Intern Projects<br>
    <small>Enhanced Security Interface • Modern Detection System</small>
</div>
""", unsafe_allow_html=True)
