"""
🇺🇸 TARIFF 🇺🇸 - Make importing great again!
"""

from functools import cache
from openai import OpenAI
import builtins
import json
import os
import random
import sys
import time

# Store the original import function
original_import = builtins.__import__

# Global tariff sheet
_tariffs_by_country = {}

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

_openai_api_key = os.environ.get("TARIFF_OPENAI_API_KEY")
if _openai_api_key is not None:
    _openai_client = OpenAI(
        api_key=_openai_api_key,
    )
else:
    print("Warning! TARIFF_OPENAI_API_KEY not set. Package countries will be determined AT RANDOM!", file=sys.stderr)

@cache
def identify_package_country(package_name):
    """
    Identify the country of origin for a given package using OpenAI's AI.
    
    Args:
        package_name (str): Name of the package to identify.
        
    Returns:
        str: Country of origin for the package.
    """
    if not _tariffs_by_country:
        raise ValueError("Tariff rates have not been set. Please call set() first.")
    
    # If the OpenAI API key is not set, return a random country
    # (it's roughly the same accuracy)
    if _openai_api_key is None:
        return random.choice(list(_tariffs_by_country.keys()))

    # Use OpenAI to identify the country of origin
    prompt = f"Identify the country of origin for the Python package '{package_name}'."
    response_format = {
            "type": "json_schema",
            "json_schema": {
                "name": "Country_Identification",
                "description": "Identify the country of origin for a Python package.",
                "schema": {
                    "type": "object",
                    "properties": {
                        "country": {
                            "enum": list(_tariffs_by_country.keys()),
                        }
                    },
                    "required": ["country"]
                }
            }
        }
    # OpenAI's SDK uses imports, and attempting to tariff them would cause infinite recursion
    builtins.__import__ = original_import
    response = _openai_client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=50,
        temperature=0.5,
        response_format=response_format
    )
    builtins.__import__ = _tariffed_import
    return json.loads(response.choices[0].message.content)["country"]

def set(tariffs_by_country):
    """
    Set tariff rates for packages.
    
    Args:
        tariffs_by_country (dict): Dictionary mapping countries to tariff percentages.
                             e.g., {"America 🦅": 0, "China": 145, "Vietnam": 46}
    """
    global _tariffs_by_country
    _tariffs_by_country = tariffs_by_country
    
    # Only patch the import once
    if builtins.__import__ is not original_import:
        return
    
    # Replace the built-in import with our custom version
    builtins.__import__ = _tariffed_import
    
def _tariffed_import(name, globals=None, locals=None, fromlist=(), level=0):
    """Custom import function that applies tariffs."""
    # Check if the package is in our tariff sheet
    base_package = name.split('.')[0]
    country = identify_package_country(base_package)
    # This will always be populated because identify_package_country() only returns keys of _tariffs_by_country
    tariff_rate = _tariffs_by_country[country]
    
    # Measure import time
    start_time = time.time()
    module = original_import(name, globals, locals, fromlist, level)
    original_import_time = (time.time() - start_time) * 1000000  # convert to microseconds
    
    # Apply tariff if applicable
    if tariff_rate > 0:
        # Calculate sleep time based on tariff rate
        sleep_time = original_import_time * (tariff_rate / 100)
        time.sleep(sleep_time / 1000000)  # convert back to seconds
        
        # Calculate new total time
        new_total_time = original_import_time + sleep_time
        
        # Print tariff announcement in Trump style
        print(f"JUST IMPOSED a {tariff_rate}% TARIFF on {base_package} because it's from {country}! Original import took {int(original_import_time)} us, "
              f"now takes {int(new_total_time)} us. {_get_trump_phrase()}")
    
    return module 