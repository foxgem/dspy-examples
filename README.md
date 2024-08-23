# DSPY Examples

## Prepare

```sh
poetry install
poetry shell
```

create the `.env` including your api keys

## Examples

### A Simple ChainOfThought

```sh
python mini.py
```

### "HTML Link" -> Summary

```sh
python html_summary/summary.py
```

### ToDO

1. pdf document -> summary
1. context, input -> output, eg, generate a new sentence based on the input sentence while considering the context
1. requirement -> code
