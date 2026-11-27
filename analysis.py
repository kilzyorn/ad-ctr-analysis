# -*- coding: utf-8 -*-
"""
Ad CTR 单维度分析：整体 / 性别 / 年龄 / 产品类别 / 城市等级
运行：python analysis.py
输出：ad_ctr_analysis_charts.png
"""
from pathlib import Path

import pandas as pd

BASE = Path(__file__).resolve().parent
df = pd.read_csv(BASE / 'train.csv')

# 查看数据
print(df.shape)      # 多少行多少列
print(df.head())     # 看前5行

# 整体点击率
ctr = df['is_click'].mean() * 100
print(f"整体点击率：{ctr:.2f}%")

# 点击和未点击各有多少人
print(df['is_click'].value_counts())

# 按性别分析点击率
gender_ctr = df.groupby('gender')['is_click'].mean() * 100
print("各性别点击率：")
print(gender_ctr.round(2))

# 按年龄层级分析点击率
age_ctr = df.groupby('age_level')['is_click'].mean() * 100
print("各年龄层点击率：")
print(age_ctr.round(2))

# 按产品类别分析点击率1
product_ctr = df.groupby('product_category_1')['is_click'].mean() * 100
print("各产品类别点击率1：")
print(product_ctr.round(2).sort_values(ascending=False))
# 2为1的子类别，暂时跳过

# 按城市发展等级分析点击率
city_ctr = df.groupby('city_development_index')['is_click'].mean() * 100
print("各城市等级点击率：")
print(city_ctr.round(2).sort_values(ascending=False))

import matplotlib.pyplot as plt

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 画年龄层点击率柱状图
age_ctr.plot(kind='bar', color='steelblue', figsize=(8, 5))
plt.title('各年龄层点击率')
plt.xlabel('年龄层')
plt.ylabel('点击率（%）')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 画一个2x2的图表组合
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# 图1：性别点击率
gender_ctr.plot(kind='bar', ax=axes[0, 0], color='steelblue')
axes[0, 0].set_title('性别 vs 点击率')
axes[0, 0].set_ylabel('点击率（%）')
axes[0, 0].tick_params(axis='x', rotation=0)

# 图2：年龄层点击率
age_ctr.plot(kind='bar', ax=axes[0, 1], color='coral')
axes[0, 1].set_title('年龄层 vs 点击率')
axes[0, 1].set_ylabel('点击率（%）')
axes[0, 1].tick_params(axis='x', rotation=0)

# 图3：产品类别点击率
product_ctr.plot(kind='bar', ax=axes[1, 0], color='green')
axes[1, 0].set_title('产品类别 vs 点击率')
axes[1, 0].set_ylabel('点击率（%）')
axes[1, 0].tick_params(axis='x', rotation=0)

# 图4：城市等级点击率
city_ctr.plot(kind='bar', ax=axes[1, 1], color='purple')
axes[1, 1].set_title('城市等级 vs 点击率')
axes[1, 1].set_ylabel('点击率（%）')
axes[1, 1].tick_params(axis='x', rotation=0)

plt.suptitle('广告点击率多维度分析', fontsize=14)
plt.tight_layout()
plt.savefig(BASE / 'ad_ctr_analysis_charts.png', dpi=150)
plt.show()

print("图表已保存！")
