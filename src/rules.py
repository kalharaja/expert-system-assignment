# src/rules.py
"""
Rule definitions for the Car No-Start Expert System.
This module contains all diagnostic rules in the knowledge base.
"""

from experta import Rule, DefFacts, MATCH
from facts import Input, Hypothesis, Phase


class CarDiagnosisRules:
    """Knowledge base rules for car no-start diagnosis"""
    
    @DefFacts()
    def _initial(self):
        """Initialize the reasoning phase"""
        yield Phase(name="reasoning")

    # --- Basic Diagnostic Rules ---
    
    @Rule(Phase(name="reasoning"),
          Input(name="engine_cranks", value="no"),
          Input(name="headlights_dim", value="yes"))
    def rule_battery_drained(self):
        """Rule R1: No cranking + dim headlights = battery drained"""
        self.trace.append("R1: no cranking & dim headlights ⇒ battery drained")
        self.declare(Hypothesis(label="battery_drained"))

    @Rule(Phase(name="reasoning"),
          Input(name="engine_cranks", value="yes"),
          Input(name="fuel_gauge_level", value="empty"))
    def rule_out_of_fuel(self):
        """Rule R2: Engine cranks + empty fuel gauge = out of fuel"""
        self.trace.append("R2: engine cranks & fuel gauge empty ⇒ out of fuel")
        self.declare(Hypothesis(label="out_of_fuel"))

    @Rule(Phase(name="reasoning"),
          Input(name="engine_cranks", value="no"),
          Input(name="headlights_dim", value="no"))
    def rule_starter_motor_fault(self):
        """Rule R3: No cranking + bright headlights = starter motor fault"""
        self.trace.append("R3: no cranking & headlights not dim ⇒ starter motor fault")
        self.declare(Hypothesis(label="starter_motor_fault"))

    # --- Additional Diagnostic Rules ---
    
    @Rule(Phase(name="reasoning"),
          Input(name="engine_cranks", value="yes"),
          Input(name="fuel_gauge_level", value="low"))
    def rule_low_fuel(self):
        """Rule R4: Engine cranks + low fuel = low fuel issue"""
        self.trace.append("R4: engine cranks & low fuel ⇒ low fuel issue")
        self.declare(Hypothesis(label="low_fuel"))

    @Rule(Phase(name="reasoning"),
          Input(name="engine_cranks", value="no"),
          Input(name="headlights_dim", value="yes"),
          Input(name="fuel_gauge_level", value="empty"))
    def rule_battery_and_fuel(self):
        """Rule R5: No cranking + dim lights + empty fuel = multiple issues"""
        self.trace.append("R5: no cranking + dim lights + empty fuel ⇒ battery and fuel issues")
        self.declare(Hypothesis(label="battery_and_fuel"))

    @Rule(Phase(name="reasoning"),
          Input(name="engine_cranks", value="yes"),
          Input(name="headlights_dim", value="yes"))
    def rule_charging_system(self):
        """Rule R6: Engine cranks + dim lights = charging system issue"""
        self.trace.append("R6: engine cranks + dim lights ⇒ charging system issue")
        self.declare(Hypothesis(label="charging_system_issue"))

    @Rule(Phase(name="reasoning"),
          Input(name="engine_cranks", value="no"),
          Input(name="headlights_dim", value="no"),
          Input(name="clicking_noise", value="yes"))
    def rule_starter_solenoid_fault(self):
        """Rule R7: No cranking + bright lights + clicking = starter solenoid fault"""
        self.trace.append("R7: no cranking + bright lights + clicking ⇒ starter solenoid fault")
        self.declare(Hypothesis(label="starter_solenoid_fault"))

    @Rule(Phase(name="reasoning"),
          Input(name="engine_cranks", value="no"),
          Input(name="headlights_dim", value="no"),
          Input(name="temperature", value="cold"))
    def rule_cold_start_issue(self):
        """Rule R8: No cranking + bright lights + cold weather = cold start issue"""
        self.trace.append("R8: no cranking + bright lights + cold weather ⇒ cold start issue")
        self.declare(Hypothesis(label="cold_start_issue"))

    @Rule(Phase(name="reasoning"),
          Input(name="engine_cranks", value="yes"),
          Input(name="fuel_gauge_level", value="ok"),
          Input(name="temperature", value="hot"))
    def rule_overheating(self):
        """Rule R9: Engine cranks + fuel OK + hot weather = overheating"""
        self.trace.append("R9: engine cranks + fuel OK + hot weather ⇒ overheating")
        self.declare(Hypothesis(label="overheating"))

    # --- Enhanced Coverage Rules ---

    @Rule(Phase(name="reasoning"),
          Input(name="engine_cranks", value="yes"),
          Input(name="headlights_dim", value="no"),
          Input(name="fuel_gauge_level", value="ok"))
    def rule_ignition_fuel_delivery(self):
        """Rule R10: Engine cranks + bright lights + fuel OK = ignition/fuel delivery issue"""
        self.trace.append("R10: engine cranks + bright lights + fuel OK ⇒ ignition/fuel delivery issue")
        self.declare(Hypothesis(label="ignition_fuel_delivery"))

    @Rule(Phase(name="reasoning"),
          Input(name="engine_cranks", value="yes"),
          Input(name="temperature", value="normal"))
    def rule_sensor_computer_issue(self):
        """Rule R11: Engine cranks in normal conditions = sensor/computer issue"""
        self.trace.append("R11: engine cranks + normal conditions ⇒ sensor/computer issue")
        self.declare(Hypothesis(label="sensor_computer_issue"))

    @Rule(Phase(name="reasoning"),
          Input(name="engine_cranks", value="yes"),
          Input(name="clicking_noise", value="yes"))
    def rule_starter_motor_wear(self):
        """Rule R12: Engine cranks with clicking = starter motor wear"""
        self.trace.append("R12: engine cranks + clicking ⇒ starter motor wear")
        self.declare(Hypothesis(label="starter_motor_wear"))

    @Rule(Phase(name="reasoning"),
          Input(name="fuel_gauge_level", value="low"),
          Input(name="headlights_dim", value="yes"))
    def rule_fuel_battery_issues(self):
        """Rule R13: Low fuel + dim lights = fuel and battery issues"""
        self.trace.append("R13: low fuel + dim lights ⇒ fuel and battery issues")
        self.declare(Hypothesis(label="fuel_battery_issues"))

    @Rule(Phase(name="reasoning"),
          Input(name="engine_cranks", value="yes"),
          Input(name="fuel_gauge_level", value="low"),
          Input(name="temperature", value="cold"))
    def rule_cold_fuel_issue(self):
        """Rule R14: Engine cranks + low fuel + cold = cold fuel issue"""
        self.trace.append("R14: engine cranks + low fuel + cold ⇒ cold fuel issue")
        self.declare(Hypothesis(label="cold_fuel_issue"))

    @Rule(Phase(name="reasoning"),
          Input(name="engine_cranks", value="no"),
          Input(name="headlights_dim", value="no"),
          Input(name="temperature", value="normal"))
    def rule_normal_starter_fault(self):
        """Rule R15: No crank + bright lights + normal temp = starter fault"""
        self.trace.append("R15: no crank + bright lights + normal temp ⇒ starter fault")
        self.declare(Hypothesis(label="normal_starter_fault"))

    @Rule(Phase(name="reasoning"),
          Input(name="engine_cranks", value="yes"),
          Input(name="headlights_dim", value="yes"),
          Input(name="fuel_gauge_level", value="low"))
    def rule_charging_fuel_issues(self):
        """Rule R16: Engine cranks + dim lights + low fuel = charging and fuel issues"""
        self.trace.append("R16: engine cranks + dim lights + low fuel ⇒ charging and fuel issues")
        self.declare(Hypothesis(label="charging_fuel_issues"))

    # --- Fallback Rules ---
    
    @Rule(Phase(name="reasoning"),
          ~Hypothesis(label=MATCH.any_label))  # no hypothesis asserted
    def rule_inconclusive(self):
        """Rule R99: No matching rule = inconclusive diagnosis"""
        self.trace.append("R99: No rule matched ⇒ diagnosis inconclusive")
        self.declare(Hypothesis(label="inconclusive"))
