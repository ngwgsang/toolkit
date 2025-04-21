# toolkit/__init__.py

"""
Toolkit: A modular library for NLP research, with utilities for evaluation, IO, and reporting.
"""

from . import evaluation, io, report, utils

__all__ = [
    "io", 
    "evaluation", 
    "report", 
    "utils"
]