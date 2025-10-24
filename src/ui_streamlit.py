# src/ui_streamlit.py
import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(__file__))

from kb_car_diag import run_engine_with_inputs, explain

def main():
    st.set_page_config(
        page_title="Car No-Start Expert System",
        page_icon="🚗",
        layout="wide"
    )
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .diagnosis-card {
        background-color: #f0f2f6;
        color: #262730;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #1f77b4;
        margin: 1rem 0;
    }
    .diagnosis-card h4 {
        color: #1f77b4;
        margin-bottom: 0.5rem;
    }
    .diagnosis-card p {
        color: #262730;
        margin: 0;
    }
    .confidence-bar {
        background-color: #e8f4fd;
        padding: 0.5rem;
        border-radius: 0.25rem;
        margin: 0.5rem 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<h1 class="main-header">🚗 Car No-Start Expert System</h1>', unsafe_allow_html=True)
    st.markdown("---")
    
    # Create tabs for different interfaces
    tab1, tab2 = st.tabs(["🔬 Diagnosis", "📊 System Info"])
    
    with tab1:
        diagnosis_interface()
    
    with tab2:
        system_info_interface()

def diagnosis_interface():
    """Main diagnosis interface - 5 essential questions"""
    st.markdown("### Car No-Start Diagnosis")
    st.markdown("Please answer these 5 essential questions about your car:")
    
    # Create three columns for better layout
    col1, col2, col3 = st.columns(3)
    
    with col1:
        engine_cranks = st.selectbox(
            "Does the engine crank?",
            options=["", "yes", "no"],
            index=0,
            help="Does the engine make any sound when you turn the key?"
        )
        
        headlights_dim = st.selectbox(
            "Are the headlights dim?",
            options=["", "yes", "no"],
            index=0,
            help="Are the headlights noticeably dimmer than usual?"
        )
    
    with col2:
        fuel_gauge_level = st.selectbox(
            "Fuel gauge level?",
            options=["", "empty", "low", "ok"],
            index=0,
            help="What does your fuel gauge show?"
        )
        
        clicking_noise = st.selectbox(
            "Clicking noise when starting?",
            options=["", "yes", "no"],
            index=0,
            help="Do you hear clicking sounds when turning the key?"
        )
    
    with col3:
        temperature = st.selectbox(
            "Ambient temperature?",
            options=["", "cold", "normal", "hot"],
            index=0,
            help="What's the current temperature outside?"
        )
    
    st.markdown("---")
    
    # Diagnosis button
    if st.button("🔍 Get Diagnosis", type="primary", use_container_width=True):
        if not all([engine_cranks, headlights_dim, fuel_gauge_level, clicking_noise, temperature]):
            st.error("Please answer all 5 questions before getting a diagnosis.")
        else:
            with st.spinner("Analyzing symptoms..."):
                try:
                    # Run the expert system with 5 inputs
                    hypos, trace = run_engine_with_inputs(engine_cranks, headlights_dim, fuel_gauge_level, clicking_noise, temperature)
                    
                    # Display results
                    st.markdown("### 🔍 Diagnosis Results")
                    
                    # Show diagnosis
                    if hypos:
                        for i, hypo in enumerate(hypos, 1):
                            st.markdown(f"""
                            <div class="diagnosis-card">
                                <h4>{i}. {hypo.replace('_', ' ').title()}</h4>
                                <p>{explain(hypo)}</p>
                            </div>
                            """, unsafe_allow_html=True)
                    else:
                        st.warning("No specific diagnosis could be determined.")
                    
                    # Show reasoning trace
                    with st.expander("📋 Reasoning Trace", expanded=False):
                        st.markdown("**Expert System Reasoning Steps:**")
                        for i, step in enumerate(trace, 1):
                            st.markdown(f"{i}. {step}")
                    
                    # Show user inputs
                    with st.expander("📝 Your Input Summary", expanded=False):
                        st.markdown("**Symptom Analysis Inputs:**")
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            st.markdown(f"**Engine Cranks:** {engine_cranks.title()}")
                            st.markdown(f"**Headlights Dim:** {headlights_dim.title()}")
                        
                        with col2:
                            st.markdown(f"**Fuel Level:** {fuel_gauge_level.title()}")
                            st.markdown(f"**Clicking Noise:** {clicking_noise.title()}")
                        
                        with col3:
                            st.markdown(f"**Temperature:** {temperature.title()}")
                        
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

def system_info_interface():
    """System information and statistics"""
    st.markdown("### System Information")
    
    # Knowledge base statistics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Rules", "16", "Enhanced")
    
    with col2:
        st.metric("Input Questions", "5", "Essential")
    
    with col3:
        st.metric("Fact Types", "3", "Core")
    
    # Knowledge base information
    st.markdown("### 📚 Knowledge Base Details")
    
    # Facts section
    st.markdown("#### 🔍 Fact Types")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Input Facts:**")
        st.markdown("- `engine_cranks`: yes/no")
        st.markdown("- `headlights_dim`: yes/no")
        st.markdown("- `fuel_gauge_level`: empty/low/ok")
        st.markdown("- `clicking_noise`: yes/no")
        st.markdown("- `temperature`: cold/normal/hot")
    
    with col2:
        st.markdown("**Hypothesis Facts:**")
        st.markdown("- `battery_drained`")
        st.markdown("- `out_of_fuel`")
        st.markdown("- `starter_motor_fault`")
        st.markdown("- `low_fuel`")
        st.markdown("- `battery_and_fuel`")
        st.markdown("- `charging_system_issue`")
        st.markdown("- `starter_solenoid_fault`")
        st.markdown("- `cold_start_issue`")
        st.markdown("- `overheating`")
    
    with col3:
        st.markdown("**Control Facts:**")
        st.markdown("- `Phase`: reasoning")
        st.markdown("- **Inference Engine:** Forward Chaining")
        st.markdown("- **Rule Engine:** Experta Framework")
        st.markdown("- **Architecture:** Modular Design")
    
    # Rules section
    st.markdown("#### ⚙️ Diagnostic Rules")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Core Rules (R1-R3):**")
        st.markdown("- **R1:** `no_crank + dim_lights → battery_drained`")
        st.markdown("- **R2:** `cranks + empty_fuel → out_of_fuel`")
        st.markdown("- **R3:** `no_crank + bright_lights → starter_motor_fault`")
        
        st.markdown("**Additional Rules (R4-R6):**")
        st.markdown("- **R4:** `cranks + low_fuel → low_fuel`")
        st.markdown("- **R5:** `no_crank + dim + empty → battery_and_fuel`")
        st.markdown("- **R6:** `cranks + dim_lights → charging_system_issue`")
    
    with col2:
        st.markdown("**Enhanced Rules (R7-R9):**")
        st.markdown("- **R7:** `no_crank + bright + clicking → starter_solenoid_fault`")
        st.markdown("- **R8:** `no_crank + bright + cold → cold_start_issue`")
        st.markdown("- **R9:** `cranks + fuel_ok + hot → overheating`")
        
        st.markdown("**Enhanced Coverage (R10-R16):**")
        st.markdown("- **R10:** `cranks + bright + fuel_ok → ignition_fuel_delivery`")
        st.markdown("- **R11:** `cranks + normal → sensor_computer_issue`")
        st.markdown("- **R12:** `cranks + clicking → starter_motor_wear`")
        st.markdown("- **R13:** `low_fuel + dim → fuel_battery_issues`")
        st.markdown("- **R14:** `cranks + low_fuel + cold → cold_fuel_issue`")
        st.markdown("- **R15:** `no_crank + bright + normal → normal_starter_fault`")
        st.markdown("- **R16:** `cranks + dim + low_fuel → charging_fuel_issues`")
        
        st.markdown("**Fallback Rule:**")
        st.markdown("- **R99:** `no_match → inconclusive`")
    
    # System architecture
    st.markdown("#### 🏗️ System Architecture")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Core Components:**")
        st.markdown("- **`facts.py`**: Fact definitions (Input, Hypothesis, Phase)")
        st.markdown("- **`rules.py`**: Diagnostic rules (R1-R9, R99)")
        st.markdown("- **`engine.py`**: Inference engine & explanations")
        st.markdown("- **`kb_car_diag.py`**: Main entry point")
    
    with col2:
        st.markdown("**Interface Components:**")
        st.markdown("- **`ui_streamlit.py`**: Web interface")
        st.markdown("- **`cli_app.py`**: Command-line interface")
        st.markdown("- **`test_cases.py`**: Test suite")
        st.markdown("- **`run_all_tests.py`**: Test runner")
    
    # System features
    st.markdown("### 🎯 System Features")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Knowledge Base:**")
        st.markdown("- ✅ 5 Essential Input Questions")
        st.markdown("- ✅ 9 Diagnostic Rules")
        st.markdown("- ✅ 3 Core Fact Types")
        st.markdown("- ✅ Forward Chaining Inference")
    
    with col2:
        st.markdown("**Technical Features:**")
        st.markdown("- ✅ Modular Architecture")
        st.markdown("- ✅ Comprehensive Test Coverage")
        st.markdown("- ✅ Professional Interface")
        st.markdown("- ✅ Clear Documentation")
    
    # About the system
    st.markdown("### ℹ️ About This System")
    st.markdown("""
    This expert system demonstrates **rule-based knowledge representation** and **forward chaining inference** for automotive diagnostics:
    
    **🧠 Knowledge Representation:**
    - **Facts**: Input symptoms, diagnostic hypotheses, control phases
    - **Rules**: IF-THEN logic for symptom-to-diagnosis mapping
    - **Engine**: Forward chaining inference with Experta framework
    - **Interface**: User-friendly input collection and result display
    
    **⚙️ Inference Process:**
    1. **Input Collection**: User provides 5 essential symptoms
    2. **Fact Declaration**: Symptoms asserted as Input facts
    3. **Rule Matching**: Engine matches facts to applicable rules
    4. **Hypothesis Generation**: Rules fire to create diagnostic hypotheses
    5. **Result Presentation**: Clear diagnosis with explanations
    
    **📚 Knowledge Base Structure:**
    - **Input Facts**: 5 symptom categories with specific values
    - **Hypothesis Facts**: 9 possible diagnostic outcomes
    - **Control Facts**: Phase markers for inference control
    - **Diagnostic Rules**: 9 focused rules + 1 fallback rule
    """)

if __name__ == "__main__":
    main()
