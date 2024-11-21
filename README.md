# Indian Name Generator

A Python package to generate Indian names.

## Installation

```bash
pip install indian-name-generator
```

## Usage

```python
from indian_name_generator import NameGenerator

# Create a name generator instance
generator = NameGenerator()

# Generate a random first name
first_name = generator.get_first_name()
print(f"First Name: {first_name}")

# Generate a random last name
last_name = generator.get_last_name()
print(f"Last Name: {last_name}")

# Generate a random full name
full_name = generator.get_full_name()
print(f"Full Name: {full_name}")
```

## Features

- Generate random Indian first names
- Generate random Indian last names
- Generate random full names (combination of first and last names)
- Based on a curated dataset of Indian names

## License

This project is licensed under the MIT License - see the LICENSE file for details.
