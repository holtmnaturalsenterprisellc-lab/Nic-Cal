import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="NicCalc", page_icon="💸", layout="centered")

GOOGLE_SHEET_URL = "https://script.google.com/macros/s/AKfycbx2-fRD3o7CUOIDPb3UiGzJKKpurjxqxsCpLTyr4Kz1Mj1E5PloTr_gtjAWdzI6NfsIRg/exec"

st.markdown("# 💸 NicCalc")
st.markdown("### How much has vaping already cost you?")
st.markdown("---")

vapes_per_week = st.number_input("Vapes per week", min_value=1, max_value=30, value=3, step=1)
cost_per_vape = st.number_input("Cost per vape ($)", min_value=1, max_value=100, value=18, step=1)
years_vaping = st.number_input("Years vaping", min_value=1, max_value=20, value=2, step=1)

spent_to_date = vapes_per_week * cost_per_vape * 52 * years_vaping
saved_in_1_year = vapes_per_week * cost_per_vape * 52

def what_you_could_buy(amount):
    if amount >= 3500:
        return "✈️ Round-trip flights to Europe — twice"
    elif amount >= 2500:
        return "💻 A MacBook Pro"
    elif amount >= 1500:
        return "📱 Latest iPhone + AirPods"
    elif amount >= 800:
        return "🎮 A PS5 + 5 games"
    elif amount >= 400:
        return "🎧 AirPods Pro + a weekend getaway"
    elif amount >= 150:
        return "🍕 50 large pizzas"
    else:
        return "☕ A month of daily artisan coffee"

st.markdown("---")
st.metric(label="💰 Total spent to date", value=f"${spent_to_date:,.0f}")
st.metric(label="📅 You'd save in 1 year if you quit", value=f"${saved_in_1_year:,.0f}")

st.markdown(f"""
<div style="background:#fff3cd; padding:1rem; border-radius:10px;
border-left:5px solid #ff6b35; margin:1rem 0;">
  <strong>🛍️ What ${spent_to_date:,.0f} could buy instead:</strong><br><br>
  <span style="font-size:1.2rem">{what_you_could_buy(spent_to_date)}</span>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div style="background:#f9f9f9; border-left:4px solid #ff6b35; border-radius:8px;
padding:1.2rem 1.5rem; margin:1.5rem 0;">
  <p style="font-size:1.1rem; font-style:italic; color:#333; margin:0 0 10px;">
    "I bought this to quit smoking. It was the ticket I was looking for."
  </p>
  <p style="font-size:0.9rem; color:#888; margin:0;">
    ⭐⭐⭐⭐⭐ &nbsp;&nbsp; <strong>Robin M.</strong> — Verified Buyer
  </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 📧 Get your free 30-Day Quit Plan by email")

email = st.text_input("Enter your email address", placeholder="you@example.com")
consent = st.checkbox("I agree to receive emails from Burst Bar")

if st.button("Send me the Quit Plan →"):
    if not email:
        st.warning("Please enter your email address.")
    elif "@" not in email or "." not in email:
        st.warning("Please enter a valid email address.")
    elif not consent:
        st.warning("Please check the box to continue.")
    else:
        try:
            payload = {
                "email": email,
                "vapes_per_week": vapes_per_week,
                "cost_per_vape": cost_per_vape,
                "years_vaping": years_vaping
            }
            response = requests.post(GOOGLE_SHEET_URL, json=payload)
            st.success("✅ You're in! Check your inbox for the Burst Quit Plan.")
        except Exception as ex:
            st.error("Something went wrong. Please try again.")

st.markdown(f"""
<div style="background:#ff6b35; padding:1.8rem; border-radius:14px;
text-align:center; margin-top:1.5rem;">
  <p style="color:white; font-size:1.1rem; margin:0 0 6px;">
    Ready to quit for good?
  </p>
  <p style="color:rgba(255,255,255,0.9); font-size:0.95rem; margin:0 0 16px;">
    The <strong>Burst B-12 Diffuser + 30-Day Quit Plan</strong> has helped
    1,000+ people replace vaping. You could save
    <strong>${saved_in_1_year:,.0f} this year alone.</strong>
  </p>
  <a href="https://shopburstbar.com/quit-plan"
     style="background:white; color:#ff6b35; font-weight:700; font-size:1rem;
     padding:12px 28px; border-radius:8px; text-decoration:none; display:inline-block;">
    Get the Burst Quit Bundle →
  </a>
  <p style="color:rgba(255,255,255,0.75); font-size:0.8rem; margin:12px 0 0;">
    shopburstbar.com
  </p>
</div>
""", unsafe_allow_html=True)
