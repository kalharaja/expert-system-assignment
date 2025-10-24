# src/facts.py
"""
Fact definitions for the Car No-Start Expert System.
This module contains all fact types used in the knowledge base.
"""

from experta import Fact, Field


class Input(Fact):
    """User inputs as facts, e.g., Input(name='engine_cranks', value='yes')"""
    name = Field(str, mandatory=True)
    value = Field(str, mandatory=True)


class Hypothesis(Fact):
    """Inferred hypothesis (diagnosis)"""
    label = Field(str, mandatory=True)


class Phase(Fact):
    """Phase marker for control flow"""
    name = Field(str, mandatory=True)
