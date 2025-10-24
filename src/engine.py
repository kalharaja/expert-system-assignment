# src/engine.py
"""
Expert system engine for car no-start diagnosis.
This module contains the main inference engine that combines facts and rules.
"""

from experta import KnowledgeEngine
from facts import Input, Hypothesis, Phase
from rules import CarDiagnosisRules


class CarDiagnosisEngine(KnowledgeEngine, CarDiagnosisRules):
    """
    Main expert system engine for car no-start diagnosis.
    Combines the knowledge base rules with the inference engine.
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Keep a reasoning trace for explanations
        self.trace = []

    def reset(self):
        """Reset the engine and clear the trace"""
        super().reset()
        self.trace = []


def run_engine_with_inputs(engine_cranks: str, headlights_dim: str, fuel_gauge_level: str, clicking_noise: str = "no", temperature: str = "normal"):
    """
    Convenience function to run the engine and return (hypotheses, trace)
    
    Args:
        engine_cranks: 'yes'/'no'
        headlights_dim: 'yes'/'no' 
        fuel_gauge_level: 'empty'/'low'/'ok'
    
    Returns:
        tuple: (list of hypotheses, reasoning trace)
    """
    eng = CarDiagnosisEngine()
    eng.reset()

    # Sanitize inputs to lowercase
    ec = engine_cranks.strip().lower()
    hd = headlights_dim.strip().lower()
    fg = fuel_gauge_level.strip().lower()
    cn = clicking_noise.strip().lower()
    temp = temperature.strip().lower()

    # Assert user inputs as facts
    eng.declare(Input(name="engine_cranks", value=ec))
    eng.declare(Input(name="headlights_dim", value=hd))
    eng.declare(Input(name="fuel_gauge_level", value=fg))
    eng.declare(Input(name="clicking_noise", value=cn))
    eng.declare(Input(name="temperature", value=temp))

    # Run the inference engine
    eng.run()

    # Collect results
    hypos = [f['label'] for f in eng.facts.values() if isinstance(f, Hypothesis)]
    return hypos, eng.trace


def explain(hypothesis_label: str) -> str:
    """
    Human-friendly recommendations for each hypothesis.
    
    Args:
        hypothesis_label: The diagnosis label
        
    Returns:
        str: Detailed explanation and recommendations
    """
    mapping = {
        # Basic diagnoses
        "battery_drained": (
            "Likely cause: Battery drained.\n"
            "Action: Try jump-starting; test/replace battery; check alternator output."
        ),
        "out_of_fuel": (
            "Likely cause: Out of fuel.\n"
            "Action: Add fuel; if recurring, inspect for leaks or faulty gauge/sender."
        ),
        "starter_motor_fault": (
            "Likely cause: Starter motor/solenoid fault.\n"
            "Action: Inspect starter relay/solenoid, wiring; consider shop service."
        ),
        
        # Additional diagnoses
        "low_fuel": (
            "Likely cause: Low fuel level.\n"
            "Action: Add fuel; check for leaks; verify fuel gauge accuracy."
        ),
        "battery_and_fuel": (
            "Likely cause: Multiple issues - battery drained and out of fuel.\n"
            "Action: Add fuel first, then jump-start or charge battery."
        ),
        "charging_system_issue": (
            "Likely cause: Charging system problem.\n"
            "Action: Test alternator output; check battery connections; inspect belt."
        ),
        "starter_solenoid_fault": (
            "Likely cause: Starter solenoid failure.\n"
            "Action: Replace starter solenoid; check starter relay; inspect wiring."
        ),
        "cold_start_issue": (
            "Likely cause: Cold weather starting problem.\n"
            "Action: Use block heater; check coolant level; consider winter oil."
        ),
        "overheating": (
            "Likely cause: Engine overheating.\n"
            "Action: Check coolant level; inspect radiator; test thermostat."
        ),
        "ignition_fuel_delivery": (
            "Likely cause: Ignition or fuel delivery problem.\n"
            "Action: Check spark plugs, fuel injectors, fuel pump, and ignition coils."
        ),
        "sensor_computer_issue": (
            "Likely cause: Sensor or computer system fault.\n"
            "Action: Check engine sensors, ECU connections, and diagnostic codes."
        ),
        "starter_motor_wear": (
            "Likely cause: Starter motor wearing out.\n"
            "Action: Test starter motor; consider replacement if clicking persists."
        ),
        "fuel_battery_issues": (
            "Likely cause: Multiple issues - low fuel and battery problems.\n"
            "Action: Add fuel first, then check battery and charging system."
        ),
        "cold_fuel_issue": (
            "Likely cause: Cold weather fuel system problem.\n"
            "Action: Use fuel additives; check fuel lines for condensation."
        ),
        "normal_starter_fault": (
            "Likely cause: Starter motor or solenoid fault.\n"
            "Action: Test starter relay; inspect starter motor and wiring."
        ),
        "charging_fuel_issues": (
            "Likely cause: Charging system and fuel problems.\n"
            "Action: Add fuel; test alternator; check battery connections."
        ),
        "inconclusive": (
            "Diagnosis inconclusive.\n"
            "Action: Check battery terminals, fuses, immobilizer, and error codes."
        ),
    }
    return mapping.get(hypothesis_label, "No explanation available.")
