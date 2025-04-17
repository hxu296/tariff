"""
🇺🇸 TARIFF 🇺🇸 - Make importing great again!
"""

import sys
import time
import builtins
import importlib
import random
import tracemalloc

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
_memory_stash = set()

def _get_trump_phrase():
    """Get a random Trump-like phrase."""
    return random.choice(_trump_phrases)

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

def _memory_diff(before, after):
    diff = after.compare_to(before, 'filename')
    total = 0
    for d in diff:
      total += d.size_diff
    return total

def _tariffed_import(name, globals=None, locals=None, fromlist=(), level=0):
    """Custom import function that applies tariffs."""
    # Check if the package is in our tariff sheet
    base_package = name.split('.')[0]
    tariff_rate = _tariff_sheet.get(base_package)
    
    # Measure import time and memory
    tracemalloc.start()
    memory_before = tracemalloc.take_snapshot()
    start_time = time.time()
    module = original_import(name, globals, locals, fromlist, level)
    original_import_time = (time.time() - start_time) * 1000000  # convert to microseconds
    memory_after = tracemalloc.take_snapshot()
    tracemalloc.stop()
    original_memory_consumption = _memory_diff(memory_before, memory_after)

    # Apply tariff if applicable
    if tariff_rate is not None:
        # Calculate sleep time based on tariff rate
        sleep_time = original_import_time * (tariff_rate / 100)
        time.sleep(sleep_time / 1000000)  # convert back to seconds

        # Calculate memory based on tariff rate
        memory_consumption = original_memory_consumption * (tarriff_rate / 100)
        _memory_stash.add(bytearray(memory_consumption))
        
        # Calculate new total time and memory
        new_total_time = original_import_time + sleep_time
        new_total_memory = original_memory_consumption + memory_consumption
        
        # Print tariff announcement in Trump style
        print(f"JUST IMPOSED a {tariff_rate}% TARIFF on {base_package}! Original import took {int(original_import_time)} us and {original_memory_consumption} bytes, "
              f"now takes {int(new_total_time)} us and {new_total_memory}. {_get_trump_phrase()}")
    
    return module 
