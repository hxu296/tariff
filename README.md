# 👊 TARIFF 🔥

The GREATEST, most TREMENDOUS Python package that makes importing great again!

![MIGA](https://i.imgur.com/2OoRBu6.png)

## About

TARIFF is a fantastic tool that lets you impose import tariffs on Python packages. We're going to bring manufacturing BACK to your codebase by making foreign imports more EXPENSIVE!

![meme](https://github.com/user-attachments/assets/c0b37be1-28ca-40d3-9234-cbdb3074c8eb)

## Installation

```bash
pip install tariff
```

## Usage

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

## How It Works

When you import a package that has a tariff:

1. TARIFF measures how long the original import takes
2. TARIFF makes the import take longer based on your tariff percentage
3. TARIFF announces the tariff with a TREMENDOUS message

## Example Output

```
JUST IMPOSED a 50% TARIFF on numpy! Original import took 45000 us, now takes 67500 us. American packages are WINNING AGAIN! #MIGA
```

## Why TARIFF?

Because foreign packages have been STEALING our CPU cycles for TOO LONG! It's time to put AMERICA FIRST and make importing FAIR and BALANCED again!

# TARIFF.exports

TARIFF is now extended with `exports` functionality. You can now set tariffs on your exported functions.
You can even selectively set export tariffs for unfriendly packages who had unilaterally imposed a tariff on your package!

## Usage

```python
from tariff.exports import set_tariff


# Set a fixed tariff rate for everyone using your function.
@set_tariff(10)
def everyone_has_tariff(message: str):
    return message


# Set a variable tariff rate based who is using your function.
@set_tariff({
    "numpy": 50,     # 50% tariff if numpy is using the function
    "pandas": 200,   # 200% tariff if pandas is using the function
    "requests": 150  # 150% tariff if requests is using the function
})
def selective_tariff(message: str):
    return message


# Impose a tariff only when tariff is also applied on your package by the user.
@set_tariff(10, retaliatory_only=True)
def with_retaliatory_tariff(message: str):
    return message


# Impose a variable tariff based on user only if user imposes a tariff on your package.
@set_tariff({
    "numpy": 50,     # 50% tariff on numpy if numpy impose a tariff on your package
    "pandas": 200,   # 200% tariff on pandas if numpy impose a tariff on your package
    "requests": 150  # 150% tariff on requests if numpy impose a tariff on your package
}, retaliatory_only=True)
def selective_retaliatory_tariff(message: str):
    return message

```

## How It Works

When someone uses your TARIFFIED function:

1. TARIFF checks if your function is a normal export tariff or a retaliatory tariff
2. For normal export tariff, TARIFF penalizes the function for everyone or based on the earmarked users
3. For retaliatory tariff, TARIFF only penalizes the function if your package is penalized by the user
4. TARIFF announces the retaliatory tariff with a YYDS messages from Pooh bear and company.

## Example Output

```
[my_package] JUST IMPOSED a 100% TARIFF on `my_func` because `usa_number_one` imposed a TARIFF on `my_package`! Original response took 2.0 sec, now takes 4.0 sec. 保护主义没有出路，贸易战和关税战没有赢家。
```

## License

This is a parody package. Use at your own risk. MAKE IMPORTING GREAT AGAIN!
