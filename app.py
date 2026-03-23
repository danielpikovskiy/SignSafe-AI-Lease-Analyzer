# app.py

import streamlit as st
from legal_knowledge_base import (
    SUPPORTED_STATES, get_violations_for_state,
    get_jurisdiction_context, get_cities_for_state,
)
import google.genai as genai
import PyPDF2
import json
import base64
from pathlib import Path
from datetime import date
from fpdf import FPDF


def load_svg_b64(path):
    """Load an SVG file and return a base64 data URI for use in HTML img tags."""
    svg_bytes = Path(path).read_bytes()
    b64 = base64.b64encode(svg_bytes).decode()
    return f"data:image/svg+xml;base64,{b64}"


LOGO_URI = load_svg_b64(Path(__file__).parent / "signsafe_icon.svg")


# ============================================================
# PAGE CONFIG (must be first Streamlit call)
# ============================================================
st.set_page_config(
    page_title="SignSafe — AI Lease Analyzer",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================
st.markdown("""
<style>
    /* ---- Hide default Streamlit chrome ---- */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}

    /* ---- Background ---- */
    .stApp {
        background-color: #0D1117;
    }
    section[data-testid="stSidebar"] {
        background-color: #0D1117;
        border-right: 1px solid #21262D;
    }

    /* ---- Global text ---- */
    html, body, [class*="css"] {
        color: #E6EDF3;
    }

    /* ---- Hero header ---- */
    .hero {
        padding: 2rem 0 1.5rem 0;
        border-bottom: 1px solid #21262D;
        margin-bottom: 1.5rem;
    }
    .hero-title {
        font-size: 2.4rem;
        font-weight: 800;
        color: #FFFFFF;
        letter-spacing: -0.5px;
        margin: 0;
    }
    .hero-title span {
        color: #4A90D9;
    }
    .hero-subtitle {
        color: #8B949E;
        font-size: 1rem;
        margin-top: 0.4rem;
    }

    /* ---- Sidebar labels ---- */
    .sidebar-label {
        font-size: 0.7rem;
        font-weight: 600;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #8B949E;
        margin-bottom: 0.3rem;
        margin-top: 1.2rem;
    }

    /* ---- State badge ---- */
    .state-badge {
        display: inline-block;
        background: #1F2937;
        border: 1px solid #374151;
        border-radius: 6px;
        padding: 0.3rem 0.75rem;
        font-size: 0.85rem;
        color: #4A90D9;
        font-weight: 600;
        margin-top: 0.5rem;
    }

    /* ---- Section headers ---- */
    .section-header {
        font-size: 1rem;
        font-weight: 700;
        color: #FFFFFF;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin: 1.5rem 0 0.75rem 0;
        padding-bottom: 0.4rem;
        border-bottom: 2px solid #21262D;
    }

    /* ---- Risk banner ---- */
    .risk-banner {
        border-radius: 8px;
        padding: 1rem 1.25rem;
        margin: 1rem 0;
        font-weight: 600;
        font-size: 1rem;
    }
    .risk-high {
        background: rgba(239, 68, 68, 0.12);
        border: 1px solid rgba(239, 68, 68, 0.4);
        color: #FCA5A5;
    }
    .risk-medium {
        background: rgba(245, 158, 11, 0.12);
        border: 1px solid rgba(245, 158, 11, 0.4);
        color: #FCD34D;
    }
    .risk-low {
        background: rgba(34, 197, 94, 0.12);
        border: 1px solid rgba(34, 197, 94, 0.4);
        color: #86EFAC;
    }

    /* ---- Violation card ---- */
    .violation-card {
        background: #161B22;
        border: 1px solid #21262D;
        border-radius: 10px;
        padding: 1.25rem 1.5rem;
        margin-bottom: 1rem;
    }
    .violation-card-header {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        margin-bottom: 0.75rem;
    }
    .violation-title {
        font-weight: 700;
        font-size: 1rem;
        color: #E6EDF3;
    }
    .severity-pill {
        display: inline-block;
        border-radius: 20px;
        padding: 0.15rem 0.6rem;
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }
    .pill-high   { background: rgba(239,68,68,0.2);  color: #FCA5A5; border: 1px solid rgba(239,68,68,0.4); }
    .pill-medium { background: rgba(245,158,11,0.2); color: #FCD34D; border: 1px solid rgba(245,158,11,0.4); }
    .pill-low    { background: rgba(34,197,94,0.2);  color: #86EFAC; border: 1px solid rgba(34,197,94,0.4); }

    .quoted-text {
        background: #0D1117;
        border-left: 3px solid #4A90D9;
        border-radius: 0 6px 6px 0;
        padding: 0.6rem 0.9rem;
        font-size: 0.88rem;
        color: #C9D1D9;
        font-style: italic;
        margin: 0.5rem 0 0.75rem 0;
    }
    .detail-label {
        font-size: 0.7rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.07em;
        color: #8B949E;
        margin-top: 0.6rem;
        margin-bottom: 0.2rem;
    }
    .statute-chip {
        display: inline-block;
        background: #1F2937;
        border: 1px solid #374151;
        border-radius: 5px;
        padding: 0.2rem 0.6rem;
        font-size: 0.8rem;
        color: #93C5FD;
        font-family: monospace;
    }
    .remedy-box {
        background: rgba(34,197,94,0.08);
        border: 1px solid rgba(34,197,94,0.25);
        border-radius: 6px;
        padding: 0.5rem 0.75rem;
        font-size: 0.85rem;
        color: #A7F3D0;
        margin-top: 0.3rem;
    }
    .compliant-box {
        background: rgba(74,144,217,0.08);
        border: 1px solid rgba(74,144,217,0.25);
        border-radius: 6px;
        padding: 0.5rem 0.75rem;
        font-size: 0.85rem;
        color: #BAE6FD;
        margin-top: 0.3rem;
    }

    /* ---- Success card ---- */
    .success-card {
        background: rgba(34,197,94,0.1);
        border: 1px solid rgba(34,197,94,0.35);
        border-radius: 10px;
        padding: 1.5rem;
        text-align: center;
        color: #86EFAC;
        font-size: 1.1rem;
        font-weight: 600;
    }

    /* ---- Letter section ---- */
    .letter-section {
        background: #161B22;
        border: 1px solid #21262D;
        border-radius: 10px;
        padding: 1.5rem;
        margin-top: 1.5rem;
    }

    /* ---- Stat cards ---- */
    .stat-row {
        display: flex;
        gap: 1rem;
        margin: 1rem 0;
    }
    .stat-card {
        flex: 1;
        background: #161B22;
        border: 1px solid #21262D;
        border-radius: 8px;
        padding: 0.9rem 1rem;
        text-align: center;
    }
    .stat-number {
        font-size: 1.6rem;
        font-weight: 800;
        color: #4A90D9;
    }
    .stat-label {
        font-size: 0.75rem;
        color: #8B949E;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-top: 0.2rem;
    }

    /* ---- Safety Score card ---- */
    .score-card {
        background: #161B22;
        border: 1px solid #21262D;
        border-radius: 12px;
        padding: 1.5rem 2rem;
        margin: 1rem 0 1.5rem 0;
        display: flex;
        align-items: center;
        gap: 2.5rem;
    }
    .score-left {
        text-align: center;
        min-width: 110px;
    }
    .score-number {
        font-size: 3.8rem;
        font-weight: 900;
        line-height: 1;
        letter-spacing: -2px;
    }
    .score-grade {
        font-size: 1.1rem;
        font-weight: 700;
        margin-top: 0.2rem;
        letter-spacing: 0.05em;
    }
    .score-right {
        flex: 1;
    }
    .score-title {
        font-size: 1rem;
        font-weight: 700;
        color: #E6EDF3;
        margin-bottom: 0.3rem;
    }
    .score-desc {
        font-size: 0.85rem;
        color: #8B949E;
        margin-bottom: 0.75rem;
    }
    .score-bar-bg {
        background: #21262D;
        border-radius: 999px;
        height: 8px;
        width: 100%;
    }
    .score-bar-fill {
        height: 8px;
        border-radius: 999px;
    }
    .score-breakdown {
        display: flex;
        gap: 1.5rem;
        margin-top: 0.6rem;
        font-size: 0.8rem;
        color: #8B949E;
    }

    /* ---- City badge ---- */
    .city-badge {
        display: inline-block;
        background: #1A2332;
        border: 1px solid #2563EB44;
        border-radius: 6px;
        padding: 0.2rem 0.6rem;
        font-size: 0.75rem;
        color: #93C5FD;
        font-weight: 500;
        margin-top: 0.3rem;
    }

    /* ---- Divider ---- */
    .divider {
        border: none;
        border-top: 1px solid #21262D;
        margin: 1.5rem 0;
    }

    /* ---- Streamlit widget overrides ---- */
    .stButton > button {
        background: #4A90D9;
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        padding: 0.5rem 1.5rem;
        width: 100%;
        transition: background 0.2s;
    }
    .stButton > button:hover {
        background: #357ABD;
        color: white;
    }
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div {
        background: #161B22 !important;
        border: 1px solid #30363D !important;
        color: #E6EDF3 !important;
        border-radius: 8px !important;
    }
    .stFileUploader {
        border: 2px dashed #30363D;
        border-radius: 10px;
        padding: 1rem;
        background: #161B22;
    }
    .stExpander {
        background: #161B22;
        border: 1px solid #21262D;
        border-radius: 8px;
    }
    div[data-testid="stMetricValue"] {
        color: #4A90D9;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.markdown(f"""
        <div style="padding: 1rem 0 0.5rem 0; display:flex; align-items:center; gap:0.6rem;">
            <img src="{LOGO_URI}" width="32" height="32" style="display:block;">
            <span style="font-size:1.5rem; font-weight:800; color:#FFFFFF;">SignSafe</span>
        </div>
        <div style="color:#8B949E; font-size:0.82rem; margin-bottom:1.5rem;">
            AI-Powered Lease Protection
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-label">State / Jurisdiction</div>', unsafe_allow_html=True)
    selected_state = st.selectbox(
        label="State",
        options=SUPPORTED_STATES,
        index=SUPPORTED_STATES.index("California"),
        label_visibility="collapsed"
    )

    st.markdown(f'<div class="state-badge">{selected_state}</div>', unsafe_allow_html=True)

    # City selector — only shown for states with notable local ordinances
    cities = get_cities_for_state(selected_state)
    if cities:
        st.markdown('<div class="sidebar-label">City / Jurisdiction</div>', unsafe_allow_html=True)
        selected_city = st.selectbox(
            label="City",
            options=cities,
            index=0,
            label_visibility="collapsed"
        )
        st.markdown(f'<div class="city-badge">{selected_city}</div>', unsafe_allow_html=True)
    else:
        selected_city = None

    st.markdown("""<hr style="border-color:#21262D; margin: 1.5rem 0;">""", unsafe_allow_html=True)

    violations_db = get_violations_for_state(selected_state)

    high = sum(1 for v in violations_db.values() if v["severity"] == "HIGH")
    med  = sum(1 for v in violations_db.values() if v["severity"] == "MEDIUM")
    low  = sum(1 for v in violations_db.values() if v["severity"] == "LOW")

    st.markdown('<div class="sidebar-label">Violation Database</div>', unsafe_allow_html=True)
    st.markdown(f"""
        <div style="font-size:0.85rem; color:#C9D1D9; line-height:2;">
            <span style="color:#FCA5A5;">&#9679;</span> {high} High severity<br>
            <span style="color:#FCD34D;">&#9679;</span> {med} Medium severity<br>
            <span style="color:#86EFAC;">&#9679;</span> {low} Low severity<br>
            <span style="color:#8B949E;">&#9472;</span> {len(violations_db)} total checks
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""<hr style="border-color:#21262D; margin: 1.5rem 0;">""", unsafe_allow_html=True)
    st.markdown("""
        <div style="font-size:0.75rem; color:#8B949E; line-height:1.6;">
            <strong style="color:#C9D1D9;">Disclaimer</strong><br>
            SignSafe is an educational tool only.
            Always consult a licensed attorney for legal advice.
        </div>
    """, unsafe_allow_html=True)


# ============================================================
# MAIN CONTENT — HEADER
# ============================================================
st.markdown(f"""
    <div class="hero">
        <div style="display:flex; align-items:center; gap:0.75rem;">
            <img src="{LOGO_URI}" width="44" height="44" style="display:block;">
            <div class="hero-title">Sign<span>Safe</span></div>
        </div>
        <div class="hero-subtitle">Upload your lease — we'll find what's illegal before you sign.</div>
    </div>
""", unsafe_allow_html=True)


# ============================================================
# ANALYSIS FUNCTION
# ============================================================
@st.cache_data(show_spinner=False)
def analyze_lease(lease_text, state, city=None):
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    model = 'gemini-2.5-flash'

    jurisdiction_context = get_jurisdiction_context(state, city)
    violations_db = get_violations_for_state(state)

    prompt = f"""You are an expert tenant rights attorney analyzing a residential lease agreement.

JURISDICTION: {jurisdiction_context}

LEASE TEXT TO ANALYZE:
{lease_text}

VIOLATIONS TO CHECK FOR:
"""
    for violation_key, violation_info in violations_db.items():
        prompt += f"""
{violation_info['violation_name']}
- Statute: {violation_info['statute']}
- What to look for: {violation_info['explanation']}
- Trigger keywords: {', '.join(violation_info['trigger_keywords'])}
"""

    prompt += """

INSTRUCTIONS:
For each violation you find in the lease:
1. Quote the EXACT problematic text from the lease
2. Identify which violation it matches
3. Explain clearly why it is illegal under the applicable law
4. Rate the severity (HIGH/MEDIUM/LOW)

Return ONLY valid JSON in this exact format — no markdown, no explanations outside JSON:
{
  "violations_found": [
    {
      "violation_type": "excessive_security_deposit",
      "violation_name": "Excessive Security Deposit",
      "quoted_text": "exact text from lease here",
      "statute": "California Civil Code Section 1950.5",
      "explanation": "why this is illegal",
      "severity": "HIGH"
    }
  ],
  "total_violations": 3,
  "overall_risk": "HIGH"
}

If no violations found, return:
{
  "violations_found": [],
  "total_violations": 0,
  "overall_risk": "LOW"
}
"""

    try:
        response = client.models.generate_content(model=model, contents=prompt)
        response_text = response.text

        if "```json" in response_text:
            response_text = response_text.split("```json")[1].split("```")[0]
        elif "```" in response_text:
            response_text = response_text.split("```")[1].split("```")[0]

        response_text = response_text.strip()
        return json.loads(response_text)

    except json.JSONDecodeError as e:
        st.error(f"Could not parse AI response. Please try again. ({str(e)})")
        return {"violations_found": [], "total_violations": 0, "overall_risk": "UNKNOWN"}
    except Exception as e:
        st.error(f"Error communicating with AI: {str(e)}")
        return {"violations_found": [], "total_violations": 0, "overall_risk": "UNKNOWN"}


# ============================================================
# SAFETY SCORE
# ============================================================
def compute_safety_score(violations_data):
    """Score the lease 0–100 based on violation count and severity."""
    score = 100
    deductions = {"HIGH": 15, "MEDIUM": 8, "LOW": 3}
    for v in violations_data.get("violations_found", []):
        score -= deductions.get(v.get("severity", "MEDIUM"), 8)
    score = max(0, score)

    if score >= 90:
        grade, label, color = "A", "Excellent", "#22C55E"
    elif score >= 75:
        grade, label, color = "B", "Good", "#86EFAC"
    elif score >= 55:
        grade, label, color = "C", "Concerning", "#F59E0B"
    elif score >= 35:
        grade, label, color = "D", "At Risk", "#F97316"
    else:
        grade, label, color = "F", "Dangerous", "#EF4444"

    return score, grade, label, color


def display_safety_score(violations_data):
    score, grade, label, color = compute_safety_score(violations_data)
    total = violations_data.get("total_violations", 0)
    high_c = sum(1 for v in violations_data["violations_found"] if v.get("severity") == "HIGH")
    med_c  = sum(1 for v in violations_data["violations_found"] if v.get("severity") == "MEDIUM")
    low_c  = sum(1 for v in violations_data["violations_found"] if v.get("severity") == "LOW")

    bar_pct = score  # score is already 0-100

    st.markdown(f"""
        <div class="score-card">
            <div class="score-left">
                <div class="score-number" style="color:{color};">{score}</div>
                <div class="score-grade" style="color:{color};">Grade: {grade}</div>
            </div>
            <div class="score-right">
                <div class="score-title">Lease Safety Score &nbsp;·&nbsp;
                    <span style="color:{color};">{label}</span>
                </div>
                <div class="score-desc">
                    {total} violation{"s" if total != 1 else ""} detected · scored out of 100
                </div>
                <div class="score-bar-bg">
                    <div class="score-bar-fill" style="width:{bar_pct}%; background:{color};"></div>
                </div>
                <div class="score-breakdown">
                    <span style="color:#FCA5A5;">{high_c} high (&minus;{high_c*15} pts)</span>
                    <span style="color:#FCD34D;">{med_c} medium (&minus;{med_c*8} pts)</span>
                    <span style="color:#86EFAC;">{low_c} low (&minus;{low_c*3} pts)</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


# ============================================================
# DISPLAY VIOLATIONS
# ============================================================
def severity_pill(severity):
    cls = {"HIGH": "pill-high", "MEDIUM": "pill-medium", "LOW": "pill-low"}.get(severity, "pill-low")
    return f'<span class="severity-pill {cls}">{severity}</span>'

def display_violations(violations_data, state):
    violations_db = get_violations_for_state(state)

    # Always show the score card first
    display_safety_score(violations_data)

    if violations_data['total_violations'] == 0:
        st.markdown("""
            <div class="success-card">
                ✅ &nbsp; No major violations detected — this lease appears compliant.
            </div>
        """, unsafe_allow_html=True)
        return

    st.markdown('<div class="section-header">Violations Detected</div>', unsafe_allow_html=True)

    for i, violation in enumerate(violations_data['violations_found'], 1):
        sev = violation.get('severity', 'MEDIUM')
        violation_key = violation.get('violation_type', '')
        kb_info = violations_db.get(violation_key, {})

        pill = severity_pill(sev)

        v_name   = violation.get('violation_name', violation_key or f'Violation #{i}')
        v_quoted = violation.get('quoted_text', '')
        v_expl   = violation.get('explanation', '')
        v_stat   = violation.get('statute', '')

        with st.expander(f"#{i} — {v_name}", expanded=(i == 1)):
            st.markdown(f"""
                <div class="violation-card-header">
                    {pill}
                    <span style="color:#8B949E; font-size:0.8rem;">Violation #{i}</span>
                </div>
                <div class="detail-label">Problematic clause in your lease</div>
                <div class="quoted-text">"{v_quoted}"</div>
                <div class="detail-label">Why it's illegal</div>
                <div style="font-size:0.88rem; color:#C9D1D9; margin-bottom:0.5rem;">{v_expl}</div>
                <div class="detail-label">Violated statute</div>
                <div style="margin-bottom:0.75rem;"><span class="statute-chip">{v_stat}</span></div>
            """, unsafe_allow_html=True)

            if kb_info:
                st.markdown(f"""
                    <div class="detail-label">What it should say instead</div>
                    <div class="compliant-box">{kb_info.get('compliant_clause_example', '—')}</div>
                    <div class="detail-label">Your rights &amp; next steps</div>
                    <div class="remedy-box">{kb_info.get('tenant_remedy', '—')}</div>
                """, unsafe_allow_html=True)


# ============================================================
# LETTER GENERATION
# ============================================================
def generate_dispute_letter(violations_data, tenant_name, landlord_name, property_address, state):
    violations_db = get_violations_for_state(state)
    today = date.today().strftime("%B %d, %Y")

    letter = f"""{today}

{landlord_name}
{property_address}

Dear {landlord_name},

I am writing to formally notify you of several provisions in the lease agreement for the above-referenced property that appear to violate applicable {state} tenant protection laws.

After careful review, I have identified the following legal issues:

"""
    for i, violation in enumerate(violations_data['violations_found'], 1):
        violation_key = violation.get('violation_type', '')
        kb_info = violations_db.get(violation_key, {})

        v_name = violation.get('violation_name', violation_key or f'Violation {i}')
        letter += f"""{i}. {v_name.upper()}

Lease states: "{violation.get('quoted_text', '')}"

Legal Issue: {violation.get('explanation', '')}

Statutory Authority: {violation.get('statute', '')}
{kb_info.get('statute_text', '')}

"""

    letter += f"""I respectfully request that the lease agreement be amended to comply with all applicable {state} laws within 14 days of receipt of this letter. Please contact me at your earliest convenience to discuss how we can resolve these issues.

I am committed to being a responsible tenant and hope we can address these matters amicably. However, I want to ensure that my rights under {state} law are protected.

Thank you for your prompt attention to this matter.

Sincerely,

{tenant_name}
"""
    return letter


# ============================================================
# PDF REPORT GENERATION
# ============================================================
def _pdf(text):
    """Sanitize text for fpdf2 latin-1 fonts by replacing common Unicode chars."""
    return (str(text)
        .replace("\u2014", "-")   # em dash
        .replace("\u2013", "-")   # en dash
        .replace("\u2019", "'")   # right single quote
        .replace("\u2018", "'")   # left single quote
        .replace("\u201c", '"')   # left double quote
        .replace("\u201d", '"')   # right double quote
        .replace("\u2022", "-")   # bullet
        .replace("\u00ae", "(R)") # registered
        .replace("\u00a9", "(c)") # copyright
        .encode("latin-1", errors="replace").decode("latin-1")
    )


def generate_pdf_report(violations_data, state, city, tenant_name="", landlord_name="", property_address=""):
    violations_db = get_violations_for_state(state)
    score, grade, label, _ = compute_safety_score(violations_data)
    today = date.today().strftime("%B %d, %Y")
    total = violations_data.get("total_violations", 0)
    high_c = sum(1 for v in violations_data["violations_found"] if v.get("severity") == "HIGH")
    med_c  = sum(1 for v in violations_data["violations_found"] if v.get("severity") == "MEDIUM")
    low_c  = sum(1 for v in violations_data["violations_found"] if v.get("severity") == "LOW")
    found_types = {v.get("violation_type") for v in violations_data["violations_found"]}

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # ---- Header ----
    pdf.set_fill_color(13, 17, 23)
    pdf.rect(0, 0, 210, 28, style='F')
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(10, 7)
    pdf.cell(0, 10, "SignSafe Lease Analysis Report", ln=True)
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(139, 148, 158)
    pdf.set_x(10)
    jurisdiction = f"{state}" + (f" | {city}" if city else "")
    pdf.cell(0, 6, _pdf(f"Generated {today}  |  Jurisdiction: {jurisdiction}"), ln=True)
    pdf.ln(6)

    # ---- Safety Score ----
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(230, 237, 243)
    pdf.cell(0, 8, "LEASE SAFETY SCORE", ln=True)
    pdf.set_draw_color(33, 38, 45)
    pdf.set_fill_color(22, 27, 34)
    pdf.rect(10, pdf.get_y(), 190, 24, style='FD')

    # Score number
    if score >= 75:
        pdf.set_text_color(34, 197, 94)
    elif score >= 55:
        pdf.set_text_color(245, 158, 11)
    else:
        pdf.set_text_color(239, 68, 68)

    pdf.set_font("Helvetica", "B", 28)
    pdf.set_xy(14, pdf.get_y() + 3)
    pdf.cell(25, 10, str(score), ln=False)
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(230, 237, 243)
    pdf.cell(0, 10, _pdf(f"/ 100 - Grade {grade} ({label}) | {total} violation{'s' if total != 1 else ''} found"), ln=True)
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(139, 148, 158)
    pdf.set_x(14)
    pdf.cell(0, 6, _pdf(f"{high_c} HIGH  |  {med_c} MEDIUM  |  {low_c} LOW"), ln=True)
    pdf.ln(4)

    # ---- Compliance Checklist ----
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(230, 237, 243)
    pdf.cell(0, 8, "COMPLIANCE CHECKLIST", ln=True)
    pdf.set_font("Helvetica", "", 9)

    categories = {}
    for key, info in violations_db.items():
        cat = info.get("category", "General")
        categories.setdefault(cat, []).append((key, info))

    for cat, items in categories.items():
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(139, 148, 158)
        pdf.cell(0, 6, _pdf(cat.upper()), ln=True)
        pdf.set_font("Helvetica", "", 9)
        for key, info in items:
            passed = key not in found_types
            if passed:
                pdf.set_text_color(34, 197, 94)
                marker = "PASS"
            else:
                pdf.set_text_color(239, 68, 68)
                marker = "FAIL"
            pdf.cell(18, 5, marker, ln=False)
            pdf.set_text_color(201, 209, 217)
            pdf.cell(0, 5, _pdf(info["violation_name"]), ln=True)
    pdf.ln(4)

    # ---- Violations Detail ----
    if total > 0:
        pdf.set_font("Helvetica", "B", 12)
        pdf.set_text_color(230, 237, 243)
        pdf.cell(0, 8, "VIOLATION DETAILS", ln=True)

        sev_colors = {"HIGH": (239, 68, 68), "MEDIUM": (245, 158, 11), "LOW": (34, 197, 94)}

        for i, v in enumerate(violations_data["violations_found"], 1):
            sev = v.get("severity", "MEDIUM")
            r, g, b = sev_colors.get(sev, (139, 148, 158))

            # Card background
            pdf.set_fill_color(22, 27, 34)
            pdf.set_draw_color(33, 38, 45)
            card_y = pdf.get_y()
            pdf.rect(10, card_y, 190, 6, style='FD')

            # Severity pill + title
            pdf.set_font("Helvetica", "B", 9)
            pdf.set_text_color(r, g, b)
            pdf.set_xy(12, card_y + 1)
            pdf.cell(18, 4, f"[{sev}]", ln=False)
            pdf.set_text_color(230, 237, 243)
            pdf.cell(0, 4, _pdf(f"#{i}  {v.get('violation_name', v.get('violation_type', f'Violation {i}'))}"), ln=True)
            pdf.ln(1)

            # Quoted text
            pdf.set_font("Helvetica", "I", 8)
            pdf.set_text_color(180, 190, 200)
            pdf.set_x(14)
            quoted = v.get("quoted_text", "")
            if len(quoted) > 200:
                quoted = quoted[:200] + "..."
            pdf.multi_cell(182, 4, _pdf(f'"{quoted}"'), ln=True)

            # Why illegal
            pdf.set_font("Helvetica", "B", 8)
            pdf.set_text_color(139, 148, 158)
            pdf.set_x(14)
            pdf.cell(0, 4, "Why it's illegal:", ln=True)
            pdf.set_font("Helvetica", "", 8)
            pdf.set_text_color(201, 209, 217)
            pdf.set_x(14)
            pdf.multi_cell(182, 4, _pdf(v.get("explanation", "")), ln=True)

            # Statute
            pdf.set_font("Helvetica", "B", 8)
            pdf.set_text_color(139, 148, 158)
            pdf.set_x(14)
            pdf.cell(22, 4, "Statute:", ln=False)
            pdf.set_font("Helvetica", "", 8)
            pdf.set_text_color(147, 197, 253)
            pdf.cell(0, 4, _pdf(v.get("statute", "")), ln=True)

            # Remedy from KB
            kb = violations_db.get(v.get("violation_type", ""), {})
            if kb.get("tenant_remedy"):
                pdf.set_font("Helvetica", "B", 8)
                pdf.set_text_color(139, 148, 158)
                pdf.set_x(14)
                pdf.cell(0, 4, "Your remedy:", ln=True)
                pdf.set_font("Helvetica", "", 8)
                pdf.set_text_color(167, 243, 208)
                pdf.set_x(14)
                pdf.multi_cell(182, 4, _pdf(kb["tenant_remedy"]), ln=True)

            pdf.ln(3)

    # ---- Demand Letter ----
    if tenant_name and landlord_name and property_address and total > 0:
        letter_text = generate_dispute_letter(violations_data, tenant_name, landlord_name, property_address, state)
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 12)
        pdf.set_text_color(230, 237, 243)
        pdf.cell(0, 8, "DEMAND LETTER", ln=True)
        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(201, 209, 217)
        pdf.multi_cell(0, 5, _pdf(letter_text))

    # ---- Footer ----
    pdf.set_y(-15)
    pdf.set_font("Helvetica", "I", 7)
    pdf.set_text_color(139, 148, 158)
    pdf.cell(0, 5, "SignSafe is an educational tool only. Always consult a licensed attorney for legal advice.", align="C")

    return bytes(pdf.output())


# ============================================================
# COMPLIANCE CHECKLIST DISPLAY
# ============================================================
def display_compliance_checklist(violations_data, state):
    violations_db = get_violations_for_state(state)
    found_types = {v.get("violation_type") for v in violations_data["violations_found"]}

    st.markdown('<div class="section-header">Compliance Checklist</div>', unsafe_allow_html=True)

    categories = {}
    for key, info in violations_db.items():
        cat = info.get("category", "General")
        categories.setdefault(cat, []).append((key, info))

    for cat, items in categories.items():
        st.markdown(f'<div class="detail-label">{cat}</div>', unsafe_allow_html=True)
        rows_html = ""
        for key, info in items:
            passed = key not in found_types
            if passed:
                icon = "&#10003;"
                color = "#86EFAC"
                bg = "rgba(34,197,94,0.07)"
                border = "rgba(34,197,94,0.2)"
            else:
                icon = "&#10007;"
                color = "#FCA5A5"
                bg = "rgba(239,68,68,0.07)"
                border = "rgba(239,68,68,0.2)"
            rows_html += f"""
                <div style="display:flex; align-items:center; gap:0.6rem;
                            background:{bg}; border:1px solid {border};
                            border-radius:6px; padding:0.35rem 0.75rem;
                            margin-bottom:0.3rem;">
                    <span style="color:{color}; font-weight:700; font-size:0.9rem; min-width:16px;">{icon}</span>
                    <span style="font-size:0.82rem; color:#C9D1D9;">{info['violation_name']}</span>
                    <span style="font-size:0.72rem; color:#8B949E; margin-left:auto;">{info['statute']}</span>
                </div>
            """
        st.markdown(rows_html, unsafe_allow_html=True)
        st.markdown("<div style='margin-bottom:0.5rem'></div>", unsafe_allow_html=True)


# ============================================================
# FILE UPLOAD + MAIN FLOW
# ============================================================
st.markdown('<div class="section-header">Upload Lease Document</div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Drop your lease PDF here or click to browse",
    type=['pdf'],
    label_visibility="collapsed"
)

if uploaded_file:
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        lease_text = ""
        for page in pdf_reader.pages:
            lease_text += page.extract_text()

        if not lease_text.strip():
            st.error("Could not extract text from this PDF. Please ensure it is a text-based PDF, not a scanned image.")
        else:
            # Document stats
            word_count  = len(lease_text.split())
            page_count  = len(pdf_reader.pages)
            st.markdown(f"""
                <div class="stat-row">
                    <div class="stat-card">
                        <div class="stat-number">{page_count}</div>
                        <div class="stat-label">Pages</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">{word_count:,}</div>
                        <div class="stat-label">Words extracted</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">{len(get_violations_for_state(selected_state))}</div>
                        <div class="stat-label">Checks running</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            with st.expander("View extracted text"):
                st.text(lease_text[:2000] + ("..." if len(lease_text) > 2000 else ""))

            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

            city_label = f" · {selected_city}" if selected_city else ""
            if st.button(f"Analyze Lease — {selected_state}{city_label}", type="primary"):
                with st.spinner("Analyzing your lease with AI... this takes 15–30 seconds."):
                    violations = analyze_lease(lease_text, selected_state, selected_city)
                st.session_state['violations'] = violations
                st.session_state['analyzed_state'] = selected_state
                st.session_state['analyzed_city'] = selected_city

    except Exception as e:
        st.error(f"Error reading PDF: {str(e)}")

# Display results if available
if 'violations' in st.session_state:
    violations = st.session_state['violations']
    analyzed_state = st.session_state.get('analyzed_state', selected_state)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    display_violations(violations, analyzed_state)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    display_compliance_checklist(violations, analyzed_state)

    # Letter generation + PDF export
    if violations['total_violations'] > 0:
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="section-header">Generate Dispute Letter & Report</div>', unsafe_allow_html=True)

        st.markdown("""
            <div style="color:#8B949E; font-size:0.85rem; margin-bottom:1rem;">
                Fill in your details to generate a demand letter and a full PDF report you can download and share.
            </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            tenant_name = st.text_input("Your Full Name", placeholder="Jane Smith", key="tenant_name")
        with col2:
            landlord_name = st.text_input("Landlord / Property Manager Name", placeholder="John Doe", key="landlord_name")

        property_address = st.text_input("Property Address", placeholder="123 Main St, Los Angeles, CA 90024", key="property_address")

        if st.button("Generate Demand Letter", key="gen_letter"):
            if tenant_name and landlord_name and property_address:
                letter = generate_dispute_letter(
                    violations,
                    tenant_name,
                    landlord_name,
                    property_address,
                    analyzed_state
                )
                st.session_state['generated_letter'] = letter
            else:
                st.warning("Please fill in your name, landlord name, and property address.")

        if 'generated_letter' in st.session_state:
            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
            st.text_area("Your Demand Letter", st.session_state['generated_letter'], height=420, key="letter_display")

            dl_col1, dl_col2 = st.columns(2)
            with dl_col1:
                st.download_button(
                    label="Download Letter (.txt)",
                    data=st.session_state['generated_letter'],
                    file_name="signsafe_demand_letter.txt",
                    mime="text/plain"
                )
            with dl_col2:
                pdf_bytes = generate_pdf_report(
                    violations,
                    analyzed_state,
                    st.session_state.get('analyzed_city'),
                    tenant_name=st.session_state.get('tenant_name', ''),
                    landlord_name=st.session_state.get('landlord_name', ''),
                    property_address=st.session_state.get('property_address', ''),
                )
                st.download_button(
                    label="Download Full Report (.pdf)",
                    data=pdf_bytes,
                    file_name="signsafe_report.pdf",
                    mime="application/pdf"
                )
    else:
        # No violations — still offer a clean PDF report
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        pdf_bytes = generate_pdf_report(violations, analyzed_state, st.session_state.get('analyzed_city'))
        st.download_button(
            label="Download Full Report (.pdf)",
            data=pdf_bytes,
            file_name="signsafe_report.pdf",
            mime="application/pdf"
        )
