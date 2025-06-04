import streamlit as st

st.set_page_config(page_title="Zombie Tech Detector 🇳🇴", layout="centered")

st.title("🧟‍♂️ Zombie Tech Detector – Norway Edition")
st.subheader("Score Norwegian tech companies for signs of strategic decay.")

company = st.text_input("Company Name", "Pexip")

st.markdown("### 📋 Answer the following based on public data:")

rd_flat = st.checkbox("📉 Flat R&D spend over last 3 years?")
revenue_flat = st.checkbox("📉 Flat or declining revenue YoY?")
buybacks = st.checkbox("🔁 Active share buyback program?")
no_product_release = st.checkbox("🛑 No major product release in past 12 months?")
github_stale = st.checkbox("🐢 Last GitHub commit was over 6 months ago?")
exec_turnover = st.checkbox("🚪 2 or more CxO-level executives left in past 18 months?")
partner_dependency = st.checkbox("🤝 Dependent on large US ecosystem (e.g. Microsoft)?")
buzzword_pivot = st.checkbox("📣 Buzzword-heavy comms (e.g., 'replatforming', 'AI pivot')?")

score = sum([
    rd_flat,
    revenue_flat,
    buybacks,
    no_product_release,
    github_stale,
    exec_turnover,
    partner_dependency,
    buzzword_pivot
])

st.markdown("### 🧠 Zombie Score")
st.metric(label=f"{company}", value=score)

if score >= 6:
    st.error("⚠️ Confirmed Zombie – Strategic reinvention needed.")
elif score >= 4:
    st.warning("☠️ Zombie Watchlist – At risk of decay.")
else:
    st.success("🧬 Still Alive – Showing signs of strategic health.")
