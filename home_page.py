import streamlit as st

def home():
    
    st.markdown('<div class="page-eyebrow">About the model</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Human vs AI Essay Detector</div>', unsafe_allow_html=True)
    
    st.markdown("""
            <div class="page-subtitle">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec id feugiat libero, eu placerat eros. Nullam et sem elementum, mattis neque vel, consectetur velit.
            </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown('<div class="accent-line"></div>', unsafe_allow_html=True)
    metric_c1, metric_c2, metric_c3, metric_c4 = st.columns(4)
    
    with metric_c1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(label = "Training Samples", value="2200")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with metric_c2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(label = "Model Type", value="NLP")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with metric_c3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(label = "Test Accuracy", value="98.91%")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with metric_c4:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(label = "Max Token Length", value="4400")
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_left, col_right = st.columns(2, gap="large")
    
    with col_left:
        st.markdown("""
                <div class="card">
                    <div class="card-title">Model Architecture</div>
                    <div class="card-body">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec id feugiat libero, eu placerat eros. Nullam et sem elementum, mattis neque vel, consectetur velit. Nulla facilisi. Morbi ultricies massa erat, a consequat justo semper sit amet. Nullam ut libero sollicitudin, consequat nunc semper, sagittis urna. 
                    </div>
                </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
                <div class="card">
                    <div class="card-title">Training Data</div>
                    <div class="card-body">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec id feugiat libero, eu placerat eros. Nullam et sem elementum, mattis neque vel, consectetur velit. Nulla facilisi. Morbi ultricies massa erat, a consequat justo semper sit amet. Nullam ut libero sollicitudin, consequat nunc semper, sagittis urna. 
                    </div>
                </div>
            """,
            unsafe_allow_html=True
        )
        
    with col_right:
        st.markdown("""
                <div class="card">
                    <div class="card-title">Training Setup</div>
                    <div class="card-body">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec id feugiat libero, eu placerat eros. Nullam et sem elementum, mattis neque vel, consectetur velit. Nulla facilisi. Morbi ultricies massa erat, a consequat justo semper sit amet. Nullam ut libero sollicitudin, consequat nunc semper, sagittis urna. 
                    </div>
                </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
                <div class="card">
                    <div class="card-title">Limitations</div>
                    <div class="card-body">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec id feugiat libero, eu placerat eros. Nullam et sem elementum, mattis neque vel, consectetur velit. Nulla facilisi. Morbi ultricies massa erat, a consequat justo semper sit amet. Nullam ut libero sollicitudin, consequat nunc semper, sagittis urna. 
                    </div>
                </div>
            """,
            unsafe_allow_html=True
        )