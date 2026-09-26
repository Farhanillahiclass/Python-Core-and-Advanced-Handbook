# 04 - Dataset-to-Chart Report

## Project Overview

This capstone extends the repository's Titanic sample workflow: load a dataset with Seaborn, inspect its structure, export it to Excel, and read it back. The project produces a reproducible descriptive report, not a predictive model or causal conclusion.

## Intuition: A Lab Notebook with a Decision Trail

A good data report is like a lab notebook: it records the question, materials, procedure, observations, and limitations. A chart without that trail is just an image; a spreadsheet without provenance is just a file. This capstone turns the notebook's starter operations into a documented analysis someone else can inspect.

## Learning Objectives

- State a descriptive question and its unit of observation.
- Inspect the Titanic sample's dimensions, types, and missingness.
- Calculate counts and proportions with explicit denominators.
- Create a labeled chart and interpret it in a following Markdown explanation.
- Export outputs while documenting limitations and file behavior.

## Project Question

Use this cautious descriptive question:

> Among rows with a recorded survival outcome in the loaded sample, how does the observed survival proportion vary by passenger class?

This describes the sample. It does not claim that passenger class caused survival differences. Before interpreting, confirm the actual column names, category levels, missing values, and how the dataset defines each field.

## Complete Workflow

The load and Excel round-trip lines are from the repository's `python_libraries/02_dataset_libraries.ipynb`. The inspection and summary/plot lines extend the starter workflow.

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
print(df.shape)
print(df.dtypes)
print(df["survived"].isna().sum())

analysis = df.loc[df["survived"].notna(), ["class", "survived"]].copy()
summary = analysis.groupby("class", observed=False)["survived"].agg(["count", "mean"])
print(summary)

ax = summary["mean"].plot(kind="bar", color="steelblue")
ax.set(title="Observed survival proportion by passenger class",
       xlabel="Passenger class", ylabel="Proportion among known outcomes")
ax.set_ylim(0, 1)
plt.tight_layout()
plt.show()

df.to_excel("./dataset/titanic.xlsx", index=False)
df_titanic = pd.read_excel("./dataset/titanic.xlsx")
print(df_titanic.shape)
```

## Line-by-Line Walkthrough

| Line or group | Explanation |
|---|---|
| imports | Load pandas, Seaborn, and Matplotlib components for the table, sample source, and chart. |
| `df = sns.load_dataset(...)` | Loads the sample into a DataFrame. It may require compatible package/data access. |
| `df.shape` | Reports row and column counts for the loaded table. |
| `df.dtypes` | Displays inferred column types for schema review. |
| missing-count expression | Counts rows where the outcome is missing. It does not yet explain why values are absent. |
| row/column selection and `.copy()` | Builds an analysis table containing only the outcome and group fields and rows with a known outcome. The filter defines the analysis denominator. |
| `groupby(...)["survived"].agg(...)` | Groups by passenger class, calculates non-missing outcome count and mean within each group. With a binary 0/1 outcome, mean is the observed proportion of ones. |
| `print(summary)` | Displays the numeric summary used to check the chart and denominator. |
| `.plot(kind="bar")` | Plots each class's mean as a bar. This is a descriptive summary, not a model. |
| `ax.set(...)` | Adds an informative title and labels, including that the y-axis is a proportion among known outcomes. |
| `ax.set_ylim(0, 1)` | Fixes the scale to the valid range for a proportion, making visual comparisons interpretable. |
| `plt.tight_layout()` | Adjusts spacing to reduce label clipping. |
| `plt.show()` | Displays the figure in an interactive session. |
| `df.to_excel(..., index=False)` | Exports the original table without its pandas row index as an extra field. The parent directory must already exist. |
| `pd.read_excel(...)` | Reloads the workbook into a DataFrame for a basic round-trip check. |
| final shape print | Compares table dimensions; this alone does not prove every value/type survived unchanged. |

## Markdown Interpretation After the Code

After running the workflow, write a Markdown section that reports the observed counts and proportions from the actual output, says which rows were excluded and why, and describes the visible chart pattern. Include a limitation: this is a historical sample with a particular data-collection process, and a descriptive difference does not establish causation. Do not fill in numeric findings before running and reviewing the code in the intended environment.

## Deep Dive: Denominators and Export Contracts

A group proportion is meaningful only with its denominator. Here, missing `survived` values are excluded from each group's mean; the `count` column gives the number of known outcomes used. If missingness differs across groups, comparisons may be affected. The report should disclose that choice and investigate missingness further before stronger claims.

Exporting also has a contract: decide whether to store raw or cleaned data, whether index values are meaningful, where the file is written, and how overwrites are handled. A reload check can verify dimensions and selected values or types; never assume an Excel round trip perfectly preserves every pandas type.

## Report Deliverables

- Notebook or script with ordered, reproducible analysis steps.
- Markdown question, inclusion rules, and data-quality observations.
- Table of counts and proportions.
- Labeled chart with readable categories and scale.
- Excel export or other approved artifact.
- Short interpretation, denominator, and limitation statement.

## Common Pitfalls

- Reporting raw survival counts as if they were survival rates.
- Ignoring missing outcomes or changing the denominator without disclosure.
- Reading a chart as causal evidence.
- Exporting the row index unintentionally or writing to the wrong directory.
- Overwriting an existing workbook without checking.
- Presenting unexecuted example output as a finding.
- Assuming a successful Excel read proves exact type/value preservation.

## Practice Challenges with Hints

1. Add a missingness summary for the class field. **Hint:** inspect both grouping and outcome columns.
2. Report each category's count beside its proportion. **Hint:** the `summary` table already contains both.
3. Verify selected values before and after Excel export. **Hint:** compare a small set of named columns and rows.
4. Write a conclusion that describes, but does not explain causally, the observed pattern. **Hint:** use “in this sample” and state the denominator.
5. Propose one follow-up quality check before any predictive modeling. **Hint:** inspect schema, missing values, duplicate records, and potential leakage.

## Summary

A data report connects a question to inspected data, a transparent denominator, a visualization, and a written interpretation. The Titanic workflow is descriptive and should not be presented as a causal or predictive result. Export and reload checks need explicit validation beyond a matching shape.
