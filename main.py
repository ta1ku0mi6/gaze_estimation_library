import gfh

# 頭部運動データの読み込み
head_seq = gfh.load_file( 'output_ASDhead.csv' )

# 視線推定
gaze_seq = gfh.estimate_gaze(  head_seq, model = "3DoF" )

# 頭部基準から世界座標基準へ変換
gaze_seq_global = gfh.trans_to_global( gaze_seq )