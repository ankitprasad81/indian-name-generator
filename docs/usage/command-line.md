# Command Line Interface

The package provides a command-line interface through the `generate-indian-name` command.

## Basic Usage

Generate a single full name:
```bash
generate-indian-name
```

## Options

### Generate Multiple Names

Use the `--count` option to generate multiple names:
```bash
generate-indian-name --count 5
```

### First Names Only

Generate only first names:
```bash
generate-indian-name --first-only --count 3
```

### Custom Separator

Use a custom separator between first and last names:
```bash
generate-indian-name --separator "-"
```

## Help

For a full list of options:
```bash
generate-indian-name --help
```
