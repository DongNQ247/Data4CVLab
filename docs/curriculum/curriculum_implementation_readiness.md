# Curriculum Implementation Readiness

This document addresses the curriculum review in `docs/reviews/curriculum/2026-08-13_004151_curriculum_review.md`.

Review response trace:

- `docs/reviews/curriculum/2026-08-13_004151_curriculum_review_response.md`

Purpose:

```text
Turn the curriculum architecture into an assessable training system.
```

The goal is not to add more topics. The goal is to define track boundaries, observable objectives, exit gates, artifact rubrics, experiment rules, and implementation prerequisites so lessons can be built without becoming shallow.

## 1. Track Boundaries

Every module belongs to one of these tracks:

- `Core`: required for every learner.
- `Production`: required for production-oriented learners; optional for pure research learners.
- `Research`: optional research-depth extension after core mastery.
- `Optional Decision Case`: taught only when a failure pattern justifies it.
- `Capstone`: integrated assessment.

Module track map:

| Module | Title | Track | Status |
|---:|---|---|---|
| 0 | Learning System, Tools and Reproducibility Basics | Core | Required |
| 1 | Problem Framing and Measurement Intent | Core | Required |
| 2 | Image, Object and Detection Foundations | Core | Required |
| 3 | Annotation Science and Ground-Truth Design | Core | Required |
| 4 | Data Collection Science | Core | Required |
| 5 | Dataset Schema, Versioning and Lineage | Core | Required |
| 6 | Data Leakage and Split Design | Core | Required |
| 7 | Dataset Audit and Distribution Diagnosis | Core | Required |
| 8 | Baselines, Metrics and Measurement Engineering | Core | Required |
| 9 | Statistical Thinking for Experiments | Core | Required |
| 10 | Experimental Methodology | Core | Required |
| 11 | Error Analysis and Failure Taxonomy | Core | Required |
| 12 | Root Cause Analysis Framework | Core | Required |
| 13 | Data-Centric Debugging of System Regressions | Core | Required |
| 14 | Intervention Design | Core | Required |
| 15 | Cost-Aware Dataset Engineering | Production | Required for production track |
| 16 | Human-in-the-Loop Systems | Production | Required for production track |
| 17 | Advanced Techniques as Decision Tools | Optional Decision Case | Not a core module |
| 18 | Production Distribution Shift and Monitoring | Production | Required for production track |
| 19 | Data Governance and Documentation | Production | Working knowledge required |
| 20 | Blind Dataset Challenge | Capstone | Required integrated assessment |
| 21 | Capstone System Diagnosis and Improvement | Capstone | Required final assessment |

Decision:

```text
Module 17 is no longer treated as one broad required module.
It becomes a library of optional decision cases selected by failure pattern.
```

## 2. Observable Objective Standard

All lessons must use observable objectives.

Do not write:

```text
Learner understands IoU.
```

Write:

```text
Given two boxes and an evaluation threshold, learner can compute IoU,
explain whether a prediction matches ground truth, and state when the chosen
threshold may or may not reflect production localization quality.
```

Required objective form:

```text
After this module, learner can <observable action>
given <input/evidence>
under <constraint/context>
and can explain <decision/tradeoff>.
```

## 3. Observable Module Objectives and Exit Criteria

### Module 0: Learning System, Tools and Reproducibility Basics

After this module, learner can:

- create and activate the `data4cv` environment;
- run notebooks, tests, and lint checks;
- explain why environment, data, split, config, and seed must be tracked;
- create a minimal experiment folder with a manifest.

Exit criteria:

- `conda run -n data4cv pytest` passes;
- learner produces an experiment README containing objective, command, data version, config, and result placeholder.

Common wrong answers:

- "The result is reproducible because the code is saved."
- "Notebook output is enough experiment tracking."

### Module 1: Problem Framing and Measurement Intent

After this module, learner can:

- convert an ambiguous request into objective, scope, constraints, actors, and operating conditions;
- define FP/FN costs for a deployment context;
- propose metrics and explain what each metric cannot prove.

Exit criteria:

- problem definition includes user action, deployment scenario, error costs, in-scope/out-of-scope cases, and metric intent.

Common wrong answers:

- "We optimize mAP because it is the standard detection metric."
- "All false positives and false negatives have the same cost."

### Module 2: Image, Object and Detection Foundations

After this module, learner can:

- inspect image tensor shape and coordinate system;
- identify bbox format mistakes;
- explain how resizing, cropping, or padding changes bbox validity;
- compute and interpret IoU;
- reason about confidence threshold and NMS effects.

Exit criteria:

- learner can debug at least five bbox examples containing coordinate, resizing, and threshold/NMS issues.

Common wrong answers:

- "A box that looks close by eye must be good enough."
- "NMS only removes duplicates and cannot create false negatives."

### Module 3: Annotation Science and Ground-Truth Design

After this module, learner can:

- write class definitions and inclusion/exclusion rules;
- define occlusion, truncation, crowd, ignore, reflection, poster, and mannequin cases;
- identify when disagreement indicates policy ambiguity;
- design a minimum viable annotation QA workflow.

Exit criteria:

- ontology v1 and annotation policy v1 cover at least 10 edge cases and define QA sampling.

Common wrong answers:

- "Annotators will know what a person/helmet means."
- "A disagreement is only an annotator mistake, not a policy signal."

### Module 4: Data Collection Science

After this module, learner can:

- define target population, sampling frame, and sampling mechanism;
- distinguish dataset size, diversity, coverage, representativeness, and effective sample size;
- design stratified collection across site, camera, time, lighting, weather, distance, and activity.

Exit criteria:

- data collection plan includes a sampling matrix and explains expected biases.

Common wrong answers:

- "100,000 frames means 100,000 useful samples."
- "More data is automatically better than more diverse data."

### Module 5: Dataset Schema, Versioning and Lineage

After this module, learner can:

- define dataset manifest fields;
- track dataset, annotation, preprocessing, split, model, and config versions;
- answer which exact data and config produced a model.

Exit criteria:

- Dataset v1 has a manifest, changelog, annotation version, split version, and source metadata.

Common wrong answers:

- "Dataset v2 is just the folder after I added images."
- "If code is versioned, data lineage is solved."

### Module 6: Data Leakage and Split Design

After this module, learner can:

- detect image, duplicate, near-duplicate, video, temporal, identity, camera, location, and preprocessing leakage risks;
- design split policy aligned with deployment;
- explain why random frame split may overestimate generalization.

Exit criteria:

- split policy specifies grouping variables and deployment-aligned test logic.

Common wrong answers:

- "Random split is fair because every image has equal chance."
- "Leakage only means exact duplicate files."

### Module 7: Dataset Audit and Distribution Diagnosis

After this module, learner can:

- compute class, instance, size, aspect ratio, spatial, metadata, quality, redundancy, and leakage summaries;
- connect dataset properties to possible model behaviors without claiming root cause too early;
- write a dataset diagnosis report.

Exit criteria:

- report includes evidence, risk interpretation, possible explanations, and recommended next checks.

Common wrong answers:

- "Class counts are the dataset audit."
- "Correlation between a property and failure proves root cause."

### Module 8: Baselines, Metrics and Measurement Engineering

After this module, learner can:

- run or fine-tune a credible baseline;
- evaluate class-wise and condition-wise;
- interpret precision, recall, AP, mAP, AP50, AP75, and operating points;
- state what each metric does not measure.

Exit criteria:

- evaluation report includes metric intent, split validity, threshold rationale, and failure slices.

Common wrong answers:

- "Higher mAP means better production system."
- "Threshold is a fixed model property, not an operating decision."

### Module 9: Statistical Thinking for Experiments

After this module, learner can:

- distinguish point estimate from uncertainty;
- decide when repeated seeds or bootstrap are needed;
- separate statistical significance from practical or production significance.

Exit criteria:

- learner interprets at least one metric comparison with uncertainty and states whether the effect is practically meaningful.

Common wrong answers:

- "85.1 is better than 84.2 because the number is higher."
- "One training run is enough to compare close interventions."

### Module 10: Experimental Methodology

After this module, learner can:

- write a controlled experiment plan before implementation;
- identify independent variable, dependent variables, controls, confounders, and decision rule;
- design ablations that support attribution.

Exit criteria:

- experiment plan follows the required manifest and states allowed/not-allowed conclusions.

Common wrong answers:

- "Before/after improvement proves the intervention worked."
- "Changing data and hyperparameters together is fine if mAP improves."

### Module 11: Error Analysis and Failure Taxonomy

After this module, learner can:

- classify false positives and false negatives into actionable categories;
- quantify failures by class, condition, size, confidence, and severity;
- separate "what failed" from "why it failed."

Exit criteria:

- failure report ranks top failure modes and includes visual evidence.

Common wrong answers:

- "Small-object recall is low, therefore we need more small-object data."
- "False positives are all background mistakes."

### Module 12: Root Cause Analysis Framework

After this module, learner can:

- convert symptoms into candidate causes and falsifiable hypotheses;
- design evidence-gathering steps to reject or support hypotheses;
- recommend an intervention only after stating competing explanations.

Exit criteria:

- root-cause report includes rejected explanations and expected results if the hypothesis is false.

Common wrong answers:

- "The most visible symptom is the root cause."
- "A plausible story is enough evidence."

### Module 13: Data-Centric Debugging of System Regressions

After this module, learner can:

- debug a regression across evaluation, dataset, annotation, distribution, split, preprocessing, training config, model, and seed;
- compare experiment manifests to isolate changed variables.

Exit criteria:

- regression report identifies at least three plausible causes, rules out at least one, and proposes a one-variable follow-up experiment.

Common wrong answers:

- "Model v2 is worse, so the architecture is worse."
- "Dataset changes cannot cause metric regression if there are more images."

### Module 14: Intervention Design

After this module, learner can:

- map failure patterns to intervention options;
- estimate impact, cost, side effects, and risk;
- choose the smallest intervention that tests a hypothesis.

Exit criteria:

- intervention proposal includes alternatives, preconditions, cost/risk, and validation experiment.

Common wrong answers:

- "Collect more data" without specifying target distribution.
- "Use a bigger model" without proving model bottleneck.

### Module 15: Cost-Aware Dataset Engineering

After this module, learner can:

- compare interventions by performance per annotation hour, dollar, and GPU hour;
- recommend a lower-cost option when performance difference is not meaningful.

Exit criteria:

- cost-performance report includes uncertainty and operational tradeoffs.

Common wrong answers:

- "The highest mAP option is always best."
- "Annotation cost is external to model quality."

### Module 16: Human-in-the-Loop Systems

After this module, learner can:

- design a review workflow for model predictions;
- define reviewer roles, disagreement handling, correction policy, and QA sampling;
- evaluate whether human review improves data quality.

Exit criteria:

- HITL plan includes queue selection, reviewer policy, QA loop, and dataset version update.

Common wrong answers:

- "Human review always improves labels."
- "Model uncertainty always identifies useful samples."

### Module 17: Advanced Techniques as Optional Decision Cases

After selected decision cases, learner can:

- justify whether a technique is appropriate for a specific failure pattern;
- compare the technique against a simpler baseline;
- state when not to use the technique.

Exit criteria:

- decision memo includes when to use, when not to use, preconditions, side effects, cost, alternatives, and validation experiment.

Common wrong answers:

- "Research requires advanced techniques."
- "Active learning/synthetic data/domain adaptation should be used because it is advanced."

### Module 18: Production Distribution Shift and Monitoring

After this module, learner can:

- define production distribution and compare it to train/validation/test;
- identify covariate, concept, camera, lighting, seasonal, geographic, and sensor shift risks;
- design monitoring and retraining triggers.

Exit criteria:

- production monitoring plan defines slices, drift indicators, feedback data, and retraining decision rules.

Common wrong answers:

- "A good offline test set means production is solved."
- "Drift only means mAP went down."

### Module 19: Data Governance and Documentation

After this module, learner can:

- document provenance, licensing, privacy, PII, consent, retention, access control, and dataset/model cards at working level;
- identify governance risks that affect data reuse and deployment.

Exit criteria:

- dataset card and governance checklist exist for the longitudinal project.

Common wrong answers:

- "Governance is non-technical."
- "Publicly accessible video is automatically safe to use."

### Module 20: Blind Dataset Challenge

After this module, learner can:

- diagnose an unknown dataset without being told the issue;
- identify hidden data, annotation, leakage, bias, or measurement problems;
- build Dataset v2 and justify why it exists.

Exit criteria:

- Dataset Autopsy Report includes diagnosis, evidence, hypotheses, interventions, controlled comparison, and limitations.

Common wrong answers:

- "The challenge is to train the best model."
- "Finding one issue is enough."

### Module 21: Capstone System Diagnosis and Improvement

After this module, learner can:

- independently diagnose, improve, validate, and communicate an ambiguous Object Detection system;
- justify every major decision from evidence;
- produce a defensible production or research recommendation.

Exit criteria:

- final case study satisfies the capstone rubric and includes complete dataset/model/measurement lineage.

Common wrong answers:

- "The capstone is complete when the model trains."
- "A metric improvement is enough without explaining attribution."

## 4. Lightweight Experiment Template for Early Modules

Use this template from Module 1 onward, before formal experiment methodology is taught.

```text
Question:
Hypothesis:
What changes:
What stays fixed:
Evidence collected:
Expected result if hypothesis is true:
Expected result if hypothesis is false:
Conclusion allowed:
Conclusion not allowed:
Limitations:
```

Purpose:

- prevent vague "experiments";
- introduce controlled reasoning early;
- make conclusions modest before statistical tools are taught.

## 5. Required Experiment Manifest

Every non-trivial experiment must include this manifest.

```yaml
experiment_id:
research_question:
hypothesis:

dataset_version:
annotation_version:
split_version:
preprocessing_version:
model_version:
training_config:
evaluation_config:

seed_or_seed_set:
independent_variable:
dependent_variables:
controlled_variables:
known_confounders:

decision_rule:
statistical_method:
practical_significance_rule:

result:
interpretation:
limitations:
next_action:
```

Minimum rules:

- Use repeated seeds when metric differences are small, training is unstable, dataset is small, or the intervention affects optimization.
- Use bootstrap or resampling when estimating uncertainty for evaluation slices or limited test sets.
- Report both statistical significance and practical/production significance.
- Dataset v1 vs Dataset v2 comparisons must state exactly what changed and what stayed fixed.

## 6. Dataset Availability and Metadata Plan

The longitudinal project needs an explicit material plan before lessons begin.

### Dataset Availability Options

Preferred order:

1. Public or permissively licensed construction safety / helmet dataset.
2. Small internally curated dataset with clear provenance.
3. Synthetic or mock dataset only for early concept labs, not final claims.

The curriculum should not depend on a large private dataset at the start.

### Minimum Dataset v0

Dataset v0 can be small and imperfect. It must contain enough examples to expose ambiguity:

- workers with helmets;
- workers without visible helmets;
- occlusion;
- truncation;
- small/distant workers;
- crowded scenes;
- background hard negatives;
- different cameras or sites if possible;
- day/night or lighting variation if possible.

### Required Metadata Schema

Every image should have a metadata record when available:

```yaml
image_id:
source_uri:
source_type: video|image|synthetic|unknown
site_id:
camera_id:
video_id:
frame_index:
timestamp:
time_of_day:
weather:
lighting:
activity_type:
scene_type:
height_or_viewpoint:
collection_method:
license_or_permission:
privacy_risk:
dataset_version:
split:
```

Minimum required fields for leakage-aware work:

- `image_id`;
- `site_id`;
- `camera_id`;
- `video_id`;
- `frame_index` or `timestamp`;
- `dataset_version`;
- `split`.

## 7. Minimal Gates Before Baseline

Do not train Baseline v1 until these gates are satisfied.

Required sequence:

```text
Problem Definition
-> Ontology v1
-> Annotation Policy v1
-> Data Collection Plan
-> Metadata Schema
-> Split Policy
-> Minimal Dataset Manifest
-> Minimal Dataset Audit
-> Baseline v1
```

Minimal dataset manifest must include:

- dataset version;
- image list;
- annotation file;
- annotation version;
- source metadata;
- split assignment;
- preprocessing notes;
- known limitations.

Minimal dataset audit must include:

- image count;
- instance count;
- class distribution;
- object-size distribution;
- at least one metadata distribution if available;
- duplicate/leakage risk note;
- annotation quality spot-check note.

## 8. Artifact Rubrics

Use four levels:

- `Weak`: output exists but does not support decision-making.
- `Acceptable`: covers core fields and identifies obvious risks.
- `Strong`: connects evidence to hypotheses and decisions.
- `Excellent`: includes falsifiable tests, alternatives, uncertainty, cost/risk, and limitations.

### Problem Definition Rubric

Weak:

- states only the task name, e.g. "detect helmets."

Acceptable:

- defines users, deployment setting, target objects, and basic FP/FN cost.

Strong:

- defines operating conditions, out-of-scope cases, metric intent, and action triggered by prediction.

Excellent:

- connects production objective to ontology, split, evaluation slices, and intervention priorities.

### Ontology and Annotation Policy Rubric

Weak:

- lists class names only.

Acceptable:

- defines classes and basic bbox policy.

Strong:

- covers ambiguity, occlusion, truncation, crowd, ignore regions, negative cases, and examples.

Excellent:

- includes disagreement handling, QA protocol, policy versioning, and expected impact on evaluation.

### Dataset Diagnosis Report Rubric

Weak:

- reports image counts and class counts.

Acceptable:

- identifies class, size, condition, quality, and leakage risks.

Strong:

- connects distribution evidence to specific failure hypotheses.

Excellent:

- proposes falsifiable tests and prioritizes interventions by cost, risk, and expected impact.

### Evaluation Report Rubric

Weak:

- reports a single mAP.

Acceptable:

- reports precision, recall, AP/mAP, class-wise and split information.

Strong:

- includes condition-wise metrics, threshold rationale, and production objective alignment.

Excellent:

- includes uncertainty, metric limitations, failure slices, and decision recommendation.

### Error Analysis Report Rubric

Weak:

- shows failed examples without taxonomy.

Acceptable:

- classifies FP/FN into basic failure categories.

Strong:

- quantifies failure modes by class, condition, size, confidence, and severity.

Excellent:

- separates error analysis from root-cause claims and proposes candidate hypotheses.

### Root-Cause Report Rubric

Weak:

- names a single cause without evidence.

Acceptable:

- lists candidate causes and supporting observations.

Strong:

- includes rejected explanations and evidence needed to distinguish hypotheses.

Excellent:

- defines isolating experiments, expected results if true/false, intervention options, and limitations.

### Experiment Report Rubric

Weak:

- reports before/after metrics.

Acceptable:

- includes manifest, baseline, intervention, and result.

Strong:

- controls confounders, states decision rule, and explains attribution.

Excellent:

- includes uncertainty, practical significance, alternative explanations, and next action.

### Capstone Rubric

Weak:

- trains a detector and reports metrics.

Acceptable:

- includes problem definition, dataset audit, baseline, evaluation, and error analysis.

Strong:

- includes root-cause reasoning, controlled intervention, lineage, and production-aware recommendation.

Excellent:

- independently handles ambiguity, conflicting evidence, cost/risk tradeoffs, uncertainty, governance, and defensible final recommendation.

## 9. Required Report Reasoning Sections

Every major report must include:

```text
Observation
Evidence
Possible explanations
Rejected explanations
Current best hypothesis
Intervention
Experiment design
Expected result if hypothesis is true
Expected result if hypothesis is false
Limitations
Recommendation
```

This prevents learner answers from staying vague.

## 10. Prerequisite Blocks to Add Before Lessons

These are short prerequisite blocks, not new full modules.

Basic probability/statistics:

- randomness;
- sample;
- variance;
- confidence interval intuition;
- why one run is not always enough.

Basic detector training loop:

- data loader;
- preprocessing;
- forward pass;
- loss;
- optimizer;
- validation;
- checkpoint;
- inference.

Basic annotation workflow:

- annotator;
- reviewer;
- disagreement;
- QA sample;
- policy update.

Basic metadata design:

- image id;
- source;
- site/camera/video/time;
- split;
- version;
- why metadata enables leakage and representativeness analysis.

Basic model prediction format:

- class;
- confidence;
- bbox;
- image id;
- thresholded vs raw predictions.

## 11. Advanced Technique Decision Cases

Module 17 is now a decision-case library. Use one case only when a failure pattern justifies it.

Required decision-case template:

```text
Failure pattern:
Candidate technique:
Why simpler approaches may fail:
Preconditions:
When to use:
When not to use:
Side effects:
Cost:
Alternative approaches:
Controlled experiment:
Decision rule:
```

Decision cases:

| Technique | Use only when |
|---|---|
| Hard-negative mining | Background FPs are systematic and not caused primarily by missing labels. |
| Active learning | Annotation budget is constrained and baseline uncertainty/diversity signals are meaningful. |
| Uncertainty sampling | Uncertainty correlates with useful missing coverage, not just ambiguity/noise. |
| Diversity sampling | Redundancy is high and coverage is the suspected bottleneck. |
| Weak supervision | Manual labels are expensive and weak signals can be validated against clean labels. |
| Semi-supervised learning | Unlabeled data matches target distribution and pseudo-label quality is measurable. |
| Synthetic data | Rare cases are hard to collect and synthetic-real gap can be tested on real validation data. |
| Domain adaptation | Source/target shift is measured and target labels are limited. |
| Dataset valuation | Research question requires estimating contribution of data subsets. |
| Dataset distillation | Research track only; not needed for core applied diagnosis. |

## 12. Evaluation-Set Governance

Test/evaluation data must be governed.

Rules:

- Test labels may be corrected only through a documented review process.
- Test-set changes require annotation version update and changelog.
- Do not tune thresholds repeatedly on the final test set.
- Validation set is for iteration; final test set is for final claims.
- Production holdout should be versioned separately when available.

Required record:

```yaml
evaluation_set_id:
dataset_version:
annotation_version:
split_version:
allowed_modifications:
review_owner:
change_log:
last_modified:
reason_for_change:
```

## 13. Model Training Failure Modes to Teach Operationally

Teach these as diagnostic possibilities, not as extra theory modules:

- bad preprocessing;
- bbox transform mismatch;
- augmentation mismatch;
- label format conversion error;
- optimization instability;
- underfitting;
- overfitting;
- train/validation leakage;
- wrong class mapping;
- threshold/NMS mismatch;
- checkpoint selection bias.

Each failure mode should be tied to:

```text
Symptom -> Evidence -> Check -> Fix -> Validation
```

## 14. Revised First Implementation Sequence

The first implementation sequence is now:

```text
1. Problem Definition
2. Ontology v1
3. Annotation Policy v1
4. Data Collection Plan
5. Metadata Schema
6. Split Policy
7. Minimal Dataset Manifest
8. Minimal Dataset Audit
9. Baseline v1
10. Evaluation v1
11. Error Analysis v1
12. Root-Cause Report v1
13. Intervention Plan
```

This fixes the prior gap where baseline work could begin before manifest, versioning, and minimal audit gates.

## 15. Implementation Freeze Rule

Lesson implementation must obey:

```text
Depth > Breadth
Reasoning > Memorization
Experimentation > Technique Collection
Diagnosis > Tool Usage
Engineering Judgment > Framework Knowledge
Research Methodology > Advanced Buzzwords
```

Before adding a lesson, ask:

1. What observable capability does it train?
2. What artifact proves the capability?
3. What common wrong answer will it correct?
4. What exit criterion tells us the learner is ready to continue?
5. Does this replace or deepen an existing lesson rather than add breadth?
