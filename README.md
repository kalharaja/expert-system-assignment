# Car No-Start Expert System

A rule-based expert system for diagnosing car no-start problems using the Experta framework.

## Features

- **5 Essential Questions**: Focused diagnostic interface with key symptoms
- **16 Diagnostic Rules**: Comprehensive coverage of common no-start issues
- **Multiple Interfaces**: CLI, web-based Streamlit interface, and Prolog knowledge base
- **Rule-based Reasoning**: Uses expert knowledge to diagnose car problems
- **Detailed Explanations**: Provides actionable recommendations for each diagnosis
- **Prolog Implementation**: Complete knowledge base in Prolog syntax with usage documentation

## Installation

1. Create a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install experta streamlit
```

## Usage

### Command Line Interface
```bash
python -m src.cli_app
```

### Web Interface (Streamlit)
```bash
streamlit run src/ui_streamlit.py
```
**Features:**
- Comprehensive symptom analysis
- Multiple diagnostic categories
- Professional diagnosis display
- System information and statistics

### Run Tests

**Test Suite:**
```bash
python tests/test_cases.py
```

**Test Coverage:**
- **Comprehensive Test Cases** covering all diagnostic scenarios
- **100% Rule Coverage** for all 16 diagnostic rules
- **New Rule Testing** for enhanced diagnostic capabilities
- **Edge Case Testing** for boundary conditions and error handling
- **Accuracy Testing** with correct predictions for all scenarios

## Diagnostic Rules

The expert system uses the following 16 rules:

**Core Rules (R1-R3):**
1. **Battery Drained**: Engine doesn't crank + dim headlights
2. **Out of Fuel**: Engine cranks + fuel gauge empty
3. **Starter Motor Fault**: Engine doesn't crank + headlights not dim

**Additional Rules (R4-R6):**
4. **Low Fuel**: Engine cranks + low fuel gauge
5. **Battery and Fuel**: Engine doesn't crank + dim headlights + empty fuel
6. **Charging System Issue**: Engine cranks + dim headlights

**Enhanced Rules (R7-R9):**
7. **Starter Solenoid Fault**: Engine doesn't crank + bright headlights + clicking noise
8. **Cold Start Issue**: Engine doesn't crank + bright headlights + cold temperature
9. **Overheating**: Engine cranks + fuel OK + hot temperature

**Enhanced Coverage Rules (R10-R16):**
10. **Ignition/Fuel Delivery**: Engine cranks + bright headlights + fuel OK
11. **Sensor/Computer Issue**: Engine cranks + normal temperature
12. **Starter Motor Wear**: Engine cranks + clicking noise
13. **Fuel and Battery Issues**: Low fuel + dim headlights
14. **Cold Fuel Issue**: Engine cranks + low fuel + cold temperature
15. **Normal Starter Fault**: Engine doesn't crank + bright headlights + normal temperature
16. **Charging and Fuel Issues**: Engine cranks + dim headlights + low fuel

**Fallback:**
17. **Inconclusive**: No matching rule (fallback diagnosis)

## Project Structure

```
src/
├── facts.py            # Fact definitions (Input, Hypothesis, Phase)
├── rules.py            # Diagnostic rules (R1-R16, R99)
├── engine.py           # Inference engine and explanations
├── kb_car_diag.py      # Main entry point and compatibility
├── cli_app.py          # Command-line interface (5 questions)
└── ui_streamlit.py     # Web-based Streamlit interface (5 questions)

tests/
└── test_cases.py       # Comprehensive test suite

# Prolog Implementation
car_diagnosis_kb.pl     # Complete Prolog knowledge base
PROLOG_USAGE.md         # Prolog usage documentation
```

## Technical Details

- **Framework**: Experta (Python expert system framework)
- **Compatibility**: Python 3.13 with compatibility patches
- **Architecture**: Rule-based expert system with forward chaining
- **Facts**: Input symptoms, diagnostic hypotheses, reasoning phases
- **Rules**: Pattern matching on symptom combinations

## Prolog Implementation

The system also includes a complete Prolog knowledge base:

### **Quick Start:**
```prolog
% Load the knowledge base
?- [car_diagnosis_kb].

% Set up your scenario
?- assert(input(engine_cranks, yes)).
?- assert(input(headlights_dim, no)).
?- assert(input(fuel_gauge_level, ok)).
?- assert(input(clicking_noise, no)).
?- assert(input(temperature, normal)).

% Get diagnoses
?- diagnosis(D).
% Results: ignition_fuel_delivery, sensor_computer_issue
```

### **Features:**
- ✅ **16 diagnostic rules** in pure Prolog syntax
- ✅ **Dynamic input facts** for flexible testing
- ✅ **Comprehensive explanations** for each diagnosis
- ✅ **Perfect compatibility** with Python system results
- ✅ **Complete usage documentation** in `PROLOG_USAGE.md`

## Example Diagnoses

- **Battery Drained**: "Try jump-starting; test/replace battery; check alternator output"
- **Out of Fuel**: "Add fuel; if recurring, inspect for leaks or faulty gauge/sender"
- **Starter Motor Fault**: "Inspect starter relay/solenoid, wiring; consider shop service"
- **Inconclusive**: "Check battery terminals, fuses, immobilizer, and error codes"
