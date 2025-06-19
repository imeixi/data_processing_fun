import argparse  # 导入argparse模块，用于解析命令行参数
import pandas as pd  # 导入pandas库

# 按指定列合并两个表
def merge_tables(df1, df2, on_cols, how):
    """
    :param df1: 第一个DataFrame
    :param df2: 第二个DataFrame
    :param on_cols: list，合并的列名
    :param how: 合并方式（inner/left/right/outer）
    :return: 合并后的DataFrame
    """
    df_merged = pd.merge(df1, df2, on=on_cols, how=how)
    return df_merged

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='按指定列合并两个表')
    parser.add_argument('-a', '--input_a', type=str, required=True, help='第一个输入文件路径')
    parser.add_argument('-b', '--input_b', type=str, required=True, help='第二个输入文件路径')
    parser.add_argument('-o', '--output_path', type=str, required=True, help='输出文件路径')
    parser.add_argument('--on', type=str, required=True, help='逗号分隔的合并列名列表')
    parser.add_argument('--how', type=str, default='inner', help='合并方式：inner/left/right/outer，默认inner')
    args = parser.parse_args()
    input_a = args.input_a
    input_b = args.input_b
    output_path = args.output_path
    on_cols = args.on
    how = args.how

    if on_cols:
        on_cols = eval(on_cols)  # 转为列表

    df1 = pd.read_csv(input_a)
    df2 = pd.read_csv(input_b)
    df_merged = merge_tables(df1, df2, on_cols=on_cols, how=how)
    df_merged.to_csv(output_path, index=False)

    # 命令行执行示例：
    # python merge_tables.py -a data1.csv -b data2.csv -o merged.csv --on '["id"]' --how left 