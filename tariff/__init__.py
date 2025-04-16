"""
🇺🇸 TARIFF 🇺🇸 - Make importing great again!
"""

import builtins
import importlib
import random
import time

# Store the original import function
original_import = builtins.__import__
original_importlib_import = importlib.__import__
original_importlib_import_module = importlib.import_module

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
    if builtins.__import__ is original_import:
        builtins.__import__ = _decorate_with_tariff(original_import)

    if importlib.__import__ is original_importlib_import:
        importlib.__import__ = _decorate_with_tariff(original_importlib_import)

    if importlib.import_module is original_importlib_import_module:
        importlib.import_module = _decorate_with_tariff(
            original_importlib_import_module
        )


def _decorate_with_tariff(import_func):
    def tariffed(*args, **kwargs):
        """Custom import function that applies tariffs."""
        # for both builtins.__import__ and importlib.import
        # this first arg is 'name' which is used to determine
        # the tariff
        if "name" in kwargs:
            name = kwargs.pop("name")
        else:
            name, args = args[0], args[1:]

        # Check if the package is in our tariff sheet
        base_package = name.split(".")[0]
        tariff_rate = _tariff_sheet.get(base_package)

        # Measure import time
        start_time = time.time()
        module = import_func(name, *args, **kwargs)
        original_import_time = (
            time.time() - start_time
        ) * 1000000  # convert to microseconds

        # Apply tariff if applicable
        if tariff_rate is not None:
            # Calculate sleep time based on tariff rate
            sleep_time = original_import_time * (tariff_rate / 100)
            time.sleep(sleep_time / 1000000)  # convert back to seconds

            # Calculate new total time
            new_total_time = original_import_time + sleep_time

            # Print tariff announcement in Trump style
            print(
                f"JUST IMPOSED a {tariff_rate}% TARIFF on {base_package}! Original import took {int(original_import_time)} us, "
                f"now takes {int(new_total_time)} us. {_get_trump_phrase()}"
            )

        return module

    return tariffed
