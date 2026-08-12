# Curriculum Implementation Readiness Review

## Review Metadata

- Review date/time: `2026-08-13 00:53:12 +07 +0700`
- Reviewer role: Curriculum & Lesson Reviewer for Data-Centric Computer Vision and Object Detection
- Review scope: implementation-readiness layer for `docs/curriculum`
- Primary file reviewed: `docs/curriculum/curriculum_implementation_readiness.md`
- Curriculum context file reviewed: `docs/curriculum/data_centric_object_detection_curriculum.md`
- Architecture freeze context file reviewed: `docs/curriculum/curriculum_architecture_freeze.md`
- Prior review referenced: `docs/reviews/curriculum/2026-08-13_004151_curriculum_review.md`
- Review response trace referenced: `docs/reviews/curriculum/2026-08-13_004151_curriculum_review_response.md`
- Reviewer instruction file: `AGENTS_reviewer.md`
- Git commit at review time: `27c58370c6b5390ab21bb7f020e9d0926355f249`
- Working tree note: `AGENTS_reviewer.md` was untracked at review time; the reviewed curriculum/review files did not appear as modified in `git status --short -- docs/curriculum docs/reviews/curriculum AGENTS_reviewer.md`.

## File Version Evidence

SHA-256 checksums at review time:

```text
55654218ce4f19d3454633214100f56bde775937711bab131fe49e37d2017bd9  docs/curriculum/curriculum_implementation_readiness.md
7025e03c1a2813843d950b7f2d63e4c5d83cfdfa1b79da92beb1951ef45e814b  docs/curriculum/data_centric_object_detection_curriculum.md
618ce98fb69106a296e052d50fd89d2370e0ce002aa3f1f6b4679549b1f343ff  docs/curriculum/curriculum_architecture_freeze.md
c854d319a9fc5eb634a8f2ca74b5602897b3fba9637e44870956d62b3c41fbe7  docs/reviews/curriculum/2026-08-13_004151_curriculum_review.md
ccd6eb6c1930fcb044edfef8fcd6e7e174d70d187dcd57356935140309098559  docs/reviews/curriculum/2026-08-13_004151_curriculum_review_response.md
d17d55247ce31bd1ceed6dcc4f9318917bfe231b9f993bc24eb9f8f39f782bf5  AGENTS_reviewer.md
```

## 1. Overall Verdict

**Strong / Implementation-Ready with Minor Revisions.**

`curriculum_implementation_readiness.md` successfully addresses the major weaknesses identified in the previous curriculum review. It turns the curriculum from a strong blueprint into a more assessable training system by adding track boundaries, observable objectives, exit criteria, common wrong answers, experiment rules, dataset gates, artifact rubrics, report reasoning sections, prerequisite blocks, and advanced-technique decision rules.

The file should be accepted as the implementation-readiness layer, but it still needs a small set of tightening changes before lesson generation becomes systematic.

## 2. Target Capability

The document is not teaching a learner directly. Its purpose is to constrain lesson designers and reviewers so lessons produce measurable capability.

The target capability being protected is:

```text
Learner can diagnose and improve an Object Detection system through
data, model, measurement, and experimentation, with evidence-based decisions.
```

This aligns with the architecture freeze and the prior curriculum review.

## 3. Target Depth

Target depth: **[C] Mastery for core applied diagnosis**, with **[D] Research extensions only where justified**.

This is mostly correct. The document now makes Module 17 an `Optional Decision Case`, which prevents advanced techniques from becoming a required checklist.

## 4. What Works

### Track boundaries are much clearer

The module track map separates `Core`, `Production`, `Optional Decision Case`, and `Capstone`. This directly reduces overload risk.

Important improvement:

```text
Module 17 is no longer treated as one broad required module.
It becomes a library of optional decision cases selected by failure pattern.
```

This is the right decision. It protects the curriculum from becoming a survey of advanced methods.

### Observable objectives are now enforceable

The objective standard is concrete:

```text
After this module, learner can <observable action>
given <input/evidence>
under <constraint/context>
and can explain <decision/tradeoff>.
```

This fixes the earlier problem where objectives used weak verbs such as `understand`.

### Exit criteria and common wrong answers are valuable

Adding exit criteria and common wrong answers for every module is a strong pedagogical improvement. The common wrong answers are especially useful because they target shallow reasoning patterns such as:

- "Higher mAP means better production system."
- "Small-object recall is low, therefore we need more small-object data."
- "Human review always improves labels."
- "Active learning/synthetic data/domain adaptation should be used because it is advanced."

This is exactly the kind of negative knowledge the curriculum needs.

### Experiment governance is much stronger

The lightweight experiment template is appropriate for early modules before formal experimental methodology is taught.

The required experiment manifest is strong because it forces dataset version, annotation version, split version, preprocessing version, model version, config, seed, variables, confounders, decision rule, statistical method, practical significance, result, interpretation, limitations, and next action.

This substantially improves reproducibility and attribution.

### Minimal gates before baseline are correct

The revised sequence prevents premature model training:

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

This fixes the earlier gap where baseline work could begin before data lineage, split policy, and audit were minimally stable.

### Artifact rubrics improve assessment quality

The Weak / Acceptable / Strong / Excellent rubrics are useful and concrete enough to guide lesson review. The strongest rubrics are for:

- Dataset Diagnosis Report;
- Evaluation Report;
- Root-Cause Report;
- Experiment Report;
- Capstone.

These rubrics directly measure reasoning and decision quality, not just whether an artifact exists.

## 5. Critical Issues

### Issue 1: The document lacks its own version/audit metadata

The document references the prior review and response trace, but the file itself does not include creation/update timestamp, author/reviewer, commit, or checksum evidence.

This is weaker than the review artifact standard. If this file becomes the official implementation gate, future agents need to know which curriculum snapshot it applies to.

Recommendation:

Add a metadata block near the top:

```text
Created:
Last updated:
Applies to curriculum file:
Applies to architecture freeze:
Prior review:
Response trace:
Commit:
Status:
```

Do not manually maintain checksum inside the curriculum file unless the project wants strict audit overhead. For reviews, checksum is useful; for active implementation docs, commit and linked review trace may be enough.

### Issue 2: Core remains large even after Module 17 is moved out

Modules 0-14 are all still `Core`. This may be justified, but it is still a heavy core path for a learner starting with limited CV foundations.

Risk:

```text
The curriculum may be conceptually correct but too long before the learner reaches visible model feedback.
```

Recommendation:

Keep Modules 0-14 as Core, but group them into milestones:

```text
Foundation Readiness: Modules 0-2
Ground Truth Readiness: Modules 3-5
Dataset Trust Readiness: Modules 6-7
Baseline Measurement Readiness: Modules 8-10
Diagnosis Readiness: Modules 11-14
```

Each milestone should have a small integrated task and pass criteria.

### Issue 3: Exit criteria still lack pass/fail thresholds

The exit criteria are useful, but many are binary artifact requirements rather than scoring rules.

Example:

```text
failure report ranks top failure modes and includes visual evidence.
```

This is good, but it does not say what minimum quality is required to continue.

Recommendation:

Define pass rules:

```text
To pass a module, learner must reach at least Acceptable on the artifact rubric
and must not contain any critical reasoning failure.
```

Critical reasoning failures should include:

- treating correlation as causation;
- claiming root cause without evidence;
- changing multiple variables while claiming attribution;
- using final test set for iterative tuning;
- proposing "more data" without target distribution.

### Issue 4: Dataset metadata should be split into required, recommended, and optional

The metadata schema is good, but some fields may not be available for public datasets.

Risk:

```text
Learner may think a dataset is unusable if weather, activity_type,
or viewpoint are missing.
```

Recommendation:

Split metadata into:

- Required for identity and lineage;
- Required for leakage-aware split;
- Recommended for diagnosis;
- Optional when available.

The file already has a minimum field list, but the full schema should also be visibly tiered.

### Issue 5: Statistical rules are correct but still too high-level

The minimum experiment rules say to use repeated seeds when differences are small, training is unstable, dataset is small, or the intervention affects optimization.

This is directionally correct, but lesson authors need more operational guidance.

Recommendation:

Add examples:

```text
Use repeated seeds:
- comparing model training runs;
- comparing augmentation or optimization changes;
- when AP difference is close to baseline variance.

Bootstrap may be useful:
- estimating uncertainty for recall on a fixed test slice;
- small condition-wise subsets.

Bootstrap is not enough:
- if the test set itself is biased, leaked, or unrepresentative.
```

## 6. Technical Issues

No major technical correctness errors found.

Minor technical concerns:

- `conda run -n data4cv pytest` in Module 0 may be too environment-specific. If the project later supports `uv` or `venv`, this should become `project-approved test command`.
- `statistical significance` should be handled carefully. Detection metrics such as AP are not always straightforward for naive significance claims.
- `effective sample size` appears in objectives, but implementation lessons must avoid pretending it can always be estimated exactly from metadata.
- `model_version` in experiment manifests should clarify whether it means architecture, pretrained weights, checkpoint, or all of them.

## 7. Pedagogical Issues

Pedagogically, this document is much better than the original curriculum alone.

Remaining issue:

```text
The readiness layer defines what good artifacts look like, but does not yet define lesson-level scaffolding.
```

Recommended standard for every lesson:

```text
1. Scenario
2. Learner prediction
3. Evidence
4. Concept
5. Guided practice
6. Independent task
7. Common wrong answers
8. Artifact
9. Rubric
10. Exit check
```

This keeps Socratic reasoning active instead of turning the document into a compliance checklist.

## 8. Reasoning Issues

The file strongly enforces reasoning. Required report sections are particularly good:

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

This structure is strong enough to prevent most vague learner answers.

Remaining weakness:

The file should explicitly say that a learner may answer `Insufficient evidence` when evidence is not enough. This matters because forcing a hypothesis in every report can accidentally train overconfidence.

Recommendation:

Add:

```text
If evidence is insufficient, learner should state insufficient evidence,
explain what is missing, and propose the smallest next evidence-gathering step.
```

## 9. Experimental Issues

The experiment manifest and early template are strong.

Remaining issue:

There is no explicit rule for allowed conclusions. The early template has `Conclusion allowed` and `Conclusion not allowed`, but the full experiment manifest does not.

Recommendation:

Add to the full manifest:

```yaml
allowed_conclusions:
not_allowed_conclusions:
```

This is useful because learners often overclaim from a controlled but narrow experiment.

## 10. Missing Prerequisites

The short prerequisite blocks are appropriate and should not become full modules.

One missing prerequisite block:

```text
Basic detection data formats:
- COCO-style image/annotation/category structure;
- YOLO-style txt labels;
- conversion risk;
- class id mapping risk;
- bbox coordinate convention risk.
```

This is important because many real detection failures come from label conversion and class mapping errors.

## 11. Missing Concepts

Important concepts still worth adding to readiness rules:

- phase/milestone gates;
- pass/fail threshold per artifact;
- `Insufficient evidence` as an acceptable conclusion;
- allowed/not-allowed conclusions in full experiment manifest;
- tiered metadata requirements;
- detection annotation format/conversion prerequisite.

These are refinements, not structural rewrites.

## 12. Unnecessary Content

No major unnecessary content in this file.

The document mostly avoids adding breadth and instead adds implementation constraints. That is aligned with the architecture freeze.

The only risk is that the detailed module objective list duplicates the main curriculum. This is acceptable if this file remains the implementation-readiness contract. If the curriculum later gets split into module files, this document should become the global standard and avoid repeating too much module content.

## 13. Recommended Revision

Apply these revisions before treating this as final:

1. Add document metadata: created time, updated time, applicable curriculum files, commit or review trace.
2. Add milestone grouping for Modules 0-14.
3. Add pass/fail rules for module exit and capstone.
4. Split metadata schema into required/recommended/optional fields.
5. Add operational examples for repeated seeds and bootstrap.
6. Add `allowed_conclusions` and `not_allowed_conclusions` to the experiment manifest.
7. Add `Insufficient evidence` as a valid report outcome.
8. Add basic detection annotation format/conversion prerequisite block.

## 14. Assessment Quality

Assessment quality is now **substantially improved**.

The rubrics are good enough to start designing lessons. The next missing layer is not another broad curriculum document. The next useful artifact should be either:

- a module template using these rules; or
- the first real lesson reviewed against these rules.

## 15. Final Score

- Technical correctness: **8.5/10**
- Conceptual depth: **8/10**
- Pedagogy: **8/10**
- Reasoning: **9/10**
- Experimental rigor: **8/10**
- Practical relevance: **8.5/10**
- Assessment alignment: **8/10**

Overall assessment: **8.3/10**

Final judgment:

```text
This readiness layer successfully fixes the major implementation-readiness gaps.
It is strong enough to guide lesson design, but should add metadata, milestone gates,
pass/fail rules, tiered metadata requirements, and stricter experiment conclusion rules
before becoming the final official implementation contract.
```
