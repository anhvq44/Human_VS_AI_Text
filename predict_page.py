import streamlit as st

def show_predict_page():
    st.markdown('<div class="page-eyebrow">Detection Engine</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Analyse an Essay</div>', unsafe_allow_html=True)
    st.markdown("""
            <div class="page-subtitle">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec id feugiat libero, eu placerat eros. Nullam et sem elementum, mattis neque vel, consectetur velit.
            </div>
        """,
        unsafe_allow_html=True
    )
    
    