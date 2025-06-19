import argparse  # 导入argparse模块，用于解析命令行参数
import pandas as pd  # 导入pandas库

# 按列分组并聚合
def groupby_aggregate(df, group_cols, agg_dict):
    """
    :param df: 输入的DataFrame
    :param group_cols: list，分组列名
    :param agg_dict: dict，聚合列及方法，如{"col1": "sum", "col2": "mean"}
    :return: 聚合后的DataFrame
    """
    df_agg = df.groupby(group_cols).agg(agg_dict).reset_index()
    return df_agg

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='按列分组并聚合')
    parser.add_argument('-i', '--input_path', type=str, required=True, help='输入文件路径')
    parser.add_argument('-o', '--output_path', type=str, required=True, help='输出文件路径')
    parser.add_argument('--groupby', type=str, required=True, help='逗号分隔的分组列名列表')
    parser.add_argument('--agg', type=str, required=True, help='聚合字典，如{"col1": "sum", "col2": "mean"}')
    args = parser.parse_args()
    input_path = args.input_path
    output_path = args.output_path
    groupby = args.groupby
    agg = args.agg

    if groupby:
        groupby = eval(groupby)  # 转为列表
    if agg:
        agg = eval(agg)  # 转为字典

    df = pd.read_csv(input_path)
    df_agg = groupby_aggregate(df, group_cols=groupby, agg_dict=agg)
    df_agg.to_csv(output_path, index=False)

    # 命令行执行示例：
    # python groupby_aggregate.py -i data.csv -o agg.csv --groupby '["col1"]' --agg '{"col2": "sum", "col3": "mean"}' 