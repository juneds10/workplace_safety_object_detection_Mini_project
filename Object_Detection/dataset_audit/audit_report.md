# SH17 Dataset Audit Report

- Dataset: `/Users/junedshaikh/Downloads/archive-3`
- Images found: **8,099**
- Label formats found: **labels, voc_labels**
- Label format used for counts: **YOLO**
- Annotation objects counted: **75,994**
- Invalid/unreadable annotation rows: **2**
- Invalid boxes in counted labels: **0**
- Images missing a matching label file: **0**
- Label files without a matching image: **0**
- Train/validation overlap by filename stem: **0**

## Main class counts

| Class | Objects |
|---|---:|
| person | 13,802 |
| ear | 7,730 |
| ear-mufs | 318 |
| face | 8,950 |
| face-guard | 134 |
| face-mask-medical | 670 |
| foot | 759 |
| tools | 4,647 |
| glasses | 1,945 |
| gloves | 2,790 |
| helmet | 927 |
| hands | 15,850 |
| head | 11,985 |
| medical-suit | 157 |
| shoes | 4,560 |
| safety-suit | 240 |
| safety-vest | 530 |

## Helmet / vest / person analysis

| Class | Objects | Images containing class | Median box area (fraction of image) | Boxes under 1% image area |
|---|---:|---:|---:|---:|
| helmet | 927 | 466 | 0.00251 | 663 (71.52%) |
| person | 13,802 | 7,617 | 0.19510 | 1,943 (14.08%) |
| safety-vest | 530 | 213 | 0.00519 | 323 (60.94%) |

## Train/validation split

- `train_files.txt`: 6,479 entries; 6,479 unique filename stems; 0 stems not found in images.
- `val_files.txt`: 1,620 entries; 1,620 unique filename stems; 0 stems not found in images.

## Output files

- `class_distribution.csv` — counts for all classes
- `focus_class_analysis.csv` — person, helmet and vest summary
- `class_cooccurrence.csv` — image-level class co-occurrence
- `bounding_boxes.csv` — per-box sizes and validity
- `audit_summary.json` — full machine-readable summary
- `audit_report.md` — this report

## Interpretation cautions

- Co-occurrence does not establish that a particular worker is wearing PPE.
- A missing label file can indicate unlabeled data, a different annotation layout, or a matching-name issue; inspect examples before deciding it is an error.
- Use the dataset's official train/validation split if it is verified and leakage-free.
