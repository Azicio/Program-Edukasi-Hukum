import streamlit as st
import json
import os

# --- INITIAL CONFIG ---
st.set_page_config(page_title="EduHukum Pro | Azicio", page_icon="⚖️", layout="centered")

# --- CUSTOM CSS: THE LAWYER'S DASHBOARD ---
st.markdown("""
    <style>
    .stApp {
        background-color: #121212; /* Charcoal */
        color: #cfd8dc;
        font-family: 'Georgia', serif;
    }
    
    /* Highlight Orange for Headers */
    h1, h2, h3 { color: #ff5722 !important; }
    
    /* Custom Tabs */
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #263238; /* Slate Gray Dark */
        color: white;
        border-radius: 8px 8px 0 0;
        padding: 10px 20px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ff5722 !important;
        font-weight: bold;
    }

    /* Cards/Boxes */
    .legal-card {
        background-color: #1e1e1e;
        border-left: 5px solid #ff5722;
        padding: 20px;
        border-radius: 4px 12px 12px 4px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    
    .term-title {
        color: #ff5722;
        font-size: 1.15rem;
        font-weight: bold;
        margin-bottom: 8px;
    }
    
    /* Expander Styling */
    .stExpander {
        border: 1px solid #37474f !important;
        background-color: #1a1a1a !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- UTILITIES ---
def load_data():
    if os.path.exists("legal_education.json"):
        with open("legal_education.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

db = load_data()

# --- MAIN UI ---
st.markdown("<h1 style='text-align: center;'>⚖️ EDU-HUKUM TERSTRUKTUR</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic;'>Integrasi Data Total: Ellen File Archive</p>", unsafe_allow_html=True)

if db:
    t1, t2, t3, t4 = st.tabs(["📚 KAMUS", "📖 PENJELASAN", "💡 MANFAAT", "📜 REFERENSI"])

    with t1:
        st.write("### Kamus Istilah & Prosedur")
        for item in db['kamus_istilah']:
            if item.get("is_dropdown"):
                with st.expander(f"▶️ {item['term']}", expanded=False):
                    for sub in item['details']:
                        st.markdown(f"<div class='term-title'>{sub['item']}</div>", unsafe_allow_html=True)
                        st.markdown(sub['desc'])
                        st.divider()
            else:
                st.markdown(f"<div class='legal-card'><div class='term-title'>{item['term']}</div>{item['content']}</div>", unsafe_allow_html=True)

    with t2:
        st.write("### Konsep Dasar & Alur Hukum")
        for item in db['penjelasan_singkat']:
            with st.container():
                st.markdown(f"#### {item['topic']}")
                st.markdown(f"<div class='legal-card'>{item['detail']}</div>", unsafe_allow_html=True)

    with t3:
        st.write("### Mengapa Pemahaman Ini Penting?")
        for item in db['mengapa_penting']:
            st.markdown(f"""
            <div class='legal-card'>
                <div class='term-title'>{item['goal']}</div>
                {item['reason']}
            </div>
            """, unsafe_allow_html=True)

    with t4:
        st.write("### Landasan Hukum & Konstitusi")
        for item in db['referensi_hukum']:
            st.markdown(f"""
            <div class='legal-card'>
                <div class='term-title'>{item['ref']}</div>
                <code style='color: #aed581;'>{item['law']}</code>
            </div>
            """, unsafe_allow_html=True)
else:
    st.error("File 'legal_education.json' tidak terdeteksi. Pastikan data fuel sudah diunggah.")

st.divider()
st.caption("Operator: Azicio | Data Source: Ellen File PDF | Powered by Gemini Architect")
