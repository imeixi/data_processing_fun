import argparse  # 导入argparse模块，用于解析命令行参数
import pandas as pd  # 导入pandas库

# 指定列缺失值填充
def fillna_columns(df, fill_cols, fill_value):
    """
    :param df: 输入的DataFrame
    :param fill_cols: list，指定填充的列名
    :param fill_value: 填充值或'mean'/'median'/'mode'
    :return: 填充后的DataFrame
    """
    for col in fill_cols:
        if fill_value == 'mean':
            df[col] = df[col].fillna(df[col].mean())
        elif fill_value == 'median':
            df[col] = df[col].fillna(df[col].median())
        elif fill_value == 'mode':
            df[col] = df[col].fillna(df[col].mode()[0])
        else:
            df[col] = df[col].fillna(fill_value)
    return df

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='指定列缺失值填充')
    parser.add_argument('-i', '--input_path', type=str, required=True, help='输入文件路径')
    parser.add_argument('-o', '--output_path', type=str, required=True, help='输出文件路径')
    parser.add_argument('--columns', type=str, required=True, help='逗号分隔的列名列表')
    parser.add_argument('--value', type=str, required=True, help='填充值或mean/median/mode')
    args = parser.parse_args()
    input_path = args.input_path
    output_path = args.output_path
    columns = args.columns
    value = args.value

    if columns:
        columns = eval(columns)  # 转为列表

    df = pd.read_csv(input_path)
    df_filled = fillna_columns(df, fill_cols=columns, fill_value=value)
    df_filled.to_csv(output_path, index=False)

    # 命令行执行示例：
    # python fillna_columns.py -i data.csv -o filled.csv --columns '["col1","col2"]' --value 0
    # python fillna_columns.py -i data.csv -o filled.csv --columns '["col1"]' --value mean 