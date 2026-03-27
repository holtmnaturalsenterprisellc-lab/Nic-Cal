import streamlit as st

st.set_page_config(page_title="NicCalc", page_icon="💸", layout="centered")

# ── Styling ──────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;700&display=swap');
  html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif; }
  .big-number { font-size: 3rem; font-weight: 700; color: #FF4500; }
  .callout { background: #1a1a2e; color: #eee; border-radius: 16px;
             padding: 1.5rem; margin: 1rem 0; border-left: 5px solid #FF4500; }
  .cta-box  { background: #FF4500; border-radius: 16px; padding: 2rem;
              text-align: center; margin-top: 2rem; }
  .cta-box a { color: white; font-size: 1.2rem; font-weight: 700;
               text-decoration: none; }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.title("💸 NicCalc")
st.subheader("How much has vaping already cost you?")
st.markdown("---")

# ── Inputs ────────────────────────────────────────────────────────────────────
col1, col2, col3 = st.columns(3)
with col1:
    vapes_per_week = st.number_input("Vapes per week", min_value=0.5, max_value=30.0,
                                      value=3.0, step=0.5)
with col2:
    cost_per_vape = st.number_input("Cost per vape ($)", min_value=1.0, max_value=100.0,
                                     value=15.0, step=1.0)
with col3:
    years_vaping = st.number_input("Years vaping", min_value=0.5, max_value=20.0,
                                    value=2.0, step=0.5)

# ── Calculations ──────────────────────────────────────────────────────────────
spent_to_date   = vapes_per_week * cost_per_vape * 52 * years_vaping
saved_in_1_year = vapes_per_week * cost_per_vape * 52

# ── What you could buy instead ────────────────────────────────────────────────
def what_you_could_buy(amount):
    if amount >= 3500:
        return "✈️ A round-trip flight to Europe — *twice*"
    elif amount >= 2500:
        return "💻 A MacBook Pro"
    elif amount >= 1500:
        return "📱 The latest iPhone + AirPods"
    elif amount >= 800:
        return "🎮 A PS5 + 5 games"
    elif amount >= 400:
        return "🎧 AirPods Pro + a weekend getaway"
    elif amount >= 150:
        return "🍕 50 large pizzas (the good kind)"
    else:
        return "☕ A month of daily artisan coffee"

st.markdown("---")

# ── Results ───────────────────────────────────────────────────────────────────
st.markdown("### 📊 Your Numbers")

c1, c2 = st.columns(2)
with c1:
    st.markdown("**💰 Total spent to date**")
    st.markdown(f'<p class="big-number">${spent_to_date:,.0f}</p>', unsafe_allow_html=True)
with c2:
    st.markdown("**📅 You'd save in 1 year if you quit**")
    st.markdown(f'<p class="big-number">${saved_in_1_year:,.0f}</p>', unsafe_allow_html=True)

# Callout
buy_instead = what_you_could_buy(spent_to_date)
st.markdown(f"""
<div class="callout">
  <strong>🛍️ What ${spent_to_date:,.0f} could buy instead:</strong><br><br>
  <span style="font-size:1.3rem">{buy_instead}</span>
</div>
""", unsafe_allow_html=True)

# ── CTA Block ─────────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="background:#ff6b35; padding:1.8rem; border-radius:14px; 
text-align:center; margin-top:1rem;">
  <p style="color:white; font-size:1.1rem; margin:0 0 6px;">
    Ready to quit for good?
  </p>
  <p style="color:rgba(255,255,255,0.9); font-size:0.95rem; margin:0 0 16px;">
    The <strong>Burst B-12 Diffuser + 30-Day Quit Plan</strong> has helped 
    1,000+ people replace vaping. You could save 
    <strong>${saved_in_1_year:,.0f} this year alone.</strong>
  </p>
  <a href="https://shopburstbar.com" 
     style="background:white; color:#ff6b35; font-weight:700; font-size:1rem;
     padding:12px 28px; border-radius:8px; text-decoration:none; display:inline-block;">
    Get the Burst Quit Bundle →
  </a>
  <p style="color:rgba(255,255,255,0.75); font-size:0.8rem; margin:12px 0 0;">
    shopburstbar.com
  </p>
</div>
""", unsafe_allow_html=True)
