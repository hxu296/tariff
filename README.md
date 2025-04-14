# 👊 TARIFF 🔥

The GREATEST, most TREMENDOUS Python package that makes importing great again!

## About

TARIFF is a fantastic tool that lets you impose import tariffs on Python packages. We're going to bring manufacturing BACK to your codebase by making foreign imports more EXPENSIVE!

## Installation

```bash
pip install tariff
```

## Usage

Tariffs on module imports:
```python
import tariff

# Set your tariff rates (package_name: percentage)
tariff.set({
    "numpy": 50,     # 50% tariff on numpy
    "pandas": 200,   # 200% tariff on pandas
    "requests": 150  # 150% tariff on requests
})

# Now when you import these packages, they'll be TARIFFED!
import numpy   # This will be 50% slower
import pandas  # This will be 200% slower
```

Tariffs on functions that run in foreign modules:
```
# Set your tariff rates
tariff.set({
    "pandas.Series.mean": 300,  # 300% tariff on pandas.Series.mean
})
import pandas
df = pandas.DataFrame({"Name": ["Alice", "Bob", "Eve", ], "Age": [22, 35, 58], })
df['Age'].mean()  # This will be 300% slower
```

## How It Works

When you import a package that has a tariff:
1. TARIFF measures how long the original import takes
2. TARIFF makes the import take longer based on your tariff percentage
3. TARIFF announces the tariff with a TREMENDOUS message

## Example Output

```
JUST IMPOSED a 50% TARIFF on numpy! Original import took 45000 us, now takes 67500 us. American packages are WINNING AGAIN! #MIPA
```

## Why TARIFF?

Because foreign packages have been STEALING our CPU cycles for TOO LONG! It's time to put AMERICA FIRST and make importing FAIR and BALANCED again!

## License

This is a parody package. Use at your own risk. MAKE IMPORTING GREAT AGAIN! 