# 02 - Loading and Inspecting Tabular Data

## Intuition: Receiving a Box of Unlabeled Records

Suppose a delivery arrives as a box of forms. Before making decisions from it, you check that each form has the expected fields, that values are understandable, and that pages are not missing. A dataset is similar: loading is only opening the box. Inspection determines what each row represents, what each column means, and whether the contents are suitable for the question.

Data inspection exists because software can successfully load data that is incomplete, malformed, or misinterpreted. A table-shaped object is not automatically a trustworthy dataset.

## Learning Objectives

- Load the repository's Seaborn Titanic sample into a DataFrame.
- Inspect dimensions, columns, types, sample rows, and missingness.
- Define a unit of observation and state an answerable question.
- Distinguish data-quality checks from transformations.
- Avoid unsupported conclusions from a preview or sample.

## Repository Example: Load the Titanic Sample

The source notebook `python_libraries/02_dataset_libraries.ipynb` contains the following load operation, preceded by its imports:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("titanic")
```

| Line or group | Explanation |
|---|---|
| imports | Bind the four libraries under common aliases. This particular load line uses Seaborn; the other imports are for subsequent data operations. |
| `df = sns.load_dataset("titanic")` | Requests the named sample dataset and stores the returned tabular data in `df`. Dataset availability can depend on the Seaborn version, cache, and network access. |

The variable `df` is a pandas DataFrame. It has labeled rows and columns; its column types may differ. The name `df` is a common abbreviation, but `titanic_df` can be clearer in a larger notebook.

## Inspect Before Transforming

The repository file demonstrates loading and Excel round-tripping. The following inspection commands extend that starter workflow:

```python
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.isna().sum())
```

| Line | What to learn |
|---|---|
| `df.head()` | Displays a small sample of leading rows; useful for orientation, not proof about all rows. |
| `df.shape` | Reports `(row_count, column_count)`, giving the table dimensions. |
| `df.columns` | Shows field names; compare them with the intended schema and question. |
| `df.dtypes` | Shows inferred column types; validate these against each field's meaning. |
| `df.isna().sum()` | Counts missing values by column. Inspect the amount and context before deciding whether to keep, drop, or impute. |

In a Jupyter notebook, an expression can display its value as output. In a script, use `print` or log the selected diagnostics. After each code cell, add a Markdown analysis that says what was observed and what remains uncertain; do not let the chart or table speak without interpretation.

## Deep Dive: Schema and Unit of Observation

A **schema** describes field names, types, units, allowed values, and relationships. The **unit of observation** is what each row represents: one passenger, transaction, event, or measurement. Misunderstanding either can invalidate summaries. For example, counting rows only means counting observations if each row corresponds to one distinct observation under the dataset's contract.

```text
question
   |
   v
unit of observation -> schema -> quality checks
                            |             |
                            +------> inspect sample and missingness
                                          |
                                          v
                               choose analysis plan
```

For every column used in an analysis, check its type, missing values, ranges, and category definitions. Investigate duplicates when uniqueness is expected. Do not automatically delete missing rows: missingness may carry information, and removing records can bias the population represented. Record a reason for each quality decision.

## Build a Descriptive Question

A cautious question about the sample might be: “How does the observed survival proportion vary by passenger class among rows with a recorded survival value?” This question states a comparison and hints at the denominator. It is descriptive: it does not ask whether class caused the outcome. Before calculating anything, verify the relevant field names, category values, and missingness in the actual loaded dataset.

## Industry Scenario

A service team receives a table of support tickets and wants to compare time-to-resolution by priority. Before summarizing, check that one row means one ticket, timestamps use compatible time zones, duplicate ticket IDs are understood, and unresolved tickets are not confused with missing data. Otherwise, an accurate calculation can answer the wrong question.

## Common Pitfalls

- Treating `head()` as a complete data-quality check.
- Treating inferred data types as guaranteed business meaning.
- Counting rows without confirming what one row represents.
- Ignoring missing values or dropping them without a reason.
- Assuming a sample dataset is representative of a current real-world population.
- Describing association as causation.
- Running analysis cells out of order and interpreting stale `df` data.

## Practice Challenges with Hints

1. State what one row appears to represent in the loaded sample. **Hint:** inspect field meanings and dataset documentation, not just one row.
2. Write down five inspection checks before a group comparison. **Hint:** include shape, types, missingness, allowed categories, and the denominator.
3. Design a descriptive question involving passenger class and one outcome. **Hint:** name the population subset and avoid causal language.
4. A column has missing values. List three context-dependent strategies. **Hint:** retain, impute, or exclude only with justification.
5. Write a Markdown paragraph following a code cell. **Hint:** report observation, evidence, and a limitation separately.

## Summary

Loading creates a DataFrame; inspection establishes whether it can support a question. Confirm schema, row meaning, types, missingness, and data quality before transforming. Interpret results with explicit denominators and avoid causal claims from descriptive patterns.
