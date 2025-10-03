#-----------------------------------------------------------------------#
#＜RobotWork＞
#  上、左、右の３画面で構成されたフレーム画面（GUI）アプリ
#
# 参考：
#  https://office54.net/python/tkinter/python-tkinter-frame
#  Pythonのtkinterで使用するFrame（フレーム）使い方
#
# ●環境構築：
#  py -3.9 -m pip install pyinstaller
#
# ●環境確認：
#  py -V
#     Python 3.9.1
#
# ●留意点：
#   Pythonプログラムコードではタブではなく半角スペースを使用するとスムーズです。
#   Pythonプログラムは上から順番に１行ずつ解釈するので順番を気にしてコーディングしましょう。
#   Pythonプログラムのオプションは大抵は半角英字の大文字です（大文字小文字に意味がある点にご注目ください）
#
# ●コンパイル＆exeファイル「PythonCSVExcel_MERGE.exe」作成方法
#  cd C:\Users\XXXXX\OneDrive\ドキュメント\GitHub\Python\PythonFrame
#  py -m  PyInstaller PythonFrame.py --onefile
#
# ●実行方法
#  cd C:\Users\XXXXX\OneDrive\ドキュメント\GitHub\Python\PythonFrame\dist
#  PythonFrame.exe
#
#-----------------------------------------------------------------------#

#---------------------------------#
# Pythonライブラリのインポート
#---------------------------------#

# Tkinter(ティーケーインター)に含まれる拡張モジュール
import tkinter as tk               # tkinter(ティーケー・インター)
import tkinter.ttk as ttk          # ttkは、“themed tkinter”の略です！ttkを使うと、標準のtkウィジェットよりも見た目が良く、クロスプラットフォームで一貫したスタイルを持つウィジェットを作成できます！
from tkinter import messagebox     # ポップアップメッセージボックス表示
from tkinter import filedialog     # ダイアログ表示（ファイル選択、フォルダ選択）
from tkinter import font           # 文字書式（カスタムフォントを作成）

# 「メインウィンドウ」の画面設定
root = tk.Tk()
memo = "[RobotWork01] tkinter(ティーケーインター)でのFrame（フレーム）見本"
root.title(memo)
root.geometry("950x600")                      # geometry (ジオメトリー)・・・・画面サイズ（幅x高さ)
root.configure(bg="ivory", padx=10, pady=10)  # configure(コンフィギュア)・・・bg=画面背景色（lightblue）、X軸枠、Y軸枠

# -----------------------------------------------------------#
# 「終了ボタン（出力）押下時」の処理
# -----------------------------------------------------------#
def end_clicked():
    #---------------------------------------------#
    # 確認メッセージ表示処理（はい・いいえ）
    #---------------------------------------------#
    ret = messagebox.askyesno('確認', '終了しますか？')
    if ret == True:
        #-------------------------------#
        # アプリ終了処理
        #-------------------------------#
        root.quit()

#--------------------------------#
# ウィジェット作成：TOP画面
#--------------------------------#
#ウィジェット書式宣言
frame_top = tk.Frame(root,               #親画面
                     pady=5,             #境界枠線とテキストとの間にある余白Y軸(縦):int型
                     padx=5,             #境界枠線とテキストとの間にある余白X軸(横):int型
                     relief=tk.RAISED,   #境界枠線スタイル:flat（平坦）、sunken（沈み込み）、raised（浮き彫り）、groove（溝）、ridge（凸部）、solid（実線）
                     bd=2)               #境界枠線の横幅(太さ):int型
button1 = tk.Button(frame_top, text='Open')
button2 = tk.Button(frame_top, text='Close', command=end_clicked)

#ウィジェット作成
frame_top.pack(fill=tk.X)#X軸(縦)方向に引き延ばす
button1.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT, padx=5)

#--------------------------------#
# ウィジェット作成：左画面
#--------------------------------#
#ウィジェット書式宣言
frame_left = tk.Frame(root,             #親画面
                      pady=5,           #境界枠線とテキストとの間にある余白Y軸(縦):int型
                      padx=5,           #境界枠線とテキストとの間にある余白X軸(横):int型
                      relief=tk.RAISED, #境界枠線スタイル:flat（平坦）、sunken（沈み込み）、raised（浮き彫り）、groove（溝）、ridge（凸部）、solid（実線）
                      bd=1,             #境界枠線の横幅(太さ):int型
                      bg="white")       #背景色
button1_left = tk.Button(frame_left, text="Func1", width=10)
button2_left = tk.Button(frame_left, text="Func2", width=10)

#ウィジェット作成
frame_left.pack(side=tk.LEFT, fill=tk.Y)#Y軸(横)方向に引き延ばす
button1_left.pack(side=tk.TOP)
button2_left.pack(side=tk.TOP,padx=5, pady=5)

#--------------------------------#
# ウィジェット作成：右画面
#--------------------------------#
#ウィジェット書式宣言
frame_right = tk.Frame(root,            #親画面
                       pady=5,          #境界枠線とテキストとの間にある余白Y軸(縦):int型
                       padx=5,          #境界枠線とテキストとの間にある余白X軸(横):int型
                       relief=tk.FLAT,  #境界枠線スタイル:flat（平坦）、sunken（沈み込み）、raised（浮き彫り）、groove（溝）、ridge（凸部）、solid（実線）
                       bg="ivory")      #背景色
#label_right = tk.Label(frame_right, text="This is Label.", width=10)

# カスタムフォントを作成
custom_font = font.Font(family="Helvetica", size=14, weight="bold")  # フォント書式名、文字サイズ、太字を指定

# 画面タイトル
title_memo = " tkinter(ティーケーインター)ライブラリで使用するFrame（フレーム）の使い方 "
label_right = ttk.Label(frame_right, text=title_memo, padding=(3, 3),foreground='linen', background='lightslategray', font=custom_font)  # ラベル前景色(文字色)、ラベル背景色、カスタムフォント 

#ウィジェット作成
frame_right.pack(side=tk.LEFT, fill=tk.BOTH)#XY軸(縦横)方向に引き延ばす
label_right.pack(side=tk.TOP)


#--------------------------------#
# ウィジェットループ
#--------------------------------#
root.mainloop()

