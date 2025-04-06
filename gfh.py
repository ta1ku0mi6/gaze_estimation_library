# coding:utf-8
import numpy as np
import pickle

# 頭部運動データの読み込み
def load_file(input):

  t_start = -0.7  # 頭部の参照時間幅のt_s(秒)
  t_end = 0.2  # 頭部の参照時間幅のt_e(秒)
  framerate = 30  # フレームレート30(fps)

  t_s_frame = int(t_start * framerate) # -21
  t_e_frame = int(t_end * framerate) # 6
  train_data_demension = (t_e_frame - t_s_frame + 1) * 2 # 56

  # 出力ファイル(頭部方向データ)のヘッダー
  header_1 = "head_horizontal,head_vertical"

  # 出力ファイル(頭部方向時系列データ)のヘッダー
  header_2 = ""
  for i in range(t_s_frame, t_e_frame+1): # -21~6まで
    header_2 += "h_" + format(i) + ","
  for i in range(t_s_frame, t_e_frame+1): # -21~6まで
    header_2 += "v_" + format(i) + ","
  
  # 頭部方向データと頭部方向時系列データの作成
  input_data = np.loadtxt(input, delimiter = ",")
  
  if (t_s_frame < 0): # t_s_frame = -21
    gaze_start = abs(t_s_frame) # 21
  else :
    gaze_start = 0

  if (t_e_frame > 0): # t_e_frame = 6
    gaze_end = len(input_data)-t_e_frame # len(input_data)-6
  else :
    gaze_end = len(input_data)

  dataset_feature = np.empty((0,train_data_demension)) # np.empty((0,56))
  
  for i in range(gaze_start, gaze_end): # for i in range(21,len(input_data)-6)

    feature_vec = np.append(input_data[i+t_s_frame : i+t_e_frame+1,0] - input_data[i,0], \
                            input_data[i+t_s_frame : i+t_e_frame+1,1] - input_data[i,1])
    dataset_feature = np.append(dataset_feature, feature_vec.reshape(1,len(feature_vec)), axis=0)

  head_gaze = input_data[gaze_start:gaze_end].copy()

  # ファイルの出力
  np.savetxt("../gaze_estimation_library/time-series data/head_gaze.csv", head_gaze, delimiter=",", header=header_1, comments="")
  np.savetxt("../gaze_estimation_library/time-series data/features.csv", dataset_feature, delimiter=",", header=header_2, comments="")  
  
  print("time-series data: Finish!!!")

  return dataset_feature

# 視線推定
def estimate_gaze(dataset_feature,model):
  
  # もしmodelが3DoFなら，移動無しモデルを
  if model == "3DoF":
    model_h_out_path = "../gaze_estimation_library/model_h_out_path(saliency)/"
    model_v_out_path = "../gaze_estimation_library/model_v_out_path(saliency)/"
  
  # もしmodelが6DoFなら，移動有りモデルを
  if model == "6DoF":
    model_h_out_path = "../gaze_estimation_library/model_h_out_path(murakami)/"
    model_v_out_path = "../gaze_estimation_library/model_v_out_path(murakami)/"
  
  # テストデータとして配列に代入 
  test_labels = np.loadtxt("../gaze_estimation_library/time-series data/head_gaze.csv", delimiter = ",", skiprows= 1)
  test_features = np.loadtxt("../gaze_estimation_library/time-series data/features.csv", delimiter = ",", skiprows= 1)
  
  # 頭部方向時系列データ
  X_test = test_features
  
  # modelの読み込み(水平角)
  with open(model_h_out_path + "model_h.pickle", mode='rb') as f:
      model_h = pickle.load(f)

  # modelの読み込み(垂直角)
  with open(model_v_out_path + "model_v.pickle", mode='rb') as f:
      model_v = pickle.load(f)
  
  # 視線推定
  predict_horizontal = model_h.predict(X_test)
  predict_vertical = model_v.predict(X_test)

  output_data = np.append(predict_horizontal.reshape(len(predict_horizontal),1), predict_vertical.reshape(len(predict_vertical),1), axis=1)
  output_data = np.append(output_data, test_labels[:,[0,1]], axis=1)

  # ヘッダー
  header_1 = "pre_gaze_horizontal,pre_gaze_vertical,measured_head_horizontal,measured_head_vertical"

  # ファイルの出力 
  np.savetxt("../gaze_estimation_library/result/estimated_gaze_dir.csv", output_data, delimiter=",", header=header_1, comments="")

  print("gde: Finish!!!")

  return output_data

# 頭部基準から世界座標基準へ変換  
def trans_to_global(output_data):

  input_filepath = "../gaze_estimation_library/result/estimated_gaze_dir.csv"

  input_data = np.loadtxt(input_filepath, delimiter = ",", skiprows=1)

  input_data_path = input_data.copy()
  
  for i in range(0,len(input_data_path)):
    input_data_path[i,0] = input_data_path[i,2] + input_data_path[i,0]
    input_data_path[i,1] = input_data_path[i,3] + input_data_path[i,1]

  # ヘッダー
  header_1 = "pre_gaze_horizontal,pre_gaze_vertical,measured_head_horizontal,measured_head_vertical"
  
  # ファイルの出力
  np.savetxt("../gaze_estimation_library/result(transformation)/estimated_gaze_ASDhead.csv", input_data_path, delimiter=",", header=header_1, comments="")
   
  #np.savetxt("../gaze_estimation_library/result(transformation)/estimated_gaze_TDhead.csv", input_data_path, delimiter=",", header=header_1, comments="")
  
  print("transformation: Finish!!!")

  return input_data_path