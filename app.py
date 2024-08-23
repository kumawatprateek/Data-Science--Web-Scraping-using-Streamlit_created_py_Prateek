import streamlit as st
import requests
from bs4 import BeautifulSoup
import urllib.parse


def fetch_doctor_profiles(location, specialization):
    encoded_specialization = urllib.parse.quote(
        f'[{{"word":"{specialization}","autocompleted":true,"category":"subspeciality"}}]')
    base_url = f"https://www.practo.com/search/doctors?results_type=doctor&q={encoded_specialization}&city={location}&page="
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    profiles = []
    page_number = 1

    while True:
        response = requests.get(base_url + str(page_number), headers=headers)
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, 'html.parser')

        if page_number == 1:
            total_count_element = soup.find("h1", class_="u-xx-large-font u-bold")
            total_count = total_count_element.text.strip() if total_count_element else "No data available."

        doctor_cards = soup.find_all("div", class_="info-section")
        if not doctor_cards:
            break

        for card in doctor_cards:
            profile = {
                "name": card.find("h2", {"data-qa-id": "doctor_name"}).text.strip() if card.find("h2", {
                    "data-qa-id": "doctor_name"}) else "N/A",
                "specialization": card.find("div", class_="u-d-flex").text.strip() if card.find("div",
                                                                                                class_="u-d-flex") else "N/A",
                "experience": card.find("div", {"data-qa-id": "doctor_experience"}).text.strip() if card.find("div", {
                    "data-qa-id": "doctor_experience"}) else "N/A",
                "clinic_name": card.find("span", {"data-qa-id": "doctor_clinic_name"}).text.strip() if card.find("span",
                                                                                                                 {
                                                                                                                     "data-qa-id": "doctor_clinic_name"}) else "N/A",
                "practice_locality": card.find("span", {"data-qa-id": "practice_locality"}).text.strip() if card.find(
                    "span", {"data-qa-id": "practice_locality"}) else "N/A",
                "consultation_fees": card.find("span", {"data-qa-id": "consultation_fee"}).text.strip() if card.find(
                    "span", {"data-qa-id": "consultation_fee"}) else "N/A",
            }
            profiles.append(profile)

        page_number += 1

    return total_count, profiles


# Streamlit configuration
st.set_page_config(page_title="Doctor Finder ", page_icon="👨‍⚕️", layout="wide")

# Style for Streamlit app
st.markdown("""
    <style>
        body { font-family: 'Arial', sans-serif; background-color: #f0f4f8; }
        .stApp { background-color: #7b61ff; }
        .css-1d391kg { background-color: #007bff; color: white; }
        .stTextInput input, .stSelectbox select { width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #ccc; }
        .stButton button { background-color: #28a745; color: white; padding: 12px 24px; border-radius: 5px; font-size: 16px; }
        .stButton button:hover { background-color: #218838; }
        .main-container { background-color: #12a4ff; border-radius: 10px; box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2); padding: 30px; margin: 20px; }
        .profile-card { background-color: #fafafa; border: 1px solid #ddd; border-radius: 8px; padding: 15px; margin-bottom: 15px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }
        .profile-card h3 { color: #007bff; }
        .profile-card p { color: #555; }
    </style>
""", unsafe_allow_html=True)

# Sidebar for inputs
st.sidebar.header("Search Parameters")
location_input = st.sidebar.text_input("Enter Location (e.g., Bangalore):")
specializations_list = [
    "Cardiologist", "Rheumatologist ","Dentist", "Dermatologist", "ENT Specialist", "General Physician",
    "Gynecologist", "Neurologist", "Orthopedic","Hematologist ", "Pediatrician", "Psychiatrist",
    "Radiologist", "Urologist", "Oncologist"
]
specialization_input = st.sidebar.selectbox("Select Specialization:", specializations_list)

# Main content
st.title("Doctor Finder 👨‍⚕️")
st.markdown("### Find Doctors in over Area")

with st.container():
    st.markdown("""
        <div class="main-container">
            Use this tool to find doctors based on location and specialization. Enter the details and click "Search" to see the results.
        </div>
    """, unsafe_allow_html=True)

    if st.sidebar.button("Search"):
        if location_input and specialization_input:
            with st.spinner("Fetching data..."):
                count, profiles = fetch_doctor_profiles(location_input, specialization_input)
                st.success(f"Total number of doctors found: {count}")

                if profiles:
                    st.subheader("Doctor Profiles")
                    for profile in profiles:
                        st.markdown(f"""
                            <div class="profile-card">
                                <h3>{profile['name']}</h3>
                                <p><strong>Specialization:</strong> {profile['specialization']}</p>
                                <p><strong>Experience:</strong> {profile['experience']}</p>
                                <p><strong>Clinic Name:</strong> {profile['clinic_name']}</p>
                                <p><strong>Practice Locality:</strong> {profile['practice_locality']}</p>
                                <p><strong>Consultation Fees:</strong> {profile['consultation_fees']}</p>
                            </div>
                        """, unsafe_allow_html=True)
                else:
                    st.warning("No doctor profiles were found.")
        else:
            st.error("Please provide both location and specialization.")

st.markdown("------")
st.markdown("Developed by Prateek Kumawat")
