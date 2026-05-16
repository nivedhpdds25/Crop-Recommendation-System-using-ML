import streamlit as st
import pickle
import numpy as np

# 1. MUST BE FIRST: Set up the page config so Streamlit Cloud can initialize paths correctly
st.set_page_config(page_title="Crop Predictor", page_icon="🌱")

st.title("🌱 Smart Crop Recommendation")
st.markdown("Enter the soil details below to find the best crop to grow.")

# 2. Load the bundled data safely using an absolute fallback path check
try:
    with open('model.pkl', 'rb') as f:
        data = pickle.load(f)
    model = data['model']
    names = data['names']
except Exception as e:
    st.error("❌ Model file ('model.pkl') not found! Please ensure 'model.pkl' is uploaded to the main directory of your GitHub repository.")
    st.stop()  # Stops execution safely so the rest of the app doesn't crash with a NameError

st.markdown("---")

# 3. Creating columns for a cleaner UI
col1, col2 = st.columns(2)

with col1:
    n = st.number_input("Nitrogen (N)", 0, 150, 50)
    p = st.number_input("Phosphorus (P)", 0, 150, 50)
    k = st.number_input("Potassium (K)", 0, 250, 50)
    ph = st.number_input("Soil pH Level", 0.0, 14.0, 6.5)

with col2:
    t = st.number_input("Temperature (°C)", 0.0, 50.0, 25.0)
    h = st.number_input("Humidity (%)", 0.0, 100.0, 80.0)
    r = st.number_input("Rainfall (mm)", 0.0, 300.0, 100.0)

st.markdown("---")

# 4. Prediction Logic
if st.button("Predict Best Crop", type="primary"):
    try:
        features = np.array([[n, p, k, t, h, ph, r]])
        prediction_index = model.predict(features)[0]
        
        # SUCCESS: Converts the numeric index back to the crop name string
        predicted_crop = names[prediction_index]
        
        st.success(f"### Result: The best crop is **{predicted_crop.upper()}**")
    except Exception as e:
        st.error(f"Prediction failed. Error details: {e}")
