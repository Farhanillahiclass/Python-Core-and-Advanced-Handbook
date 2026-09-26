# 01 - Question-Driven Analysis

## Intuition: Investigate Before You Conclude

Imagine investigating why deliveries arrive late. Before drawing a chart, you define what counts as a delivery, what “late” means, which time zone is used, and whether canceled orders belong in the comparison. Data analysis follows the same discipline: the dataset is evidence, but a precise question and an understanding of how the data were recorded determine what that evidence can support.

This process exists because computation can return a precise number for an imprecise or mistaken question. Analysis begins by defining the observation, population, fields, and decision—not by choosing a plot or model.

## Learning Objectives

- Turn a broad interest into an answerable descriptive question.
- Identify the unit of observation, population, and relevant schema.
- Inspect data quality, missingness, duplicates, ranges, and categories.
- Distinguish description, association, causation, and prediction.
- Communicate findings with denominators and limitations.

## Start with the Question and Unit of Observation

The **unit of observation** is what one row represents: one passenger, event, transaction, day, or measurement. Verify this from documentation and data construction; do not infer it from a few sample rows alone. The **population** is the group the analysis intends to describe. A sample can differ from a larger target population because of how it was collected.

A useful question specifies:

- what outcome or quantity is being described;
- which groups, period, or population are included;
- what is counted or averaged;
- the denominator or unit;
- whether the goal is description, explanation, or prediction.

“Which passenger class has more survivors?” is ambiguous: raw counts depend on group sizes. “What proportion of records with known survival status show survival in each class?” specifies a denominator more clearly, though it remains descriptive of the observed data.

## Repository Example: Inspect Before Asking

The author's `python_libraries/02_dataset_libraries.ipynb` loads Seaborn's Titanic sample. The first two lines are from that notebook; the inspection expressions extend its starter workflow:

```python
import seaborn as sns

df = sns.load_dataset("titanic")
print(df.shape)
print(df.dtypes)
print(df.isna().sum())
```

| Line | Purpose |
|---|---|
| `import seaborn as sns` | Loads the sample-data and visualization library under its conventional alias. |
| `df = sns.load_dataset(...)` | Requests the Titanic dataset and stores the returned table. Availability may depend on Seaborn version, network access, and cache. |
| `print(df.shape)` | Shows the number of rows and columns. This is an initial size check, not a completeness guarantee. |
| `print(df.dtypes)` | Shows inferred column types to compare with documented field meanings. |
| `print(df.isna().sum())` | Counts missing values per field. Counts must be interpreted in context before treatment. |

After this code, a notebook should contain a Markdown interpretation: what the displayed shape and missingness suggest, what questions remain, and what cannot yet be concluded. Do not invent counts or patterns without running the code in the intended environment.

## Data Quality Before Analysis

Check that field names, units, date conventions, category values, and identifiers agree with the data contract. Look for impossible values, duplicate records where uniqueness is expected, missing outcomes, and types that were inferred incorrectly. Decide whether to retain, correct, exclude, or impute questionable values based on domain meaning, and document the decision.

```text
question -> row meaning -> schema -> quality checks -> analysis plan
                                         |
                    missing / invalid / duplicate records
                                         |
                               documented decisions
```

Missingness is not automatically a reason to discard a row. It may be informative, concentrated in a subgroup, or caused by a collection process. Analyze its frequency and context first. Any filter changes the set of rows represented and may change the denominator.

## Description Is Not Causation

A descriptive comparison summarizes observed data. An association means two variables vary together in the observed sample. A causal claim asserts that changing one factor would change another under a defined intervention and assumptions. A group difference alone does not establish that one feature caused the outcome; confounding, selection, timing, and measurement can explain the association.

Prediction is a different goal: estimate an unknown outcome for new cases. A predictive model needs held-out evaluation and a metric aligned with the intended decision. A model can predict accurately without identifying causes.

| Goal | Typical question | What supports the answer? |
|---|---|---|
| Description | What proportion was observed? | Defined data subset and denominator |
| Association | How do two measured variables vary together? | Suitable summary plus limitations/confounders |
| Causation | What changes if an intervention is applied? | Design and assumptions that address alternative explanations |
| Prediction | How well can unseen outcomes be estimated? | Leakage-safe validation on data not used for fitting |

## Industry Scenario

A product team asks whether a new onboarding step reduces early cancellations. Clarify the cancellation window, eligible users, release dates, duplicate accounts, and whether users were assigned to the step randomly. If not, describe the observed association and possible confounding rather than claiming the step caused the difference.

## Common Pitfalls

- Starting with a chart instead of a question.
- Treating row count as the number of unique people or events without checking identifiers.
- Comparing raw counts when group denominators differ.
- Dropping missing rows automatically and hiding how the sample changed.
- Treating association as causation.
- Reporting an exact statistic without a unit, population, or denominator.
- Reusing a sample-data result as if it represented current real-world conditions.

## Practice Challenges with Hints

1. Write a descriptive question about Titanic survival by passenger class. **Hint:** define the denominator and how missing outcomes are handled.
2. State what a row represents in a dataset you know. **Hint:** inspect documentation and identifiers before deciding.
3. List five quality checks for a sales table. **Hint:** include types, missingness, duplicates, ranges, and units.
4. Rewrite “Does class determine survival?” as a descriptive question the sample can answer. **Hint:** describe observed proportions without causal language.
5. Draft a Markdown interpretation for the inspection code without inventing results. **Hint:** state what each diagnostic reveals and what still needs checking.

## Summary

A defensible analysis starts with a clear question and row meaning, then checks schema and quality before choosing a method. Keep denominators visible, document data decisions, and distinguish observed descriptions from causal or predictive claims.
