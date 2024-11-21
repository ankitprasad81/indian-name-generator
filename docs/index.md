# Indian Name Generator

A Python package to generate Indian names using a synthetically generated dataset created with state-of-the-art language models.

## Features

- Generate random Indian first names
- Generate random Indian last names
- Generate random full names
- Generate multiple names at once
- Command-line interface for easy access
- Based on a synthetically generated dataset

## Quick Start

```bash
# Install the package
pip install indian-name-generator

# Generate a name using Python
from indian_name_generator import NameGenerator
generator = NameGenerator()
print(generator.get_full_name())

# Or use the command line
generate-indian-name
```

## Dataset

The name dataset is synthetically generated using:
- Llama-3.2-11B-Vision-Instruct model (Hugging Face)
- OpenAI ChatGPT-4 (v2.0)

This ensures:
- Diverse name combinations
- Culturally appropriate naming patterns
