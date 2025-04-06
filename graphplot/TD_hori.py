import pandas as pd
import matplotlib.pyplot as plt
import os

# 2つのCSVファイルを読み込み
file1 = 'output_TDhead.csv'  # 最初のCSVファイルのパス
file2 = 'output_TDleft.csv'  # 2番目のCSVファイルのパス
file3 = '../gaze_estimation_library/result(transformation)/estimated_gaze_TDhead.csv'

data1 = pd.read_csv(file1)
data2 = pd.read_csv(file2)
data3 = pd.read_csv(file3)

# FPSを定義
fps = 30

# time[s]を計算
data1['time'] = data1.index / fps
data2['time'] = data2.index / fps
data3['time'] = data3.index / fps
shifted_time3 = data3['time'] + 0.7

angle1 = data1.iloc[:, 0]  # 最初のCSVの垂直角データ
angle2 = data2.iloc[:, 0]  # 2番目のCSVの垂直角データ
angle3 = data3.iloc[:, 0]

# 保存ディレクトリ
save_dir = '../gaze_estimation_library/result(estimation_gaze)/TD1/horizontal'
os.makedirs(save_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成

# 30秒毎のデータをプロット
start = 0
end = 640
interval = 30

# プロットのループ
for start in range(start, end, interval):
    # 各30秒範囲のデータを抽出
    end = start + interval
    mask1 = (data1['time'] >= start) & (data1['time'] < end)
    mask2 = (data2['time'] >= start) & (data2['time'] < end)
    mask3 = (shifted_time3 >= start) & (shifted_time3 < end)

    time1 = data1['time'][mask1]
    angle_subset1 = angle1[mask1]
    time2 = data2['time'][mask2]
    angle_subset2 = angle2[mask2]
    time3 = shifted_time3[mask3]
    angle_subset3 = angle3[mask3]

    # 新しいプロット作成
    plt.figure(figsize=(8, 6))
    
    # データをプロット
    plt.plot(time1, angle_subset1, label='Measured Head', color='black')
    plt.plot(time2, angle_subset2, label='Measured Gaze', color='red')
    plt.plot(time3, angle_subset3, label='Estimated Gaze', color='blue', linestyle='--')

    # グラフ設定
    plt.ylim(-180, 180)
    plt.xlabel('Time (s)')
    plt.ylabel('(deg)')
    plt.title(f'TD Horizontal (Time {start}s-{end}s)')
    plt.legend()
    plt.grid(True)

    # ファイル名を生成して保存
    filename = os.path.join(save_dir, f'TDplot_hori_{start}s-{end}s.png')
    plt.savefig(filename)
    print(f"Saved plot: {filename}")
    plt.close()

    
