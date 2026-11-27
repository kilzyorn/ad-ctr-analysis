# -*- coding: utf-8 -*-
"""
Ad CTR 交叉分析：性别 × 年龄层、产品类别 × 城市等级 透视表与热力图
运行：python heatmap.py
输出：pivot_heatmap.png
"""
from pathlib import Path

import pandas as pd

BASE = Path(__file__).resolve().parent
df = pd.read_csv(BASE / 'train.csv')

# 透视表：性别 × 年龄层的点击率
pivot = df.pivot_table(
    values='is_click',
    index='gender',
    columns='age_level',
    aggfunc='mean'
) * 100

print("性别 × 年龄层点击率（%）：")
print(pivot.round(2))

# 透视表：产品类别 × 城市等级的点击率
pivot2 = df.pivot_table(
    values='is_click',
    index='product_category_1',
    columns='city_development_index',
    aggfunc='mean'
) * 100

print("产品类别 × 城市等级点击率（%）：")
print(pivot2.round(2))

import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 热力图1：性别 × 年龄层
sns.heatmap(pivot,
            annot=True,
            fmt='.1f',
            cmap='YlOrRd',
            ax=axes[0])
axes[0].set_title('性别 × 年龄层点击率（%）')

# 热力图2：产品类别 × 城市等级
sns.heatmap(pivot2,
            annot=True,
            fmt='.1f',
            cmap='YlOrRd',
            ax=axes[1])
axes[1].set_title('产品类别 × 城市等级点击率（%）')

plt.tight_layout()
plt.savefig(BASE / 'pivot_heatmap.png', dpi=150)
plt.show()
