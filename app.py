import streamlit as st
import json
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="EduHukum | Azicio", page_icon="⚖️", layout="centered")

# --- CSS: CHARCOAL & DEEP ORANGE THEME ---
st.markdown("""
    <style>
    /* Global Styles */
    .stApp {
        background-color: #121212; /* Charcoal */
        color: #cfd8dc;
        font-family: 'Georgia', serif;
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: #37474f; /* Slate Gray */
        border-radius: 5px 5px 0px 0px;
        color: white;
        padding: 10px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ff5722 !important; /* Deep Orange */
    }

    /* Content Cards */
    .legal-box {
        background-color: #1e1e1e;
        border-left: 4px solid #ff5722;
        padding: 20px;
        border-radius: 0 10px 10px 0;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.4);
    }
    
    .highlight-text {
        color: #ff5722;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOAD DATA ---
def load_fuel():
    if os.path.exists("legal_education.json"):
        with open("legal_education.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

data = load_fuel()

# --- HEADER ---
st.markdown("<h1 style='text-align: center; color: #ff5722;'>⚖️ PROGRAM EDUKASI HUKUM</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Membangun Literasi Hukum yang Berkeadilan</p>", unsafe_allow_html=True)

if not data:
    st.error("Fuel 'legal_education.json' tidak ditemukan.")
else:
    # --- UI: 4 TAB KATEGORI ---
    tab1, tab2, tab3, tab4 = st.tabs([
        "📖 Kamus Istilah", 
        "🔍 Penjelasan", 
        "💡 Mengapa Penting", 
        "📜 Referensi Hukum"
    ])

    with tab1:
        st.subheader("Daftar Istilah Dasar")
        for item in data['kamus_istilah']:
            st.markdown(f"""
            <div class="legal-box">
                <div class="highlight-text">{item['term']}</div>
                <div>{item['content']}</div>
            </div>
            """, unsafe_allow_html=True)

    with tab2:
        st.subheader("Konsep & Pondasi Dasar")
        for item in data['penjelasan_singkat']:
            st.markdown(f"""
            <div class="legal-box">
                <div class="highlight-text">{item['topic']}</div>
                <div>{item['detail']}</div>
            </div>
            """, unsafe_allow_html=True)

    with tab3:
        st.subheader("Tujuan & Manfaat")
        for item in data['mengapa_penting']:
            st.markdown(f"""
            <div class="legal-box">
                <div class="highlight-text">{item['goal']}</div>
                <div>{item['reason']}</div>
            </div>
            """, unsafe_allow_html=True)

    with tab4:
        st.subheader("Dasar Hukum & UU")
        for item in data['referensi_hukum']:
            st.markdown(f"""
            <div class="legal-box">
                <div class="highlight-text">{item['ref']}</div>
                <div style="font-style: italic;">{item['law']}</div>
            </div>
            """, unsafe_allow_html=True)

st.divider()
st.caption("Aplikasi Edukasi Terstruktur v2.1 | Azicio System Integration")
