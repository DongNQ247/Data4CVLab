# Data-Centric Object Detection Curriculum

Tài liệu này mô tả chương trình đào tạo tổng thể trước khi triển khai từng bài học chi tiết. Mục tiêu không phải là học thật nhiều model, mà là xây dựng năng lực giải quyết một bài toán Object Detection thực tế theo vòng lặp:

```text
Problem -> Data -> Experiment -> Evaluation -> Explanation -> Iteration
```

## 1. Mục Tiêu Đào Tạo

Sau chương trình, người học cần có khả năng nhận một yêu cầu thực tế như:

```text
Xây dựng hệ thống phát hiện công nhân và mũ bảo hộ từ camera công trường.
```

Và tự thiết kế được:

- problem definition;
- detection ontology;
- annotation policy;
- data collection strategy;
- dataset schema;
- annotation QA;
- dataset audit;
- distribution analysis;
- train/validation/test split;
- baseline model;
- evaluation protocol;
- failure taxonomy;
- error analysis;
- data intervention;
- model intervention;
- controlled experiment;
- dataset iteration;
- final evaluation;
- production monitoring strategy.

Người học phải giải thích được vì sao mỗi quyết định được đưa ra.

## 2. Đối Tượng Và Prerequisites

Chương trình phù hợp với người học muốn đi theo hướng:

- Applied Computer Vision Engineer;
- ML Engineer chuyên về Vision;
- Data-Centric AI Engineer;
- Dataset Engineer;
- Applied Research Engineer;
- Computer Vision Research Engineer;
- ML Evaluation Engineer.

Prerequisites tối thiểu:

- biết Python cơ bản;
- biết dùng notebook hoặc script Python;
- hiểu array/matrix ở mức cơ bản;
- biết đọc biểu đồ đơn giản;
- chưa cần biết sâu về deep learning hoặc object detection.

Các kiến thức thiếu sẽ được bổ sung theo thứ tự từ foundation đến applied research.

## 3. Nguyên Tắc Thiết Kế Chương Trình

Chương trình được thiết kế theo các nguyên tắc:

- dữ liệu là thành phần trung tâm, không phải phần phụ của model training;
- model architecture vẫn quan trọng, nhưng không phải điểm bắt đầu mặc định;
- mọi experiment cần có hypothesis, baseline, control và interpretation;
- evaluation không dừng ở một con số mAP;
- error analysis là một phần của vòng lặp học và cải thiện;
- mỗi chương phải tạo ra artifact cụ thể: notebook, script, report, policy, config hoặc experiment record.

Working rule trong repo:

```text
Explore in notebook.
Stabilize into src/.
Run with scripts/.
Report in reports/.
```

## 4. Cấu Trúc Tổng Thể

Chương trình gồm 10 chương:

1. Foundations of Computer Vision and Images
2. Object Detection Fundamentals
3. Dataset Fundamentals for Detection
4. Ontology and Annotation Policy
5. Dataset Engineering and Curation
6. Dataset Analysis and Dataset Reports
7. Baseline Modeling and Model-Dataset Interaction
8. Evaluation Protocols and Metrics
9. Error Analysis and Dataset Iteration
10. Advanced Data-Centric AI and Applied Research

Mỗi chương gồm nhiều bài học. Mỗi bài nên có:

- motivation;
- intuition;
- formal definition;
- math nếu cần;
- visualization;
- real-world example;
- Python hoặc dataset experiment;
- critical-thinking questions;
- assignment;
- expected artifact.

## 5. Chapter 1: Foundations of Computer Vision and Images

Mục tiêu: giúp người học hiểu ảnh là dữ liệu số, không phải chỉ là thứ nhìn bằng mắt người.

### Lesson 1.1: What Is Computer Vision?

Nội dung:

- computer vision là gì;
- classification, detection, segmentation khác nhau thế nào;
- vì sao visual perception của người và model khác nhau;
- vai trò của domain, camera, ánh sáng, context.

Artifact:

- short note trong `docs/curriculum/`;
- notebook minh họa các loại task vision.

Assignment:

- chọn một bài toán thực tế và phân loại xem nó là classification, detection, segmentation hay multi-task.

### Lesson 1.2: Image Representation

Nội dung:

- pixel, channel, resolution;
- RGB vs grayscale;
- image as tensor;
- coordinate system trong ảnh;
- resize, crop, padding và ảnh hưởng đến annotation.

Artifact:

- notebook đọc ảnh, inspect shape, visualize channel.

Assignment:

- lấy một ảnh, resize nhiều tỉ lệ và giải thích điều gì xảy ra với object.

### Lesson 1.3: Visual Data Quality

Nội dung:

- blur;
- low light;
- overexposure;
- compression artifacts;
- motion blur;
- camera angle;
- weather/domain conditions.

Artifact:

- notebook tạo một mini image-quality checklist.

Assignment:

- phân loại 20 ảnh thành các nhóm quality issue.

## 6. Chapter 2: Object Detection Fundamentals

Mục tiêu: hiểu object detection bằng các thành phần cơ bản trước khi dùng framework.

### Lesson 2.1: Object, Class, Instance

Nội dung:

- object vs background;
- class vs instance;
- object boundary ambiguity;
- class granularity;
- multi-label và hierarchical class.

Artifact:

- ontology draft nhỏ cho một bài toán thực tế.

Assignment:

- định nghĩa 3 class và 5 ambiguous cases cho một detection problem.

### Lesson 2.2: Bounding Boxes

Nội dung:

- bbox format: `xyxy`, `xywh`, normalized vs absolute;
- coordinate convention;
- visible box vs full object box;
- bbox tightness;
- annotation consistency.

Artifact:

- notebook vẽ bbox lên ảnh.

Assignment:

- so sánh 3 annotation policy khác nhau cho object bị che khuất.

### Lesson 2.3: IoU

Nội dung:

- intersection, union;
- IoU formula;
- IoU threshold;
- localization quality;
- vì sao IoU cao/thấp ảnh hưởng đến metric.

Artifact:

- notebook `01_image_bbox_iou.ipynb`.

Assignment:

- thay đổi predicted box và quan sát IoU.

### Lesson 2.4: Prediction, Confidence, NMS

Nội dung:

- model prediction gồm class, box, confidence;
- threshold;
- duplicate detection;
- non-maximum suppression;
- tradeoff giữa precision và recall.

Artifact:

- notebook mô phỏng NMS bằng boxes giả lập.

Assignment:

- giải thích khi nào giảm confidence threshold là hợp lý và khi nào nguy hiểm.

## 7. Chapter 3: Dataset Fundamentals for Detection

Mục tiêu: hiểu dataset detection gồm những thành phần nào và vì sao annotation là một quyết định kỹ thuật.

### Lesson 3.1: Dataset Anatomy

Nội dung:

- image;
- object instance;
- annotation;
- metadata;
- split;
- dataset version;
- dataset card/report.

Artifact:

- template dataset card.

Assignment:

- mô tả một dataset detection bằng các thành phần trên.

### Lesson 3.2: Annotation Formats

Nội dung:

- COCO;
- YOLO;
- Pascal VOC;
- conversion risks;
- category id;
- image id;
- bbox coordinate conventions.

Artifact:

- script hoặc notebook đọc annotation mẫu.

Assignment:

- convert 5 annotation giả lập giữa `xyxy` và `xywh`.

### Lesson 3.3: Positive, Negative, and Ignore Samples

Nội dung:

- positive image;
- negative image;
- hard negative;
- ignore region;
- unlabeled object risk;
- effect on false positives and false negatives.

Artifact:

- annotation policy section cho negative/ignore cases.

Assignment:

- thiết kế negative sample strategy cho helmet detection.

## 8. Chapter 4: Ontology and Annotation Policy

Mục tiêu: biết biến yêu cầu business thành ontology và annotation policy có thể dùng cho annotator và evaluator.

### Lesson 4.1: Problem Definition

Nội dung:

- user objective;
- production context;
- allowed mistakes;
- operating conditions;
- real-world cost of FP/FN;
- metric alignment.

Artifact:

- problem-definition document.

Assignment:

- viết problem definition cho một bài toán traffic surveillance.

### Lesson 4.2: Detection Ontology

Nội dung:

- class definition;
- inclusion/exclusion criteria;
- class hierarchy;
- ambiguous labels;
- granularity tradeoffs.

Artifact:

- `docs/ontology/<project>_ontology.md`.

Assignment:

- thiết kế ontology cho `worker`, `helmet`, `no_helmet`, `vest`.

### Lesson 4.3: Bounding-Box Policy

Nội dung:

- visible region vs full extent;
- occlusion;
- truncation;
- reflection;
- crowd;
- tiny objects;
- partially visible objects.

Artifact:

- `docs/annotation_policy/<project>_annotation_policy.md`.

Assignment:

- viết rule cho 10 edge cases.

### Lesson 4.4: Annotation QA

Nội dung:

- inter-annotator agreement;
- review workflow;
- spot check;
- missing-label detection;
- label consistency;
- quality acceptance criteria.

Artifact:

- QA checklist.

Assignment:

- thiết kế quy trình review 1,000 ảnh với ngân sách hạn chế.

## 9. Chapter 5: Dataset Engineering and Curation

Mục tiêu: biết thu thập, lọc, tổ chức, làm sạch và version dataset.

### Lesson 5.1: Data Collection Strategy

Nội dung:

- target distribution;
- sampling frame;
- camera/source diversity;
- temporal diversity;
- rare cases;
- privacy and licensing;
- collection bias.

Artifact:

- data collection plan.

Assignment:

- đề xuất sampling strategy cho CCTV công trường.

### Lesson 5.2: Dataset Split Design

Nội dung:

- random split vs group split;
- video/frame leakage;
- scene leakage;
- camera leakage;
- time-based split;
- validation vs test purpose.

Artifact:

- split policy.

Assignment:

- phân tích vì sao random split frame từ cùng video có thể làm metric ảo.

### Lesson 5.3: Cleaning and Curation

Nội dung:

- corrupted images;
- duplicates;
- near-duplicates;
- annotation inconsistencies;
- out-of-scope data;
- curation logs.

Artifact:

- dataset cleaning checklist;
- script skeleton cho audit.

Assignment:

- thiết kế rule loại bỏ ảnh không phù hợp mà không làm mất rare cases.

### Lesson 5.4: Dataset Versioning and Lineage

Nội dung:

- dataset version;
- source lineage;
- annotation version;
- split version;
- reproducibility;
- changelog.

Artifact:

- dataset version template.

Assignment:

- mô tả sự khác nhau giữa dataset v1 và v2 sau một data intervention.

## 10. Chapter 6: Dataset Analysis and Dataset Reports

Mục tiêu: biến dataset thành một đối tượng có thể đo lường, phân tích và báo cáo.

### Lesson 6.1: Class and Instance Distribution

Nội dung:

- image count;
- object count;
- class imbalance;
- images per class;
- instances per image;
- long-tail distribution.

Artifact:

- notebook phân tích class distribution.

Assignment:

- giải thích rủi ro của một dataset có 90% object thuộc một class.

### Lesson 6.2: Object Size and Aspect Ratio

Nội dung:

- bbox area;
- relative object size;
- small/medium/large objects;
- aspect ratio;
- anchor/model implications;
- resolution implications.

Artifact:

- histogram size/aspect ratio.

Assignment:

- quyết định khi nào tăng image resolution có thể hữu ích.

### Lesson 6.3: Spatial and Context Distribution

Nội dung:

- object center heatmap;
- object position bias;
- context correlation;
- background shortcuts;
- camera viewpoint.

Artifact:

- spatial distribution plot.

Assignment:

- phân tích rủi ro nếu helmet luôn nằm gần trung tâm ảnh trong train set.

### Lesson 6.4: Dataset Quality Report

Nội dung:

- report structure;
- evidence;
- risks;
- recommended actions;
- limitations.

Artifact:

- `reports/dataset_reports/<dataset>_quality_report.md`.

Assignment:

- viết dataset report ngắn từ một dataset mẫu.

## 11. Chapter 7: Baseline Modeling and Model-Dataset Interaction

Mục tiêu: dùng model như một công cụ kiểm tra dataset và tạo baseline có thể so sánh.

### Lesson 7.1: What Is a Baseline?

Nội dung:

- baseline purpose;
- simple but credible baseline;
- pretrained detector;
- fixed config;
- reproducibility;
- what baseline can and cannot prove.

Artifact:

- baseline experiment plan.

Assignment:

- thiết kế baseline cho một dataset nhỏ và nói rõ điều gì sẽ không kết luận được.

### Lesson 7.2: Transfer Learning and Fine-Tuning

Nội dung:

- pretrained weights;
- domain gap;
- freezing vs fine-tuning;
- learning rate;
- epochs;
- overfitting;
- augmentation.

Artifact:

- training config template.

Assignment:

- giải thích khi nào fine-tuning thất bại do dataset chứ không phải model.

### Lesson 7.3: Image Resolution and Augmentation

Nội dung:

- resolution vs small objects;
- augmentation as distribution design;
- harmful augmentation;
- preserving annotation validity.

Artifact:

- controlled ablation plan.

Assignment:

- chọn 3 augmentation phù hợp và 2 augmentation nguy hiểm cho CCTV.

### Lesson 7.4: Thresholds and Inference Behavior

Nội dung:

- confidence threshold;
- NMS threshold;
- precision/recall tradeoff;
- operating point;
- production objective.

Artifact:

- threshold sweep notebook.

Assignment:

- chọn operating point cho use case ưu tiên recall.

## 12. Chapter 8: Evaluation Protocols and Metrics

Mục tiêu: đánh giá model theo cách phản ánh đúng bài toán, không chỉ nhìn mAP tổng.

### Lesson 8.1: Precision, Recall, FP, FN

Nội dung:

- true positive;
- false positive;
- false negative;
- confidence threshold;
- business cost of errors.

Artifact:

- notebook mô phỏng confusion cases cho detection.

Assignment:

- giải thích vì sao một hệ thống safety thường ưu tiên recall.

### Lesson 8.2: AP, mAP, AP50, AP75

Nội dung:

- precision-recall curve;
- average precision;
- mean average precision;
- IoU thresholds;
- AP50 vs AP75 interpretation.

Artifact:

- metric explainer notebook.

Assignment:

- phân tích trường hợp AP50 cao nhưng AP75 thấp.

### Lesson 8.3: Class-Wise and Condition-Wise Evaluation

Nội dung:

- class-wise AP;
- small/medium/large;
- lighting;
- occlusion;
- blur;
- camera/site;
- subgroup performance.

Artifact:

- evaluation report template.

Assignment:

- thiết kế bảng evaluation cho helmet detection theo điều kiện ánh sáng và occlusion.

### Lesson 8.4: Evaluation Leakage and Metric Trust

Nội dung:

- duplicate leakage;
- near-duplicate leakage;
- video frame leakage;
- test-set contamination;
- tuning on test;
- metric overconfidence.

Artifact:

- leakage checklist.

Assignment:

- xác định 5 cách một detection benchmark nội bộ có thể bị leakage.

## 13. Chapter 9: Error Analysis and Dataset Iteration

Mục tiêu: biến lỗi model thành hypothesis và data/model intervention có thể kiểm chứng.

### Lesson 9.1: Failure Taxonomy

Nội dung:

- false positive categories;
- false negative categories;
- localization error;
- duplicate error;
- wrong class;
- background confusion;
- missing labels.

Artifact:

- failure taxonomy document.

Assignment:

- phân loại 30 lỗi inference thành nhóm có nguyên nhân rõ ràng.

### Lesson 9.2: Quantifying Failure Modes

Nội dung:

- error count;
- error rate;
- class-wise failure;
- condition-wise failure;
- severity ranking;
- confidence distribution.

Artifact:

- failure summary table.

Assignment:

- chọn top 3 failure modes cần xử lý trước và giải thích tradeoff.

### Lesson 9.3: Hypothesis and Intervention

Nội dung:

- data intervention;
- model intervention;
- annotation intervention;
- evaluation intervention;
- smallest useful change;
- controlled comparison.

Artifact:

- intervention proposal.

Assignment:

- viết hypothesis cho lỗi small-object false negative và thiết kế experiment kiểm chứng.

### Lesson 9.4: Dataset v2 and Re-Evaluation

Nội dung:

- targeted data collection;
- hard-negative mining;
- annotation correction;
- dataset v2;
- before/after evaluation;
- avoiding regressions.

Artifact:

- experiment report so sánh v1 vs v2.

Assignment:

- thiết kế dataset iteration dựa trên 3 failure modes.

## 14. Chapter 10: Advanced Data-Centric AI and Applied Research

Mục tiêu: chuyển từ thực hành cơ bản sang các phương pháp nâng cao và tư duy nghiên cứu ứng dụng.

### Lesson 10.1: Hard Negative Mining

Nội dung:

- hard negatives;
- false positive reduction;
- sampling strategy;
- overfitting to hard cases;
- evaluation after mining.

Artifact:

- hard-negative mining experiment plan.

Assignment:

- thiết kế mining loop cho background bị nhầm thành helmet.

### Lesson 10.2: Active Learning

Nội dung:

- annotation budget;
- uncertainty sampling;
- diversity sampling;
- model-assisted selection;
- random sampling baseline.

Artifact:

- active learning comparison plan.

Assignment:

- so sánh random sampling vs uncertainty sampling với cùng 500 ảnh annotation budget.

### Lesson 10.3: Synthetic Data and Domain Adaptation

Nội dung:

- synthetic data purpose;
- domain gap;
- simulation bias;
- style mismatch;
- validation on real data;
- domain adaptation overview.

Artifact:

- synthetic data risk assessment.

Assignment:

- nêu điều kiện để synthetic data có thể cải thiện small-object recall.

### Lesson 10.4: Applied Research Design

Nội dung:

- research question;
- hypothesis;
- baseline;
- control;
- ablation;
- reproducibility;
- interpretation;
- research writing.

Artifact:

- mini research proposal.

Assignment:

- viết proposal: "Can targeted data collection outperform random collection for helmet detection?"

## 15. Project Track

Chương trình nên duy trì song song hai track thực hành.

### Track A: Benchmark Dataset

Mục đích:

- hiểu format chuẩn;
- hiểu benchmark metrics;
- làm quen với COCO-style annotation;
- so sánh với expected behavior của pretrained models.

Dataset đề xuất:

- COCO subset;
- hoặc dataset nhỏ có COCO annotation.

Artifact:

- benchmark dataset reader;
- dataset report;
- baseline evaluation.

### Track B: Real-World Dataset

Mục đích:

- thực hành toàn bộ data-centric loop;
- học ontology, annotation policy, curation và error analysis trong tình huống gần production.

Dataset đề xuất:

- helmet detection;
- worker/person detection;
- traffic object detection;
- industrial defect detection;
- agriculture object detection.

Artifact:

- problem definition;
- ontology;
- annotation policy;
- dataset report;
- baseline model;
- evaluation report;
- error analysis report;
- dataset v2 experiment.

## 16. Suggested Repository Mapping

Khi triển khai từng bài, nên map artifact vào repo như sau:

```text
docs/curriculum/
  data_centric_object_detection_curriculum.md
  lesson_plan_<chapter>_<lesson>.md

docs/ontology/
  <project>_ontology.md

docs/annotation_policy/
  <project>_annotation_policy.md

notebooks/
  01_cv_fundamentals/
  02_object_detection_fundamentals/
  03_dataset_fundamentals/
  04_ontology_annotation_policy/
  05_dataset_engineering/
  06_dataset_analysis/
  07_baseline_modeling/
  08_evaluation/
  09_error_analysis/
  10_advanced_data_centric_ai/

src/data4cvlab/
  datasets/
  analysis/
  visualization/
  training/
  evaluation/
  utils/

scripts/
  audit_dataset.py
  visualize_samples.py
  convert_annotations.py
  train_baseline.py
  evaluate_predictions.py

reports/
  dataset_reports/
  experiment_reports/
  error_analysis/
```

## 17. Milestone Plan

### Milestone 1: Foundation Readiness

Chapters:

- Chapter 1;
- Chapter 2.

Expected capability:

- người học hiểu image, bbox, IoU, prediction, confidence, FP/FN ở mức nền tảng.

Deliverables:

- 3-5 notebooks;
- short assignments;
- bbox/IoU visualization utilities.

### Milestone 2: Dataset Design Readiness

Chapters:

- Chapter 3;
- Chapter 4;
- Chapter 5.

Expected capability:

- người học có thể viết ontology, annotation policy và dataset split strategy.

Deliverables:

- ontology document;
- annotation policy;
- dataset card;
- split policy;
- QA checklist.

### Milestone 3: Dataset Analysis Readiness

Chapters:

- Chapter 6.

Expected capability:

- người học có thể đọc annotation, phân tích distribution, phát hiện bias/leakage risk và viết dataset report.

Deliverables:

- dataset audit notebook;
- reusable analysis code;
- dataset quality report.

### Milestone 4: Baseline and Evaluation Readiness

Chapters:

- Chapter 7;
- Chapter 8.

Expected capability:

- người học có thể train/fine-tune baseline, chọn metric phù hợp và đọc evaluation theo class/condition.

Deliverables:

- baseline config;
- training script;
- evaluation report;
- threshold sweep analysis.

### Milestone 5: Iteration and Applied Research Readiness

Chapters:

- Chapter 9;
- Chapter 10.

Expected capability:

- người học có thể biến failure modes thành hypothesis, intervention và controlled experiment.

Deliverables:

- failure taxonomy;
- error analysis report;
- dataset v2 plan;
- applied research proposal.

## 18. First Implementation Recommendation

Không nên bắt đầu bằng training model. Nên bắt đầu bằng foundation và dataset thinking:

1. Hoàn thiện Chapter 1 và Chapter 2 dưới dạng notebook ngắn.
2. Tạo project giả lập hoặc dataset nhỏ cho helmet detection.
3. Viết ontology và annotation policy trước khi train.
4. Sau đó mới xây dataset audit tool và baseline model.

Thứ tự bài đầu tiên nên là:

```text
Chapter 1.2: Image Representation
Chapter 2.2: Bounding Boxes
Chapter 2.3: IoU
Chapter 3.1: Dataset Anatomy
Chapter 4.1: Problem Definition
```

Lý do: nếu chưa hiểu ảnh, bbox, IoU, dataset anatomy và problem definition, người học sẽ dễ biến object detection thành bài tập chạy framework thay vì một quy trình engineering có kiểm soát.
