import json  # 导入json模块，虽然本脚本未使用
import argparse  # 导入argparse模块，用于解析命令行参数
import pandas as pd  # 导入pandas库并简写为pd，用于数据处理

# 设置变量：配置特征列和标签列
def feature_label_split(df, features, labels):  # 定义函数，用于分离特征列和标签列
    """
    :param df:
    :param features: list 特征列
    :param label: str 标签列
    :return:
    """
    df_train = df[features]  # 从数据框中提取特征列，生成新的数据框df_train
    df_label = df[labels]  # 从数据框中提取标签列，生成新的数据框df_label
    return df_train, df_label  # 返回特征数据框和标签数据框


if __name__ == "__main__":  # 如果当前脚本作为主程序运行
    parser = argparse.ArgumentParser(description='Split features and labels from a dataset')  # 创建ArgumentParser对象，添加描述信息
    parser.add_argument('-i', '--input_path', type=str, required=True, help='Path to the input file')  # 添加输入文件路径参数
    parser.add_argument('-t', '--output_train_path', type=str, required=True, help='Base path to save the output files (e.g., features.parquet, labels.parquet)')  # 添加特征输出文件路径参数
    parser.add_argument('-l', '--labels_output_path', type=str, required=True, help='Base path to save the output files (e.g., features.parquet, labels.parquet)')  # 添加标签输出文件路径参数
    parser.add_argument('--features', type=str, required=True, help='Comma-separated list of feature column names')  # 添加特征列名参数
    parser.add_argument('--labels', type=str, required=True, help='Comma-separated list of label column names')  # 添加标签列名参数
    args = parser.parse_args()  # 解析命令行参数
    input_path = args.input_path  # 获取输入文件路径
    output_train_path = args.output_train_path  # 获取特征输出文件路径
    labels_output_path = args.labels_output_path  # 获取标签输出文件路径
    data_df = pd.read_csv(input_path)  # 读取输入的csv文件，生成DataFrame

    # 获取参数
    features = args.features  # 获取特征列参数
    labels = args.labels  # 获取标签列参数

    if features:features=eval(features)  # 如果特征列参数不为空，将其转为列表
    if labels:labels=eval(labels)  # 如果标签列参数不为空，将其转为列表

    # 执行特征与标签分离
    df_train, df_label = feature_label_split(data_df, features=features, labels=labels)  # 调用函数分离特征和标签

    df_train.to_csv(output_train_path, index=False)  # 将特征数据保存为csv文件
    df_label.to_csv(labels_output_path, index=False)  # 将标签数据保存为csv文件



