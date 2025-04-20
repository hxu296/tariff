#!/usr/bin/env python3
# /// script
# dependencies = [
#     "tariff",
# ]
# ///
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

print("\nDemo completed! Make importing great again! 🇺🇸") 