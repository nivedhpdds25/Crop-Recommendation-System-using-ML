# Crop Recommendation System Using Soil and Climate Data

Team Members:
- Ashliya M Riyaz (MSc Data Science with Specialization in Computational Sciences)
- P D Nivedh (MSc Data Science and BioAI)
- Bainty Kaur Chugh (MSc Data Science and Geoinformatics)

## Work Distribution
- **P D Nivedh** - Data Collection, Data Preprocessing and Cleaning, Exploratory Data Analysis, README.md

- **Bainty Kaur Chugh** - Feature Engineering, Model Development and Model Comparison

- **Ashliya M Riyaz** - Deployment, Model Interpretation and Explainability

## Problem Statement & Motivation

Agriculture is one of the most critical sectors for food security, yet farmers often struggle to determine which crop is best suited for their land. Choosing the wrong crop based on incorrect assumptions about soil or climate conditions can lead to poor yields and economic loss. This project aims to address that by building a machine learning-based Crop Recommendation System that takes in soil nutrient levels and climate conditions as inputs and recommends the most suitable crop for farming. By leveraging data-driven insights, this system can empower farmers to make informed decisions and improve agricultural productivity.

Dataset Description

Source: Kaggle — madhuraatmarambhagat/crop-recommendation-dataset (downloaded via kagglehub)
File: Crop_recommendation.csv
Size: 2,200 samples × 8 columns

Target: label — crop type (22 classes, 100 samples each)
Class Distribution: Balanced — each of the 22 crop types has exactly 100 samples
Data Preprocessing & Exploratory Data Analysis (EDA)
Overview

This section covers the initial data loading, inspection, and exploratory data analysis performed on the Crop Recommendation dataset. The goal was to understand the structure of the data, identify patterns across features, and visualize how different soil and climate conditions relate to various crops.

Dataset
The dataset was downloaded directly from Kaggle using the kagglehub library:

Source: madhuraatmarambhagat/crop-recommendation-dataset
File: Crop_recommendation.csv
Features: N, P, K, temperature, humidity, ph, rainfall
Target: label (crop type)


Steps Performed
1. Dataset Loading

The dataset was downloaded via kagglehub and copied into the working directory for easy access.

2. Basic EDA

Initial inspection of the dataset included:

* Shape and structure of the data
* First few rows using .head()
* Data types and null value checks using .info() and .isnull().sum()
* Statistical summary using .describe()
* Class distribution using .value_counts() on the label column

3. Feature Distributions

Histograms were plotted for all 7 features to understand the spread and distribution of values across the dataset. Saved as feature_distributions.png.

4. Correlation Heatmap

A heatmap was generated to analyze the correlation between all numerical features, helping identify which features are strongly or weakly related to each other. Saved as correlation_heatmap.png.

5. Samples per Crop

A count plot was created to visualize how many data samples exist for each crop type, confirming a balanced dataset. Saved as crop_distribution.png.

6. Boxplots per Crop

Boxplots were generated for each feature grouped by crop type, giving insight into how feature values vary across different crops and highlighting outliers. Saved as boxplots_per_crop.png.

7. Pair Plots

Pairplots were created for a sample of 5 crops (rice, maize, wheat, mango, coffee) using the first 4 features, to visualize relationships and cluster separability between crops. Saved as pairplot.png.

8. EDA Folder Organization

All generated visualizations were moved into a dedicated /EDA folder for clean project structure.
## Deployment & Model Serving

- **Responsible Team Member:** Ashliya M Riyaz

To transition the project from a static machine learning model to an interactive, user-facing application, a web-based prediction dashboard was engineered and deployed for live accessibility.

### 1. Model Serialization and Artifact Bundling
Once the **Random Forest Classifier** was selected as the optimal model (achieving 99.4% accuracy), the trained model object was serialized alongside its underlying computational dependencies. 
* **Tool Used:** Python's native `pickle` library.
* **Implementation:** The model was exported into a standalone binary file (`model.pkl`). Crucially, the deployment pipeline was configured to bypass numerical index outputs by mapping categorical class weights directly back to the original text strings of the 22 crop types (e.g., mapping an internal array index output to readable labels like `"PAPAYA"` or `"RICE"`).

### 2. Interface Engineering via Streamlit
An interactive graphical user interface (GUI) was developed to allow non-technical users or researchers to perform real-time inferences.
* **Framework:** Streamlit
* **Input Architecture:** The front-end exposes ergonomic numeric input fields and data sliders matching the 7 exact environmental dimensions required by the feature matrix:
  * **Macronutrients:** Nitrogen ($N$), Phosphorus ($P$), Potassium ($K$)
  * **Climatic Inputs:** Temperature (°C) and Relative Humidity (%)
  * **Environmental Inputs:** Soil pH levels and annual Rainfall (mm)
* **Execution Logic:** When a user clicks the **"Predict Best Crop"** button, the application captures the browser states, constructs a 2D NumPy array matching the training feature shape, and passes the array to the unpickled Random Forest model to instantly output the matching recommendation.

### 3. Secure Tunneling & Global Access via Ngrok
To host the application directly from the transient development environment without complex cloud-infrastructure overhead, a secure network gateway was established.
* **Tool Used:** `pyngrok` (Python wrapper for the Ngrok edge ingress platform)
* **Networking Topology:** Streamlit's local web server natively spins up a loopback socket on `http://localhost:8501`. A secure background token process hooks into this port, creating a public, encrypted reverse proxy link (`https://*.ngrok-free.dev`). This architectural choice makes the live application accessible on any internet-connected smartphone or computing device during live evaluations.
## Web Application Demo

### 🔗 Live Application Access
The interactive dashboard is served via a secure network gateway during live project demonstrations:
* **Live Link:** [Launch Web Application](https://panorama-mockup-sustainer.ngrok-free.dev/)
* *Note: Because free Ngrok tunnel URLs are generated dynamically upon runtime execution, the link is active exclusively during live presentation sessions. For offline evaluation, please follow the local installation guidelines below.*

### Application User Interface
The screenshot below illustrates the functional Streamlit interface executing a live inference, processing input variables to successfully recommend the optimal crop selection:

![Crop Recommendation System App Interface](Screenshot 2026-05-16 070901.png)
