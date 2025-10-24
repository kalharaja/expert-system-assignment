# src/kb_car_diag.py
"""
Main knowledge base module for the Car No-Start Expert System.
This module provides the main interface and imports all components.
"""

# Fix for frozendict compatibility with modern Python versions
import collections.abc
if not hasattr(collections, 'Mapping'):
    collections.Mapping = collections.abc.Mapping
    collections.MutableMapping = collections.abc.MutableMapping
    collections.Sequence = collections.abc.Sequence
    collections.MutableSequence = collections.abc.MutableSequence
    collections.Set = collections.abc.Set
    collections.MutableSet = collections.abc.MutableSet

# Import the main engine and convenience functions
from engine import run_engine_with_inputs, explain