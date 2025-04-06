import pandas as pd
import matplotlib.pyplot as plt
import os

# 2つのCSVファイルを読み込み
file1 = 'output_ASDhead.csv'  # 最初のCSVファイルのパス
file2 = 'output_ASDleft.csv'  # 2番目のCSVファイルのパス
file3 = '../gaze_estimation_library/result(transformation)/estimated_gaze_ASDhead.csv'

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

angle1 = data1.iloc[:, 0]  
angle2 = data2.iloc[:, 0]  
angle3 = data3.iloc[:, 0]

# 保存ディレクトリ
save_dir = '../gaze_estimation_library/result(estimation_gaze)/ASD1/horizontal'
os.makedirs(save_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成


# 新しいプロット作成
plt.figure(figsize=(12, 6))

# 全データをプロット
plt.plot(data1['time'], angle1, label='Measured Head', color='black')
plt.plot(data2['time'], angle2, label='Measured Gaze', color='red')
plt.plot(shifted_time3, angle3, label='Estimated Gaze', color='blue', linestyle='--')

# グラフ設定
plt.ylim(-180, 180)
plt.xlabel('Time (s)')
plt.ylabel('(deg)')
plt.title('ASD Horizontal - Full Range')
plt.legend()
plt.grid(True)

# ファイル名を生成して保存
filename = os.path.join(save_dir, f'ASDplot_hori_full.png')
plt.savefig(filename)
print(f"Saved plot: {filename}")
plt.close()


