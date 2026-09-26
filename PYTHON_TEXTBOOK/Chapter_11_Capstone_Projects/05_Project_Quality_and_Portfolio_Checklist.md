# 05 - Project Quality and Portfolio Checklist

## Project Overview

A project is not complete when the code runs once on its author's machine. A professional handoff lets another person understand the problem, reproduce the environment, run representative tests, inspect results, and recognize limitations. This topic consolidates the repository roadmap's portfolio-quality rules and the engineering habits practiced throughout the course.

## Intuition: A Product Handoff

Think of a project as a kit handed to another team. The kit needs the tool, instructions, compatible parts, evidence that it works, and warning labels for known hazards. A repository with unexplained code and no setup steps is like a machine shipped without a manual: it may work, but it cannot be trusted or maintained easily.

## Learning Objectives

- Prepare a project repository for another person to run.
- Document problem, data, setup, behavior, tests, and limitations.
- Protect secrets and sensitive data.
- Make experiments reproducible and outputs interpretable.
- Assess whether a portfolio claim is supported by evidence.

## Definition of Done

| Area | Completion evidence |
|---|---|
| Problem | Clear user, need, and expected behavior |
| Code | Organized modules/functions and readable names |
| Setup | Interpreter/environment and dependencies documented |
| Data | Source, license, schema, and privacy constraints explained |
| Tests | Normal, boundary, invalid, and regression cases |
| Results | Outputs reproducible and interpreted in context |
| Safety | No credentials or sensitive data committed |
| Limits | Known failure modes and future work stated |

## Repository Structure Example

A small project might be organized like this:

```text
course-registry/
├── README.md
├── pyproject.toml or requirements.txt
├── src/
│   └── course_registry.py
├── tests/
│   └── test_course_registry.py
├── data/
│   └── README.md
└── reports/
    └── sample-output.md
```

This is a suggested layout, not a requirement for every short exercise. A notebook-only exploration may need fewer files, but should still record dependencies, data source, run order, and interpretation.

## README Content Checklist

1. **Title and purpose:** what the project does and for whom.
2. **Problem statement:** assumptions, inputs, and expected outputs.
3. **Setup:** supported Python version, environment creation, and dependencies.
4. **Run instructions:** exact command or notebook entry point.
5. **Example:** representative input/output or chart screenshot.
6. **Tests:** command and cases covered.
7. **Data:** source, license, handling, and exclusions.
8. **Limitations:** known failures, intended use, and future improvements.

Avoid claims such as “highly accurate” unless the project includes an appropriate evaluation design, metric, and comparison baseline.

## Deep Dive: Reproducibility, Privacy, and Provenance

A reproducible project records the code version, relevant package dependencies, input-data source, preprocessing choices, and steps needed to regenerate outputs. For an ML project, it also records data partitions, fitted preprocessing, random seeds when applicable, evaluation metrics, and error analysis. Reproducibility does not mean every environment behaves identically, but the decisions affecting results should be visible.

For any data project:

- confirm permission/license before distributing data;
- remove secrets, personal data, and private credentials;
- do not commit API keys or local configuration files;
- explain how missing, invalid, and duplicate records were handled;
- identify outputs that are synthetic, sampled, or manually edited;
- state the limitations of the data and method.

## Portfolio Review: Evidence Before Promotion

A strong project page demonstrates both outcome and reasoning. Include code that can be inspected, a README that can be followed, tests that can be rerun, and results that can be interpreted. A short video or screenshot can help communication but does not replace source, setup, or evaluation evidence.

For a data report, show the question, schema checks, denominator, chart, and interpretation. For a model, also show a baseline, split design, metrics, error analysis, and limitations. For an automation tool, show supported inputs, failure behavior, and how it avoids destructive surprises.

## Common Pitfalls

- Project runs only because of hidden notebook state or local files.
- Setup instructions omit the selected interpreter or required packages.
- Data is uploaded without license or privacy review.
- Tests cover only the happy path.
- Screenshots show output without the question or context.
- Results are described without units, denominator, or baseline.
- Secrets are committed and later removed only from the visible file, not repository history.
- Planned features are described as complete functionality.

## Final Review Checklist

- [ ] A new user can understand purpose in under a minute.
- [ ] Setup and run steps work from a clean environment.
- [ ] Tests include normal, boundary, invalid, and regression behavior.
- [ ] Dependencies are declared and necessary.
- [ ] Data rights, privacy, and provenance are documented.
- [ ] Outputs can be regenerated or are clearly labeled as static samples.
- [ ] Claims are supported by evidence and limits are visible.
- [ ] No credentials or private information are present.
- [ ] The repository has a clear license where appropriate.
- [ ] The next improvement is specific and technically useful.

## Practice Challenges with Hints

1. Audit one earlier capstone using the checklist. **Hint:** mark missing evidence rather than assuming it exists.
2. Write a README for the course registry. **Hint:** include duplicate policy, setup, sample calls, tests, and limitations.
3. Identify privacy risks in a contact registry. **Hint:** minimize fields and avoid publishing real contact records.
4. Make a chart reproducible. **Hint:** document data source, filters, denominator, dependencies, and code path.
5. Review a model claim. **Hint:** ask for baseline, held-out metrics, error slices, and limitations.

## Summary

A portfolio project is a reproducible handoff, not just a working demo. Document setup, inputs, data rights, tests, results, and known limits. Protect sensitive information and make every public claim traceable to evidence.
