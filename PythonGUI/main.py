#---------------------------------------------------------------#
# RobotWork01
# 参考：https://zenn.dev/unr_tech_lab/articles/882fdddb2f8028
#      FreeSimpleGUIの使い方・クイックスタートガイド
#
# 環境構築方法
#py -3.9 -m pip install pyinstaller
#pip install freesimplegui
#
# コンパイル＆exeファイル「main.exe」作成方法
#py -m  PyInstaller main.py --onefile
#
# 実行方法：
# exeファイルをダブルクリック
#---------------------------------------------------------------#

# PySimpleGUI パッケージの代替として、FreeSimpleGUI パッケージを利用
import FreeSimpleGUI as sg

# レイアウトの定義：ウィジェットをリストでまとめる
layout = [
[sg.Text('あなたの名前を入力してください：')],
[sg.Input(key='-NAME-')],
[sg.Button('送信'), sg.Button('終了')],
]

# ウィンドウの作成
window = sg.Window('RobotWork01【FreeSimpleGUI】', layout)

# イベントループの開始
while True:
  event, values = window.read()
  # 終了ボタンやウィンドウの×ボタンが押された場合、ループを終了
  if event == sg.WINDOW_CLOSED or event == '終了':break
  # 送信ボタンが押されたら、入力内容を表示
  if event == '送信':sg.popup('こんにちは、' + values['-NAME-'] + 'さん！')

  # ウィンドウの破棄
  window.close()

