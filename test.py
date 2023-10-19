# test_cron.py
import pytest
from cron_parser import expand_cron_expression

def test_valid_expression():
    expression = "0 2 * * * /usr/bin/job"
    expanded = expand_cron_expression(expression)
    assert len(expanded) == 6

def test_invalid_expression():
    expression = "0 2" 
    with pytest.raises(ValueError):
        expand_cron_expression(expression)

def test_february_day():
    expression = "0 2 31 2 * /usr/bin/job"
    with pytest.raises(ValueError):
        expand_cron_expression(expression)

def test_expanded_fields():
    expression = "0 2 28 2 * /usr/bin/job"
    expanded = expand_cron_expression(expression)
    assert expanded[2] == "28" # day of month
    assert expanded[3] == "2" # month

def test_command():
    expression = "0 2 * * * /usr/bin/job"
    expanded = expand_cron_expression(expression) 
    assert expanded[5] == "/usr/bin/job"