import argparse  # 导入argparse模块，用于解析命令行参数
import pandas as pd  # 导入pandas库

# 按条件筛选行
def filter_rows(df, query_str):
    """
    :param df: 输入的DataFrame
    :param query_str: 查询条件字符串（pandas query语法）
    :return: 筛选后的DataFrame
    """
    df_filtered = df.query(query_str)
    return df_filtered

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='按条件筛选行')
    parser.add_argument('-i', '--input_path', type=str, required=True, help='输入文件路径')
    parser.add_argument('-o', '--output_path', type=str, required=True, help='输出文件路径')
    parser.add_argument('--query', type=str, required=True, help='筛选条件（pandas query语法）')
    args = parser.parse_args()
    input_path = args.input_path
    output_path = args.output_path
    query = args.query

    df = pd.read_csv(input_path)
    df_filtered = filter_rows(df, query_str=query)
    df_filtered.to_csv(output_path, index=False)

    # 命令行执行示例：
    # python filter_rows.py -i data.csv -o filtered.csv --query 'col1 > 10 and col2 == "A"' 