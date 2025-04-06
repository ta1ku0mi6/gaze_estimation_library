import pandas as pd
import matplotlib.pyplot as plt
import os
import japanize_matplotlib
import numpy as np

# 2つのCSVファイルを読み込み
file1 = 'output_ASDhead.csv'  # 最初のCSVファイルのパス
file2 = 'output_ASDleft.csv'  # 2番目のCSVファイルのパス

data1 = pd.read_csv(file1)
data2 = pd.read_csv(file2)

# FPSを定義
fps = 30

# time[s]を計算
data1['time'] = data1.index / fps
data2['time'] = data2.index / fps

angle1 = data1.iloc[:, 0]  # Measured Head
angle2 = data2.iloc[:, 0]  # Measured Gaze


# 保存ディレクトリ
save_dir = '../gaze_estimation_library/result(estimation_gaze)/ASD1/histogram/Measured Head - Measured Gaze_histogram/horizontal'
os.makedirs(save_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成

# ヒストグラム設定
bin_width = 5  # ビンの幅
range_min = -180  # 横軸の最小範囲
range_max = 180   # 横軸の最大範囲
bins = int((range_max - range_min) / bin_width)  # ビン数を計算

# 2つのデータの長さを短い方に揃える
min_length = min(len(angle1), len(angle2))
angle1 = angle1[:min_length]
angle2 = angle2[:min_length]

# 差分計算
angle_difference = angle1.values - angle2.values

# ヒストグラム作成
counts, edges = np.histogram(angle_difference, bins=bins, range=(range_min, range_max))
counts_in_seconds = counts / fps  # フレーム数を秒数に変換

plt.figure(figsize=(10, 6))
plt.bar(edges[:-1], counts_in_seconds, width=bin_width, color='blue', alpha=0.7, edgecolor='black')
    
    
# グラフ設定
plt.xlabel('Measured Head - Measured Gaze')
plt.ylabel('Second')
plt.title(f'ASD 水平方向の角度差（全体）')
plt.grid(True)
plt.xlim(range_min, range_max)  # 横軸の範囲を統一
plt.ylim(0, 260)  # 縦軸の最大値を統一

# ファイル名を生成して保存
filename = os.path.join(save_dir, f'ASD_hori_histogram_full.png')
plt.savefig(filename)
print(f"Saved histogram: {filename}")
plt.close()
