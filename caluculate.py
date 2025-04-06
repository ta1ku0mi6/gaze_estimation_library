# coding: utf-8
import pandas as pd
import numpy as np


# 入力と出力のファイルパス
input_file = '../gaze_estimation_library/input_csv/ASDhead_30fps.csv'  # 入力CSV
#input_file = '../gaze_estimation_library/input_csv/ASDleft_30fps.csv'  # 入力CSV
output_file = "output_ASDhead.csv"  # 出力CSV
#output_file = "output_ASDleft.csv"  # 出力CSV
#output_file = "output_TDhead.csv"  # 出力CSV
#output_file = "output_TDleft.csv"  # 出力CSV


# CSVデータの読み込み
data = pd.read_csv(input_file)

# 水平角と垂直角を計算する関数（度単位）
def calculate_angles(vec_x, vec_y, vec_z):
    horizontal = np.degrees(np.arctan2(vec_x, vec_z))  # 水平角
    vertical = np.degrees(np.arcsin(vec_y / np.sqrt(vec_x**2 + vec_y**2 + vec_z**2)))  # 垂直角
    return horizontal, vertical

# 方向ベクトルから水平角と垂直角を計算
angles = data[["vec_x", "vec_y", "vec_z"]].apply(
    lambda row: calculate_angles(row["vec_x"], row["vec_y"], row["vec_z"]),
    axis=1
)

# 結果をデータフレームに保存
angles_df = pd.DataFrame(angles.tolist(), columns=["horizontal", "vertical"])
angles_df["horizontal"] = angles_df["horizontal"].apply(lambda x: f"{x:.18e}")  
angles_df["vertical"] = angles_df["vertical"].apply(lambda x: f"{x:.18e}")  

# 新しいCSVファイルに保存
angles_df.to_csv(output_file, index=False, header=False)

print(f"Data saved:{output_file} ")