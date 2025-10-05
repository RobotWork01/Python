#------------------------------------------------------------------------------------------------------------------#
#＜RobotWork01＞
#  CSVファイル読込み・検索（GUI）アプリ　※FreeSimpleGUI、pandas利用の場合
#
#参考１:
#  https://neenet-pro.com/pysimplegui-parquet-viewer/
#  PySimpleGUIでParquet Viewerを作成する【Windows・Mac両対応】
#       ※懸念：動作としてはあまり軽快とは言えず，少しでも容量の大きいcsvファイルを読み込むとカクついてしまう。
#
#  補足資料：
#  https://pandasquest.com/pandas%E3%81%A7%E3%83%87%E3%83%BC%E3%82%BF%E8%AA%AD%E3%81%BF%E8%BE%BC%E3%81%BF%E3%82%92%E9%AB%98%E9%80%9F%E5%8C%96%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/944/
#  Pandasでデータ読み込みを高速化する方法
#      Pandasは、その便利さと多機能性からデータ分析において広く利用されています。
#      しかし、大規模なデータセットを扱う際には、データの読み込み速度が問題となることがあります。
#      Pandasのデータ読み込みは、データのサイズが大きくなると非常に時間がかかることがあります。
#      これは、Pandasがデータをメモリ上に全て読み込むため、大量のデータを扱う際にはその限界が露呈します。
#      特に、数GB以上のデータを扱う場合、データの読み込みだけで数分から数十分かかることもあります。
#      また、Pandasはデータの型推論を行うため、データ読み込み時に全てのデータをスキャンします。
#      これにより、データの読み込み速度がさらに遅くなる可能性があります。
#
#参考２：[AI による概要]
#      PythonのFreeSimpleGUIを使って高速なCSV検索GUIを作成するには、まずFreeSimpleGUIをインストールし、
#      CSVファイルをPandasライブラリで読み込み、DataFrameとして扱います。
#      次に、GUIレイアウトに検索用入力フィールドと結果表示用のテーブルを配置し、検索ボタンのクリックイベント
#      でDataFrameをフィルタリングしてテーブルを更新する処理を実装することで、CSVの高速検索GUIが実現できます。
#      ※留意点：無償のFreeSimpleGUIでは不可な点も、有償のPySimpleGUIでは可能な点があります。
#
# 環境構築方法
#py -3.9 -m pip install pyinstaller
#pip install freesimplegui
#
# コンパイル＆exeファイル「main.exe」作成方法
#py -m  PyInstaller PythonCSV.py --onefile
#
# 実行方法：
# exeファイルをダブルクリック
#------------------------------------------------------------------------------------------------------------------#
import FreeSimpleGUI as sg
import pandas as pd

# Tkinter(ティーケーインター)ライブラリ　※Pythonに同梱される「標準ライブラリ」
import tkinter as tk               # tkinter(ティーケー・インター)
import tkinter.ttk as ttk          # ttkは、“themed tkinter”の略です！ttkを使うと、標準のtkウィジェットよりも見た目が良く、クロスプラットフォームで一貫したスタイルを持つウィジェットを作成できます！
from tkinter import messagebox     # ポップアップメッセージボックス表示
from tkinter import filedialog     # ダイアログ表示（ファイル選択、フォルダ選択）
from tkinter import font           # 文字書式（カスタムフォントを作成）


#＜ヘッダー用配列＞　※注：固定です（ファイル名変更しても列数、列名変更不可）
data = {'名前': ['Alice', 'Bob', 'Charlie', 'David'],
        '年齢': [25, 30, 35, 40],
        '都市': ['Tokyo', 'Osaka', 'Tokyo', 'Nagoya']}
df = pd.DataFrame(data)

# GUIレイアウトの定義
layout = [
    [sg.Text('CSVファイル名:', size=(15, 1)), sg.Input(key='-CSV-'), sg.Button('ファイル参照')],
    [sg.Text('CSVデータ検索', font=('Helvetica', 16))],
    [sg.Text('検索キーワード:', size=(15, 1)), sg.Input(key='-INPUT-')],
    [sg.Button('検索', bind_return_key=True), sg.Button('全件表示'), sg.Button('終了')],
    [sg.Table(values=[], headings=df.columns.tolist(),
              display_row_numbers=True,   # 行番号表示
              auto_size_columns=True,     # 列幅自動調整を有効にする
              vertical_scroll_only=False, # 横スクロールを有効にする
              justification='left',       # 左寄せ
              key='-TABLE-',              # キーコード
              enable_events=True,         # イベント受信可否
              expand_x=True,              # ウィンドウX軸(横)幅
              expand_y=True)]             # ウィンドウY軸(縦)幅
]


# ウィンドウサイズ
window_width = 586   # 横幅を指定
window_height = 629  # 縦幅を指定

# 画面の中央にウィンドウを配置するための計算
screen_width, screen_height = sg.Window.get_screen_size()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# ウィンドウの作成
window = sg.Window(
 '[RobotWork01] CSV高速検索',
 layout,
 size=(window_width, window_height), # ウィンドウサイズを指定
 location=(x_position, y_position),  # 中央に配置
 resizable=True)                     # サイズ変更操作可否


#-----------------------------------------------------------#
# 「参照ボタン（csv）押下時」の処理
#-----------------------------------------------------------#
def file_dialog_csv_clicked():
    #------------------------------------#
    # ファイル選択用ダイアログの表示
    #------------------------------------#
    fTyp = [("", "csv")] #csvファイル指定
    iFile = os.path.abspath(os.path.dirname(__file__))
    iFilePath = filedialog.askopenfilename(filetype = fTyp, initialdir = iFile)
    return iFilePath

# 初期値
oFilePath = ''

# イベントループ
while True:
    event, values = window.read()

    #------------------------------------------#
    # ×ボタンが押された場合
    #------------------------------------------#
    if event == sg.WIN_CLOSED:break

    #------------------------------------------#
    # 終了ボタンが押された場合
    #------------------------------------------#
    if event == '終了':
        if tk.messagebox.askyesno('確認', '終了しますか？'):break

    #------------------------------------------#
    # ファイル参照ボタンが押された場合
    #------------------------------------------#
    if event == 'ファイル参照':
       oFilePath = file_dialog_csv_clicked()
       window['-CSV-'].update(value=oFilePath)
       
       # 新しいファイルを使ってDataFrameを再作成
       table_data = pd.read_csv(oFilePath)

       # データフレームの作成
       df = pd.DataFrame(table_data)
       data = df.values.tolist()
       window['-TABLE-'].update(values=data)

       # 検索結果メッセージ
       search_count = len(data)
       tk.messagebox.showinfo('CSVファイル読込', f'全件表示しました！[{search_count}件]')

    #-------------------------------------------------------#
    # 検索ボタンが押された、またはEnterキーが押された場合
    #-------------------------------------------------------#
    if event == '検索':
    
        if oFilePath=='':
           sg.popup('CSVファイルを選択してください。')
        else:
           keyword = values['-INPUT-'].lower()  # 小文字に変換

           if keyword:
           #------------------------------------------#
           # pandasを使って高速にフィルタリング
           #------------------------------------------#
               # 新しいファイルを使ってDataFrameを再作成
               df = pd.DataFrame(pd.read_csv(oFilePath))

               # 検索条件の設定
               filtered_df = df[df.apply(lambda row: any(keyword in str(cell).lower() for cell in row), axis=1)]
               
               # 検索を行い、検索結果を画面表示
               table_data = filtered_df.values.tolist()
               window['-TABLE-'].update(values=table_data)

               # 検索結果メッセージ
               search_count = filtered_df.shape[0]
               tk.messagebox.showinfo('検索結果', f'検索しました！[{search_count}件]')
           else:
               sg.popup('検索キーワードを入力してください。')

    #------------------------------------------#
    # 全件表示ボタンが押された場合
    #------------------------------------------#
    if event == '全件表示':
    
        if oFilePath=='':
           sg.popup('CSVファイルを選択してください。')
        else:
           # 新しいファイルを使ってDataFrameを再作成
           df = pd.DataFrame(pd.read_csv(oFilePath))

           # 検索を行い、検索結果を画面表示
           table_data = df.values.tolist()
           window['-TABLE-'].update(values=table_data)

           # 検索結果メッセージ
           search_count = len(table_data)
           tk.messagebox.showinfo('検索結果', f'全件表示しました！[{search_count}件]')

# ウィンドウを閉じる
window.close()