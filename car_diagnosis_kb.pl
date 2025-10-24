% Car No-Start Expert System Knowledge Base
% Prolog implementation with 16 diagnostic rules
% Complete knowledge base for automotive diagnostics

% ============================================================================
% DIAGNOSTIC RULES
% ============================================================================

% Make input facts dynamic
:- dynamic input/2.

% Core Rules (R1-R3)
% Rule R1: Battery drained
diagnosis(battery_drained) :-
    input(engine_cranks, no),
    input(headlights_dim, yes).

% Rule R2: Out of fuel
diagnosis(out_of_fuel) :-
    input(engine_cranks, yes),
    input(fuel_gauge_level, empty).

% Rule R3: Starter motor fault
diagnosis(starter_motor_fault) :-
    input(engine_cranks, no),
    input(headlights_dim, no).

% Additional Rules (R4-R6)
% Rule R4: Low fuel issue
diagnosis(low_fuel) :-
    input(engine_cranks, yes),
    input(fuel_gauge_level, low).

% Rule R5: Battery and fuel issues
diagnosis(battery_and_fuel) :-
    input(engine_cranks, no),
    input(headlights_dim, yes),
    input(fuel_gauge_level, empty).

% Rule R6: Charging system issue
diagnosis(charging_system_issue) :-
    input(engine_cranks, yes),
    input(headlights_dim, yes).

% Enhanced Rules (R7-R9)
% Rule R7: Starter solenoid fault
diagnosis(starter_solenoid_fault) :-
    input(engine_cranks, no),
    input(headlights_dim, no),
    input(clicking_noise, yes).

% Rule R8: Cold start issue
diagnosis(cold_start_issue) :-
    input(engine_cranks, no),
    input(headlights_dim, no),
    input(temperature, cold).

% Rule R9: Overheating
diagnosis(overheating) :-
    input(engine_cranks, yes),
    input(fuel_gauge_level, ok),
    input(temperature, hot).

% Enhanced Coverage Rules (R10-R16)
% Rule R10: Ignition/fuel delivery issue
diagnosis(ignition_fuel_delivery) :-
    input(engine_cranks, yes),
    input(headlights_dim, no),
    input(fuel_gauge_level, ok).

% Rule R11: Sensor/computer issue
diagnosis(sensor_computer_issue) :-
    input(engine_cranks, yes),
    input(temperature, normal).

% Rule R12: Starter motor wear
diagnosis(starter_motor_wear) :-
    input(engine_cranks, yes),
    input(clicking_noise, yes).

% Rule R13: Fuel and battery issues
diagnosis(fuel_battery_issues) :-
    input(fuel_gauge_level, low),
    input(headlights_dim, yes).

% Rule R14: Cold fuel issue
diagnosis(cold_fuel_issue) :-
    input(engine_cranks, yes),
    input(fuel_gauge_level, low),
    input(temperature, cold).

% Rule R15: Normal starter fault
diagnosis(normal_starter_fault) :-
    input(engine_cranks, no),
    input(headlights_dim, no),
    input(temperature, normal).

% Rule R16: Charging and fuel issues
diagnosis(charging_fuel_issues) :-
    input(engine_cranks, yes),
    input(headlights_dim, yes),
    input(fuel_gauge_level, low).

% Fallback Rule (R99)
% Rule R99: Inconclusive diagnosis
diagnosis(inconclusive) :-
    \+ (diagnosis(battery_drained); diagnosis(out_of_fuel); diagnosis(starter_motor_fault);
        diagnosis(low_fuel); diagnosis(battery_and_fuel); diagnosis(charging_system_issue);
        diagnosis(starter_solenoid_fault); diagnosis(cold_start_issue); diagnosis(overheating);
        diagnosis(ignition_fuel_delivery); diagnosis(sensor_computer_issue); diagnosis(starter_motor_wear);
        diagnosis(fuel_battery_issues); diagnosis(cold_fuel_issue); diagnosis(normal_starter_fault);
        diagnosis(charging_fuel_issues)).

% ============================================================================
% EXPLANATIONS AND RECOMMENDATIONS
% ============================================================================

% Explanation facts for each diagnosis
explanation(battery_drained, 
    "Likely cause: Battery drained.\\nAction: Try jump-starting; test/replace battery; check alternator output.").

explanation(out_of_fuel, 
    "Likely cause: Out of fuel.\\nAction: Add fuel; if recurring, inspect for leaks or faulty gauge/sender.").

explanation(starter_motor_fault, 
    "Likely cause: Starter motor/solenoid fault.\\nAction: Inspect starter relay/solenoid, wiring; consider shop service.").

explanation(low_fuel, 
    "Likely cause: Low fuel level.\\nAction: Add fuel; check for leaks; verify fuel gauge accuracy.").

explanation(battery_and_fuel, 
    "Likely cause: Multiple issues - battery drained and out of fuel.\\nAction: Add fuel first, then jump-start or charge battery.").

explanation(charging_system_issue, 
    "Likely cause: Charging system problem.\\nAction: Test alternator output; check battery connections; inspect belt.").

explanation(starter_solenoid_fault, 
    "Likely cause: Starter solenoid failure.\\nAction: Replace starter solenoid; check starter relay; inspect wiring.").

explanation(cold_start_issue, 
    "Likely cause: Cold weather starting problem.\\nAction: Use block heater; check coolant level; consider winter oil.").

explanation(overheating, 
    "Likely cause: Engine overheating.\\nAction: Check coolant level; inspect radiator; test thermostat.").

explanation(ignition_fuel_delivery, 
    "Likely cause: Ignition or fuel delivery problem.\\nAction: Check spark plugs, fuel injectors, fuel pump, and ignition coils.").

explanation(sensor_computer_issue, 
    "Likely cause: Sensor or computer system fault.\\nAction: Check engine sensors, ECU connections, and diagnostic codes.").

explanation(starter_motor_wear, 
    "Likely cause: Starter motor wearing out.\\nAction: Test starter motor; consider replacement if clicking persists.").

explanation(fuel_battery_issues, 
    "Likely cause: Multiple issues - low fuel and battery problems.\\nAction: Add fuel first, then check battery and charging system.").

explanation(cold_fuel_issue, 
    "Likely cause: Cold weather fuel system problem.\\nAction: Use fuel additives; check fuel lines for condensation.").

explanation(normal_starter_fault, 
    "Likely cause: Starter motor or solenoid fault.\\nAction: Test starter relay; inspect starter motor and wiring.").

explanation(charging_fuel_issues, 
    "Likely cause: Charging system and fuel problems.\\nAction: Add fuel; test alternator; check battery connections.").

explanation(inconclusive, 
    "Diagnosis inconclusive.\\nAction: Check battery terminals, fuses, immobilizer, and error codes.").

% ============================================================================
% QUERY HELPERS
% ============================================================================

% Get all possible diagnoses
all_diagnoses(Diagnoses) :-
    findall(D, diagnosis(D), Diagnoses).

% Get diagnosis with explanation
diagnosis_with_explanation(Diagnosis, Explanation) :-
    diagnosis(Diagnosis),
    explanation(Diagnosis, Explanation).

% Check if a specific diagnosis is possible
possible_diagnosis(Diagnosis) :-
    diagnosis(Diagnosis).

% Get all explanations
all_explanations(Explanations) :-
    findall(Exp, explanation(_, Exp), Explanations).

% ============================================================================
% USAGE EXAMPLES
% ============================================================================

% Example 1: Your scenario (Engine cranks + bright lights + fuel OK + no clicking + normal temp)
% Query: ?- assert(input(engine_cranks, yes)), assert(input(headlights_dim, no)), 
%        assert(input(fuel_gauge_level, ok)), assert(input(clicking_noise, no)), 
%        assert(input(temperature, normal)), diagnosis(D).
% Expected results: ignition_fuel_delivery, sensor_computer_issue

% Example 2: Battery drained scenario
% Query: ?- assert(input(engine_cranks, no)), assert(input(headlights_dim, yes)), diagnosis(D).
% Expected result: battery_drained

% Example 3: Get all possible diagnoses
% Query: ?- all_diagnoses(D).
% Expected: List of all 16 possible diagnoses

% Example 4: Get diagnosis with explanation
% Query: ?- diagnosis_with_explanation(D, E).
% Expected: All diagnosis-explanation pairs

% ============================================================================
% USAGE INSTRUCTIONS
% ============================================================================

% To use this knowledge base:
% 1. Load the file: ?- [car_diagnosis_kb].
% 2. Set input facts: assert(input(engine_cranks, yes)).
% 3. Query diagnoses: ?- diagnosis(D).
% 4. Get explanations: ?- diagnosis_with_explanation(D, E).

% Example session:
% ?- [car_diagnosis_kb].
% ?- assert(input(engine_cranks, yes)).
% ?- assert(input(headlights_dim, no)).
% ?- assert(input(fuel_gauge_level, ok)).
% ?- assert(input(clicking_noise, no)).
% ?- assert(input(temperature, normal)).
% ?- diagnosis(D).
% D = ignition_fuel_delivery ;
% D = sensor_computer_issue.
