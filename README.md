# アイトラッキングVRシステムを用いたTD/ASDの注視行動比較
# 🧠  研究再現用リポジトリ

このリポジトリは，【アイトラッキングVRシステムを用いたTD/ASDの注視行動比較】の研究成果を引き継ぐための資料をまとめたものです．使用データ，処理スクリプト，生成物，実験結果を含んでいます．

本研究では視線推定ライブラリを使用しますが，こちらの使用方法については広島市立大学の方が作成した[引き継ぎ資料.pdf](https://github.com/ta1ku0mi6/gaze_estimation_library/blob/a66a188853843f49f652de588cd9d954b71f6546/%E5%BC%95%E3%81%8D%E7%B6%99%E3%81%8E%E8%B3%87%E6%96%99.pdf)
を参照してください．

---
## 環境構築

本研究では仮想環境であるanaconda3を使用しました．

## 研究の流れ
VRゴーグルを使い得られた頭部・眼球運動のデータを方向ベクトルから水平・垂直の角度情報に変換します．ワールド座標(0, 0, 0)にあるカメラ位置を原点に，左手座標系でx,y,z軸を取っています．正面方向はz軸方向です．
[caluculate.py](https://github.com/ta1ku0mi6/gaze_estimation_library/blob/adee66b7c6354ca429f20b8e6189570fca4f82cb/caluculate.py)を使用．
![image_480](https://github.com/user-attachments/assets/f62e0294-08a9-4d01-b138-30515dabd011)


