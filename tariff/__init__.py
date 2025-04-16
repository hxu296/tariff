"""
🇺🇸 TARIFF 🇺🇸 - Make importing great again!
"""

import builtins
import importlib
import multiprocessing
import random
import sys
import time
from functools import partial
from math import cos, sin, sqrt, tan

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
    "HUGE success!",
]


def _get_trump_phrase():
    """Get a random Trump-like phrase."""
    return random.choice(_trump_phrases)


def manufacture_float(x: float, depth: int = 10):
    if depth == 0:
        return x
    return sqrt(tan(cos(sin(manufacture_float(x, depth - 1)))) ** 2)


def domestic_float_factory(T: float):
    t = time.time()
    while time.time() - t < T:
        yield 1 / manufacture_float(time.time())


def work(T: float, process_id: int):
    """
    Do work on all CPU cores for T seconds.
    Float generation the likes of which have NEVER been SEEN before.

    Args:
        T (float): The time in seconds to apply the tariff for.
    """

    [n for n in domestic_float_factory(T)]


def apply_tariff(T: float):
    """Duplicate the same calculation across all cores"""

    num_cores = multiprocessing.cpu_count()
    with multiprocessing.Pool(processes=num_cores) as pool:
        _ = pool.map(partial(work, T), range(num_cores))


def set(tariff_sheet):
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


def _tariffed_import(name, globals=None, locals=None, fromlist=(), level=0):
    """Custom import function that applies tariffs."""
    # Check if the package is in our tariff sheet
    base_package = name.split(".")[0]
    tariff_rate = _tariff_sheet.get(base_package)

    # Measure import time
    start_time = time.time()
    module = original_import(name, globals, locals, fromlist, level)
    original_import_time = (
        time.time() - start_time
    ) * 1000000  # convert to microseconds

    # Apply tariff if applicable
    if tariff_rate is not None:
        # Calculate sleep time based on tariff rate
        tariff_time = original_import_time * (tariff_rate / 100)

        builtins.__import__ = original_import
        apply_tariff(tariff_time / 1000000)
        builtins.__import__ = _tariffed_import

        # Calculate new total time
        new_total_time = original_import_time + tariff_time

        # Print tariff announcement in Trump style
        print(
            f"JUST IMPOSED a {tariff_rate}% TARIFF on {base_package}! Original import took {int(original_import_time)} us, "
            f"now takes {int(new_total_time)} us. {_get_trump_phrase()}"
        )

    return module
