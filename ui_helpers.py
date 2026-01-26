import streamlit as st

def setup_page():
    st.set_page_config(page_title="Weather App", page_icon="⛅", layout="wide")
    st.markdown("""
        <style>
        .stApp { background: linear-gradient(to right, #e0f7fa, #80deea); }
        .big-font { font-size: 20px !important; }
        </style>
    """, unsafe_allow_html=True)

def show_header():
    st.title("⛅ Dự Báo Thời Tiết & Sổ Tay Du Lịch")
    st.markdown("---")

# Hàm xuất dữ liệu ra CSV
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8-sig')