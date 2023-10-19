

# Cron Parser
A tool for parsing and expanding cron expressions.

### Usage
To use the cron parser:


```python
python cron_parser.py "0 2 * * * /usr/bin/script"
```

This will parse and expand the given cron expression.


To see the help text:
``` python
python cron_parser.py --help
```

# Test

Tests are located in the tests directory. To run tests:

Run Tests
```python
pytest test.py
```

### Requirements
- python 3.6+
- cron-parser module



#### The test cover the following:
- test_valid_expression - Checks that a valid cron expression parses correctly
- test_invalid_expression - Checks that an invalid expression raises a ValueError
- test_february_day - Checks for error on invalid February day numbers
- test_expanded_fields - Checks field values after parsing a valid expression
- test_command - Checks that the command is extracted properly

