import streamlit as st

from home_page import home
from predict_page import show_predict_page

st.set_page_config(
    page_title="Human VS AI Generated Text",
    layout="centered",
    initial_sidebar_state="expanded"
)

if "page" not in st.session_state:
    st.session_state.page = "Home"

st.markdown(
    '''<style>
        @import url("https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap")
    
        html, body, [class*='css'] { font-family: 'DM Sans', sans-serif }
        
        
        /* sidebar stuffs */
        .sidebar-title{
            font-family: 'DM Mono', monospace;
            font-size: 1.3rem;
            text-transform: uppercase;
            margin-bottom: 2rem;
        }
        .sidebar-divider{
            border: none;
            border-top: 1px solid white;
        }
        [data-testid="stSidebar"] .stButton > button{
            background: tramsparent !important;
            border: none !important;
            border-left: 3px solid transparent !important;
            border-radius: 0 8px 8px 0 !important;
            font-family: 'DM Sans', sans-serif !important;
            font-weight: 500 !important;
            font-size: 0.9rem !important;
            padding: 0.6rem !important;
            text-align: left !important;
        }
        
        
        /* typography */
        .page-eyebrow{
            font-family: 'DM Mono', monospace;
            font-size: 1rem;
            letter-spacing: 0.2rem;
            text-transform: uppercase;
            margin-bottom: 0.6rem;
        }
        .page-title{
            font-family: 'Syne', sans-serif;
            font-weight: 800;
            font-size: 2rem;
            marginbottom: 0.4rem;
        }
        .page-substitle{
            font-family: 'DM Sans', sans-serif;
            font-size: 1.05rem;
            font-weight: 300;
            margin-bottom: 2.5rem;
            max-width: 520px;
        }
        .accent-line{
            width: 48px;
            height: 3px;
            border-radius: 2px;
            margin-bottom: 1.6rem;
        }
        
        
        /* metric card */
        .metric-card{
            border: 1px solid white;
            border-radius: 14px;
            padding 1.2rem 1.4rem;
            text-align: center;
        }
        
        /* card */
        .card{
            border: 1px solid white;
            border-radius: 16px;
            padding: 1.6rem 1.8rem;
            margin-bottom: 1rem'
        }
        .card-title{
            font-family: 'Syne', sans-serif;
            font-weight: 700;
            font-size: 1rem;
            margin-bottom: 0.35rem;
        }
        .card-body{
            font-size: 0.8rem;
            line-height: 1.6;
        }
    </style>''',
    unsafe_allow_html=True
)

with st.sidebar:
    
    st.markdown(
        '<div class="sidebar-title"> AI Essay Detection Engine</div>',
        unsafe_allow_html=True
    )
    
    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)
    
    if st.button("Home", key="nav-home-btn", use_container_width=True):
        st.session_state.page = "Home"
        st.rerun()
    if st.button("Predict", key="nav-predict-page-btn", use_container_width=True):
        st.session_state.page = "Predict"
        st.rerun()
    
if st.session_state.page == "Home":
    home()
elif st.session_state.page == "Predict":
    show_predict_page()