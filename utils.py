"""
This module contains reusable functions which are used in various places around the application.
"""


def parse_form_errors(form_errors):
    errors = []

    for field, errorMessages in form_errors:
        for error in errorMessages:
            errors.append([field, error])

    return errors
