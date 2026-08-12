# Curriculum Review

## Review Metadata

- Review date/time: `2026-08-13 00:41:51 +07 +0700`
- Reviewer role: Curriculum & Lesson Reviewer for Data-Centric Computer Vision and Object Detection
- Review scope: `docs/curriculum`
- Primary file reviewed: `docs/curriculum/data_centric_object_detection_curriculum.md`
- Supporting file reviewed: `docs/curriculum/curriculum_architecture_freeze.md`
- Reviewer instruction file: `AGENTS_reviewer.md`
- Git commit at review time: `0a80291b107a2e02d71cf81efc7586be6cdb97a8`
- Working tree note: `AGENTS_reviewer.md` was untracked at review time; the curriculum files reviewed did not appear as modified in `git status --short -- docs/curriculum AGENTS_reviewer.md`.

## File Version Evidence

SHA-256 checksums at review time:

```text
92fadedcf2e0872df424eb378d6e4f9655af52b8113aa112ff7fa8218b0f25bb  docs/curriculum/data_centric_object_detection_curriculum.md
13757fb81504d18bd606f85cd73e416210323429f7e939ae33d0adf24460460f  docs/curriculum/curriculum_architecture_freeze.md
d17d55247ce31bd1ceed6dcc4f9318917bfe231b9f993bc24eb9f8f39f782bf5  AGENTS_reviewer.md
```

## 1. Overall Verdict

**Strong, but Needs Revision before lesson implementation.**

`docs/curriculum` has a strong curriculum philosophy and protects the right center: diagnosis, bottleneck finding, data/model/measurement interaction, controlled experiments, and applied reasoning. The architecture is much better than a model-centric CV syllabus.

The main weakness is that it is currently a high-quality curriculum blueprint, not yet a fully assessable curriculum. It says what the learner should do, but often does not define enough rubrics, exit criteria, artifact quality standards, prerequisite gates, or module-level mastery checks.

## 2. Target Capability

The curriculum is trying to train the learner from Recognition through Diagnosis, Root Cause Analysis, Intervention, Experimentation, and Research.

This target capability is appropriate for an Applied CV Engineer / Applied Research Engineer track. The strongest design decision is that Object Detection is treated as the learning vehicle, not as a narrow architecture survey.

## 3. Target Depth

Overall target depth: **[C] Mastery**, with selected **[D] Research** outcomes.

This is appropriate for the final goal, but the curriculum needs clearer separation between:

- Core Mastery topics: problem framing, annotation policy, split design, dataset audit, evaluation, error analysis, root-cause analysis, controlled experiments.
- Optional or research-track topics: dataset distillation, dataset valuation, weak supervision, semi-supervised learning, synthetic data, domain adaptation, and novel active learning methods.

## 4. What Works

The core objective is clear and competency-oriented. The learner must determine what is wrong, why it is wrong, what should change, how to test that change, and whether the change worked.

The curriculum avoids the common shortcut that dataset is always more important than model. It explicitly frames the task as finding the bottleneck across data, annotation, model, optimization, evaluation, and deployment.

The capability progression is strong:

```text
Recognition -> Diagnosis -> Root Cause Analysis -> Intervention -> Experimentation -> Research
```

The longitudinal helmet/worker CCTV project is a good applied vehicle because it naturally exposes ontology ambiguity, leakage, object scale, FP/FN tradeoffs, domain shift, and cost-aware collection.

The statistical thinking module is correctly positioned as a guard against overinterpreting small metric deltas.

The blind dataset challenge and capstone are strong assessment ideas because they test whether the learner can discover hidden issues without being told where to look.

## 5. Critical Issues

### Issue 1: The curriculum is too broad for a frozen depth-first architecture

The curriculum says the architecture is frozen and that future changes should prioritize depth over breadth, but the detailed curriculum contains 22 modules, including advanced techniques, HITL, governance, production monitoring, blind challenge, and capstone.

This is not automatically wrong, but it creates a serious risk that each module becomes shallow. Module 17 is the clearest example: it includes hard-negative mining, active learning, uncertainty sampling, diversity sampling, weak supervision, semi-supervised learning, synthetic data, domain adaptation, dataset pruning, dataset valuation, dataset distillation, and label quality estimation.

Recommendation:

```text
Split modules into Core Track, Optional Production Track, and Optional Research Track.
```

Module 17 should become a set of optional decision cases, not a single core module.

### Issue 2: Many learning objectives are not observable enough

Several objectives still use verbs such as `understand`. This is weaker than the reviewer standard, which expects observable learner capability.

Example problem:

```text
understand image tensors, coordinates and resolution
```

Better:

```text
Given an image and a set of bounding boxes, learner can identify coordinate-format errors, explain how resizing changes bbox validity, and predict which small objects are at risk after preprocessing.
```

Recommendation:

Rewrite every module objective into `After this module, learner can...` form.

### Issue 3: Assessment framework is directionally good but too generic

The assessment framework lists good dimensions:

- identifies the correct bottleneck region;
- separates symptom from root cause;
- considers alternative hypotheses;
- designs controlled experiments;
- handles uncertainty;
- connects metric to production objective;
- accounts for cost and governance;
- communicates recommendation clearly.

But it does not define performance levels.

Recommendation:

For each major artifact, define weak / acceptable / strong / excellent criteria.

Example for a dataset diagnosis report:

```text
Weak: reports class counts and image counts.
Acceptable: identifies class, size, condition, and leakage risks.
Strong: connects distribution evidence to specific failure hypotheses.
Excellent: proposes falsifiable tests and prioritizes interventions by cost, risk, and expected impact.
```

### Issue 4: First implementation sequence skips necessary audit/versioning gates

The first implementation plan recommends:

```text
Module 1 -> Module 2 -> Module 3 -> Module 4 -> Module 6
```

This is mostly reasonable, but it skips minimal dataset manifest/versioning and minimal dataset audit before model work. Baseline and evaluation later depend on knowing dataset version, annotation version, split version, and basic distribution properties.

Recommendation:

Add lightweight gates before baseline:

```text
Problem Definition
-> Ontology v1
-> Annotation Policy v1
-> Data Collection Plan
-> Split Policy
-> Minimal Dataset Manifest
-> Minimal Dataset Audit
```

### Issue 5: Early modules use "Experiment" before experimental prerequisites are taught

Modules 1, 3, 4, 5, 6, 7, and 8 already include experiments, while formal statistical and experimental thinking appears in Modules 9 and 10.

This can work only if early experiments are explicitly guided and lightweight. Otherwise the curriculum asks learners to perform experimental reasoning before the framework is taught.

Recommendation:

Add an early mini-template:

```text
Question
Hypothesis
What changes
What stays fixed
What evidence is collected
What conclusion is allowed
What conclusion is not allowed
```

Use this template from Module 1 onward.

## 6. Technical Issues

No major technical correctness error was found in the reviewed curriculum. The technical framing is generally sound.

However, several areas require more precise operational definitions before implementation:

- `effective diversity`;
- `statistical significance` for detection metrics;
- `bootstrap` use for AP/recall;
- `calibration` and operating point selection;
- `annotation disagreement` measurement;
- `production distribution` vs `test distribution`;
- `dataset valuation`.

These are not necessarily wrong, but if lessons implement them loosely, they can become misleading.

## 7. Pedagogical Issues

The curriculum is strong at macro-structure but weaker at local progression control.

Main pedagogical risk:

```text
The learner sees many important concepts, but does not get enough repeated, graded practice to know whether they can actually diagnose.
```

Each module should include:

- prerequisites;
- observable objectives;
- a worked example;
- a guided practice task;
- an independent task;
- exit criteria;
- common wrong answers;
- reviewer rubric.

## 8. Reasoning Issues

The reasoning philosophy is excellent. The curriculum repeatedly asks the right questions:

- What does this dataset represent?
- Does mAP reflect the production objective?
- What evidence would change your mind?
- What exactly changed?

The weakness is not intent. The weakness is enforcement. The curriculum needs concrete mechanisms that prevent learner answers from staying vague.

Recommendation:

Every report should require these sections:

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
```

## 9. Experimental Issues

The experimental backbone is strong, especially around controls, confounders, repeated runs, uncertainty, and fixed annotation budgets.

Missing rigor:

- no required experiment metadata schema;
- no rule for when repeated seeds are required;
- no rule for when bootstrap is appropriate;
- no explicit difference between statistical significance and practical/production significance;
- no minimum standard for comparing Dataset v1 vs Dataset v2.

Recommendation:

Add a required experiment manifest:

```text
experiment_id
research_question
hypothesis
dataset_version
annotation_version
split_version
model_version
training_config
evaluation_config
seed_or_seed_set
independent_variable
dependent_variables
controlled_variables
known_confounders
decision_rule
result
interpretation
limitations
```

## 10. Missing Prerequisites

Potential prerequisite gaps:

- basic probability/statistics before confidence intervals and bootstrap;
- basic detector training loop before optimization diagnosis;
- basic annotation platform workflow before inter-annotator agreement labs;
- basic metadata design before sampling and representativeness analysis;
- basic model prediction format before error taxonomy and failure gallery work.

These do not need large new modules. They can be short prerequisite blocks.

## 11. Missing Concepts

Important missing or under-specified concepts:

- explicit dataset/material availability plan for the helmet/worker project;
- minimum viable annotation workflow;
- metadata schema for site/camera/time/weather/activity;
- evaluation-set governance: who is allowed to modify test labels, when, and how changes are versioned;
- model training failure modes: bad preprocessing, augmentation mismatch, optimization instability, underfitting, overfitting, and leakage;
- calibration and threshold selection under production cost constraints;
- review rubric examples with weak/strong learner answers.

## 12. Unnecessary Content

The following should move to optional or research track unless a concrete failure pattern requires them:

- dataset distillation;
- dataset valuation;
- broad weak supervision;
- broad semi-supervised learning;
- broad domain adaptation;
- synthetic data generators;
- novel active learning algorithms.

The curriculum correctly says not to become a technique collector, but Module 17 currently risks becoming exactly that.

## 13. Recommended Revision

Priority revisions:

1. Add `Core / Optional / Research / Production` labels to every module.
2. Rewrite all learning objectives into observable `learner can...` statements.
3. Add module exit criteria.
4. Add artifact rubrics for all major reports.
5. Split Module 17 into optional decision cases.
6. Add an early lightweight experiment template before Module 1 labs.
7. Add a required experiment manifest.
8. Add a dataset availability and metadata plan for the longitudinal project.
9. Add common wrong-answer patterns to each module.
10. Fix the first implementation plan to include minimal dataset manifest and minimal audit before baseline.

## 14. Assessment Quality

Current assessment quality: **Promising but incomplete.**

The blind dataset challenge and capstone are strong because they measure integrated diagnosis rather than framework usage. But the rubric is too high-level to reliably grade.

Assessment should require evidence that the learner can:

- identify the bottleneck region;
- avoid premature root-cause claims;
- compare alternative hypotheses;
- design an isolating experiment;
- interpret uncertainty;
- choose an intervention based on cost and risk;
- communicate limitations.

## 15. Final Score

- Technical correctness: **8.5/10**
- Conceptual depth: **7.5/10**
- Pedagogy: **7/10**
- Reasoning: **9/10**
- Experimental rigor: **7.5/10**
- Practical relevance: **8.5/10**
- Assessment alignment: **6.5/10**

Overall assessment: **7.6/10**

Final judgment:

```text
Strong architecture, correct philosophy, and good applied CV direction.
Not ready to implement as lessons until objectives, rubrics, exit gates,
and core/optional boundaries are tightened.
```
