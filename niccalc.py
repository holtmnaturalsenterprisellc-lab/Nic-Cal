import streamlit as st
import requests

st.set_page_config(page_title="NicCalc — How Much Has Vaping Cost You?",
                   page_icon="🔥", layout="centered")

GOOGLE_SHEET_URL = "https://docs.google.com/spreadsheets/d/17lBQDG9-kGOvQtfEN1u2ZigNfdQ-b32VYGQpBN_vNaM/edit?gid=0#gid=0"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@400;500;600&display=swap');
html, body, [class*="css"] { background-color: #0d0d0d !important; }
.stApp { background-color: #0d0d0d; }
* { font-family: 'DM Sans', sans-serif; color: #ffffff; }
.block-container { max-width: 560px; padding: 2rem 1rem; }
div[data-testid="stNumberInput"] input {
    background: #161616; border: 1px solid #2a2a2a;
    color: #fff; border-radius: 8px; font-size: 1.1rem;
}
div[data-testid="stTextInput"] input {
    background: #161616; border: 1px solid #2a2a2a;
    color: #fff; border-radius: 8px;
}
.stButton > button {
    background: #ff4500; color: white; border: none;
    border-radius: 8px; font-weight: 600; font-size: 1rem;
    padding: 0.6rem 1.5rem; width: 100%;
}
.stButton > button:hover { background: #e03d00; }
.stCheckbox label { color: #888 !important; font-size: 13px; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; padding: 1.5rem 0 1rem;">
  <div style="font-size:11px; letter-spacing:3px; color:#ff4500; 
  text-transform:uppercase; margin-bottom:10px;">The Real Cost of Vaping</div>
  <div style="font-family:'Bebas Neue',sans-serif; font-size:3.5rem; 
  line-height:1; color:#fff;">NIC<span style="color:#ff4500;">CALC</span></div>
  <div style="font-size:14px; color:#666; margin-top:8px;">
    Type in your habit. See the number that changes everything.
  </div>
</div>
<hr style="border-color:#1e1e1e; margin: 0.5rem 0 1.5rem;">
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    vapes_per_week = st.number_input("Vapes / week", min_value=1, max_value=30, value=3, step=1)
with col2:
    cost_per_vape = st.number_input("Cost per vape ($)", min_value=1, max_value=100, value=15, step=1)
with col3:
    years_vaping = st.number_input("Years vaping", min_value=1, max_value=20, value=2, step=1)

spent = vapes_per_week * cost_per_vape * 52 * years_vaping
saved = vapes_per_week * cost_per_vape * 52

def buy(n):
    if n >= 3500: return "✈️ Round-trip flights to Europe — twice"
    if n >= 2500: return "💻 A MacBook Pro"
    if n >= 1500: return "📱 Latest iPhone + AirPods"
    if n >= 800:  return "🎮 A PS5 + 5 games"
    if n >= 400:  return "🎧 AirPods Pro + a weekend trip"
    if n >= 150:  return "🍕 50 large pizzas"
    return "☕ A month of daily artisan coffee"

st.markdown(f"""
<div style="background:#0d0d0d; text-align:center; padding:2rem 0 1rem;">
  <div style="font-size:11px; letter-spacing:3px; color:#555; 
  text-transform:uppercase; margin-bottom:6px;">You have already spent</div>
  <div style="font-family:'Bebas Neue',sans-serif; font-size:5rem; 
  color:#ff4500; line-height:1;">${spent:,.0f}</div>
  <div style="font-size:12px; color:#444; margin-top:4px;">
    on vaping over {years_vaping} year{'s' if years_vaping > 1 else ''}
  </div>
</div>
""", unsafe_allow_html=True)

col4, col5 = st.columns(2)
with col4:
    st.markdown(f"""
    <div style="background:#161616; border:1px solid #222; border-radius:12px; padding:1rem;">
      <div style="font-size:10px; letter-spacing:2px; text-transform:uppercase; 
      color:#555; margin-bottom:6px;">Per year</div>
      <div style="font-family:'Bebas Neue',sans-serif; font-size:1.8rem; 
      color:#fff;">${saved:,.0f}</div>
    </div>""", unsafe_allow_html=True)
with col5:
    st.markdown(f"""
    <div style="background:#161616; border:1px solid #222; border-radius:12px; padding:1rem;">
      <div style="font-size:10px; letter-spacing:2px; text-transform:uppercase; 
      color:#555; margin-bottom:6px;">Save if you quit</div>
      <div style="font-family:'Bebas Neue',sans-serif; font-size:1.8rem; 
      color:#4ade80;">${saved:,.0f}/yr</div>
    </div>""", unsafe_allow_html=True)

st.markdown(f"""
<div style="background:#1a0f00; border:1px solid #3d1f00; border-radius:12px; 
padding:1rem 1.2rem; margin:1rem 0;">
  <div style="font-size:10px; letter-spacing:2px; text-transform:uppercase; 
  color:#854F0B; margin-bottom:4px;">Instead you could have bought</div>
  <div style="font-size:15px; font-weight:600; color:#EF9F27;">
    {buy(spent)}
  </div>
</div>

<div style="background:#111; border-radius:12px; padding:1rem 1.2rem; 
margin-bottom:1rem; border-left:3px solid #ff4500;">
  <div style="font-size:13px; color:#aaa; font-style:italic; 
  line-height:1.6; margin-bottom:6px;">
    "I bought this to quit smoking. It was the ticket I was looking for."
  </div>
  <div style="font-size:11px; color:#ff4500; letter-spacing:1px; 
  text-transform:uppercase;">Robin M. — Verified Buyer &nbsp;★★★★★</div>
</div>

<div style="background:#ff4500; border-radius:12px; padding:1.4rem; 
text-align:center; margin:1rem 0 1.5rem;">
  <div style="font-size:12px; color:rgba(255,255,255,0.7); margin-bottom:4px;">
    Keep ${saved:,.0f}/year in your pocket
  </div>
  <div style="font-family:'Bebas Neue',sans-serif; font-size:1.4rem; 
  color:#fff; letter-spacing:1px;">Ready to quit for good?</div>
  <div style="margin-top:10px;">
    <a href="https://shopburstbar.com/quit-plan" 
    style="background:#fff; color:#ff4500; font-weight:600; font-size:13px;
    padding:10px 24px; border-radius:8px; text-decoration:none; 
    display:inline-block; letter-spacing:0.5px;">
      Get the Burst Quit Bundle — Free 30-Day Plan →
    </a>
  </div>
</div>

<hr style="border-color:#1e1e1e; margin:1rem 0;">
""", unsafe_allow_html=True)

st.markdown("""
<div style="font-size:11px; letter-spacing:2px; text-transform:uppercase; 
color:#555; margin-bottom:8px;">Get your free quit plan by email</div>
""", unsafe_allow_html=True)

email = st.text_input("", placeholder="you@example.com", label_visibility="collapsed")
consent = st.checkbox("I agree to receive emails from Burst Bar")

if st.button("Send me the Quit Plan →"):
    if not email or "@" not in email:
        st.warning("Please enter a valid email address.")
    elif not consent:
        st.warning("Please check the box to continue.")
    else:
        try:
            requests.post(GOOGLE_SHEET_URL, json={
                "email": email,
                "vapes_per_week": vapes_per_week,
                "cost_per_vape": cost_per_vape,
                "years_vaping": years_vaping
            })
            st.success("You're in! Check your inbox for the Burst Quit Plan.")
        except:
            st.error("Something went wrong. Please try again.")
