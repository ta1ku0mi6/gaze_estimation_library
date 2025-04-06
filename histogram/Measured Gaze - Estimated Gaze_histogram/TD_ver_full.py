import japanize_matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# 2つのCSVファイルを読み込み
file1 = 'output_TDleft.csv'  # 最初のCSVファイルのパス
file3 = '../gaze_estimation_library/result(transformation)/estimated_gaze_TDhead.csv'

data1 = pd.read_csv(file1)
data3 = pd.read_csv(file3)

# FPSを定義
fps = 30

# time[s]を計算
data1['time'] = data1.index / fps
data3['time'] = data3.index / fps
shifted_time3 = data3['time'] + 0.7

angle1 = data1.iloc[:, 1]  # 最初のCSVの角度データ
angle3 = data3.iloc[:, 1]  # 推定視線データ

# 保存ディレクトリ
save_dir = '../gaze_estimation_library/result(estimation_gaze)/TD1/histogram/Measured Gaze - Estimated Gaze_histogram/vertical'
os.makedirs(save_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成

# ヒストグラム設定
bin_width = 5  # ビンの幅
range_min = -180  # 横軸の最小範囲
range_max = 180   # 横軸の最大範囲
bins = int((range_max - range_min) / bin_width)  # ビン数を計算

# データ長を短い方に合わせる
min_length = min(len(angle1), len(angle3))
angle1 = angle1.iloc[:min_length]
angle3 = angle3.iloc[:min_length]
shifted_time3 = shifted_time3.iloc[:min_length]

# 差を計算
angle_difference = angle1.values - angle3.values

# ヒストグラムを作成
counts, edges = np.histogram(angle_difference, bins=bins, range=(range_min, range_max))
counts_in_seconds = counts / fps  # フレーム数を秒数に変換

# 新しいプロット作成
plt.figure(figsize=(10, 6))
plt.bar(edges[:-1], counts_in_seconds, width=bin_width, color='blue', alpha=0.7, edgecolor='black')

# グラフ設定
plt.xlabel('Measured Gaze - Estimated Gaze (deg)')
plt.ylabel('Second')
plt.title('TD 垂直方向の角度差（全体）')
plt.grid(True)
plt.xlim(range_min, range_max)  # 横軸の範囲を統一
plt.ylim(0, 260)  # 縦軸を適切に設定

# ファイル名を生成して保存
filename = os.path.join(save_dir, 'TD_ver_histogram_full.png')
plt.savefig(filename)
print(f"Saved histogram: {filename}")
plt.show()
