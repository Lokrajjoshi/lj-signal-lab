# Reproducible Student Workflow

This guide records the small habits I use while building and checking LJ Signal Lab during my MCA work.

## Before changing a rule

1. Write down the input shape and the expected result.
2. Add a small fixture under `data/` or `tests/fixtures/`.
3. Decide whether the case is valid, invalid, or only a warning.
4. Add a test that explains the decision in plain language.

## A useful validation loop

```text
sample input
    -> parse
    -> validate required fields
    -> validate values and status
    -> record a readable signal
    -> test the result
```

For API checks, keep a small response sample beside the test. This makes failures easier to understand without depending on a live service.

## Running the checks locally

```bash
python -m pytest -q
```

If the project adds another check later, document the command here and keep the CI command aligned with the local command.

## What to include in a project report

- the question or workflow being checked;
- the sample data and its source;
- the rule that was applied;
- the expected and observed result;
- known limitations;
- the next improvement to try.

The goal is not to make a small student project look bigger than it is. The goal is to make the reasoning, evidence, and limits easy for another person to follow.
