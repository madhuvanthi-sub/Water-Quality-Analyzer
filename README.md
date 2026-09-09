# Water-Quality-Analyzer

A beginner-friendly Python project that analyzes water quality based on
common chemical and physical parameters such as pH, TDS, hardness,
chloride, and turbidity.

The project takes measured water-quality values, compares them with
reference limits, classifies the individual parameters, and displays
the results using an interactive Streamlit dashboard and charts.

> **Note:** This project is created for educational and demonstration
> purposes. The reference limits used in the project should not be
> treated as official drinking-water certification.

---

## Project Overview

Water quality can be evaluated by measuring different physical and
chemical parameters.

This project analyzes:

- pH
- Total Dissolved Solids (TDS)
- Hardness
- Chloride
- Turbidity

The basic workflow is:

```text
Water Sample
     ↓
Enter Measurements
     ↓
Chemical Analysis
     ↓
Compare with Reference Limits
     ↓
Parameter Classification
     ↓
Overall Water Quality
     ↓
Charts and Visualization

## Features

### 1. Water Quality Analysis

The project checks the following parameters:

| Parameter | Unit |
|-----------|------|
| pH | pH scale |
| TDS | mg/L |
| Hardness | mg/L |
| Chloride | mg/L |
| Turbidity | NTU |

### 2. Reference Limit Comparison

The measured values are compared against the reference limits used for this educational project.

| Parameter | Reference Value |
|-----------|-----------------|
| pH | 6.5 – 8.5 |
| TDS | 500 mg/L |
| Hardness | 200 mg/L |
| Chloride | 250 mg/L |
| Turbidity | 5 NTU |

### 3. Water Quality Classification

Each parameter is classified based on the implemented limits.

The application also provides an overall water-quality classification.

Possible overall results include:

- Good
- Moderate
- Poor

### 4. Interactive Dashboard

The project uses Streamlit to provide an interactive interface where the user can enter water sample measurements.

### 5. Data Visualization

The application generates charts comparing:

```text
Measured Value
       vs
Reference Limit
```

Separate charts are provided for:

- pH
- TDS
- Hardness
- Chloride
- Turbidity

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- Streamlit
- CSV

---

## Project Structure

```text
Water-Quality-Analyzer/
│
├── data/
│   └── water_samples.csv
│
├── venv/
│
├── analyzer.py
├── app.py
├── data_test.py
├── test_analyzer.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

### File Description

**`analyzer.py`**

Contains the functions used to analyze the individual water-quality parameters and determine the overall water-quality classification.

**`app.py`**

Contains the Streamlit web application. It accepts water-quality measurements from the user and displays analysis results and charts.

**`data_test.py`**

Tests reading the water sample CSV file using Pandas.

**`test_analyzer.py`**

Tests the water-quality analysis functions.

**`data/water_samples.csv`**

Contains sample water-quality data used by the project.

**`requirements.txt`**

Contains the Python packages required to run the project.

**`.gitignore`**

Contains files and folders that should not be uploaded to GitHub.

---

## How to Run the Project

### Step 1: Clone the Repository

Clone this repository to your computer using Git:

```bash
git clone <your-github-repository-url>
```

Then move into the project folder:

```bash
cd Water-Quality-Analyzer
```

---

### Step 2: Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv venv
```

---

### Step 3: Activate the Virtual Environment

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

You should see:

```text
(venv)
```

at the beginning of your terminal.

---

### Step 4: Install the Required Packages

Run:

```bash
pip install -r requirements.txt
```

---

### Step 5: Run the Streamlit Application

The main application is `app.py`.

Run:

```bash
streamlit run app.py
```

Streamlit will provide a local address such as:

```text
http://localhost:8501
```

Open that address in your browser.

---

## Testing the Project

### Test the Analyzer

Run:

```bash
python test_analyzer.py
```

This tests the water-quality analysis functions.

### Test CSV Data Reading

Run:

```bash
python data_test.py
```

This checks whether Pandas can successfully read the water sample CSV file.

---

## Current Analysis Parameters

### pH

The project currently uses a reference range of:

```text
6.5 – 8.5
```

Values within this range are considered normal for the purposes of this project.

### TDS

Reference limit:

```text
500 mg/L
```

### Hardness

Reference limit:

```text
200 mg/L
```

### Chloride

Reference limit:

```text
250 mg/L
```

### Turbidity

Reference limit:

```text
5 NTU
```

---

## Limitations

This project is an educational implementation and has several limitations.

- It does not perform real laboratory testing.
- The user must provide the measured values.
- The reference limits are simplified for this project.
- Water quality depends on many additional parameters that are not currently analyzed.
- The results should not be used as official confirmation that water is safe to drink.
- The charts are intended for visualization and comparison.

---

## Future Improvements

Possible future improvements include:

- Uploading CSV files through the Streamlit interface
- Adding more water-quality parameters
- Adding historical sample analysis
- Improving the visual design of the dashboard
- Adding downloadable analysis reports
- Adding more detailed recommendations
- Adding additional data visualizations
- Adding a database for storing water samples
- Improving the overall water-quality scoring system

---

## Project Status

Current progress:

- [x] Python analyzer functions
- [x] Water-quality classification
- [x] Sample CSV dataset
- [x] Pandas CSV testing
- [x] Streamlit interface
- [x] Measured value vs reference limit charts
- [ ] Downloadable reports
- [ ] Additional visualizations
- [ ] Final dashboard improvements

---

## Disclaimer

This project is intended for learning and demonstration purposes only.

It is not a substitute for professional laboratory water-quality testing or official drinking-water standards.