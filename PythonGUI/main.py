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
# 留意点
# プログラムコードにタブは使用しないこと（半角スペースのみを使用する）
# PySimpleGUIパッケージの代替として、FreeSimpleGUIパッケージを利用しているため
# PySimpleGUIに出来ることでも、FreeSimpleGUIには出来ないことがあります。
#
# 実行方法：
# exeファイルをダブルクリック
#---------------------------------------------------------------#

# PySimpleGUIパッケージの代替として、FreeSimpleGUIパッケージを利用
import FreeSimpleGUI as sg
import tkinter as tk # Tkinterの機能を使うためにインポート

# ウィンドウサイズ
window_width = 586   # 横幅を指定
window_height = 629  # 縦幅を指定

# 画面の中央にウィンドウを配置するための計算
screen_width, screen_height = sg.Window.get_screen_size()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# レイアウトの定義：ウィジェットをリストでまとめる
layout = [
[sg.Text('あなたの名前を入力してください：')],
[sg.Input(key='-NAME-')],
[sg.Text('性別を選択してください：')],
    [sg.Radio('女', group_id='seibetu', key='-WOMAN-')],
    [sg.Radio('男', group_id='seibetu', key='-MAN-')],
    [sg.Radio('未回答', group_id='seibetu', default=True, key='-NODATA-')],
[sg.Text("以下のオプションを選択してください:")],
    [sg.Checkbox("オプション1", key="-OPTION1-", default=False)],
    [sg.Checkbox("オプション2", key="-OPTION2-", default=False)],
    [sg.Checkbox("オプション3", key="-OPTION3-", default=False)],

#[sg.Text('リストボックスから選択してください:')],
#    #[sg.Listbox(values=items, size=(20, 4), key='-LIST-', enable_events=True)],
#    #[sg.Listbox(values=items, size=(20, 4), key='-LIST-')],
#    [sg.Listbox(values=['項目1', '項目2', '項目3'], size=(20, 5), key='-LISTBOX-')],

[sg.Text("備考:")],
    #[sg.Multiline(default_text="ここにテキストを入力してください", write_only=True, size=(60,10), reroute_cprint=True, key="-MULTILINE-")],
    [sg.Multiline(default_text="ここにテキストを入力してください", size=(40, 10), key="-MULTILINE-")],  # マルチライン入力フィールド
[sg.Button('送信', key='-Btn-'), sg.Button('終了', key='-BEnd-')],   # sg.Button('ラベル名'),
]

# ウィンドウの作成
window = sg.Window(
 'RobotWork01【FreeSimpleGUI】',     # ウィンドウタイトルを指定
 layout,
 size=(window_width, window_height), # ウィンドウサイズを指定
 location=(x_position, y_position),  # 中央に配置
 finalize=True                       # ウィンドウを作成後に操作可能にする
)

# イベントループの開始
while True:
  event, value = window.read()       # イベント発生するまでずっと待つ

  # 終了ボタンやウィンドウの×ボタンが押された場合、ループを終了
  if event == sg.WINDOW_CLOSED or event == '終了':break

  # 送信ボタン
  if event == '-Btn-':

      # チェックボックス・オプション(すべて未選択か１以上選択)
      check_out = ''
      if value['-OPTION1-']:
          check_out = check_out + 'オプション1,'
      else:
          check_out = check_out  # continueではない
      if value['-OPTION2-']:
          check_out = check_out + 'オプション2,'
      else:
          check_out = check_out  # continueではない
      if value['-OPTION3-']:
          check_out = check_out + 'オプション3,'
      else:
          check_out = check_out  # continueではない

      # 性別(必ず１以上選択)
      if value['-WOMAN-']:
          output1 = '女'
      elif value['-MAN-']:
          output1 = '男'
      else:
          output1 = '未回答'

      # 送信ボタンが押されたら、入力内容をポップアップ表示
      message = ''
      
      # 名前＋性別
      if value['-NAME-'] != '':
          message = message + 'こんにちは、' + value['-NAME-'] + 'です！ 性別：' + output1
      else:
          message = message + 'こんにちは、名前なしです！ 性別：' + output1
      
      # チェックボックス・オプション
      if check_out == '':
          message = message + '\n チェックボックス・オプション：選択なし'
      else:
          message = message + '\n チェックボックス・オプション：' + check_out

      # マルチラインの内容を取得して表示
      multiline_content = value["-MULTILINE-"]

      # 備考
      if multiline_content == '':
          message = message + "\n 備考：なし"
      else:
          message = message + "\n 備考：" + multiline_content

      # ポップアップ表示
      #sg.popup_ok(message + listbox_out, title="送信データ")
      sg.popup_ok(message, title="送信データ")

      continue
      #break
  elif event is None:
      continue
      #break

  # ウィンドウの破棄
  window.close()

