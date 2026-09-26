# 02 - Statistics and Machine-Learning Readiness

## Intuition: Learn the Rules Before Keeping Score

A sports team does not judge a strategy by one lucky play. It asks how performance is measured, whether opponents are comparable, and whether the result repeats. Statistics and machine learning use the same discipline: define quantities, quantify uncertainty, compare against a baseline, and evaluate on evidence not used to construct the answer.

This topic is a learning roadmap, not a claim that the current repository contains complete statistics or ML implementations. The roadmap notebook names statistics, NumPy/pandas, visualization, scikit-learn, and later projects as progression phases. The existing repository currently offers Python foundations and an introductory data-library workflow.

## Learning Objectives

- Identify foundational statistical concepts needed for data work.
- Distinguish descriptive analysis from supervised and unsupervised learning.
- Understand baseline, train/validation/test split, leakage, and metric selection.
- Recognize why preprocessing must be fit without evaluation-data leakage.
- Plan future practice projects without overstating current coverage.

## Statistics Foundations

Statistics provides tools for describing data and reasoning under uncertainty. A study sequence can include:

- counts, proportions, mean, median, mode, range, and quantiles;
- distributions, variability, outliers, and sampling;
- probability and conditional probability;
- sampling uncertainty and confidence intervals;
- correlation and regression intuition;
- chart reading, units, denominators, and limitations.

A single average may hide skew or subgroups. Use summaries that fit the data's shape and question. For example, a median can better represent a skewed duration distribution than a mean, while a proportion is more interpretable for a binary outcome when its denominator is explicit.

## From Question to Model

Machine learning uses data to fit a rule that can generalize to new cases. In supervised learning, examples include a target label/value; classification predicts categories, while regression predicts numeric values. Unsupervised learning looks for structure without a supplied target, such as clusters. The algorithm is only one part of the system: problem definition, data quality, evaluation, and operational consequences matter equally.

```text
question + domain context
        |
inspect schema / quality / missingness
        |
choose a simple baseline
        |
[supervised task] split data before learned preprocessing
        |
fit on training -> choose with validation -> evaluate once on held-out test
        |
inspect errors, subgroups, uncertainty, and operational cost
```

## Evaluation Without Leakage

For a supervised task, separate data into training, validation, and test partitions before fitting preprocessing steps such as imputers, encoders, or scalers. Fit each transformation on training data only; apply that already-fitted transformation to validation and test data. Otherwise information from evaluation data can leak into training and make results look better than they are. If observations are temporal, preserve chronology. If multiple rows come from the same person or entity, consider group-aware splitting so related records do not appear in both train and test.

Start with a simple baseline, such as the majority class or mean prediction, and compare more complex models using the same splits. Choose metrics that reflect consequences: accuracy can obscure rare positive cases; precision/recall trade-offs matter for alerts; MAE/RMSE express regression error in task-specific units. Inspect errors and performance across meaningful subgroups, not just one aggregate score.

| Stage | Main purpose | Keep separate from |
|---|---|---|
| Training | Fit model and preprocessing parameters | Validation/test outcomes |
| Validation | Choose settings and compare candidates | Final unbiased estimate |
| Test | Estimate final performance once decisions are set | Repeated model selection |

A test set is not a development playground. Repeatedly adjusting a model based on test results gradually leaks information from the test set into decisions.

## Repository Connection and Coverage Boundary

`python_libraries/02_dataset_libraries.ipynb` loads, exports, and reloads the Titanic sample. The `BOOKS/shd.ipynb` roadmap proposes later statistics, pandas/visualization, scikit-learn projects, and model metrics. It does not supply a complete model-training pipeline. Future lessons should build on the inspection workflow from Chapter 8 before fitting a model.

A first project plan might be: formulate a descriptive question, inspect missingness and feature meanings, define a target only if prediction is appropriate, create leakage-safe partitions, establish a baseline, compare a small number of models, evaluate suitable metrics, and communicate limits. Do not present an unrun or unvalidated model as a result.

## Industry Scenario

A support team wants to prioritize tickets likely to breach a response-time target. Define the prediction moment: only data available at that time may be used. Split by time or ticket/customer group as appropriate. Establish a simple baseline, compare false alarms with missed urgent tickets, and review errors by ticket category. A model with a slightly better average score may be unsuitable if it fails on a critical subgroup or adds too much delay.

## Common Pitfalls

- Training a model before defining the decision it will support.
- Fitting scaling or encoding on all rows before splitting.
- Using random splits for time-dependent data.
- Allowing the same person's or entity's records to leak across partitions.
- Reporting accuracy alone for an imbalanced task.
- Confusing correlation, prediction, and causation.
- Removing missing data without checking its frequency or context.
- Claiming ML coverage from repository materials that currently provide only a roadmap and starter data imports.

## Practice Challenges with Hints

1. For a classification problem, propose a naive baseline and one metric beyond accuracy. **Hint:** consider the class balance and relative costs of false positives and false negatives.
2. Explain how fitting a scaler before splitting leaks information. **Hint:** its mean and variance would incorporate evaluation rows.
3. Choose a split method for monthly historical data. **Hint:** train on earlier periods and validate/test on later periods.
4. Suggest a group split for repeated customer records. **Hint:** keep each customer wholly within one partition.
5. Draft a future ML project plan using the Titanic sample without claiming a model result. **Hint:** schema, missingness, target, split, baseline, metrics, and limitations.

## Summary

Statistics and ML depend on careful question design and evaluation. Establish context, inspect data, use baselines, prevent leakage, select consequential metrics, and analyze errors. The repository indicates these as future learning stages rather than completed model implementations.
