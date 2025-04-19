"""
🇺🇸 TARIFF 🇺🇸 - Make importing great again!
"""

import sys
import time
import builtins
import importlib
import random
# Store the original import function
original_import = builtins.__import__

# Global tariff sheet
_tariff_sheet = {}

# List of Trump-like phrases
_trump_phrases = [
    "American packages are WINNING AGAIN!",
    "We're bringing back JOBS to our codebase!",
    "This is how we get FAIR TRADE in Python!",
    "Big win for AMERICAN programmers!",
    "No more BAD DEALS with foreign packages!",
    "Making Programming Great Again!",
    "Believe me, this is the BEST tariff!",
    "We're going to win SO MUCH, you'll get tired of winning!",
    "This is how we Keep America Coding Again!",
    "HUGE success!"
]


def _get_trump_phrase():
    """Get a random Trump-like phrase."""
    return random.choice(_trump_phrases)


def set(tariff_sheet, big_num=None, max_num=None):
    """
    Set tariff rates for packages.

    Args:
        tariff_sheet (dict): Dictionary mapping package names to tariff percentages.
                             e.g., {"numpy": 50, "pandas": 200}
    """
    global _tariff_sheet
    _tariff_sheet = tariff_sheet

    # Only patch the import once
    if builtins.__import__ is not original_import:
        return

    # Replace the built-in import with our custom version
    builtins.__import__ = _tariffed_import

    global big_num

    big_num = big_num if big_num else 20
    max_num = max_num if max_num else 20


def _tariffed_import(name, globals=None, locals=None, fromlist=(), level=0):
    """Custom import function that applies tariffs."""
    # Check if the package is in our tariff sheet
    packages_num += 1
    if packages_num >= max_num:
        print("Too much packages.😡😡😡")
        return
    base_package = name.split('.')[0]
    if base_package in _tariff_sheet:
        tariff_rate = _tariff_sheet.pop(base_package)
    else:
        tariff_rate = _tariff_sheet[0]
    for i in _tariff_sheet:
        # Tariff up
        _tariff_sheet[i] *= 1.1
        if packages_num >= big_num:
            _tariff_sheet[i] *= 1.1

    # Measure import time
    start_time = time.time()
    module = original_import(name, globals, locals, fromlist, level)
    original_import_time = (time.time() - start_time) * \
        1000000  # convert to microseconds

    # Apply tariff if applicable
    if tariff_rate is not None:
        # Calculate sleep time based on tariff rate
        sleep_time = original_import_time * (100+tariff_rate / 1000)
        if packages_num >= big_num:
            sleep_time *= 10
        time.sleep(sleep_time / 1000000)  # convert back to seconds

        # Calculate new total time
        new_total_time = original_import_time + sleep_time

        # Print tariff announcement in Trump style
        print(f"JUST IMPOSED a {tariff_rate}% TARIFF on {base_package}! Original import took {int(original_import_time)} us, "
              f"now takes {int(new_total_time)} us. {_get_trump_phrase()}")

    return module


print("Setting tariffs on packages...")

set({
    0: 100,
    "time": 50,        # 50% tariff
    "os": 100,         # 100% tariff
    "sys": 200         # 200% tariff
},
    big_num=20,
    max_num=100)
packages_num = 0
