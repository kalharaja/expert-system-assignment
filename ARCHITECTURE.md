# Expert System Architecture

## Modular Knowledge Base Structure

The Car No-Start Expert System features a clean, modular architecture with 5 essential questions and 16 diagnostic rules, providing comprehensive coverage while maintaining simplicity.

### 📁 **File Structure**

```
src/
├── facts.py          # Fact definitions (Input, Hypothesis, Phase)
├── rules.py          # Knowledge base rules (R1-R16, R99)
├── engine.py         # Main inference engine + explanations
├── kb_car_diag.py    # Main interface (imports from engine)
├── cli_app.py        # Command-line interface (5 questions)
└── ui_streamlit.py   # Web interface (5 questions)

tests/
└── test_cases.py     # Comprehensive test suite
```

### 🔧 **Module Responsibilities**

#### **facts.py** - Data Structures
- **Purpose:** Define all fact types used in the knowledge base
- **Contents:**
  - `Input` - User symptom inputs (5 essential questions)
  - `Hypothesis` - Diagnostic conclusions (16 possible diagnoses)
  - `Phase` - Control flow markers (reasoning phase)
- **Benefits:** Centralized fact definitions, easy to extend

#### **rules.py** - Knowledge Base
- **Purpose:** Contains all diagnostic rules and logic
- **Contents:**
  - `CarDiagnosisRules` class with all rule methods
  - **Core Rules (R1-R3):** Battery drained, Out of fuel, Starter motor fault
  - **Additional Rules (R4-R6):** Low fuel, Battery and fuel, Charging system
  - **Enhanced Rules (R7-R9):** Starter solenoid, Cold start, Overheating
  - **Enhanced Coverage (R10-R16):** Ignition, sensors, wear, fuel issues, etc.
  - **Fallback Rule (R99):** Inconclusive diagnosis
- **Benefits:** Pure knowledge representation, no engine logic

#### **engine.py** - Inference Engine
- **Purpose:** Combines facts and rules into working expert system
- **Contents:**
  - `CarDiagnosisEngine` - Main inference engine with forward chaining
  - `run_engine_with_inputs()` - Convenience function (5 parameters)
  - `explain()` - Human-readable explanations for all 16 diagnoses
- **Benefits:** Clean separation of inference from knowledge

#### **kb_car_diag.py** - Main Interface
- **Purpose:** Public API for the expert system
- **Contents:**
  - Compatibility patches for Python 3.11
  - Imports from engine module
  - Exposes public functions
- **Benefits:** Single entry point, clean API

### 🎯 **5-Question System Design**

The system uses 5 essential questions to capture the most critical diagnostic information:

1. **Engine Cranks?** (yes/no) - Primary mechanical indicator
2. **Headlights Dim?** (yes/no) - Electrical system indicator  
3. **Fuel Gauge Level?** (empty/low/ok) - Fuel system status
4. **Clicking Noise?** (yes/no) - Starter system indicator
5. **Ambient Temperature?** (cold/normal/hot) - Environmental factor

This focused approach provides comprehensive coverage while maintaining user-friendly simplicity.

### 🔧 **Diagnostic Rules Overview**

The system implements 9 focused diagnostic rules plus 1 fallback rule:

**Core Rules (R1-R3):**
- **R1:** No crank + dim lights → Battery drained
- **R2:** Cranks + empty fuel → Out of fuel  
- **R3:** No crank + bright lights → Starter motor fault

**Additional Rules (R4-R6):**
- **R4:** Cranks + low fuel → Low fuel issue
- **R5:** No crank + dim + empty → Battery and fuel issues
- **R6:** Cranks + dim lights → Charging system issue

**Enhanced Rules (R7-R9):**
- **R7:** No crank + bright + clicking → Starter solenoid fault
- **R8:** No crank + bright + cold → Cold start issue
- **R9:** Cranks + fuel OK + hot → Overheating

**Enhanced Coverage (R10-R16):**
- **R10:** Cranks + bright + fuel OK → Ignition/Fuel delivery issue
- **R11:** Cranks + normal temperature → Sensor/Computer issue
- **R12:** Cranks + clicking → Starter motor wear
- **R13:** Low fuel + dim lights → Fuel and battery issues
- **R14:** Cranks + low fuel + cold → Cold fuel issue
- **R15:** No crank + bright + normal → Normal starter fault
- **R16:** Cranks + dim + low fuel → Charging and fuel issues

**Fallback Rule (R99):**
- **R99:** No match → Inconclusive diagnosis

### 🔄 **Import Flow**

```
kb_car_diag.py
    ↓ imports
engine.py
    ↓ imports
facts.py + rules.py
```

### ✅ **Benefits of Modular Design**

1. **Separation of Concerns**
   - Facts are separate from rules
   - Rules are separate from engine logic
   - UI is separate from knowledge base

2. **Maintainability**
   - Easy to modify rules without touching engine
   - Easy to add new facts without changing rules
   - Clear responsibility boundaries

3. **Extensibility**
   - Add new facts in `facts.py`
   - Add new rules in `rules.py`
   - Engine automatically picks up changes

4. **Testability**
   - Each module can be tested independently
   - Mock facts and rules for unit testing
   - Clear interfaces between components

5. **Reusability**
   - Facts can be reused in other systems
   - Rules can be shared across engines
   - Engine can work with different rule sets

### 🚀 **Usage Examples**

#### **Adding New Facts**
```python
# In facts.py
class Temperature(Fact):
    level = Field(str, mandatory=True)  # hot/warm/cold
```

#### **Adding New Rules**
```python
# In rules.py
@Rule(Phase(name="reasoning"),
      Input(name="engine_cranks", value="no"),
      Temperature(level="hot"))
def rule_overheating(self):
    self.trace.append("R4: no cranking & hot engine ⇒ overheating")
    self.declare(Hypothesis(label="engine_overheating"))
```

#### **Using the System**
```python
# In any application
from kb_car_diag import run_engine_with_inputs, explain

# 5-question system
hypos, trace = run_engine_with_inputs("no", "yes", "ok", "no", "normal")
print(f"Diagnosis: {hypos}")
print(f"Explanation: {explain(hypos[0])}")

# Example: Cold start issue
hypos, trace = run_engine_with_inputs("no", "no", "ok", "no", "cold")
# Result: ['cold_start_issue']
```

### 📊 **Architecture Diagram**

```
┌─────────────────┐    ┌─────────────────┐
│   CLI App       │    │  Streamlit UI  │
│  (5 questions)  │    │  (5 questions)  │
└─────────┬───────┘    └─────────┬───────┘
          │                      │
          └──────────┬───────────┘
                     │
          ┌──────────▼───────────┐
          │   kb_car_diag.py     │ ← Main Interface
          │  (Compatibility)     │
          └──────────┬───────────┘
                     │
          ┌──────────▼───────────┐
          │     engine.py       │ ← Inference Engine
          │  (5 inputs, 16 rules)│
          └──────────┬───────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
┌───────▼──────┐ ┌──▼──────┐ ┌───▼──────┐
│  facts.py    │ │rules.py │ │ tests/   │
│  (3 types)   │ │(16 rules)│ │test_cases│
└──────────────┘ └─────────┘ └──────────┘
```

### 🎯 **System Capabilities**

- **5 Essential Questions**: Focused diagnostic interface
- **16 Diagnostic Rules**: Comprehensive coverage of common issues
- **Forward Chaining**: Efficient inference engine
- **Multiple Interfaces**: CLI, web-based, and Prolog options
- **Comprehensive Testing**: 21 test cases covering all scenarios
- **Modular Design**: Easy to maintain and extend

This modular architecture provides a solid foundation for future enhancements while maintaining clean separation of concerns and excellent maintainability.
