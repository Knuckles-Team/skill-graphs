
            - 'skipped-choice': A choice field was skipped because it had no valid choices.
            - 'non-serializable-default': A default value was skipped because it was not JSON-serializable.
        detail: A string with additional details about the warning.

    Returns:
        The formatted warning message, or `None` if no warning should be emitted.
    """
    if kind in self.ignored_warning_kinds:
        return None
    return f'{detail} [{kind}]'

```

---|---
