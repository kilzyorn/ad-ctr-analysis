# -*- coding: utf-8 -*-
"""
Ad CTR Analysis | 广告点击率多维度分析
数据：Kaggle Ad Click Prediction（463,291 行 × 15 列）
运行：python analysis.py
输出：控制台统计表 + 广告分析报告.png
"""
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
DATA = BASE / 'Ad_click_prediction_train.csv'
OUT = BASE / '广告分析报告.png'

# 兼容 Windows / macOS 中文字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv(DATA)

# ---------------- 整体 ----------------
total = len(df)
clicks = int(df['is_click'].sum())
ctr = clicks / total * 100
print(f'样本量: {total:,}，点击: {clicks:,}，整体 CTR: {ctr:.2f}%')

def ctr_table(col):
    g = df.groupby(col)['is_click'].agg(['mean', 'size'])
    g['mean'] = (g['mean'] * 100).round(2)
    g.columns = ['CTR(%)', '样本数']
    return g

for col in ['gender', 'age_level', 'product_category_1', 'city_development_index']:
    print(f'\n===== {col} =====')
    print(ctr_table(col).to_string())

# ---------------- 可视化 ----------------
gender = ctr_table('gender').reindex(['Female', 'Male'])
age = ctr_table('age_level')
prod = ctr_table('product_category_1')
city = ctr_table('city_development_index')

fig, axes = plt.subplots(2, 2, figsize=(14, 9))
fig.suptitle(f'广告点击率多维度分析（整体 CTR = {ctr:.2f}%）', fontsize=16)

axes[0, 0].bar(gender.index, gender['CTR(%)'], color='#4C8CBF')
axes[0, 0].set_title('性别 vs 点击率')
axes[0, 0].set_xlabel('gender')
axes[0, 0].set_ylabel('点击率 (%)')

axes[0, 1].bar(age.index.astype(str), age['CTR(%)'], color='#FF8C5A')
axes[0, 1].set_title('年龄层 vs 点击率')
axes[0, 1].set_xlabel('age_level')
axes[0, 1].set_ylabel('点击率 (%)')

axes[1, 0].bar(prod.index.astype(str), prod['CTR(%)'], color='green')
axes[1, 0].set_title('产品类别 vs 点击率')
axes[1, 0].set_xlabel('product_category_1')
axes[1, 0].set_ylabel('点击率 (%)')

axes[1, 1].bar(city.index.astype(str), city['CTR(%)'], color='purple')
axes[1, 1].set_title('城市等级 vs 点击率')
axes[1, 1].set_xlabel('city_development_index')
axes[1, 1].set_ylabel('点击率 (%)')

for ax in axes.flat:
    ax.grid(axis='y', alpha=0.25)

plt.tight_layout()
plt.savefig(OUT, dpi=200, bbox_inches='tight')
print(f'\n图表已保存: {OUT}')
