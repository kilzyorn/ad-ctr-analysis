# Ad CTR Analysis | 广告点击率分析

## Project Overview
Analysis of 463,291 real advertising records to identify key factors affecting Click-Through Rate (CTR).

## Dataset
- Source: Kaggle - Ad Click Prediction Dataset
- Size: 463,291 rows × 15 columns
- Key variable: `is_click` (1 = clicked, 0 = not clicked)
- Files: `train.csv` (training set), `test.csv` (test set)

## Tools Used
- Python 3
- pandas
- matplotlib

## Key Findings
| Dimension | Finding |
|---|---|
| Overall CTR | 6.76% (31,331 / 463,291) |
| Gender | Male (6.79%) slightly higher than Female (6.44%), difference not significant |
| Age | U-shaped pattern — youngest (8.50%) and oldest (8.23%) click most, age 4 lowest (5.87%) |
| Product Category | Category 3 performs best (8.35%), 42% higher than Category 4 (5.89%) |
| City Level | Minimal impact, range only 6.53%–6.98% |
| Cross: Gender × Age | Young male (age 0) 10.00% vs young female 3.03%; older female (8.89%) > older male (7.83%) |
| Cross: Category × City | Category 3 in city level 2 peaks at 8.83%; Category 1 rises with city level (6.83% → 7.56%); Category 4 weakest everywhere |

## Files
| File | Description |
|---|---|
| `ad_ctr_analysis_report.pdf` | Full analysis report (includes single-dimension and cross analysis) |
| `ad_ctr_analysis_charts.png` | Visualization charts (gender / age / category / city) |
| `pivot_heatmap.png` | Pivot heatmaps (gender × age, category × city) |
| `train.csv` | Training data (463,291 × 15, 32.7 MB) |
| `test.csv` | Test data (9.0 MB) |

## Conclusion
Product category is the strongest predictor of CTR. Age shows a U-shaped relationship with CTR. Gender and city development level have minimal impact on their own, but cross analysis reveals young male users (10.00%) as the highest-value audience and Category 3 in tier-2 cities (8.83%) as the best combination. Prioritize young male and older female users, and Category 3 products in tier-2 cities.
