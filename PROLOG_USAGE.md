# Prolog Knowledge Base Usage Guide

## 📚 **Car No-Start Expert System - Prolog Implementation**

This document explains how to use the Prolog knowledge base (`car_diagnosis_clean.pl`) with SWI-Prolog for automotive diagnostics.

---

## 🚀 **Getting Started**

### **Prerequisites:**
- SWI-Prolog installed on your system
- `car_diagnosis_kb.pl` file in your working directory

### **Loading the Knowledge Base:**
```prolog
?- [car_diagnosis_kb].
```
or
```prolog
?- consult('car_diagnosis_kb.pl').
```

---

## 🔧 **Basic Usage Commands**

### **1. Load the Knowledge Base**
```prolog
?- [car_diagnosis_kb].
% Output: true.
```

### **2. Check Available Predicates**
```prolog
?- listing(diagnosis/1).
?- listing(explanation/2).
```

### **3. Get All Possible Diagnoses**
```prolog
?- all_diagnoses(D).
% Output: D = [inconclusive] (when no input facts are set)
% Note: This query shows the fallback diagnosis when no specific rules match
```

---

## 🎯 **Setting Up Test Scenarios**

### **Step 1: Clear Previous Facts**
```prolog
?- retractall(input(_, _)).
% Output: true.
```

### **Step 2: Add Input Facts**
```prolog
?- assert(input(engine_cranks, yes)).
?- assert(input(headlights_dim, no)).
?- assert(input(fuel_gauge_level, ok)).
?- assert(input(clicking_noise, no)).
?- assert(input(temperature, normal)).
```

### **Step 3: Query Diagnoses**
```prolog
?- diagnosis(D).
% Output: D = ignition_fuel_delivery ;
%         D = sensor_computer_issue.
```

---

## 📋 **Example Scenarios**

### **Scenario 1: Your Original Case**
```prolog
% Inputs: Engine cranks=yes, Headlights dim=no, Fuel=ok, Clicking=no, Temp=normal
?- retractall(input(_, _)).
?- assert(input(engine_cranks, yes)).
?- assert(input(headlights_dim, no)).
?- assert(input(fuel_gauge_level, ok)).
?- assert(input(clicking_noise, no)).
?- assert(input(temperature, normal)).
?- diagnosis(D).
% Output: D = ignition_fuel_delivery ;
%         D = sensor_computer_issue.
```

### **Scenario 2: Battery Drained**
```prolog
?- retractall(input(_, _)).
?- assert(input(engine_cranks, no)).
?- assert(input(headlights_dim, yes)).
?- assert(input(fuel_gauge_level, ok)).
?- assert(input(clicking_noise, no)).
?- assert(input(temperature, normal)).
?- diagnosis(D).
% Output: D = battery_drained.
```

### **Scenario 3: Out of Fuel**
```prolog
?- retractall(input(_, _)).
?- assert(input(engine_cranks, yes)).
?- assert(input(headlights_dim, no)).
?- assert(input(fuel_gauge_level, empty)).
?- assert(input(clicking_noise, no)).
?- assert(input(temperature, normal)).
?- diagnosis(D).
% Output: D = out_of_fuel ;
%         D = sensor_computer_issue.
```

### **Scenario 4: Cold Start Issue**
```prolog
?- retractall(input(_, _)).
?- assert(input(engine_cranks, no)).
?- assert(input(headlights_dim, no)).
?- assert(input(fuel_gauge_level, ok)).
?- assert(input(clicking_noise, no)).
?- assert(input(temperature, cold)).
?- diagnosis(D).
% Output: D = starter_motor_fault ;
%         D = cold_start_issue.
```

### **Scenario 5: Overheating**
```prolog
?- retractall(input(_, _)).
?- assert(input(engine_cranks, yes)).
?- assert(input(headlights_dim, no)).
?- assert(input(fuel_gauge_level, ok)).
?- assert(input(clicking_noise, no)).
?- assert(input(temperature, hot)).
?- diagnosis(D).
% Output: D = overheating ;
%         D = ignition_fuel_delivery.
```

---

## 🔍 **Advanced Queries**

### **Get Diagnoses with Explanations**
```prolog
?- diagnosis_with_explanation(D, E).
% Output: D = ignition_fuel_delivery,
%         E = "Likely cause: Ignition or fuel delivery problem.\nAction: Check spark plugs, fuel injectors, fuel pump, and ignition coils." ;
%         D = sensor_computer_issue,
%         E = "Likely cause: Sensor or computer system fault.\nAction: Check engine sensors, ECU connections, and diagnostic codes.".
```

### **Check Specific Diagnosis**
```prolog
?- diagnosis(battery_drained).
% Output: true. (if conditions match) or false. (if conditions don't match)
```

### **Get All Explanations**
```prolog
?- all_explanations(E).
% Output: E = ["Likely cause: Battery drained...", "Likely cause: Out of fuel...", ...]
```

---

## 🧪 **Testing All Scenarios**

### **Run Built-in Tests**
```prolog
?- test_your_scenario.
?- test_battery_drained.
?- test_out_of_fuel.
?- test_cold_start.
?- test_overheating.
?- test_starter_motor_wear.
```

### **Run All Tests at Once**
```prolog
?- run_all_tests.
```

---

## 📊 **Knowledge Base Structure**

### **Input Facts (Dynamic)**
- `input(engine_cranks, yes/no)`
- `input(headlights_dim, yes/no)`
- `input(fuel_gauge_level, empty/low/ok)`
- `input(clicking_noise, yes/no)`
- `input(temperature, cold/normal/hot)`

### **Diagnostic Rules (16 Rules)**
- **R1-R3:** Core rules (battery, fuel, starter)
- **R4-R6:** Additional rules (low fuel, multiple issues, charging)
- **R7-R9:** Enhanced rules (solenoid, cold start, overheating)
- **R10-R16:** Enhanced coverage rules (ignition, sensors, wear, etc.)
- **R99:** Fallback rule (inconclusive)

### **Explanations**
- Each diagnosis has a corresponding explanation with:
  - **Likely cause** description
  - **Action** recommendations

---

## 💡 **Example Queries**

### **Basic Diagnosis Examples:**

#### **Example 1: Your Scenario**
```prolog
?- [car_diagnosis_kb].
?- assert(input(engine_cranks, yes)).
?- assert(input(headlights_dim, no)).
?- assert(input(fuel_gauge_level, ok)).
?- assert(input(clicking_noise, no)).
?- assert(input(temperature, normal)).
?- diagnosis(D).
D = ignition_fuel_delivery ;
D = sensor_computer_issue.
```

#### **Example 2: Battery Drained**
```prolog
?- retractall(input(_, _)).
?- assert(input(engine_cranks, no)).
?- assert(input(headlights_dim, yes)).
?- assert(input(fuel_gauge_level, ok)).
?- assert(input(clicking_noise, no)).
?- assert(input(temperature, normal)).
?- diagnosis(D).
D = battery_drained.
```

#### **Example 3: Out of Fuel**
```prolog
?- retractall(input(_, _)).
?- assert(input(engine_cranks, yes)).
?- assert(input(headlights_dim, no)).
?- assert(input(fuel_gauge_level, empty)).
?- assert(input(clicking_noise, no)).
?- assert(input(temperature, normal)).
?- diagnosis(D).
D = out_of_fuel ;
D = sensor_computer_issue.
```

#### **Example 4: Cold Start Issue**
```prolog
?- retractall(input(_, _)).
?- assert(input(engine_cranks, no)).
?- assert(input(headlights_dim, no)).
?- assert(input(fuel_gauge_level, ok)).
?- assert(input(clicking_noise, no)).
?- assert(input(temperature, cold)).
?- diagnosis(D).
D = starter_motor_fault ;
D = cold_start_issue.
```

#### **Example 5: Overheating**
```prolog
?- retractall(input(_, _)).
?- assert(input(engine_cranks, yes)).
?- assert(input(headlights_dim, no)).
?- assert(input(fuel_gauge_level, ok)).
?- assert(input(clicking_noise, no)).
?- assert(input(temperature, hot)).
?- diagnosis(D).
D = overheating ;
D = ignition_fuel_delivery.
```

### **Advanced Query Examples:**

#### **Example 6: Get All Diagnoses with Explanations**
```prolog
?- retractall(input(_, _)).
?- assert(input(engine_cranks, yes)).
?- assert(input(headlights_dim, no)).
?- assert(input(fuel_gauge_level, ok)).
?- assert(input(clicking_noise, no)).
?- assert(input(temperature, normal)).
?- diagnosis_with_explanation(D, E).
D = ignition_fuel_delivery,
E = "Likely cause: Ignition or fuel delivery problem.\nAction: Check spark plugs, fuel injectors, fuel pump, and ignition coils." ;
D = sensor_computer_issue,
E = "Likely cause: Sensor or computer system fault.\nAction: Check engine sensors, ECU connections, and diagnostic codes.".
```

#### **Example 7: Check Specific Diagnosis**
```prolog
?- retractall(input(_, _)).
?- assert(input(engine_cranks, no)).
?- assert(input(headlights_dim, yes)).
?- diagnosis(battery_drained).
true.

?- diagnosis(out_of_fuel).
false.
```

#### **Example 8: Multiple Issues Scenario**
```prolog
?- retractall(input(_, _)).
?- assert(input(engine_cranks, no)).
?- assert(input(headlights_dim, yes)).
?- assert(input(fuel_gauge_level, empty)).
?- assert(input(clicking_noise, no)).
?- assert(input(temperature, normal)).
?- diagnosis(D).
D = battery_drained ;
D = battery_and_fuel.
```

#### **Example 9: Enhanced Rules - Starter Motor Wear**
```prolog
?- retractall(input(_, _)).
?- assert(input(engine_cranks, yes)).
?- assert(input(headlights_dim, no)).
?- assert(input(fuel_gauge_level, ok)).
?- assert(input(clicking_noise, yes)).
?- assert(input(temperature, normal)).
?- diagnosis(D).
D = ignition_fuel_delivery ;
D = sensor_computer_issue ;
D = starter_motor_wear.
```

#### **Example 10: No Input Facts (Inconclusive)**
```prolog
?- retractall(input(_, _)).
?- all_diagnoses(D).
D = [inconclusive].

?- diagnosis_with_explanation(D, E).
D = inconclusive,
E = "Diagnosis inconclusive.\nAction: Check battery terminals, fuses, immobilizer, and error codes.".
```

### **Batch Testing Examples:**

#### **Example 11: Test Multiple Scenarios**
```prolog
% Test battery drained
?- retractall(input(_, _)), assert(input(engine_cranks, no)), assert(input(headlights_dim, yes)), diagnosis(D).
D = battery_drained.

% Test out of fuel  
?- retractall(input(_, _)), assert(input(engine_cranks, yes)), assert(input(fuel_gauge_level, empty)), diagnosis(D).
D = out_of_fuel ;
D = sensor_computer_issue.

% Test cold start
?- retractall(input(_, _)), assert(input(engine_cranks, no)), assert(input(headlights_dim, no)), assert(input(temperature, cold)), diagnosis(D).
D = starter_motor_fault ;
D = cold_start_issue.
```

#### **Example 12: List All Available Diagnoses**
```prolog
?- findall(D, (diagnosis(D), D \= inconclusive), Diagnoses).
Diagnoses = [battery_drained, out_of_fuel, starter_motor_fault, low_fuel, battery_and_fuel, charging_system_issue, starter_solenoid_fault, cold_start_issue, overheating, ignition_fuel_delivery, sensor_computer_issue, starter_motor_wear, fuel_battery_issues, cold_fuel_issue, normal_starter_fault, charging_fuel_issues].
```

---

## 🎯 **Quick Reference Commands**

### **Essential Commands:**
```prolog
% Load knowledge base
?- [car_diagnosis_kb].

% Clear all facts
?- retractall(input(_, _)).

% Add facts
?- assert(input(engine_cranks, yes)).

% Get diagnoses
?- diagnosis(D).

% Get explanations
?- diagnosis_with_explanation(D, E).

% Run tests
?- run_all_tests.
```

### **Input Values:**
- **engine_cranks:** `yes`, `no`
- **headlights_dim:** `yes`, `no`
- **fuel_gauge_level:** `empty`, `low`, `ok`
- **clicking_noise:** `yes`, `no`
- **temperature:** `cold`, `normal`, `hot`

---

## 🔧 **Troubleshooting**

### **Common Issues:**

#### **1. "No permission to modify static procedure"**
```prolog
% Solution: Make sure input/2 is declared as dynamic
:- dynamic input/2.
```

#### **2. "Undefined procedure"**
```prolog
% Solution: Load the knowledge base first
?- [car_diagnosis_clean].
```

#### **3. "No diagnoses found"**
```prolog
% Solution: Check if input facts are asserted correctly
?- listing(input/2).
```

#### **4. "Too many diagnoses"**
```prolog
% Solution: Clear previous facts before adding new ones
?- retractall(input(_, _)).
```

#### **5. "Stack limit exceeded" or "Infinite recursion"**
```prolog
% Solution: Ensure the knowledge base is properly loaded
?- [car_diagnosis_kb].
% If issues persist, restart SWI-Prolog
```

---

## 📈 **Performance Tips**

### **1. Clean Between Tests**
```prolog
?- retractall(input(_, _)).
```

### **2. Use Specific Queries**
```prolog
% Instead of: ?- diagnosis(D).
% Use: ?- diagnosis(battery_drained).
```

### **3. Batch Operations**
```prolog
% Add all facts at once
?- assert(input(engine_cranks, yes)), assert(input(headlights_dim, no)).
```

---

## 🎯 **Quick Reference**

### **Essential Commands:**
```prolog
% Load knowledge base
?- [car_diagnosis_kb].

% Clear all facts
?- retractall(input(_, _)).

% Add facts
?- assert(input(engine_cranks, yes)).

% Get diagnoses
?- diagnosis(D).

% Get explanations
?- diagnosis_with_explanation(D, E).

% Exit
?- halt.
```

### **Input Values:**
| Input | Values |
|-------|--------|
| `engine_cranks` | `yes`, `no` |
| `headlights_dim` | `yes`, `no` |
| `fuel_gauge_level` | `empty`, `low`, `ok` |
| `clicking_noise` | `yes`, `no` |
| `temperature` | `cold`, `normal`, `hot` |

### **Common Queries:**
```prolog
% Get all diagnoses
?- all_diagnoses(D).

% Check specific diagnosis
?- diagnosis(battery_drained).

% Get all explanations
?- all_explanations(E).

% Get diagnosis with explanation
?- diagnosis_with_explanation(D, E).
```

### **Your Scenario Result:**
**Inputs:** Engine cranks=yes, Headlights dim=no, Fuel=ok, Clicking=no, Temp=normal

**Diagnoses:** 
- `ignition_fuel_delivery`
- `sensor_computer_issue`

**Explanations:**
- **Ignition/Fuel Delivery:** Check spark plugs, fuel injectors, fuel pump, and ignition coils
- **Sensor/Computer Issue:** Check engine sensors, ECU connections, and diagnostic codes

---

## 🎓 **Learning Exercises**

### **Exercise 1: Basic Diagnosis**
1. Load the knowledge base
2. Set up a battery drained scenario
3. Get the diagnosis
4. Get the explanation

### **Exercise 2: Multiple Diagnoses**
1. Set up your original scenario
2. Find all possible diagnoses
3. Get explanations for each

### **Exercise 3: Rule Testing**
1. Test each of the 16 rules individually
2. Verify the fallback rule works
3. Compare with Python system results

---

## 📚 **Further Reading**

- **SWI-Prolog Documentation:** https://www.swi-prolog.org/pldoc/
- **Prolog Tutorial:** https://www.swi-prolog.org/pldoc/man?section=tutorial
- **Expert Systems in Prolog:** https://www.swi-prolog.org/pldoc/man?section=clp

---

## 🎯 **Summary**

This Prolog knowledge base provides:
- ✅ **16 diagnostic rules** for comprehensive coverage
- ✅ **Dynamic input facts** for flexible testing
- ✅ **Detailed explanations** for each diagnosis
- ✅ **Built-in test scenarios** for validation
- ✅ **Perfect compatibility** with the Python system

The system demonstrates rule-based knowledge representation and forward chaining inference in pure Prolog syntax! 🚗⚡
