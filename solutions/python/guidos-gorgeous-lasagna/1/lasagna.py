"""
Functions used in preparing Guido's gorgeous lasagna.
"""

# Constants
EXPECTED_BAKE_TIME = 40  # minutes
PREPARATION_TIME = 2     # minutes per layer

# Function 1
def bake_time_remaining(minutes_in_oven):
    """Calculate remaining bake time."""
    return EXPECTED_BAKE_TIME - minutes_in_oven

# Function 2
def preparation_time_in_minutes(number_of_layers):
    """Calculate prep time for number of layers."""
    return number_of_layers * PREPARATION_TIME

# Function 3
def elapsed_time_in_minutes(number_of_layers, bake_time):
    """Calculate total time spent (prep + bake)."""
    return preparation_time_in_minutes(number_of_layers) + bake_time