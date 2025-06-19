import argparse  # 导入argparse模块，用于解析命令行参数
import pandas as pd  # 导入pandas库
import json

# 按指定列去重
def deduplicate_rows(df, subset_cols):
    """
    :param df: 输入的DataFrame
    :param subset_cols: list，指定去重的列名
    :return: 去重后的DataFrame
    """
    df_dedup = df.drop_duplicates(subset=subset_cols)
    return df_dedup

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='按指定列去重数据')
    parser.add_argument('-i', '--input_path', type=str, required=True, help='输入文件路径')
    parser.add_argument('-o', '--output_path', type=str, required=True, help='输出文件路径')
    parser.add_argument('--subset', type=str, required=True, help='逗号分隔的去重列名列表')
    args = parser.parse_args()
    input_path = args.input_path
    output_path = args.output_path
    subset = args.subset

    if subset:
        subset = subset.strip()
        # 兼容外层带引号的情况
        if (subset.startswith("'") and subset.endswith("'")) or (subset.startswith('"') and subset.endswith('"')):
            subset = subset[1:-1]
        print(f"subset参数实际内容: {repr(subset)}")  # 调试用
        try:
            subset = json.loads(subset)
        except json.JSONDecodeError:
            # 尝试修复无引号的情况，如 [id,name]
            if subset.startswith('[') and subset.endswith(']'):
                items = [item.strip() for item in subset[1:-1].split(',')]
                subset = items
                print(f"自动修正后的subset: {subset}")
            else:
                subset = eval(subset)  # 兜底方案（仅本地可信数据时可用）

    df = pd.read_csv(input_path)
    df_dedup = deduplicate_rows(df, subset_cols=subset)
    df_dedup.to_csv(output_path, index=False)

    # 命令行执行示例：
    # python deduplicate_rows.py -i data.csv -o deduped.csv --subset '["col1","col2"]' 