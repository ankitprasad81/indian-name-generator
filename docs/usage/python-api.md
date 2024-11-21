# Python API

The Indian Name Generator provides a simple and intuitive Python API through the `NameGenerator` class.

## Basic Usage

```python
from indian_name_generator import NameGenerator

# Create a generator instance
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

## Advanced Usage

### Generate Multiple Names

```python
# Generate multiple full names
names = generator.get_multiple_names(count=5)
print("Multiple Names:", names)
```

### Custom Separator

```python
# Generate a name with custom separator
name = generator.get_full_name(separator="-")
print(f"Name with custom separator: {name}")
```
