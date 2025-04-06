import japanize_matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# 2つのCSVファイルを読み込み
file1 = 'output_ASDleft.csv'  # 最初のCSVファイルのパス
file3 = '../gaze_estimation_library/result(transformation)/estimated_gaze_ASDhead.csv'

data1 = pd.read_csv(file1)
data3 = pd.read_csv(file3)

# FPSを定義
fps = 30

# time[s]を計算
data1['time'] = data1.index / fps
data3['time'] = data3.index / fps
shifted_time3 = data3['time'] + 0.7

angle1 = data1.iloc[:, 0]  # 最初のCSVの角度データ
angle3 = data3.iloc[:, 0]  # 推定視線データ

# 保存ディレクトリ
save_dir = '../gaze_estimation_library/result(estimation_gaze)/ASD1/histogram/Measured Gaze - Estimated Gaze_histogram/horizontal'
os.makedirs(save_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成

# ヒストグラム設定

bin_width = 5  # ビンの幅
range_min = -180  # 横軸の最小範囲
range_max = 180   # 横軸の最大範囲
bins = int((range_max - range_min) / bin_width)  # ビン数を計算
duration = 30     # 各グラフでの時間範囲（秒）

# 30秒毎のデータをヒストグラムにプロット
start = 0
end = 640



for start in range(0, end, duration):
    # 各30秒範囲のデータを抽出
    end = start + duration
    mask3 = (shifted_time3 >= start) & (shifted_time3 < end)

    angle_subset3 = angle3[mask3]
    time_subset3 = shifted_time3[mask3]
    # angle_subset1 を shifted_time3 に対応させる
    mask1 = data1['time'].isin(time_subset3)
    angle_subset1 = angle1[mask1]

    # データ長を短い方に合わせる
    min_length = min(len(angle_subset1), len(angle_subset3))
    angle_subset1 = angle_subset1.iloc[:min_length]
    angle_subset3 = angle_subset3.iloc[:min_length]

    # 差を計算
    angle_difference = angle_subset1.values - angle_subset3.values

    # ヒストグラムを作成
    counts, edges = np.histogram(angle_difference, bins=bins, range=(range_min, range_max))
    counts_in_seconds = counts / fps  # フレーム数を秒数に変換
    
   

    # 新しいプロット作成
    plt.figure(figsize=(8, 6))
    plt.bar(edges[:-1], counts_in_seconds, width=bin_width, color='blue', alpha=0.7, edgecolor='black')
    
    
    # グラフ設定
    plt.xlabel('Measured Gaze - Estimated Gaze')
    plt.ylabel('Second')
    plt.title(f'ASD 水平方向の角度差 (Time {start}s-{end}s)')
    plt.grid(True)
    plt.xlim(-100, 100)  # 横軸の範囲を統一
    plt.ylim(0, 20)  # 縦軸の最大値を統一

    # ファイル名を生成して保存
    filename = os.path.join(save_dir, f'ASD_hori_histogram_{start}s-{end}s.png')
    plt.savefig(filename)
    print(f"Saved histogram: {filename}")
    plt.close()
