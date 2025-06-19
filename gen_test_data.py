import pandas as pd
import numpy as np

# 1. deduplicate_rows.py 测试数据
dedup_df = pd.DataFrame({
    'id': np.random.randint(1, 21, 100),
    'name': np.random.choice(['A', 'B', 'C', 'D', 'E'], 100),
    'value': np.random.randint(10, 100, 100)
})
dedup_df.to_csv('deduplicate_rows.csv', index=False)

# 2. fillna_columns.py 测试数据
fillna_df = pd.DataFrame({
    'id': np.arange(1, 101),
    'score': np.where(np.random.rand(100) < 0.2, np.nan, np.random.randint(60, 100, 100)),
    'age': np.where(np.random.rand(100) < 0.2, np.nan, np.random.randint(18, 25, 100))
})
fillna_df.to_csv('fillna_columns.csv', index=False)

# 3. filter_rows.py 测试数据
filter_df = pd.DataFrame({
    'id': np.arange(1, 101),
    'category': np.random.choice(['A', 'B', 'C'], 100),
    'amount': np.random.randint(50, 500, 100)
})
filter_df.to_csv('filter_rows.csv', index=False)

# 4. merge_tables.py 测试数据
df_a = pd.DataFrame({
    'id': np.arange(1, 101),
    'name': np.random.choice(['A', 'B', 'C', 'D', 'E'], 100)
})
df_b = pd.DataFrame({
    'id': np.random.randint(1, 121, 100),
    'score': np.random.randint(60, 100, 100)
})
df_a.to_csv('merge_tables_a.csv', index=False)
df_b.to_csv('merge_tables_b.csv', index=False)

# 5. groupby_aggregate.py 测试数据
groupby_df = pd.DataFrame({
    'group': np.random.choice(['A', 'B', 'C', 'D'], 100),
    'subgroup': np.random.choice(['X', 'Y', 'Z'], 100),
    'value1': np.random.randint(10, 100, 100),
    'value2': np.random.randint(100, 1000, 100)
})
groupby_df.to_csv('groupby_aggregate.csv', index=False)

# 说明：
# 运行本脚本后，会在当前目录下生成5个csv文件，分别用于各功能脚本的测试。 