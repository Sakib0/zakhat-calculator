import streamlit as st
import pandas as pd

# Islamic UI Theme Styling
st.markdown("""
    <style>
    body {
        background-color: #f8f9fa;
    }
    .main {
        background-color: #fefefe;
    }
    .stButton>button {
        background-color: #2ecc71;
        color: white;
        font-size: 16px;
        border-radius: 8px;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #27ae60;
        color: white;
    }
    .stNumberInput>div>input {
        border-radius: 10px;
        padding: 8px;
        font-size: 16px;
    }
    .stTitle {
        color: #27ae60;
        font-size: 38px;
        text-align: center;
    }
    .stMarkdown h3 {
        color: #2c3e50;
    }
    </style>
""", unsafe_allow_html=True)

# App Title & Image
st.image("zakhat.png", width=100)  # Replace with your own logo if desired
st.title("🌙 Zakat Calculator")
#st.markdown("### Calculate your annual zakat with ease. Compliant with Islamic financial principles.")

# --- Manual Input Section ---
st.header("🧾 Enter Your Assets")
cash = st.number_input("Cash on Hand (BDT)", min_value=0.0, step=100.0)
gold = st.number_input("Gold (in grams)", min_value=0.0, step=0.1)
silver = st.number_input("Silver (in grams)", min_value=0.0, step=0.1)
business_assets = st.number_input("Business Assets (BDT)", min_value=0.0, step=100.0)
investments = st.number_input("Investments (BDT)", min_value=0.0, step=100.0)
receivables = st.number_input("Receivables / Loans Given (BDT)", min_value=0.0, step=100.0)

st.header("💳 Enter Your Liabilities")
liabilities = st.number_input("Payable Debts / Liabilities (BDT)", min_value=0.0, step=100.0)

# --- CSV Upload Section ---
st.markdown("#### 📤 Or Upload a CSV File (Optional)")
uploaded_file = st.file_uploader("Upload your asset/liability sheet", type=["csv"])
df = None
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("CSV Uploaded Successfully!")
    st.write(df)

# --- Nisab Threshold ---
nisab_per_gram = 9400  # Adjust according to real-time price
nisab_gold_85g = nisab_per_gram * 85
st.markdown(f"### 🕌 Nisab Threshold: {nisab_gold_85g:,.0f} BDT (Based on 85g gold @ {nisab_per_gram:,} BDT/g)")

# --- Calculate Zakat ---
if st.button("🧮 Calculate Zakat"):
    # Convert gold/silver to BDT
    gold_value = gold * nisab_per_gram
    silver_value = silver * 120  # Approx rate per gram for silver

    total_assets = cash + gold_value + silver_value + business_assets + investments + receivables
    net_assets = total_assets - liabilities

    if net_assets >= nisab_gold_85g:
        zakat_due = net_assets * 0.025
        st.success(f"✅ Zakat is applicable. You owe: {zakat_due:,.0f} BDT")
        st.markdown(f"**Total Zakatable Wealth**: {net_assets:,.0f} BDT")
    else:
        st.info("ℹ️ Your wealth is below the Nisab threshold. Zakat is not obligatory.")

# --- Footer ---
st.markdown("---")
st.markdown("### 💡 Note:")
st.markdown("This calculator is for educational purposes. Please consult a qualified scholar for personalized advice.")