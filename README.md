# SignSafe — AI Lease Analyzer

**AI-powered legal protection for renters.** SignSafe analyzes your residential lease, detects illegal clauses, cites the exact statute violated, and generates a demand letter. All in under 30 seconds.

Built with Python, Streamlit, and the Google Gemini 2.5 Flash API.

---

## What It Does

Most renters sign leases without legal representation. SignSafe closes that gap. Upload any PDF lease, select your state and city, and the app will cross-reference every clause against your jurisdiction's tenant protection law. If it finds a violation, an illegal security deposit, an excessive late fee, or a waived right. SignSafe tells you exactly which statute was broken and generates a demand letter you can send directly to your landlord.

**The three-step flow:**

1. **Upload** — Drag and drop any residential lease PDF into the app
2. **Analyze** — The AI audits every clause against your state and city's tenant law
3. **Act** — Review flagged violations and generate a legally-framed demand letter

---

## Tech Stack

- **Frontend:** Streamlit
- **AI Model:** Google Gemini 2.5 Flash API
- **Language:** Python

---

## Running the App Locally

### Prerequisites

- Python 3.9 or higher
- A Google Gemini API key — get one free at [aistudio.google.com](https://aistudio.google.com)

### 1. Clone the repository
```bash
git clone https://github.com/danielpikovskiy/SignSafe-AI-Lease-Analyzer.git
cd SignSafe-AI-Lease-Analyzer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your Gemini API key

Create a file called `.env` in the root of the project and add the following line:
```
GEMINI_API_KEY=your_api_key_here
```

Alternatively, if you're using Streamlit's built-in secrets manager, create a file at `.streamlit/secrets.toml` and add:
```toml
GEMINI_API_KEY = "your_api_key_here"
```

### 4. Run the app
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## How to Use It

1. Open the app in your browser
2. Select your **state** from the dropdown (e.g. California)
3. Select your **city** if applicable (e.g. Los Angeles, for RSO coverage)
4. Upload your lease as a **PDF file**
5. Click **Analyze Lease**
6. Review the violations report — each flagged clause includes the statute number, the violation, and the dollar amount at stake
7. Click **Generate Demand Letter** to produce a letter you can send to your landlord

---

## Current Coverage

SignSafe currently supports the following jurisdictions:

| State | City-Level Overlays |
|---|---|
| California | Los Angeles (RSO), San Francisco |
| New York | New York City (Rent Stabilization) |
| Texas | Austin |
| Florida | Miami-Dade |
| Illinois | Chicago |

---

## Disclaimer

SignSafe is an educational tool. It is not a substitute for legal advice. Always consult a licensed attorney for guidance specific to your situation.

---

## Author

**Daniel Pikovskiy** — UCLA, Business Economics '26  
Built as part of UCLA MGMT 161 · 2026
