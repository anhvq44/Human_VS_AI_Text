import streamlit as st

from home_page import home
from predict_page import show_predict_page

st.set_page_config(
    page_title="Human VS AI Generated Text",
    layout="centered",
    initial_sidebar_state="expanded"
)

# set default page to home
if "page" not in st.session_state:
    st.session_state.page = "Home"

# style for all pages
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
        
        /* arch blocks */
        .arch-row{
            display: flex;
            gap: 0.5rem;
            align-items: center;
            flex-wrap: wrap;
            margin-bottom: 1rem;
        }
        .arch-block{
            border: 1px solid;
            border-radius: 8px;
            padding: 0.35rem 0.8rem;
            font-family: 'DM Mono', monospace;
            font-size: 0.7rem;
        }
        .arch-arrow{
            font-size: 1rem;
        }
        
        /* text area */
        textarea{
            border: 1px solid !important;
            border-radius: 12px !important;
            font-family: 'DM Sans', sans-serif !important; font-size: 0.9rem !important;
        }
        
        /* probability bars */
        .prob-row{
            margin-bottom: 0.75rem;
        }
        .prob-label-row{
            display: flex;
            justify-content: space-between;
            margin-bottom: 0.3rem
        }
        .prob-label{
            font-family: 'DM Mono', monospace;
            font-size: 0.7rem;
            letter-spacing: 0.08em;
            text-transform: uppercase
        }
        .prob-pct{
            font-family: 'Syne', sans-serif;
            font-weight: 700;
            font-size: 0.85rem;
        }
        .prob-track{
            height: 8px;
            border: 1px solid;
            border-radius: 4px;
            overflow: hidden
        }
        .prob-fill-ai {
            height: 100%;
            border-radius: 4px;
            background: linear-gradient(90deg, #7744cc, #cc55ff)
        }
        .prob-fill-human {
            height: 100%;
            border-radius: 4px;
            background: linear-gradient(90deg, #228855, #44dd88)
        }
        
        /* result box */
        .result-box{
            border-radius: 20px;
            padding: 2rem 2.2rem;
            margin: 1.5rem 0;
            border: 1px solid transparent
        }
        .result-box.ai{
            border-color: #6633aa
        }
        .result-box.human{
            
            border-color: #228855
        }
        .result-verdict{
            font-family: 'Syne', sans-serif;
            font-weight: 800;
            font-size: 2rem;
            letter-spacing: -0.02em;
            margin-bottom: 0.2rem
        }
        .result-verdict.ai{
            color: #cc77ff
        }
        .result-verdict.human{
            color: #44dd88
        }
        .result-sub{
            font-family: 'DM Mono', monospace;
            font-size: 0.72rem;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            margin-bottom: 1.4rem;
        }
        .result-sub.ai{
            color: #8844bb
        }
        .result-sub.human{
            color: #228855
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