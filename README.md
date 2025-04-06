# アイトラッキングVRシステムを用いたTD/ASDの注視行動比較
# 🧠  研究再現用リポジトリ

このリポジトリは，【アイトラッキングVRシステムを用いたTD/ASDの注視行動比較】の研究成果を引き継ぐための資料をまとめたものです．使用データ，処理スクリプト，生成物，実験結果を含んでいます．



---
## 環境構築
本研究では視線推定ライブラリを使用しますが，こちらの使用方法については広島市立大学の方が作成した[引き継ぎ資料.pdf](https://github.com/ta1ku0mi6/gaze_estimation_library/blob/a66a188853843f49f652de588cd9d954b71f6546/%E5%BC%95%E3%81%8D%E7%B6%99%E3%81%8E%E8%B3%87%E6%96%99.pdf)
を参照してください．

本研究では仮想環境であるanaconda3を使用しました．

## 研究の流れ
1️⃣頭部・眼球運動のデータを方向ベクトルから角度情報に変換

VRゴーグルを使い得られた頭部・眼球運動のデータを方向ベクトルから水平・垂直の角度情報に変換します．ワールド座標(0, 0, 0)にあるカメラ位置を原点に，左手座標系でx,y,z軸を取っています．正面方向はz軸方向です．データは[input_csv](https://github.com/ta1ku0mi6/gaze_estimation_library/tree/cc1e08b2085ba5da58421dc6efbb2b82a9c93d5b/input_csv)にあります．
角度情報への変換には[caluculate.py](https://github.com/ta1ku0mi6/gaze_estimation_library/blob/adee66b7c6354ca429f20b8e6189570fca4f82cb/caluculate.py)を使用し，
変換後のデータは[output_csv](https://github.com/ta1ku0mi6/gaze_estimation_library/tree/e4c6a7c398a527cfa58012c30df70a132cb34950/output_csv)に保存されます．
![image_480](https://github.com/user-attachments/assets/f62e0294-08a9-4d01-b138-30515dabd011)

2️⃣出力されたデータを用いて眼球頭部強調運動モデルにかける
[main.py](https://github.com/ta1ku0mi6/gaze_estimation_library/blob/1bee185ab05a125eb7f36f0db34b8b9309e1da59/main.py)を使用します．TDのデータをモデルにかける際は[gfh.py](https://github.com/ta1ku0mi6/gaze_estimation_library/blob/79198268c9f8a9b7ad1c31084f6d816dd0dda134/gfh.py)の119行目をコメントアウト，ASDの場合は121行目をコメントアウトしてください．

モデル適用後のデータは[result(transformation)](https://github.com/ta1ku0mi6/gaze_estimation_library/tree/066e05f63fa1258b0d3e0e85ba84127de5297474/result(transformation))に保存されます．

私は一人ひとり同じファイルに上書きする形でモデルを適用してしまっていたので，被験者ごとにファイルを作成するようにした方が後々データから考察する際に楽になると思います．

3️⃣実験データの考察

被験者の頭部運動と眼球運動を可視化するために卒論11ページのようなグラフを作成しました．（約10分のデータで30秒ごとのグラフと全体のグラフ）
グラフ作成（水平・垂直）のプログラムは[graphplot](https://github.com/ta1ku0mi6/gaze_estimation_library/tree/04898022b25201c49a04668a19b0a2ad87d849da/graphplot)にあります．

※0s-30sのグラフで推定視線のグラフの始まりが少し遅れて始まるのは，眼球頭部強調運動モデルが0.7秒分頭の動きを読み込んでから推定するためです．(30fps x 0.7s = 21フレーム)

また，それぞれのグラフの差から特徴を得るために[histogram](https://github.com/ta1ku0mi6/gaze_estimation_library/tree/45425d1c165b00f6ed1b992abf37f1eb7d27fb5b/histogram)を作成しました．

TD,ASDのグラフとヒストグラムの結果は，[result(estimation_gaze)](https://github.com/ta1ku0mi6/gaze_estimation_library/tree/45425d1c165b00f6ed1b992abf37f1eb7d27fb5b/result(estimation_gaze))にあります．


## おわりに

上記の流れで研究の再現ができると思います．
研究頑張ってください!
