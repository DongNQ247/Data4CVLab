# Curriculum Architecture Freeze

This document freezes the architecture of the Data4CVLab curriculum. From this point, the priority is depth, reasoning, experimentation, and real-world diagnostic ability. Do not keep expanding the syllabus by adding more topics unless a new topic directly improves one of the core capabilities below.

Core training objective:

```text
Learn how to systematically diagnose and improve an Object Detection system
through data, models, measurement, and experimentation.
```

Object Detection is the primary case study. Data-Centric Computer Vision is the general competency. The principles transfer to classification, segmentation, OCR, tracking, pose estimation, industrial vision, and other visual ML systems.

## 1. Final Capability Map

The final capability progression remains:

```text
Recognition
-> Diagnosis
-> Root Cause Analysis
-> Intervention
-> Experimentation
-> Research
```

### Level 1: Recognition

The learner can recognize symptoms, risks, and system components.

Examples:

- "The dataset is imbalanced."
- "There are many small objects."
- "Train performance is much higher than test performance."
- "The model produces background false positives."
- "Some annotations are inconsistent."

Evidence of competence:

- uses correct terminology;
- identifies which evidence should be collected next;
- separates raw observation from interpretation.

### Level 2: Diagnosis

The learner can locate the likely bottleneck region.

Bottleneck regions:

- data;
- annotation;
- model;
- optimization;
- evaluation;
- deployment.

Examples:

- "Minority class recall is low, but only under night lighting."
- "AP50 is acceptable but AP75 is low, suggesting localization or annotation tightness issues."
- "The random split likely leaks adjacent video frames."

Evidence of competence:

- analyzes class-wise and condition-wise metrics;
- checks data/model/measurement together;
- avoids treating a metric drop as automatically a model problem.

### Level 3: Root Cause Analysis

The learner can formulate competing hypotheses and distinguish them.

Framework:

```text
Symptom
-> Evidence
-> Candidate Causes
-> Hypothesis
-> Experiment
-> Root Cause
-> Intervention
```

Example:

```text
Symptom: Small objects have poor recall.

Candidate causes:
- insufficient pixels;
- low input resolution;
- underrepresentation of small objects;
- inconsistent small-object annotation;
- harmful augmentation;
- detector architecture limitation;
- NMS suppression;
- confidence threshold too high.
```

Evidence of competence:

- does not confuse symptom with root cause;
- states what evidence would falsify each hypothesis;
- designs experiments that isolate causes.

### Level 4: Intervention

The learner can choose a targeted intervention based on evidence.

Intervention classes:

- collect targeted data;
- improve annotation policy;
- correct annotations;
- redesign split;
- adjust preprocessing;
- tune augmentation;
- tune thresholds/NMS;
- adjust optimization;
- change model only when evidence supports model bottleneck.

Evidence of competence:

- states preconditions;
- predicts side effects;
- estimates cost;
- chooses the smallest meaningful intervention.

### Level 5: Experimentation

The learner can design controlled experiments.

Required concepts:

- baseline;
- control;
- independent variable;
- dependent variable;
- confounding factor;
- ablation;
- repeated runs;
- uncertainty;
- reproducibility.

Evidence of competence:

- changes one major factor at a time when attribution matters;
- tracks dataset version, annotation version, split, model, config, seed, and evaluation protocol;
- interprets results with uncertainty, not just point estimates.

### Level 6: Research

The learner can generate new knowledge from a practical system.

Research does not require complex techniques. A project using a pretrained detector, careful dataset design, strong evaluation, and controlled experiments can be good research.

Evidence of competence:

- formulates research questions;
- defines hypotheses;
- compares against simple baselines;
- quantifies uncertainty;
- writes limitations;
- identifies the next question.

## 2. Final Depth Map

Depth levels:

- `[A] Awareness`: know the concept and terminology; no deep implementation required.
- `[B] Working Knowledge`: understand mechanism; can use in a project; can read and adjust implementation.
- `[C] Mastery`: can diagnose problems, choose techniques, design experiments, and explain trade-offs.
- `[D] Research`: can formulate questions, design investigations, and generate new insight.

### Core Foundations

| Area | Depth | Reason |
|---|---:|---|
| Image tensors, coordinates, resolution | C | Required for bbox, resizing, preprocessing, and small-object diagnosis. |
| Bounding boxes and coordinate formats | C | Required for annotation correctness, conversion, localization, and evaluation. |
| IoU | C | Required for matching, AP interpretation, localization diagnosis, and policy decisions. |
| Confidence threshold and NMS | C | Required for FP/FN tradeoffs and post-processing diagnosis. |
| Precision, recall, FP, FN | C | Required for production-oriented evaluation. |
| AP, mAP, AP50, AP75 | C | Required for measurement diagnosis, but must not be treated as sufficient alone. |

### Data and Annotation

| Area | Depth | Reason |
|---|---:|---|
| Problem definition | C | Determines ontology, metrics, split, and production relevance. |
| Ontology and class definition | C | Ground truth is a design decision, not a labeling detail. |
| Annotation policy | C | Required for consistency, QA, and interpreting model behavior. |
| Occlusion, truncation, crowd, ignore regions | C | Common sources of detection ambiguity and evaluation error. |
| Missing labels and label noise | C | Directly affect false positives, false negatives, and metric trust. |
| Inter-annotator agreement | B/C | Mastery for annotation-focused learners; working knowledge for general CV engineers. |
| Annotation platform operations | B | Need workflow competence, not mastery of every tool. |

### Dataset Science

| Area | Depth | Reason |
|---|---:|---|
| Sampling frame and sampling mechanism | C | Foundation for representativeness and bias diagnosis. |
| Representative, stratified, temporal, spatial, camera sampling | C | Required for real-world CV data collection. |
| Independence, correlation, effective sample size | C | Prevents confusing many frames with many independent samples. |
| Dataset quality framework | C | Required for systematic dataset diagnosis. |
| Dataset size vs diversity vs coverage vs representativeness | C | Required to avoid "large dataset equals good dataset" thinking. |
| Dataset versioning and lineage | C | Required for reproducibility and scientific reasoning. |
| Data governance, licensing, PII, retention | B | Required for production awareness; not a legal course. |

### Model Understanding

| Area | Depth | Reason |
|---|---:|---|
| Detector input and preprocessing | C | Required for resolution, normalization, and augmentation diagnosis. |
| Backbone and feature extraction | B/C | Diagnostic understanding required; implementation from scratch not required. |
| Feature pyramid / multi-scale features | B/C | Important for small-object and scale-related failures. |
| Detection head: classification and localization | B/C | Required for class vs localization failure reasoning. |
| Losses and optimization behavior | B | Need working diagnosis of optimization issues. |
| Post-processing: threshold and NMS | C | Directly affects production FP/FN behavior. |
| YOLO/DETR/Faster R-CNN family details | B | Know tradeoffs; do not memorize versions. |
| Implementing detectors from scratch | A | Not needed unless entering architecture research. |

### Measurement and Experimentation

| Area | Depth | Reason |
|---|---:|---|
| Split design and leakage | C | Required for trustworthy evaluation. |
| Class-wise and condition-wise evaluation | C | Required for diagnosis. |
| Production metric alignment | C | Required for applied system decisions. |
| Statistical uncertainty, bootstrap, confidence intervals | C | Required for Senior/Research-level claims. |
| Repeated experiments and seeds | C | Required to avoid overinterpreting noise. |
| Baseline, controls, ablation | C | Required for valid intervention claims. |
| Factorial experimental design | B/C | Mastery for research track; working knowledge for applied track. |
| Causal inference formalism | A/B | Useful context, not core unless research requires it. |

### Advanced Techniques

| Area | Depth | Reason |
|---|---:|---|
| Hard-negative mining | C | Common intervention for background FP patterns. |
| Active learning | C | Important when annotation budget and sample selection matter. |
| Uncertainty sampling | B/C | Mastery only when used in experiments. |
| Diversity sampling | B/C | Mastery when comparing to uncertainty/random sampling. |
| Semi-supervised learning | B | Useful but not core to every project. |
| Weak supervision | B | Useful under labeling constraints; not core initially. |
| Synthetic data | B | Needs strong "when not to use" judgment. |
| Domain adaptation | B | Important for production shift; deep algorithmic mastery optional. |
| Dataset distillation | A | Awareness unless research track specifically needs it. |
| Novel active learning algorithms | D | Research track only. |
| Novel detector architectures | D | Architecture research track only, not the main program. |

## 3. Data Quality Framework

Question:

```text
What makes a dataset good?
```

Answer: a good dataset is fit for a specific problem, measurement protocol, deployment distribution, and cost constraint. It is not simply large.

### Quality Dimensions

| Dimension | Meaning | Why it matters | How to measure | Model impact | Possible trap |
|---|---|---|---|---|---|
| Correctness | Labels and metadata are true under the policy. | Incorrect labels teach wrong associations. | Manual QA, disagreement review, label-noise detection. | Wrong class, localization errors, metric distortion. | "Correct" depends on policy; unclear policy makes correctness impossible to judge. |
| Completeness | Relevant objects/labels are present. | Missing labels turn true detections into apparent false positives. | Missing-label audit, prediction-assisted review. | FP inflation, poor recall learning signal. | A visually clean dataset can still have many missing labels. |
| Consistency | Similar cases are labeled similarly. | Inconsistent ground truth increases noise. | Inter-annotator agreement, edge-case review. | Unstable localization/classification behavior. | High agreement on easy cases can hide inconsistency on hard cases. |
| Coverage | Dataset includes required conditions/cases. | Missing conditions cause subgroup failures. | Condition matrix, coverage by site/time/camera/object size. | Poor performance on uncovered conditions. | Coverage count is not representativeness. |
| Diversity | Dataset contains varied independent situations. | Diversity improves robustness. | Metadata diversity, clustering, near-duplicate rate, effective sample size. | Better generalization if diversity is relevant. | Random visual variety may not cover target risks. |
| Representativeness | Dataset reflects target population/deployment. | Evaluation should predict production behavior. | Compare dataset distribution with deployment distribution. | Production gap if unrepresentative. | A balanced dataset may be less representative if production is imbalanced. |
| Balance | Classes/conditions have enough learning signal. | Extreme imbalance can lower minority recall. | Class/condition counts, instances per class, effective examples. | Minority FN, biased threshold behavior. | Balance is not always the goal; production priors matter. |
| Noise | Labels/images contain errors or irrelevant variation. | Noise weakens signal and can distort evaluation. | QA sampling, duplicate/noise audit, loss/error inspection. | Lower ceiling, unstable training. | Some real-world noise should remain if production contains it. |
| Redundancy | Samples repeat the same information. | High redundancy wastes annotation/compute. | Duplicate/near-duplicate detection, cluster counts. | Inflated dataset size, low effective diversity. | Some redundancy is useful for repeated production conditions. |
| Freshness | Data reflects current production distribution. | Old data may not match current cameras/sites/processes. | Time-based distribution comparison. | Drift and production degradation. | Fresh data can still be biased or low quality. |
| Reliability | Dataset can support reproducible decisions. | Decisions need traceable data, split and annotation versions. | Manifests, versioning, lineage checks. | Untrustworthy comparisons. | A reliable dataset can still be unrepresentative. |

### Required Distinctions

Dataset size:

- number of images or instances;
- easy to measure;
- often misleading.

Dataset diversity:

- variety of independent visual situations;
- depends on camera, scene, object, lighting, time and behavior;
- reduced by duplicate or consecutive-frame sampling.

Dataset coverage:

- whether important cases are included;
- tied to the problem and deployment risks;
- e.g. night, rain, occlusion, far camera, crowded scene.

Dataset representativeness:

- whether dataset distribution matches target population;
- not the same as balance;
- depends on deployment.

Rule:

```text
Large dataset != diverse dataset != representative dataset != good dataset.
```

## 4. Statistical View of Dataset

Learners must see a dataset as a sample from a target population.

```text
Real-world Population
-> Sampling Frame
-> Sampling Mechanism
-> Dataset
-> Train / Validation / Test
-> Model
-> Generalization
```

### Core Terms

Target population:

- the real distribution the system must work on;
- e.g. construction-site CCTV across sites, cameras, shifts, weather and months.

Sampling frame:

- the accessible subset from which data is collected;
- e.g. only three cameras from one site.

Sampling mechanism:

- how samples are selected;
- e.g. every frame, every 10 seconds, event-triggered frames, stratified by camera/time.

Selection bias:

- systematic exclusion or overrepresentation caused by collection process.

Sampling bias:

- dataset sample differs from target population in a way that affects conclusions.

Stratification:

- deliberately sampling across important groups;
- e.g. site, camera, day/night, distance, activity, object size.

Independence:

- whether one sample adds new information independent from another.

Temporal dependence:

- adjacent frames are highly correlated.

Spatial dependence:

- images from same site/camera share background and geometry.

Cluster sampling:

- samples collected in groups, such as video clips or site batches.

Effective sample size:

- approximate amount of independent information, often far smaller than raw image count.

Core principle:

```text
100,000 consecutive CCTV frames may contain far less effective diversity
than 5,000 frames sampled across sites, cameras, shifts and conditions.
```

### Statistical Competency

Learner must be able to ask:

- What is the target population?
- What is the sampling frame?
- How were samples selected?
- Are samples independent?
- Which correlations exist?
- Which strata matter?
- What does the dataset fail to cover?
- Does the test set estimate deployment performance?

## 5. Data Property to Model Behavior Framework

Learner must connect dataset properties to model behavior without jumping to root-cause conclusions.

Framework:

```text
DATA PROPERTY
-> MODEL BEHAVIOR
-> FAILURE MODE
-> PERFORMANCE IMPACT
-> HYPOTHESIS
-> INTERVENTION
-> EXPERIMENT
```

Examples:

| Data property | Model behavior | Failure mode | Performance impact | Hypothesis | Intervention | Experiment |
|---|---|---|---|---|---|---|
| Small-object underrepresentation | Weak features for small objects | FN on distant workers/helmets | APsmall and recall drop | Small-object coverage is insufficient | Targeted small-object collection or oversampling | Targeted vs random collection with same budget |
| Missing helmet labels | Correct detections counted as FP | Apparent background/wrong FP | Precision and mAP drop | Missing annotations inflate FP | Prediction-assisted annotation QA | Evaluate before/after label completion |
| Consecutive video frames | Scene memorization | High random-test score, low new-site score | Generalization gap | Split leaks temporal correlation | Group split by video/site | Random split vs video/site split |
| Inconsistent occlusion policy | Unstable positive/ignore labels | Confusing FN/FP near occlusion cases | Condition-wise instability | Policy ambiguity causes label noise | Rewrite policy and retrain annotators | Agreement and performance before/after policy |
| Background undercoverage | Overconfident false positives | Background FP | Precision drop | Hard negatives missing | Hard-negative mining | Targeted negatives vs random negatives |
| Domain undercoverage | Weak adaptation to new cameras/sites | Domain-shift FN/FP | Production recall/precision drop | Site/camera coverage insufficient | Stratified site/camera collection | Seen-site vs unseen-site evaluation |
| High redundancy | Overfitting to repeated scenes | Poor robustness | Test gap under deployment split | Effective diversity too low | Deduplicate and diversify | Same size redundant vs diverse subset |
| Annotation noise | Conflicting learning signal | Wrong class/localization | Lower AP and unstable training | Label noise dominates error | QA cleanup | Cleaned subset vs original subset |

Rule:

```text
The arrow from data property to model behavior is a hypothesis, not proof.
```

Every claim needs an experiment or strong evidence.

## 6. Negative Knowledge Framework

Senior-level judgment requires knowing when not to use a technique.

Template for every major technique:

```text
Technique
When to use
When NOT to use
Preconditions
Failure modes
Side effects
Cost
Alternatives
Validation experiment
```

### Required Negative Knowledge

Class imbalance:

- Do not automatically oversample.
- First check minority recall, sample quality, label quality, class difficulty and production priors.
- Oversampling can overfit duplicates and distort calibration.

Low recall:

- Do not automatically collect more data.
- First localize recall drop by class, size, condition, threshold and annotation completeness.
- Threshold tuning or label correction may be the first intervention.

Low mAP:

- Do not automatically change model.
- First inspect AP50/AP75, class-wise AP, condition-wise AP, split validity and annotation quality.

Train/test gap:

- Do not automatically call it overfitting.
- Check split leakage, distribution shift, preprocessing mismatch, annotation version mismatch and test-set reliability.

Small dataset:

- Do not automatically use synthetic data.
- Check whether the bottleneck is sample count, coverage, annotation quality, diversity or measurement uncertainty.

High uncertainty:

- Do not automatically use active learning.
- Check whether uncertainty correlates with useful missing distribution or only noisy/ambiguous cases.

Hard-negative mining:

- Use when background false positives are frequent and systematic.
- Do not use when FPs are caused by missing labels or unclear ontology.

Active learning:

- Use when annotation budget is constrained and model scores help identify informative samples.
- Do not use before a reliable baseline and evaluation loop exist.

Synthetic data:

- Use when rare conditions are hard to collect and simulation is realistic enough for the target signal.
- Do not use when domain gap cannot be measured on real validation data.

Domain adaptation:

- Use when source and target distributions differ and target labels are limited.
- Do not use as a substitute for understanding target distribution and evaluation.

Model architecture change:

- Use when evidence indicates current model capacity, scale handling or architecture assumptions are limiting.
- Do not use when failures are primarily caused by labels, split, thresholds or missing coverage.

## 7. Diagnostic Model Understanding Scope

The learner does not need Architecture Research Depth. The learner needs Diagnostic Model Understanding.

### Required Diagnostic Understanding

Detector pipeline:

```text
Input
-> Preprocessing
-> Backbone
-> Feature Extraction / Feature Pyramid
-> Detection Head
-> Classification Branch
-> Localization Branch
-> Post-processing
-> Evaluation
```

What the learner must understand:

- how input resolution affects small objects;
- how preprocessing can change bbox validity;
- how backbone features affect texture, shape and context sensitivity;
- why feature pyramids matter for scale;
- how classification errors differ from localization errors;
- how confidence thresholds affect precision/recall;
- how NMS can suppress crowded or nearby objects;
- how augmentation can help or harm real distribution coverage;
- when optimization, not data, may be the issue;
- when architecture is plausibly the bottleneck.

What the learner does not need:

- implement YOLO/DETR/Faster R-CNN from scratch;
- memorize every model version;
- derive every detector loss in full research detail;
- optimize CUDA kernels;
- design a novel architecture unless entering research track.

Diagnostic question:

```text
Which detector component could plausibly explain this failure,
and what evidence would support or reject that hypothesis?
```

## 8. Error Analysis vs Root Cause Analysis

Keep the distinction explicit.

Error Analysis answers:

```text
What failed?
```

Root Cause Analysis answers:

```text
Why did it fail?
```

Example:

```text
Observation: Small objects have poor recall.
```

This is not a root cause. It is an error analysis result.

Possible root-cause hypotheses:

- insufficient resolution;
- insufficient small-object data;
- annotation quality issues for tiny objects;
- class imbalance;
- sampling bias;
- augmentation removes small-object signal;
- detector architecture is weak for small objects;
- post-processing suppresses nearby objects;
- threshold is too high.

Required reasoning chain:

```text
Symptom
-> Evidence
-> Candidate Causes
-> Hypothesis
-> Experiment
-> Root Cause
-> Intervention
```

## 9. Research Methodology Spine

Research is methodology, not a collection of advanced techniques.

Research spine:

```text
Observation
-> Question
-> Hypothesis
-> Experiment
-> Result
-> Interpretation
-> Limitation
-> Next Question
```

A strong research project may use only:

- a pretrained detector;
- a carefully designed dataset;
- a valid split;
- strong evaluation;
- controlled experiments;
- clear statistical interpretation.

Advanced techniques are optional tools, not proof of research quality.

Good research questions for this curriculum:

- Does targeted collection outperform random collection under the same annotation budget?
- How does annotation disagreement affect AP50 vs AP75?
- Does effective diversity predict generalization better than raw dataset size?
- Does hard-negative mining improve precision more cost-effectively than collecting more general data?
- How much production performance loss is explained by camera/site shift?

Research quality criteria:

- clear question;
- falsifiable hypothesis;
- controlled comparison;
- credible baseline;
- uncertainty estimate;
- limitation statement;
- actionable insight.

## 10. Updated Longitudinal Project Structure

The longitudinal project remains:

```text
Helmet and Worker Detection in Construction-Site CCTV
```

Evolution:

```text
Problem
-> Dataset v0
-> Annotation Policy v1
-> Dataset v1
-> Baseline v1
-> Evaluation v1
-> Error Analysis v1
-> Root Cause Analysis v1
-> Intervention Plan
-> Dataset v2 and/or Model v2
-> Controlled Experiment
-> Dataset v3
-> Final Evaluation
-> Production Simulation
```

### Dataset Lineage Questions

For every dataset version, learner must answer:

- Why does this version exist?
- What evidence justified creating it?
- What changed?
- What stayed controlled?
- Which hypothesis does it test?
- How did performance change?
- How large is uncertainty?
- How confident are we that improvement came from the change?
- What new failure mode appeared?

### Required Dataset Versions

Dataset v0:

- messy seed data;
- used for problem discovery and annotation policy drafting.

Dataset v1:

- first curated dataset;
- has ontology, annotation policy, split policy and audit report.

Dataset v2:

- evidence-driven intervention dataset;
- created only after error/root-cause analysis.

Dataset v3:

- final validation or production-simulation dataset;
- used to test whether improvements generalize.

## 11. Dataset Quality to Model Performance Experiments

At least one experiment group must quantify how dataset properties affect model behavior.

Required experiment family:

```text
Changing X dataset property produced Y model behavior change,
under controlled conditions Z.
```

Candidate experiment groups:

| Dataset property X | Model behavior Y | Controlled condition Z |
|---|---|---|
| Dataset size | AP/recall variance and learning curve | Same sampling policy, same annotation quality |
| Effective diversity | New-site/new-camera generalization | Same raw image count |
| Class balance | Minority recall and calibration | Same total annotation budget |
| Annotation noise | AP50/AP75 and training stability | Same images, clean vs noisy labels |
| Small-object coverage | APsmall and small-object recall | Same model/config/split |
| Domain coverage | production holdout performance | Same model/config |
| Redundancy | generalization under deployment split | Same image count, redundant vs deduplicated |

Required report:

```text
Dataset Property
-> Manipulation
-> Control
-> Expected Model Behavior
-> Observed Model Behavior
-> Uncertainty
-> Interpretation
-> Limitation
```

## 12. Updated Assessment Rubric

Assessment prioritizes reasoning over code.

Weights:

| Criterion | Weight |
|---|---:|
| Problem formulation | 15% |
| Evidence quality | 15% |
| Diagnosis quality | 15% |
| Hypothesis quality | 15% |
| Experimental design | 15% |
| Interpretation and uncertainty | 10% |
| Decision quality and tradeoffs | 10% |
| Reproducibility and lineage | 5% |

Code is evaluated as supporting evidence, not as the main outcome.

A learner with polished code but weak reasoning should not score higher than a learner with adequate implementation and strong diagnosis, experiment design and interpretation.

### Capstone Rubric

Capstone must evaluate:

- ambiguous problem formulation;
- ontology and annotation policy decisions;
- sampling and split rationale;
- dataset quality diagnosis;
- metric-production alignment;
- error analysis;
- root-cause hypotheses;
- controlled intervention;
- statistical interpretation;
- cost-aware recommendation;
- production monitoring;
- reproducibility.

## 13. Topics That Must Reach Mastery

These are non-negotiable `[C] Mastery` topics:

- problem definition;
- data/model/measurement bottleneck framing;
- ontology and annotation policy;
- bbox formats and IoU;
- precision, recall, FP/FN;
- AP/mAP interpretation and limitations;
- split design and leakage;
- sampling frame and sampling mechanism;
- dataset quality dimensions;
- dataset size vs diversity vs coverage vs representativeness;
- effective sample size and correlated data;
- dataset audit and distribution analysis;
- class-wise and condition-wise evaluation;
- error analysis vs root-cause analysis;
- hypothesis formulation;
- controlled experiments;
- baseline/control/ablation;
- repeated runs and uncertainty;
- dataset versioning and lineage;
- intervention decision-making;
- root-cause report writing.

## 14. Topics That Need Awareness or Working Knowledge

Awareness `[A]` is enough for:

- implementing detectors from scratch;
- novel detector architecture design;
- dataset distillation;
- formal causal inference theory;
- low-level CUDA optimization;
- exhaustive benchmark leaderboard history;
- every annotation platform feature.

Working Knowledge `[B]` is enough for:

- detector architecture families;
- backbone and feature pyramid mechanics;
- training losses;
- semi-supervised learning;
- weak supervision;
- synthetic data;
- domain adaptation algorithms;
- experiment tracking tools;
- governance/legal vocabulary;
- model cards and datasheets;
- annotation platform workflows.

## 15. Research Track Topics

Research `[D]` topics are optional and should be entered only after core mastery.

Research track may include:

- novel active learning algorithms;
- new sampling strategies;
- label quality estimation methods;
- dataset valuation;
- dataset distillation;
- domain adaptation research;
- synthetic-to-real transfer investigation;
- causal analysis of dataset properties;
- new evaluation protocols;
- uncertainty-aware dataset selection.

Research track requirement:

```text
Technique complexity is not the criterion.
Methodological strength is the criterion.
```

## 16. Topics to Cut or De-Emphasize

Cut or strongly de-emphasize:

- memorizing every YOLO version;
- implementing YOLO/DETR/Faster R-CNN from scratch;
- deep CUDA/kernel optimization;
- collecting a catalog of advanced methods without a failure pattern;
- comparing frameworks as a main learning objective;
- leaderboard chasing;
- large synthetic data pipelines before real validation exists;
- using active learning before a reliable baseline/evaluation loop;
- using domain adaptation before defining source/target distributions;
- long theoretical treatment of legal/privacy issues beyond practical governance awareness.

Reason:

```text
Depth > Breadth
Reasoning > Memorization
Experimentation > Technique Collection
Diagnosis > Tool Usage
Engineering Judgment > Framework Knowledge
Research Methodology > Advanced Buzzwords
```

## 17. Transferability Beyond Object Detection

Object Detection remains the main learning vehicle because it exposes object-level labels, localization, ambiguity, false positives, false negatives, split leakage, scale issues and production monitoring clearly.

The transferable competency is broader:

- sampling applies to classification, segmentation, OCR, tracking and pose estimation;
- annotation policy applies to segmentation masks, OCR text regions, tracking IDs and pose keypoints;
- dataset audit applies to all visual ML datasets;
- leakage applies to video, identity, camera, location and preprocessing across tasks;
- error analysis applies to classification mistakes, mask errors, OCR failures, tracking switches and pose keypoint errors;
- root-cause analysis applies to any ML system with data/model/measurement interaction;
- controlled experiments apply to every applied ML workflow.

Do not expand the curriculum into separate full courses for each task. Use short transfer notes when relevant.

## 18. Freeze Rule for Future Curriculum Changes

Before adding a new topic, answer:

1. Which core capability does it improve?
2. Does it require Mastery, Working Knowledge or Awareness?
3. What decision will the learner make better because of it?
4. What experiment will it enable?
5. What topic should be removed or de-emphasized to preserve depth?

If these cannot be answered, do not add the topic.

## 19. Final Statement

After completing this program, the learner can independently do what a conventional Computer Vision engineer who only knows model architectures usually cannot:

```text
They can take an ambiguous real-world vision problem, define what should be
detected and measured, design the ground truth, collect and audit data,
identify whether the bottleneck is data, annotation, model, optimization,
evaluation or deployment, form competing root-cause hypotheses, design
controlled experiments to test them, interpret results under uncertainty,
choose cost-aware interventions, track dataset/model lineage, and produce a
defensible technical recommendation for production.
```

They are not merely able to train a detector. They are able to investigate and improve an Object Detection system as an evidence-driven engineering system.
