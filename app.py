import streamlit as st

# --- DISEASE DATABASE ---
# You can add any disease here. It will automatically create the website sections.
DISEASES = {
    "Endometrial Carcinoma (MI Depth)": {
        "Clinical Factors": ["Age", "Histological Grade (1-3)", "CA-125 Level"],
        "Imaging/Labs": ["MRI Predicted Invasion (%)", "Tumor Diameter (cm)"],
        "Guideline": "If MRI > 50% or Grade 3, recommend Lymphadenectomy."
    },
    "Cervical Cancer (Parametrial Invasion)": {
        "Clinical Factors": ["FIGO Stage", "Vaginal Involvement"],
        "Imaging/Labs": ["MRI Parametrial Status", "Lymph Node Size"],
        "Guideline": "If Parametrial invasion present, consider Chemoradiation over Surgery."
    },
    "General Health Screening": {
        "Clinical Factors": ["Blood Pressure", "BMI", "Smoking Status"],
        "Imaging/Labs": ["HbA1c", "LDL Cholesterol"],
        "Guideline": "Follow standard WHO screening protocols based on risk score."
    }
}

st.set_page_config(page_title="MMC Multi-Disease Validator", layout="wide")
st.title("🏥 Multi-Disease Clinical Decision Support")
st.write("Validation of Preoperative Factors and Imaging across multiple specialties.")

# 1. Select Disease
selected_disease = st.sidebar.selectbox("Select Research/Disease Area", list(DISEASES.keys()))
data = DISEASES[selected_disease]

# 2. Dynamic Layout
col1, col2 = st.columns(2)

with col1:
    st.header("📋 Preoperative Factors")
    for factor in data["Clinical Factors"]:
        st.text_input(f"Enter {factor}")

with col2:
    st.header("🩻 Imaging & Lab Results")
    for lab in data["Imaging/Labs"]:
        st.text_input(f"Enter {lab}")

st.divider()

# 3. Benefits/Logic Section
st.header("🩺 Clinical Benefit & Surgical Insight")
st.info(f"**Research Guidance for {selected_disease}:**\n\n{data['Guideline']}")

st.success("This tool helps decide the surgical depth and necessity by validating clinical data against imaging.")
