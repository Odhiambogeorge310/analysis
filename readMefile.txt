📊 ASSESSMENT DASHBOARD

📋 Project Overview
    The assessment dashboard project analyze written assessment scores done by learners, and generates usefull insights such as learners' populaton count, gender population and scores distribution across all learning areas done in different grades once the rsult uploaded.

🚀 Key Features
    📂 Upload CSV or Excel (.csv, .xlsx, .xls) files for analysis.
        Ensure the excel file type named is as results
    🔗 Try assessment dashboard now on Streamlit Cloud:
    💻 Streamlit web app interface for easy and beautiful use
    ☁️ Access assessment dashboard easily online — no installation needed!

📊 Summary metrics:
    Total learners
    Boys  count
    Girls count

🧮 Subject-wise assessment distribution:
    Bar charts for Mathematics, English, Kiswahili, and Science and Technology.

🥧 Subject-wise composition:
    Pie charts for CRE, Creative Arts, and Social Studies.

📋 Tabular data view with customizable columns.

📈 Descriptive statistics table.

.
├── file.py        # Main Streamlit app script
├── style.css      # Custom styles for the dashboard
├── README.md      # (This file)

📁 File Structure
    file.py        # Main Streamlit app script
    style.css      # Custom styles for the dashboard 
    README.md      # (This file)

🛠️ Setup and Installation
    Clone the repository:
    git clone 
    cd cluster-analysis-dashboard

Create and activate a virtual environment
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

Install the dependencies:
    pip install -r requirements.txt

If you don't have a requirements.txt, based on the script you should install:
    pip install streamlit pandas numpy plotly Pillow streamlit-extras streamlit-option-menu

Run the application:
    streamlit run file.py

🧩 Dependencies
    Streamlit
    Pandas
    NumPy
    Plotly Express
    Pillow
    streamlit-extras
    streamlit-option-menu

📈 Sample Data Format
The uploaded file must contain at least the following columns:
    ID (Learner ID)
    GENDER (Boy/Girl)
    GRADE  (Grade Level)
    MATHS, ENGLISH, KISWAHILI, SCIENCE_TECH, CRE, CREATIVE_ARTS, SST (Assessment Scores)


Example:
| ID | GENDER | GRADE | MATHS | ENGLISH | KISWAHILI | SCIENCE_TECH | CRE | CREATIVE_ARTS | SST |
|----|--------|-------|-------|---------|-----------|--------------|-----|---------------|-----|
| 1  | Boy    | 5     | 3     | 2       | 4         | 3            | 2   | 4             | 3   |

⚠️ Notes
Ensure the uploaded file has the above format of columns, GENDER and GRADE to avoid errors.

The app automatically styles metric cards using a style.css file (you may need to provide or customize it).

📜 License
This project is open-source and available.

Created by George Odhiambo.
(It's all about Asking Data The Right Question)
