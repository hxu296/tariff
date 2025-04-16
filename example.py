#!/usr/bin/env python3
"""
Example usage of the tariff package.
"""

import tariff

print("Setting tariffs on packages...")
tariff.set({
    "time": 50,        # 50% tariff
    "os": 100,         # 100% tariff
    "sys": 200         # 200% tariff
})

print("\nImporting packages with tariffs:")
import time
import os
import sys

print("\nImporting a package without tariffs:")
import json

print("\nSetting tariffs on packages the Trump way (at random)...")
tariff.set_the_trump_way(["time", "os", "sys"])

print("\nImporting packages with new tariffs:")
import time
import os
import sys

print("\nDemo completed! Make importing great again! 🇺🇸") 