# Systematic Object Detection Diagnosis and Improvement Curriculum

Tài liệu này là bản thiết kế lại của chương trình đào tạo `Data4CVLab`. Mục tiêu không phải là "học Data-Centric Computer Vision" như một tập hợp thuật ngữ. Mục tiêu là đào tạo một năng lực engineering và applied research rõ ràng:

Curriculum architecture is frozen in `docs/curriculum/curriculum_architecture_freeze.md`. Implementation readiness, module exit gates, rubrics, and experiment manifests are defined in `docs/curriculum/curriculum_implementation_readiness.md`. Future changes should prioritize depth over breadth and must follow the freeze rule in those documents.

```text
Given an ambiguous Computer Vision problem, the learner can systematically
determine what is wrong, why it is wrong, what should be changed,
how to test that change, and whether the change actually worked.
```

Trong chương trình này, Object Detection được xem như một hệ thống gồm ba trục liên tục tương tác:

```text
DATA <-> MODEL <-> MEASUREMENT
```

Trọng tâm không phải là "dataset luôn quan trọng hơn model". Trọng tâm là:

```text
Find the bottleneck.
```

Một bottleneck có thể nằm ở data, annotation, model, optimization, evaluation hoặc deployment. Learner phải học cách điều tra toàn bộ hệ thống, không chỉ debug model.

## 1. Philosophy

Triết lý đào tạo:

```text
Problem -> Evidence -> Diagnosis -> Root Cause Hypothesis
-> Intervention -> Controlled Experiment -> Interpretation -> Iteration
```

Chương trình dùng data-centric thinking, nhưng không biến nó thành dogma. Dataset Engineering là một discipline quan trọng ngang với Model Engineering và Measurement Engineering. Một engineer tốt không bắt đầu bằng câu hỏi "làm sao cải thiện dataset?", mà bắt đầu bằng:

```text
Where is the bottleneck?
```

Các nguyên tắc vận hành:

- Không kết luận từ một metric tổng hợp duy nhất.
- Không thay model trước khi biết failure pattern.
- Không nói "thêm data" nếu chưa biết thêm data nào.
- Không coi annotation là việc thủ công đơn giản; annotation là ground-truth design.
- Không coi mAP là production objective nếu chưa chứng minh được alignment.
- Không so sánh experiment nếu data, split, config, seed hoặc evaluation không kiểm soát được.
- Không dùng advanced technique nếu không có failure pattern phù hợp.

Mỗi chủ đề quan trọng phải được dạy theo cấu trúc:

```text
Concept
Intuition
When useful
When not useful
Failure modes
Decision criteria
Experiment
Interpretation
```

## 2. Target Learner

Chương trình dành cho người học muốn trở thành:

- Applied Computer Vision Engineer;
- ML Engineer chuyên về Vision;
- Data-Centric AI Engineer;
- Dataset Engineer;
- ML Evaluation Engineer;
- Applied Research Engineer;
- Computer Vision Research Engineer;
- Production CV Engineer.

Giả định ban đầu:

- learner biết Python cơ bản;
- có thể đọc code notebook;
- có thể đọc biểu đồ đơn giản;
- chưa cần biết sâu về deep learning;
- chưa cần có kinh nghiệm production ML.

Chương trình tăng độ khó bằng cách tăng ambiguity, số lượng hypothesis, độ nhiễu của evidence, trade-off và yêu cầu tự thiết kế experiment.

## 3. Final Competencies

Sau chương trình, learner phải nhận được bài toán:

```text
Build an object detector for detecting workers and helmets
in construction-site CCTV footage.
```

Và tự mình thực hiện được:

```text
Problem Definition
-> Ontology
-> Annotation Policy
-> Data Collection
-> Dataset Audit
-> Dataset Analysis
-> Dataset Split
-> Baseline
-> Evaluation
-> Error Analysis
-> Root Cause Analysis
-> Hypothesis
-> Intervention
-> Controlled Experiment
-> Dataset/Model Iteration
-> Final Evaluation
-> Production Monitoring
```

Quan trọng hơn, learner phải giải thích được vì sao từng quyết định được đưa ra.

Final competencies được chia thành 8 nhóm:

1. Problem framing: biến yêu cầu mơ hồ thành objective, constraint và risk.
2. Ground-truth design: thiết kế ontology, class definition và annotation policy.
3. Data collection science: chọn sampling frame và chiến lược thu thập có mục tiêu.
4. Dataset diagnosis: audit schema, distribution, quality, leakage, bias và noise.
5. Model-system diagnosis: phân biệt lỗi do data, annotation, model, optimization, evaluation hoặc deployment.
6. Measurement design: chọn metric, split và protocol phản ánh production objective.
7. Experimental methodology: xây baseline, control, ablation, repeated runs và statistical interpretation.
8. Iteration and communication: viết root-cause report, intervention report, dataset version notes và final recommendation.

## 4. Capability Map

Curriculum được thiết kế theo progression năng lực, không chỉ theo topic.

### Level 1: Recognition

Learner nhận ra hiện tượng hoặc rủi ro.

Examples:

- "Dataset bị mất cân bằng."
- "Có nhiều object nhỏ."
- "Train score cao hơn test score."
- "Có nhiều false positives trên background."
- "Một vài annotation không nhất quán."

Expected behavior:

- mô tả được symptom;
- dùng đúng thuật ngữ;
- biết cần thu thập evidence gì tiếp theo.

### Level 2: Diagnosis

Learner xác định vấn đề nằm ở vùng nào trong hệ thống.

Examples:

- "Minority class có recall thấp."
- "AP75 thấp hơn AP50 nhiều, có thể localization không tốt."
- "Test set có frame gần giống train set, metric có nguy cơ leakage."
- "False positives tập trung ở vùng background có texture giống helmet."

Expected behavior:

- phân tích theo data/model/measurement;
- đọc metric theo class, condition và failure mode;
- phân biệt symptom với evidence.

### Level 3: Root Cause Analysis

Learner hình thành nhiều hypothesis và biết cách phân biệt chúng.

Example:

```text
Symptom: Model fails on small objects.

Possible causes:
- insufficient pixels;
- input resolution too low;
- annotation inconsistency for tiny objects;
- too few small-object samples;
- augmentation destroys small objects;
- architecture is weak for small objects;
- NMS suppresses close small objects;
- confidence threshold is too high.
```

Expected behavior:

- tách observation, correlation, hypothesis và root cause;
- không kết luận quá sớm;
- thiết kế test để loại trừ hypothesis.

### Level 4: Intervention

Learner đề xuất thay đổi có cơ sở.

Examples:

- collect targeted small-object samples;
- refine annotation policy for occlusion;
- redesign split by camera/site/video;
- tune image resolution;
- add hard negatives;
- change threshold;
- change model family only khi evidence chỉ ra model bottleneck.

Expected behavior:

- nêu intervention nhỏ nhất có khả năng tạo tác động;
- nêu cost, risk và failure mode của intervention;
- không can thiệp nhiều biến cùng lúc nếu mục tiêu là chứng minh nguyên nhân.

### Level 5: Experimentation

Learner thiết kế controlled experiment để kiểm chứng.

Examples:

- random negatives vs targeted hard negatives with same annotation budget;
- resolution 640 vs 960 while keeping dataset and config fixed;
- annotation policy v1 vs v2 with agreement measured before/after;
- repeated seeds for baseline variance;
- group split vs random split to test leakage effect.

Expected behavior:

- có baseline;
- có control;
- xác định independent/dependent variables;
- kiểm soát confounders;
- biết khi nào difference là noise;
- viết interpretation chứ không chỉ báo metric.

### Level 6: Research

Learner đặt câu hỏi mới và tạo knowledge mới.

Examples:

- "Does targeted data collection outperform random collection under the same annotation budget?"
- "How much annotation disagreement can a detector tolerate before AP drops meaningfully?"
- "Does diversity matter more than dataset size for CCTV helmet detection?"
- "Can failure-driven sampling reduce cost per AP improvement?"

Expected behavior:

- đặt research question rõ;
- xây hypothesis;
- thiết kế baseline và ablation;
- phân tích uncertainty;
- viết research-style report với limitations.

## 5. Knowledge Map

Knowledge map không phải là thứ tự học cứng nhắc. Nó là bản đồ kiến thức cần dùng để phát triển capability.

### DATA

- problem definition;
- data requirements;
- sampling frame;
- representative sampling;
- stratified sampling;
- temporal/spatial/camera/domain sampling;
- rare-event sampling;
- effective diversity;
- dataset schema;
- dataset versioning;
- data lineage;
- dataset governance.

### ANNOTATION

- ontology;
- class definition;
- annotation policy;
- bounding-box policy;
- ambiguity;
- occlusion;
- truncation;
- crowd;
- ignore regions;
- difficult cases;
- missing annotation;
- label noise;
- annotation consistency;
- inter-annotator agreement;
- annotation QA.

### MODEL

- detector prediction structure;
- pretrained detectors;
- transfer learning;
- fine-tuning;
- optimization;
- augmentation;
- image resolution;
- confidence threshold;
- NMS;
- architecture tradeoffs;
- model capacity and bottleneck analysis.

### MEASUREMENT

- train/validation/test purpose;
- split design;
- precision and recall;
- AP and mAP;
- AP50/AP75;
- class-wise metrics;
- condition-wise metrics;
- small/medium/large object evaluation;
- calibration and thresholds;
- production metric alignment;
- statistical uncertainty.

### EXPERIMENTATION

- baseline;
- controls;
- independent/dependent variables;
- confounding factors;
- ablation;
- factorial thinking;
- repeated experiments;
- seeds;
- confidence intervals;
- bootstrap;
- experiment tracking;
- reproducibility.

### PRODUCTION

- production distribution;
- covariate shift;
- concept drift;
- domain/camera/lighting/sensor/geographic/seasonal shift;
- monitoring;
- feedback loop;
- human-in-the-loop;
- cost-aware dataset engineering;
- privacy, licensing, PII and retention.

## 6. Curriculum Phases

The curriculum has 8 phases. Each phase develops a capability level while preserving the full system loop.

```text
Phase 0: Operating System for Learning
Phase 1: Foundations and Recognition
Phase 2: Ground Truth and Data Collection
Phase 3: Dataset Audit, Leakage and Diagnosis
Phase 4: Baseline, Measurement and Statistical Thinking
Phase 5: Root Cause Analysis and Intervention Design
Phase 6: Iteration, Advanced Techniques and Cost-Aware Decisions
Phase 7: Production, Governance and Capstone
```

Progression:

```text
Foundation
-> Recognition
-> Diagnosis
-> Root Cause Analysis
-> Intervention
-> Experimentation
-> Research
```

## 7. Prerequisites

Minimum prerequisites:

- Python basics;
- notebooks and scripts;
- basic NumPy array thinking;
- basic plotting;
- reading CSV/JSON;
- command line basics.

Prerequisites developed inside the curriculum:

- image representation;
- coordinate systems;
- bounding boxes;
- IoU;
- precision and recall;
- AP/mAP;
- basic statistical thinking;
- experiment design;
- dataset versioning.

The learner should not need to know deep learning deeply before starting. Model internals are introduced only when they help explain system behavior.

## 8. Longitudinal Dataset

The curriculum uses one longitudinal real-world problem:

```text
Helmet and Worker Detection in Construction-Site CCTV
```

Why this problem is suitable:

- ontology is ambiguous enough to teach ground-truth design;
- objects vary in scale, occlusion, posture and camera angle;
- safety use case makes FP/FN tradeoffs meaningful;
- CCTV creates leakage and low-diversity risks;
- production shift is realistic across sites, cameras, time and lighting;
- cost-aware data collection is natural.

Dataset evolution:

```text
Problem Draft
-> Dataset v0: messy seed data
-> Annotation Policy v1
-> Dataset v1: first curated dataset
-> Baseline v1
-> Evaluation Report v1
-> Error Analysis v1
-> Root-Cause Report v1
-> Dataset/Model Intervention
-> Dataset v2
-> Controlled Experiment
-> Dataset v3 or Model v2
-> Final Evaluation
-> Production Simulation
```

Optional benchmark track:

- COCO subset or a COCO-style public detection dataset;
- used only to learn standard format, metric and baseline behavior;
- not allowed to replace the longitudinal real-world project.

## 9. Detailed Modules

Each module below includes learning objectives, labs, experiments, assignments and expected artifacts. Modules are ordered by capability progression.

## Module 0: Learning System, Tools and Reproducibility Basics

Capability focus:

- Foundation;
- Recognition of reproducibility requirements.

Learning objectives:

- understand repo layout;
- use Conda environment `data4cv`;
- distinguish notebook exploration from reusable package code;
- understand why experiment artifacts must be traceable.

Core concepts:

- project structure;
- environment file;
- editable package install;
- notebooks vs scripts;
- artifact locations;
- experiment ID.

Practical labs:

- run the existing bbox/IoU notebook;
- run `pytest` and `ruff`;
- create a simple experiment folder with a README.

Assignment:

- explain what information is needed to rerun a result 3 months later.

Expected artifacts:

- `experiments/exp000_environment_smoke_test/README.md`;
- short reproducibility checklist.

Decision question:

```text
If a result cannot be reproduced, should we trust the intervention?
```

## Module 1: Problem Framing and Measurement Intent

Capability focus:

- Recognition;
- early decision-making.

Learning objectives:

- convert an ambiguous business request into an engineering problem;
- identify allowed actors, scene, camera, object classes and cost of errors;
- define what "good" means before training a model.

Core concepts:

- production objective;
- operating conditions;
- false positive cost;
- false negative cost;
- metric alignment;
- system boundary.

Practical labs:

- write a problem definition for construction-site helmet detection;
- list deployment conditions: camera height, frame rate, lighting, distance, weather, site type.

Experiment:

- compare two metric priorities: safety-first recall vs inspection-cost precision.

Assignment:

- write a one-page problem definition answering:
  - who uses the system;
  - what action follows detection;
  - what errors are expensive;
  - which conditions are in scope/out of scope.

Expected artifacts:

- `docs/curriculum/problem_definition_helmet_worker.md`;
- metric intent table.

Decision question:

```text
Does mAP reflect the production objective, or do we need condition-specific recall?
```

## Module 2: Image, Object and Detection Foundations

Capability focus:

- Foundation;
- Recognition.

Learning objectives:

- understand image tensors, coordinates and resolution;
- understand object, class and instance;
- understand bbox formats and IoU;
- reason about when IoU thresholds are meaningful.

Core concepts:

- pixel;
- channel;
- resolution;
- bbox `xyxy`, `xywh`, normalized coordinates;
- visible vs full object extent;
- IoU;
- confidence;
- NMS.

Practical labs:

- inspect image shape and channels;
- draw bounding boxes;
- compute IoU for multiple box pairs;
- simulate NMS with overlapping predictions.

Experiments:

- measure how resizing affects small object visibility;
- test how IoU changes under shift vs scale error.

Assignment:

- answer: "Can two boxes look acceptable to a human but fail IoU 0.75?"

Expected artifacts:

- notebook: `notebooks/01_cv_fundamentals/`;
- small reusable bbox utility in `src/data4cvlab/`.

Decision question:

```text
When is IoU 0.5 acceptable, and when is IoU 0.75 or higher necessary?
```

## Module 3: Annotation Science and Ground-Truth Design

Capability focus:

- Recognition;
- Diagnosis of annotation ambiguity.

Learning objectives:

- understand annotation as ground-truth design;
- design ontology and annotation policy;
- handle ambiguity, occlusion, truncation, crowd and ignore regions;
- measure annotation consistency.

Core concepts:

- ontology;
- class definition;
- inclusion/exclusion criteria;
- ambiguity;
- occlusion percentage;
- truncation;
- crowd;
- ignore region;
- difficult cases;
- missing annotation;
- label noise;
- inter-annotator agreement;
- annotation QA.

Practical labs:

- design ontology for `worker`, `helmet`, `head`, `vest`, `vehicle`;
- write rules for:
  - object 70% occluded;
  - object 20% visible;
  - reflection;
  - poster/person image;
  - mannequin;
  - worker without visible head;
  - helmet held in hand;
  - crowded group;
  - object at image boundary;
  - motion-blurred object.

Experiments:

- have two annotators label the same 50 images, then measure disagreement;
- revise policy and remeasure agreement.

Assignment:

- produce annotation policy v1 and a QA checklist.

Expected artifacts:

- `docs/ontology/helmet_worker_ontology.md`;
- `docs/annotation_policy/helmet_worker_annotation_policy.md`;
- annotation QA checklist.

Decision question:

```text
Is disagreement a labeling detail, or evidence that the ontology is under-specified?
```

## Module 4: Data Collection Science

Capability focus:

- Diagnosis;
- intervention planning.

Learning objectives:

- design data collection before assuming a raw dataset is sufficient;
- understand why dataset size is not the same as information diversity;
- choose sampling strategy based on deployment scenario.

Core concepts:

- sampling frame;
- representative sampling;
- convenience sampling;
- stratified sampling;
- temporal sampling;
- spatial sampling;
- camera sampling;
- rare-event sampling;
- domain sampling;
- effective diversity;
- collection bias.

Important principle:

```text
100,000 images does not mean 100,000 independent information samples.
```

Practical labs:

- compare 10,000 adjacent CCTV frames with 1,000 frames sampled across sites, cameras and days;
- estimate effective diversity from metadata.

Experiments:

- random frame sampling vs stratified camera-time sampling;
- rare-event oversampling vs natural distribution sampling.

Assignment:

- design a collection strategy for 5 construction sites with limited annotation budget.

Expected artifacts:

- data collection plan;
- sampling matrix by site, camera, time, weather and activity.

Decision question:

```text
Should we collect more images, or more independent situations?
```

## Module 5: Dataset Schema, Versioning and Lineage

Capability focus:

- Diagnosis;
- reproducibility.

Learning objectives:

- represent datasets as versioned technical artifacts;
- track image source, annotation version, preprocessing and split;
- answer which data produced a given model.

Core concepts:

- dataset schema;
- dataset card;
- dataset v1/v1.1/v2/v2.1;
- annotation version;
- preprocessing version;
- split version;
- model version;
- training configuration;
- experiment ID;
- data lineage.

Practical labs:

- create dataset manifest for Dataset v0;
- define version changelog format;
- link experiment ID to dataset/config/model.

Experiments:

- compare results from same model on split v1 vs split v2;
- show how untracked preprocessing invalidates comparison.

Assignment:

- answer: "Model này được train bằng dataset nào, annotation version nào và config nào?"

Expected artifacts:

- dataset card template;
- version changelog template;
- experiment tracking template.

Decision question:

```text
If dataset v2 improves mAP, can we prove what changed?
```

## Module 6: Data Leakage and Split Design

Capability focus:

- Diagnosis;
- root-cause hypothesis.

Learning objectives:

- identify leakage modes;
- design train/validation/test split aligned with deployment;
- understand why high test performance may be untrustworthy.

Core concepts:

- image leakage;
- duplicate leakage;
- near-duplicate leakage;
- video leakage;
- temporal leakage;
- identity leakage;
- camera leakage;
- location leakage;
- preprocessing leakage;
- group split;
- time-based split;
- deployment-aligned test set.

Practical labs:

- detect duplicate and near-duplicate images;
- simulate video leakage:

```text
frame 001 -> train
frame 002 -> train
frame 003 -> test
```

Experiments:

- random frame split vs video-group split;
- same-site test vs unseen-site test;
- same-camera test vs unseen-camera test.

Assignment:

- design a split policy for helmet detection deployed on unseen construction sites.

Expected artifacts:

- leakage audit checklist;
- split policy;
- leakage risk report.

Decision question:

```text
Does our test set measure memorization of scenes or generalization to deployment?
```

## Module 7: Dataset Audit and Distribution Diagnosis

Capability focus:

- Diagnosis.

Learning objectives:

- audit schema, annotations and distributions;
- identify dataset bias and quality risks;
- connect distribution evidence to likely model failures.

Core concepts:

- class distribution;
- instance distribution;
- object-size distribution;
- aspect-ratio distribution;
- spatial distribution;
- image quality;
- blur, low light, weather and camera conditions;
- long-tail distribution;
- label noise;
- missing labels;
- dataset bias.

Practical labs:

- compute class counts;
- plot bbox size and aspect ratio;
- build object center heatmap;
- sample images by condition;
- inspect missing label candidates.

Experiments:

- compare performance by object size and lighting;
- correlate failure rate with image-quality groups.

Assignment:

- write a Dataset Diagnosis Report for Dataset v1.

Expected artifacts:

- `reports/dataset_reports/helmet_worker_dataset_v1_diagnosis.md`;
- analysis notebooks;
- reusable audit utilities.

Decision question:

```text
What does this dataset actually represent?
```

## Module 8: Baselines, Metrics and Measurement Engineering

Capability focus:

- Diagnosis;
- measurement design.

Learning objectives:

- build a credible baseline;
- choose metrics based on production objective;
- evaluate beyond a single mAP number.

Core concepts:

- baseline;
- train/validation/test;
- precision;
- recall;
- FP/FN;
- AP/mAP;
- AP50/AP75;
- APsmall/APmedium/APlarge;
- class-wise evaluation;
- condition-wise evaluation;
- threshold sweep;
- operating point.

Practical labs:

- train or run a pretrained baseline;
- evaluate class-wise and condition-wise;
- sweep confidence threshold;
- compare AP50 and AP75.

Experiments:

- choose threshold for safety-first recall;
- evaluate same model under random split vs deployment-aligned split.

Assignment:

- write an Evaluation Protocol document explaining why chosen metrics fit the problem.

Expected artifacts:

- baseline config;
- evaluation report;
- threshold sweep notebook.

Decision questions:

```text
Does mAP reflect the production objective?
When should recall matter more than precision?
What does AP50 high but AP75 low tell us?
```

## Module 9: Statistical Thinking for Experiments

Capability focus:

- Experimentation.

Learning objectives:

- avoid overinterpreting small metric differences;
- understand randomness and uncertainty;
- use repeated runs, confidence intervals and bootstrap.

Core concepts:

- randomness;
- variance;
- seed;
- repeated experiments;
- confidence interval;
- bootstrap;
- statistical significance;
- sampling uncertainty;
- practical significance.

Important warning:

```text
Experiment A = 84.2
Experiment B = 85.1
```

This does not automatically mean B is better.

Practical labs:

- run repeated evaluations with different seeds or bootstrap samples;
- compute confidence intervals for AP/recall;
- compare metric differences against uncertainty.

Experiments:

- repeated baseline runs;
- bootstrap confidence interval for condition-wise recall.

Assignment:

- decide whether a 0.9 AP improvement is meaningful under observed variance.

Expected artifacts:

- statistical evaluation notebook;
- experiment interpretation memo.

Decision question:

```text
Is the observed improvement real, or just noise?
```

## Module 10: Experimental Methodology

Capability focus:

- Experimentation;
- research mindset.

Learning objectives:

- design controlled experiments;
- distinguish intervention effect from confounding factors;
- structure ablations and factorial comparisons.

Core concepts:

- hypothesis;
- baseline;
- control;
- independent variable;
- dependent variable;
- confounding factor;
- ablation;
- factorial thinking;
- reproducibility;
- experiment tracking.

Practical labs:

- design an experiment to test hard negatives while holding annotation budget constant;
- design an experiment to isolate resolution effect from dataset effect.

Experiments:

- hard negatives vs random negatives;
- image resolution 640 vs 960 with fixed data/config;
- annotation policy v1 vs v2 with agreement measured before/after.

Assignment:

- write an experiment design before running anything.

Expected artifacts:

- experiment plan template;
- ablation table;
- controlled experiment report.

Decision question:

```text
What exactly changed, and can we attribute the result to that change?
```

## Module 11: Error Analysis and Failure Taxonomy

Capability focus:

- Diagnosis;
- root-cause analysis.

Learning objectives:

- classify errors into actionable categories;
- quantify failure modes;
- separate symptom from cause.

Core concepts:

- false positive;
- false negative;
- background FP;
- wrong class;
- duplicate;
- localization error;
- small-object FN;
- occlusion FN;
- blur/low-light FN;
- crowded-scene FN;
- domain shift;
- missing annotation.

Practical labs:

- review prediction samples;
- label each failure with taxonomy;
- aggregate failure modes by class/condition.

Experiments:

- compare failure taxonomy before and after threshold changes;
- test whether low recall is concentrated in small objects, occlusion or a class.

Assignment:

- classify 100 model failures and rank top 5 by production impact.

Expected artifacts:

- `reports/error_analysis/baseline_v1_failure_taxonomy.md`;
- failure summary table;
- sample gallery.

Decision question:

```text
Which failure pattern should drive the next intervention?
```

## Module 12: Root Cause Analysis Framework

Capability focus:

- Root Cause Analysis.

Learning objectives:

- convert failure symptoms into competing hypotheses;
- design tests to distinguish causes;
- avoid treating correlation as root cause.

Framework:

```text
Symptom
-> Observation
-> Correlation
-> Hypothesis
-> Evidence Needed
-> Root Cause Candidate
-> Intervention
-> Experiment
-> Interpretation
```

Example:

```text
Symptom: Model fails on small objects.

Hypotheses:
- objects have insufficient pixels;
- input resolution is too low;
- small-object annotation is inconsistent;
- dataset undersamples small objects;
- augmentation destroys small objects;
- model architecture is weak for small objects;
- NMS suppresses nearby small objects;
- confidence threshold is too high.
```

Practical labs:

- build root-cause trees for small-object failure, background FP and high train/low test;
- list evidence needed for each hypothesis.

Experiments:

- resolution ablation;
- annotation consistency audit;
- targeted data collection;
- threshold/NMS sweep;
- split redesign.

Assignment:

- write a Root-Cause Report for one major failure.

Expected artifacts:

- `reports/error_analysis/root_cause_report_v1.md`;
- hypothesis matrix.

Decision question:

```text
What evidence would change your mind?
```

## Module 13: Data-Centric Debugging of System Regressions

Capability focus:

- Diagnosis;
- root-cause analysis under ambiguity.

Learning objectives:

- debug full system regressions;
- check reproducibility before blaming model or data;
- trace changes across data, annotation, split, preprocessing, training and evaluation.

Scenario:

```text
Model v1 = 87%
Model v2 = 81%
```

Debug checklist:

1. Is evaluation reproducible?
2. Did the dataset change?
3. Did annotation change?
4. Did distribution change?
5. Did train/test split change?
6. Did preprocessing change?
7. Did training configuration change?
8. Did model architecture or weights change?
9. Did random seed affect the result?
10. Did production distribution shift?

Practical labs:

- intentionally introduce one regression and diagnose it;
- compare experiment manifests.

Experiments:

- same model/different split;
- same split/different preprocessing;
- same config/different seed;
- same dataset/different annotation version.

Assignment:

- produce a regression diagnosis memo.

Expected artifacts:

- debugging checklist;
- regression report;
- experiment diff table.

Decision question:

```text
Are we debugging the model, or the whole measurement system?
```

## Module 14: Intervention Design

Capability focus:

- Intervention.

Learning objectives:

- choose intervention based on failure pattern and root-cause hypothesis;
- estimate cost and risk;
- avoid uncontrolled multi-change improvements.

Intervention categories:

- data collection;
- data selection;
- annotation correction;
- annotation policy refinement;
- split redesign;
- preprocessing change;
- augmentation change;
- hyperparameter change;
- model architecture change;
- threshold/NMS change;
- deployment monitoring change.

Practical labs:

- map failure patterns to interventions;
- estimate annotation and compute cost.

Experiments:

- targeted small-object collection vs random collection;
- hard-negative mining vs more general data;
- annotation cleanup vs model tuning.

Assignment:

- propose three interventions for the same failure, rank by expected impact, cost and risk.

Expected artifacts:

- intervention proposal;
- cost-impact-risk matrix.

Decision question:

```text
What is the smallest intervention likely to test the root-cause hypothesis?
```

## Module 15: Cost-Aware Dataset Engineering

Capability focus:

- Intervention;
- production tradeoff.

Learning objectives:

- reason about performance relative to cost;
- compare data strategies using annotation, compute, storage and maintenance cost.

Core concepts:

- annotation cost;
- collection cost;
- QA cost;
- compute cost;
- storage cost;
- engineering cost;
- maintenance cost;
- performance per annotation hour;
- performance per dollar;
- performance per GPU hour.

Practical labs:

- compare:

```text
Option A: 100k images, $20k annotation, mAP = 90
Option B: 40k images, $8k annotation, mAP = 89
```

Experiments:

- random 5k annotation budget vs targeted 5k annotation budget;
- low-cost QA vs high-cost double annotation.

Assignment:

- recommend a data strategy under a fixed budget.

Expected artifacts:

- cost-aware experiment plan;
- performance-cost report.

Decision question:

```text
Which option is best for production, not just best for leaderboard score?
```

## Module 16: Human-in-the-Loop Systems

Capability focus:

- Intervention;
- production feedback loop.

Learning objectives:

- design workflows where model predictions support human review;
- understand disagreement, correction and QA;
- connect active learning to human annotation cost.

Pipeline:

```text
Model
-> Prediction
-> Human Review
-> Correction
-> New Training Data
-> Model
```

Core concepts:

- annotation workflow;
- reviewer;
- disagreement;
- QA;
- model-assisted labeling;
- active learning;
- correction queue;
- feedback loop.

Practical labs:

- create review workflow for low-confidence predictions;
- prioritize samples for human review.

Experiments:

- human review on random samples vs uncertain samples;
- reviewer policy before/after guideline refinement.

Assignment:

- design a human-in-the-loop loop for construction-site deployment.

Expected artifacts:

- HITL workflow document;
- review queue policy.

Decision question:

```text
When does adding humans improve data quality, and when does it create inconsistency?
```

## Module 17: Advanced Techniques as Decision Tools

Capability focus:

- Intervention;
- experimentation;
- research.

Learning objectives:

- learn advanced methods as responses to specific failure patterns;
- know when not to use them;
- compare against simpler baselines.

Teaching pattern for each technique:

```text
Problem
-> Why existing approach fails
-> Technique
-> When useful
-> When not useful
-> Cost
-> Failure modes
-> Experiment
-> Interpretation
```

Techniques:

- hard-negative mining;
- active learning;
- uncertainty sampling;
- diversity sampling;
- weak supervision;
- semi-supervised learning;
- synthetic data;
- domain adaptation;
- dataset pruning;
- dataset valuation;
- dataset distillation;
- label quality estimation.

Practical labs:

- hard-negative mining for background FPs;
- active learning under fixed annotation budget;
- synthetic data risk assessment for rare cases.

Experiments:

- random sampling vs active learning;
- real data only vs real + synthetic;
- weak labels vs cleaned labels.

Assignment:

- choose one advanced method for one failure mode and explain why two other methods are not appropriate.

Expected artifacts:

- advanced intervention decision memo;
- experiment report.

Decision question:

```text
What failure pattern justifies this technique?
```

## Module 18: Production Distribution Shift and Monitoring

Capability focus:

- Diagnosis;
- production readiness.

Learning objectives:

- understand offline vs production distributions;
- monitor model and data after deployment;
- plan for drift and feedback.

Distribution chain:

```text
Training Distribution
-> Validation Distribution
-> Test Distribution
-> Production Distribution
```

Core concepts:

- covariate shift;
- concept drift;
- domain shift;
- camera shift;
- lighting shift;
- seasonal shift;
- geographic shift;
- sensor shift;
- production monitoring;
- alerting;
- sampling production failures.

Practical labs:

- define monitoring metrics for production CCTV;
- simulate camera/site shift.

Experiments:

- evaluate on unseen camera;
- evaluate on night vs day;
- evaluate on new construction site.

Assignment:

- answer: "Model hôm nay tốt, nhưng 6 tháng sau thì sao?"

Expected artifacts:

- production monitoring plan;
- drift risk matrix;
- retraining trigger policy.

Decision question:

```text
What signal tells us the model is no longer valid in production?
```

## Module 19: Data Governance and Documentation

Capability focus:

- Production;
- senior engineering responsibility.

Learning objectives:

- treat dataset as technical and organizational artifact;
- document provenance, privacy and access constraints;
- understand governance without turning the course into legal training.

Core concepts:

- data provenance;
- licensing;
- privacy;
- PII;
- consent;
- retention;
- access control;
- dataset documentation;
- datasheets;
- model cards.

Practical labs:

- write a dataset card;
- identify PII and retention risks in CCTV data;
- create access-control assumptions.

Assignment:

- write a governance checklist for construction-site CCTV dataset.

Expected artifacts:

- dataset card;
- model card;
- governance checklist.

Decision question:

```text
Can we legally, ethically and operationally reuse this data?
```

## Module 20: Blind Dataset Challenge

Capability focus:

- Integrated diagnosis;
- root-cause analysis;
- experimentation.

Assessment format:

Learner receives an object detection dataset with unknown issues. The issues are not announced in advance.

Learner must:

1. audit schema;
2. analyze annotation;
3. analyze distribution;
4. find duplicates;
5. find leakage;
6. find bias;
7. find noise;
8. evaluate baseline;
9. analyze failures;
10. form hypotheses;
11. propose interventions;
12. design experiments;
13. build Dataset v2;
14. compare v1 vs v2;
15. write diagnosis report.

Possible hidden issues:

- video leakage;
- class imbalance;
- missing labels;
- inconsistent occlusion policy;
- duplicate images;
- wrong class mapping;
- rare class absent from validation;
- background shortcut;
- production split mismatch.

Expected artifacts:

- Dataset Autopsy Report;
- Root-Cause Report;
- Intervention Plan;
- Controlled Experiment Report;
- Dataset v2 changelog.

Decision question:

```text
Can the learner discover what is wrong without being told where to look?
```

## Module 21: Capstone System Diagnosis and Improvement

Capability focus:

- Senior-level integration;
- applied research readiness.

Capstone prompt:

```text
Given an ambiguous real-world Object Detection problem and a partially prepared
dataset, independently diagnose, design, improve and validate the entire system.
```

The learner must decide:

- ontology;
- annotation policy;
- data strategy;
- split;
- baseline;
- metric;
- experiment;
- intervention;
- evaluation;
- production considerations.

Capstone is not:

```text
Train YOLO on dataset X.
```

Capstone deliverables:

- problem definition;
- ontology and annotation policy;
- data collection and split plan;
- dataset audit;
- baseline and evaluation report;
- error analysis;
- root-cause report;
- intervention proposal;
- controlled experiment;
- dataset/model iteration;
- final evaluation;
- production monitoring plan;
- final technical case study.

Evaluation criteria:

- quality of reasoning;
- evidence use;
- decision clarity;
- experiment control;
- statistical interpretation;
- production realism;
- cost-awareness;
- reproducibility.

## 10. Decision Matrix

This matrix should be reused throughout the curriculum.

| Problem pattern | Investigate first | Possible causes | Possible interventions | Experiment |
|---|---|---|---|---|
| Small-object failures | Object-size distribution, resolution, APsmall, visual errors | insufficient pixels, low resolution, weak small-object sampling, annotation inconsistency, architecture, NMS | targeted small-object data, higher resolution, policy refinement, model change, NMS tuning | resolution ablation; targeted vs random small-object collection |
| Background false positives | FP gallery, background clusters, confidence distribution | missing hard negatives, confusing texture, unlabeled objects, threshold too low | hard-negative mining, annotation cleanup, threshold tuning | random negatives vs targeted hard negatives |
| High train / low test | split, leakage, distribution shift, overfitting | duplicate leakage, camera leakage, location leakage, weak regularization | group split, time/site split, augmentation, more diverse data | random split vs deployment-aligned split |
| Annotation disagreement | policy, edge cases, annotator agreement | ambiguous ontology, unclear occlusion/truncation rules, class granularity | refine policy, train annotators, review workflow, ignore regions | agreement before/after policy refinement |
| AP50 high / AP75 low | localization errors, bbox tightness, annotation policy | loose boxes, inconsistent boxes, low resolution, weak localization | bbox policy cleanup, resolution change, model/anchor changes | AP50/AP75 comparison before/after intervention |
| Minority class recall low | class distribution, condition distribution, sample quality | imbalance, rare conditions, poor labels, not enough diversity | stratified sampling, targeted collection, class-aware sampling | equal budget random vs targeted collection |
| Production performance drop | production samples, drift metrics, camera/site/time metadata | domain shift, sensor shift, lighting shift, concept drift | production monitoring, targeted refresh data, retraining | old test vs recent production holdout |
| Regression from v1 to v2 | experiment manifest diff | data change, annotation change, split change, preprocessing change, seed, model/config change | isolate changed variable, rerun baseline, restore control | one-variable-at-a-time regression diagnosis |

## 11. Assessment Framework

Assess reasoning, not only code.

Every major assessment should require this report structure:

```text
Problem
-> Evidence
-> Observation
-> Hypothesis
-> Root Cause Candidate
-> Intervention
-> Experiment
-> Result
-> Interpretation
-> Recommendation
```

Assessment types:

- concept checks;
- notebook labs;
- dataset audit reports;
- annotation policy reviews;
- experiment design reviews;
- root-cause reports;
- regression debugging exercises;
- blind dataset challenge;
- final capstone.

Rubric dimensions:

- identifies the correct bottleneck region;
- separates symptom from root cause;
- considers alternative hypotheses;
- designs controlled experiments;
- handles uncertainty;
- connects metric to production objective;
- accounts for cost and governance;
- communicates recommendation clearly.

## 12. Progressive Difficulty

Difficulty increases across five dimensions:

1. Problem clarity: from explicit problems to ambiguous requests.
2. Evidence quality: from clean evidence to incomplete/noisy evidence.
3. Hypothesis count: from one likely cause to multiple competing causes.
4. Tradeoff complexity: from metric-only to cost, governance and production constraints.
5. Experiment autonomy: from guided experiment to learner-designed study.

Progression examples:

Junior task:

```text
Identify class imbalance and describe likely metric impact.
```

Mid task:

```text
Diagnose why minority-class recall is low using class-wise and condition-wise metrics.
```

Senior task:

```text
Distinguish sampling effect from annotation effect and propose a controlled intervention.
```

Research Engineer task:

```text
Design an experiment to test whether targeted collection outperforms random sampling
under a fixed annotation budget, with uncertainty estimates.
```

## 13. Research Track

Research mindset appears from the first module:

```text
Observation
-> Question
-> Hypothesis
-> Experiment
-> Result
-> Interpretation
-> Next Question
```

Research questions introduced early:

- Does IoU always reflect localization quality?
- How does annotation disagreement affect detection performance?
- Does diversity matter more than raw dataset size?
- Does mAP reflect production objective?
- Can model failures identify missing data?
- Can targeted data collection outperform random collection?
- Can performance improve without changing architecture?

Research track deliverables:

- mini research questions;
- hypothesis memos;
- ablation reports;
- uncertainty analysis;
- final applied research proposal.

## 14. Production Track

Production thinking appears throughout the curriculum, not only at the end.

Production competencies:

- define operating conditions;
- align metrics with action;
- design deployment-aligned splits;
- monitor production shift;
- design human review workflow;
- track dataset/model lineage;
- manage cost;
- document governance constraints.

Production deliverables:

- production objective document;
- monitoring plan;
- retraining trigger policy;
- governance checklist;
- model card;
- dataset card.

## 15. Practical Labs and Experiment Inventory

Core labs:

- image tensor and bbox visualization;
- IoU sensitivity lab;
- NMS simulation;
- annotation ambiguity lab;
- inter-annotator agreement lab;
- sampling strategy simulation;
- dataset leakage lab;
- distribution audit lab;
- baseline evaluation lab;
- threshold sweep lab;
- bootstrap confidence interval lab;
- failure taxonomy lab;
- root-cause tree lab;
- regression debugging lab;
- active learning vs random sampling lab;
- hard-negative mining lab;
- production drift simulation.

Core experiments:

- random split vs deployment split;
- AP50/AP75 interpretation before/after annotation cleanup;
- small-object targeted collection vs random collection;
- hard negatives vs random negatives;
- resolution ablation;
- annotation policy v1 vs v2;
- repeated seeds;
- old test set vs recent production holdout;
- active learning vs random sampling under fixed budget.

## 16. Recommended Tools and Frameworks

Use tools only when they support the capability being trained.

Core:

- Python;
- Conda environment `data4cv`;
- JupyterLab or VS Code Notebook;
- NumPy;
- Pandas;
- Matplotlib;
- Seaborn;
- OpenCV;
- Pillow;
- Pytest;
- Ruff.

Detection and dataset tools, introduced when needed:

- COCO format and `pycocotools`;
- FiftyOne for dataset inspection when dataset size justifies it;
- supervision for visualization/evaluation helpers;
- Ultralytics only as a practical baseline tool, not as the center of the course;
- MLflow, DVC or lightweight manifests for experiment/data tracking when reproducibility needs increase.

Do not introduce heavy tooling before the learner understands the underlying decision.

## 17. What Not To Learn Too Deeply

The learner does not need to deeply study:

- every YOLO version;
- every DETR variant;
- low-level CUDA optimization;
- training a detector from scratch before understanding pretrained fine-tuning;
- every annotation platform;
- every active learning algorithm;
- every synthetic data generator;
- benchmark leaderboard history;
- framework API memorization.

These can be explored later if a real bottleneck or research question requires them.

## 18. Career Mapping

### Junior Applied CV Engineer

Can:

- run notebooks and scripts;
- inspect images and annotations;
- compute basic dataset stats;
- train/evaluate a baseline with guidance;
- identify obvious issues such as class imbalance or missing labels.

Needs guidance for:

- root-cause analysis;
- experiment design;
- production split design.

### Mid-Level CV/ML Engineer

Can:

- write annotation policy drafts;
- design dataset audits;
- evaluate class-wise and condition-wise;
- debug common failure modes;
- propose reasonable interventions;
- run controlled experiments with limited variables.

Needs guidance for:

- ambiguous bottleneck diagnosis;
- statistical interpretation;
- production monitoring strategy.

### Senior Applied CV Engineer

Can:

- frame ambiguous production problems;
- identify bottleneck region across data/model/measurement;
- design split and evaluation aligned with deployment;
- distinguish symptoms from root causes;
- balance performance, cost, risk and maintainability;
- lead dataset/model iteration.

Needs guidance only for:

- novel research questions;
- unfamiliar domains;
- organizational constraints outside engineering control.

### Applied Research Engineer

Can:

- formulate research questions from production failures;
- design controlled and statistically defensible studies;
- compare advanced techniques against simple baselines;
- create reusable knowledge, not just one-off fixes;
- write clear technical reports with limitations and next questions.

## 19. Completion Criteria

The learner is considered ready when they can independently produce a complete case study for the longitudinal helmet/worker detection problem.

Minimum final evidence:

- problem definition;
- ontology and annotation policy;
- data collection plan;
- dataset versioning and lineage;
- leakage-aware split;
- dataset diagnosis report;
- baseline model and evaluation;
- statistical interpretation;
- failure taxonomy;
- root-cause report;
- intervention plan;
- controlled experiment result;
- dataset/model iteration;
- cost-aware recommendation;
- production monitoring plan;
- final case study.

The final judgment is not based on highest mAP. It is based on whether the learner can reason clearly:

```text
What is wrong?
Why is it likely wrong?
What should change?
How do we test that change?
Did it actually work?
What should we do next?
```

## 20. Suggested Repository Mapping

Use the repository as an engineering lab, not just a place to store notebooks.

```text
docs/curriculum/
  data_centric_object_detection_curriculum.md
  module_<number>_<name>.md

docs/ontology/
  helmet_worker_ontology.md

docs/annotation_policy/
  helmet_worker_annotation_policy.md

notebooks/
  01_cv_fundamentals/
  02_detection_foundations/
  03_annotation_science/
  04_data_collection/
  05_dataset_audit/
  06_leakage_split_design/
  07_baseline_measurement/
  08_statistical_thinking/
  09_error_analysis/
  10_root_cause_analysis/
  11_interventions/
  12_production_monitoring/

src/data4cvlab/
  datasets/
  analysis/
  visualization/
  training/
  evaluation/
  utils/

scripts/
  audit_dataset.py
  detect_leakage.py
  visualize_samples.py
  convert_annotations.py
  train_baseline.py
  evaluate_predictions.py
  summarize_failures.py

reports/
  dataset_reports/
  experiment_reports/
  error_analysis/
```

## 21. First Implementation Plan

Do not start by training a model. Start by creating the learner's diagnostic foundation.

Recommended first sequence:

1. Module 1: Problem Framing and Measurement Intent
2. Module 2: Image, Object and Detection Foundations
3. Module 3: Annotation Science and Ground-Truth Design
4. Module 4: Data Collection Science
5. Module 6: Data Leakage and Split Design

Reason:

If the learner does not understand problem definition, annotation policy, collection strategy, leakage and measurement intent, model training will produce numbers without trustworthy interpretation.

The first substantial artifact should be:

```text
Helmet/Worker Detection Problem Definition
-> Ontology v1
-> Annotation Policy v1
-> Data Collection Plan
-> Split Policy
```

Only after that should the learner build Dataset v1 and train Baseline v1.
