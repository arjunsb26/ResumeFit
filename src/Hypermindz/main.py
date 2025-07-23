#!/usr/bin/env python
import sys
from Hypermindz.crew import HypermindzCrew


def run():
    """
    Run the crew.
    """
    inputs = {}    # Example: {"input_key": "input_value"}  # Replace with actual inputs as needed
    HypermindzCrew().crew().kickoff(inputs=inputs)
