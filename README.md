# Doctor Finder 👨‍⚕️

**Doctor Finder** is a Streamlit application designed to help users find doctors based on location and specialization by scraping doctor profiles from Practo.com. This project is part of the PaidIntern internship.

## Features

- **Search Doctors:** Allows users to search for doctors by entering a location and selecting a specialization.
- **Profile Details:** Displays detailed information about each doctor including name, specialization, experience, clinic name, practice locality, and consultation fees.
- **User-Friendly Interface:** Features an intuitive and modern user interface with custom styling.

## Installation

To run the Doctor Finder application, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd doctor-finder
   ```

2. **Create a Virtual Environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Required Packages:**

   Make sure you have `pip` installed and run:

   ```bash
   pip install -r requirements.txt
   ```

## Requirements

- **Python 3.7+**
- **Streamlit**
- **Requests**
- **BeautifulSoup4**

## Usage

1. **Run the Application:**

   ```bash
   streamlit run app.py
   ```

2. **Access the App:**

   Open your browser and navigate to `http://localhost:8501` to use the Doctor Finder application.

## Code Explanation

### `fetch_doctor_profiles(location, specialization)`

This function handles the core logic of scraping doctor profiles from Practo.com.

- **Parameters:**
  - `location` (str): The city or location to search for doctors.
  - `specialization` (str): The medical specialization to filter the search.
- **Returns:**
  - `total_count` (str): Total number of doctors found.
  - `profiles` (list of dicts): List of doctor profiles containing details like name, specialization, experience, clinic name, practice locality, and consultation fees.

### Streamlit Configuration

- **Page Setup:**
  Configures the Streamlit page with a title, icon, and layout.
  
- **Sidebar:**
  Provides input fields for location and specialization.
  
- **Main Content:**
  Displays a search form, results, and styling. Shows a loading spinner while fetching data and displays doctor profiles once available.

## Styling

Custom CSS is used to enhance the appearance of the application. This includes:

- Background colors
- Font styles
- Button designs
- Profile card styling

## Contributing

Contributions to the Doctor Finder project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Streamlit** for building the web application framework.
- **Requests** and **BeautifulSoup4** for web scraping.

## Contact

For any inquiries or issues, please contact:

- **Name:** Prateek Kumawat
- **Email:** kumawatprateek008@gmail.com

