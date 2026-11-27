# Ad CTR Analysis | 广告点击率分析

## Project Overview
Analysis of 463,291 real advertising records to identify key factors affecting Click-Through Rate (CTR).

## Dataset
- Source: Kaggle - Ad Click Prediction Dataset
- Size: 463,291 rows × 15 columns
- Key variable: `is_click` (1 = clicked, 0 = not clicked)

## Tools Used
- Python 3
- pandas
- matplotlib

## Key Findings
| Dimension | Finding |
|---|---|
| Overall CTR | 6.76% |
| Gender | Male (6.79%) slightly higher than Female (6.44%), difference not significant |
| Age | U-shaped pattern — youngest and oldest users click most |
| Product Category | Category 3 performs best (8.35%), 42% higher than lowest |
| City Level | Minimal impact, range only 0.45% |

## Files
| File | Description |
|---|---|
| `analysis.py` | Main analysis code |
| `广告分析报告.png` | Visualization charts |
| `ad_ctr_analysis_report.pdf` | Full analysis report |
| `Ad_click_prediction_train.csv` | Training data (463,291 × 15) |

## Reproduce
```bash
python analysis.py
```

## Conclusion
Product category is the strongest predictor of CTR. Age shows a U-shaped relationship with CTR. Gender and city development level have minimal impact on click behavior.
