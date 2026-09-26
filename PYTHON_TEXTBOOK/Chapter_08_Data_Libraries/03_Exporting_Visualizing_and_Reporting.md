# 03 - Exporting, Visualizing, and Reporting

## Intuition: A Lab Report, Not Just a Machine Readout

A lab instrument can produce numbers, but a useful report explains what was measured, how it was measured, and what the result does not establish. Data visualization works the same way: a chart is a communication tool, not a conclusion by itself. Exporting a dataset preserves a handoff artifact, while interpretation connects the artifact to a well-defined question.

These steps exist because analysis is rarely complete when code runs. Other people need outputs they can inspect, repeat, and understand without guessing at units, inclusion rules, or limitations.

## Learning Objectives

- Export a DataFrame to Excel and reload it.
- Understand the purpose of `index=False` and the current working directory.
- Create a chart with Seaborn/Matplotlib and label it clearly.
- Distinguish group counts from proportions.
- Write a defensible Markdown interpretation after code and visualization.

## Repository Example: Excel Round Trip

The notebook `python_libraries/02_dataset_libraries.ipynb` contains these operations after loading the Titanic sample:

```python
df.to_excel("./dataset/titanic.xlsx", index=False)
df_titanic = pd.read_excel("./dataset/titanic.xlsx")
```

| Line | Detailed explanation |
|---|---|
| `df.to_excel(...)` | Calls a DataFrame method that serializes the table into an Excel workbook at the relative path `./dataset/titanic.xlsx`. |
| `index=False` | Omits pandas' row index from the workbook. Use this when the index is not a meaningful data field; keep it when the index itself is part of the record identity. |
| `pd.read_excel(...)` | Reads the workbook back through pandas and returns another DataFrame, bound here to `df_titanic`. |

The relative path is resolved from the process's current working directory. The target folder must exist or be created first. Writing the same path can replace an existing workbook depending on the writer behavior; verify the destination before running. Excel is a serialization format with its own type and precision behavior, so a round trip should be checked rather than assumed lossless.

## Visualization: Counts Versus Rates

A count plot can show observed records in categories:

```python
ax = sns.countplot(data=df, x="class", hue="survived")
ax.set(title="Observed passenger counts by class and outcome",
       xlabel="Passenger class", ylabel="Number of records")
plt.tight_layout()
plt.show()
```

This code creates a grouped count plot. The x-axis is the class category, the hue distinguishes outcome groups, and the y-axis is the number of rows counted. The title and labels make the chart readable outside the notebook.

### Interpret the Output in Markdown

After the cell, write a Markdown paragraph that:

- states which categories and records were included;
- describes only visible, supported patterns;
- says whether the chart displays counts or a normalized proportion;
- notes missing-value handling and sample limitations;
- avoids explaining the pattern as causal without a suitable study design.

Do not assert a specific pattern unless you have run the code and inspected the actual output. A count plot can differ between groups simply because the group sizes differ.

To examine proportions, calculate group means of a binary outcome after inspecting missingness and category definitions:

```python
survival_rate = df.groupby("class", observed=False)["survived"].mean()
print(survival_rate)
```

Because a Boolean or 0/1 outcome's mean is the proportion of observed ones, this estimates the observed survival proportion within each class among non-missing `survived` entries. The denominator must be stated. This is still descriptive of the loaded sample, not evidence that passenger class caused an outcome.

## Deep Dive: Reproducible Figure and Data Contracts

A chart depends on more than its plotting call: input data, row filters, aggregation, category ordering, units, and library versions all affect its meaning. Keep transformations explicit, label axes with units, and make random or version-sensitive choices reproducible when applicable.

```text
question -> define included rows/denominator -> compute summary
                                                 |
                                                 v
                                           visualize
                                                 |
                                                 v
                              Markdown: finding + evidence + limitation
                                                 |
                                                 v
                                        export/share artifact
```

When exporting, record the source and transformation steps. A saved spreadsheet is not a substitute for documenting how it was created. For a chart embedded in a report, include a caption or surrounding explanation so readers do not have to reverse-engineer notebook state.

## Industry Scenario

A service manager requests a monthly report of ticket resolution. Before charting, define whether unresolved tickets are included, how duration is calculated, and whether month is based on creation or closure date. Export the cleaned summary, not necessarily sensitive row-level data. Include the code or query version and a short interpretation with limitations.

## Common Pitfalls

- Exporting the DataFrame index as an accidental extra column.
- Writing to a path relative to an unexpected working directory.
- Overwriting an existing workbook without checking.
- Treating counts as rates or comparing groups with different denominators.
- Omitting missing values without documenting their effect.
- Using unlabeled axes, ambiguous colors, or a title that overstates the result.
- Reporting a descriptive association as cause.
- Creating a plot but no Markdown explanation of what it shows.

## Practice Challenges with Hints

1. Export a cleaned DataFrame and reload it. Compare shape and selected column types. **Hint:** a successful read does not guarantee exact schema preservation.
2. Add a count plot with a clear title and units. **Hint:** make the y-axis describe row counts.
3. Convert counts to proportions and state the denominator. **Hint:** group by category and compute the mean of a binary variable only after checking missingness.
4. Write three sentences after a chart: observation, evidence, and limitation. **Hint:** avoid causal verbs unless the design supports causal inference.
5. Change the output path to a project-relative location. **Hint:** check the current working directory and ensure the folder exists.

## Summary

Exporting and visualizing are parts of a reproducible reporting workflow. `index=False` prevents an unintended index column when appropriate; relative paths depend on the process working directory. Counts and proportions answer different questions. Every analysis chart needs a clear denominator, labels, and a written interpretation with limitations.
