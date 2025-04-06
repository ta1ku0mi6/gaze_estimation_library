import pandas as pd
import matplotlib.pyplot as plt
import os
import japanize_matplotlib
import numpy as np

# 2つのCSVファイルを読み込み
file1 = 'output_TDhead.csv'  # 最初のCSVファイルのパス
file2 = 'output_TDleft.csv'  # 2番目のCSVファイルのパス

data1 = pd.read_csv(file1)
data2 = pd.read_csv(file2)

# FPSを定義
fps = 30

# time[s]を計算
data1['time'] = data1.index / fps
data2['time'] = data2.index / fps

angle1 = data1.iloc[:, 1]  # Measured Head
angle2 = data2.iloc[:, 1]  # Measured Gaze

# 保存ディレクトリ
save_dir = '../gaze_estimation_library/result(estimation_gaze)/TD1/histogram/Measured Head - Measured Gaze_histogram/vertical'
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

# ヒストグラムプロットのループ
for start in range(0, end, duration):
    end = start + duration

    # 各30秒範囲のデータを抽出
    mask1 = (data1['time'] >= start) & (data1['time'] < end)
    mask2 = (data2['time'] >= start) & (data2['time'] < end)

    # 両方のマスクが適用されたインデックスを取得
    common_index = data1[mask1].index.intersection(data2[mask2].index)

    angle_subset1 = angle1.loc[common_index]
    angle_subset2 = angle2.loc[common_index]

    # 差分計算
    angle_difference = angle_subset1.values - angle_subset2.values

    # ヒストグラム作成
    counts, edges = np.histogram(angle_difference, bins=bins, range=(range_min, range_max))
    counts_in_seconds = counts / fps  # フレーム数を秒数に変換

    plt.figure(figsize=(8, 6))
    plt.bar(edges[:-1], counts_in_seconds, width=bin_width, color='blue', alpha=0.7, edgecolor='black')

    # グラフ設定
    plt.xlabel('Measured Head - Measured Gaze')
    plt.ylabel('Second')
    plt.title(f'TD 垂直方向の角度差 (Time {start}s-{end}s)')
    plt.grid(True)
    plt.xlim(-100, 100)  # 横軸の範囲を統一
    plt.ylim(0, 20)  # 縦軸の最大値を統一

    # ファイル名を生成して保存
    filename = os.path.join(save_dir, f'TD_ver_histogram_{start}s-{end}s.png')
    plt.savefig(filename)
    print(f"Saved histogram: {filename}")
    plt.close()
