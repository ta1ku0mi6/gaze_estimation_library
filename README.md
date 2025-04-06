# アイトラッキングVRシステムを用いたTD/ASDの注視行動比較
# 🧠  研究再現用リポジトリ

このリポジトリは，アイトラッキングVRシステムを用いたTD/ASDの注視行動比較の研究成果を引き継ぐための資料をまとめたものです．使用データ，処理スクリプト，生成物，実験結果を含んでいます．

本研究では視線推定ライブラリを使用しますが，こちらの使用方法については広島市立大学の方が作成した[引き継ぎ資料.pdf](https://github.com/ta1ku0mi6/gaze_estimation_library/blob/a66a188853843f49f652de588cd9d954b71f6546/%E5%BC%95%E3%81%8D%E7%B6%99%E3%81%8E%E8%B3%87%E6%96%99.pdf)
を参照してください．

---

## 📁 ディレクトリ構成
project-root/ 
├── data/ # データフォルダ 
│ ├── raw/ # 元データ（未加工） 
│ └── processed/ # 前処理済みデータ 
├── scripts/ # PythonスクリプトやJupyter Notebook
│ ├── preprocess.py # データ前処理
│ └── analysis.ipynb # 可視化・分析用ノートブック 
├── figures/ # 作成した図表 
├── results/ # 実験結果・ログ・評価結果 
├── models/ # 学習済みモデル 
├── requirements.txt # 使用ライブラリ一覧 
└── README.md # このファイル
