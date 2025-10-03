#----------------------------------------------------------------------------------------#
# ＜＜　RobotWork　＞＞
# 　　参考サイト：
#      https://qiita.com/yuya2220/items/ea67c89a0cd2caf5adb8
#      @yuya2220 in パーソルクロステクノロジー株式会社
#     【Python】Tkinterで2つのデータを結合し出力するGUIアプリを作成する
#
# ●環境構築：
#  py -3.9 -m pip install pyinstaller
#  pip install pandas
# ●環境確認：
#  pip show pandas
#   Name: pandas
#   Version: 2.3.3
#   Summary: Powerful data structures for data analysis, time series, and statistics
#
# ●コンパイル＆exeファイル「PythonCSVExcel_MERGE.exe」作成方法
#  cd C:\Users\XXXXX\OneDrive\ドキュメント\GitHub\Python\PythonCSV+Excel_MERGE
#  py -m  PyInstaller PythonCSVExcel_MERGE.py --onefile
#
# ●実行方法
#  cd C:\Users\XXXXX\OneDrive\ドキュメント\GitHub\Python\PythonCSV+Excel_MERGE\dist
#  PythonCSVExcel_MERGE.exe
#
#----------------------------------------------------------------------------------------#
import os
import pandas as pd

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#threading(スレッディング)モジュールは、
#Pythonでマルチスレッドプログラミングを行うための標準ライブラリです。
#このモジュールを使用すると、複数のスレッドを作成し並列処理を実現できます。
#スレッドは、OSがプログラムを実行する際の最小単位であり、
#複数のスレッドを活用することで、効率的な処理が可能になります。
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
import threading

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#tkinter(ティーケーインター)ライブラリは、
# Python3でGUIアプリケーションを開発するための標準ライブラリです。
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
import tkinter as tk

# Tkinter(ティーケーインター)に含まれる拡張モジュール
from tkinter import *
from tkinter import ttk            # ttkは、“themed tkinter”の略です！ttkを使うと、標準のtkウィジェットよりも見た目が良く、クロスプラットフォームで一貫したスタイルを持つウィジェットを作成できます！
from tkinter import messagebox     # ポップアップメッセージボックス表示
from tkinter import filedialog     # ダイアログ表示（ファイル選択、フォルダ選択）
from tkinter import font           # 文字書式（カスタムフォントを作成）

#------------------------------------------------------------------------------------------------#
#class Application(tk.Frame):
#   Tkinter(ティーケーインター)のフレームウィジェットを使用してアプリケーションのフレームを作成するためのクラス定義です。
#   このクラス内で、フレームの親ウィジェットを定義し、フレーム内に他のウィジェットを配置するためのメソッドを定義します。
#   クラスをインスタンス化することで、フレームウィジェットを用いてアプリケーションの画面を構築することができます。
#------------------------------------------------------------------------------------------------#
class Application(tk.Frame):
    #-----------------------------------------------------------#
    #def __init__(self, master):
    #  クラスのインスタンスを生成する際に、masterという引数を受け取り、
    #  その値を初期化処理で利用するための構文です。
    # -----------------------------------------------------------#
    def __init__(self,master):
        super().__init__(master)                                           # フレームの親ウィジェットを定義
        self.pack(fill="both", expand=True)                                # pack(パック)・・・・・・・・・ TKオブジェクトの起動(フレームをウィンドウ全体に広げる)
        self.master.title("RobotWork　[csv・Excelファイル結合(マージ)]")     # title(タイトル)・・・・・・・・ウィンドウ・タイトルの設定
        self.master.geometry('750x300')                                    # geometry (ジオメトリー)・・・・画面サイズ（幅x高さ)
        self.master.configure(bg="lightblue", padx=10, pady=10)            # configure(コンフィギュア)・・・画面背景色（lightblue）、X軸枠、Y軸枠

        #------------------------------------------#
        # Tkinterの「フレームウィジェット」動的作成
        #------------------------------------------#
        self.set_csv_widgets()
        self.set_excel_widgets()
        self.set_output_widgets()
        self.set_run_widgets()

    #------------------------------------------------------------------------#
    # Tkinterのフレーム（ウィンドウ画面）パーツ（ラベル、ボタン）の動的配置
    # ＜入力ファイル：csvファイル関連＞
    #------------------------------------------------------------------------#
    def set_csv_widgets(self):

        # カスタムフォントを作成
        custom_font = font.Font(family="Helvetica", size=10, weight="bold")  # フォント書式名、文字サイズ、太字を指定
        
        # フレーム
        self.csv_frame = ttk.Frame(self, padding=10)            # TTKフレーム作成　第一引数：ルート　第二引数：オプション　　　　　
        self.csv_frame.grid(row=0, column=1, sticky=E)          # グリッド枠 オプション：stickyではウィジェットを寄せる方向を指定できます。寄せる方向は英語の方角（North、South、East、West）の頭文字を指定します。

        # 画面タイトル
        title_memo = "【Python】2つのデータ(csv＋Excel)を結合し指定した出力フォルダに結果ファイルを出力するGUIアプリ"
        self.head_title = ttk.Label(self.csv_frame, text=title_memo, padding=(3, 3),foreground='linen', background='lightslategray', font=custom_font)  # ラベル前景色(文字色)、ラベル背景色、カスタムフォント 
        self.head_title.pack(side=TOP)

        # 項目ラベル
        self.csv_label = ttk.Label(self.csv_frame, text="csvファイル：", padding=(5, 2))
        self.csv_label.pack(side=LEFT)

        # テキストボックス
        self.csv_entry = StringVar()
        self.csv_dir = ttk.Entry(self.csv_frame, textvariable=self.csv_entry, width=90)
        self.csv_dir.pack(side=LEFT)

        # 参照ボタン
        self.csv_button = ttk.Button(self.csv_frame, text="参照", command=self.file_dialog_csv_clicked)
        self.csv_button.pack(side=LEFT)

    #------------------------------------------------------------------------#
    # Tkinterのフレーム（ウィンドウ画面）パーツ（ラベル、ボタン）の動的配置
    # ＜入力ファイル：Excelファイル関連＞
    #------------------------------------------------------------------------#
    def set_excel_widgets(self):
        # フレーム
        self.excel_frame = ttk.Frame(self, padding=10)            # TTKフレーム作成　第一引数：ルート　第二引数：オプション
        self.excel_frame.grid(row=2, column=1, sticky=E)          # グリッド枠 オプション：stickyではウィジェットを寄せる方向を指定できます。寄せる方向は英語の方角（North、South、East、West）の頭文字を指定します。

        # ラベル
        self.excel_label = ttk.Label(self.excel_frame, text="Excelファイル：", padding=(5, 2))
        self.excel_label.pack(side=LEFT)

        # テキストボックス
        self.excel_entry = StringVar()
        self.excel_dir = ttk.Entry(self.excel_frame, textvariable=self.excel_entry, width=90)
        self.excel_dir.pack(side=LEFT)

        # 参照ボタン
        self.excel_button = ttk.Button(self.excel_frame, text="参照", command=self.file_dialog_excel_clicked)
        self.excel_button.pack(side=LEFT)

    #------------------------------------------------------------------------#
    # Tkinterのフレーム（ウィンドウ画面）パーツ（ラベル、ボタン）の動的配置
    # ＜出力先フォルダ指定関連＞
    #------------------------------------------------------------------------#
    def set_output_widgets(self):
        # フレーム
        self.output_frame = ttk.Frame(self, padding=10)            # TTKフレーム作成　第一引数：ルート　第二引数：オプション
        self.output_frame.grid(row=4, column=1, sticky=E)          # グリッド枠 オプション：stickyではウィジェットを寄せる方向を指定できます。寄せる方向は英語の方角（North、South、East、West）の頭文字を指定します。

        # ラベル
        self.output_label = ttk.Label(self.output_frame, text="出力フォルダ：", padding=(5, 2))
        self.output_label.pack(side=LEFT)

        # テキストボックス
        self.output_entry = StringVar()
        self.output_dir = ttk.Entry(self.output_frame, textvariable=self.output_entry, width=90)
        self.output_dir.pack(side=LEFT)

        # 参照ボタン
        self.output_button = ttk.Button(self.output_frame, text="参照", command=self.dir_dialog_clicked)
        self.output_button.pack(side=LEFT)

    #------------------------------------------------------------------------#
    # Tkinterのフレーム（ウィンドウ画面）パーツ（ラベル、ボタン）の動的配置
    # ＜実行ボタン関連＞
    #------------------------------------------------------------------------#
    def set_run_widgets(self):
        # フレーム
        #self.run_frame = ttk.Frame(self, padding=10)            # TTKフレーム作成　第一引数：ルート　第二引数：オプション
        self.run_frame = ttk.Frame(self, padding=(5,2))          # グリッド枠 オプション：stickyではウィジェットを寄せる方向を指定できます。寄せる方向は英語の方角（North、South、East、West）の頭文字を指定します。
        self.run_frame.grid(row=6,column=1,sticky=E)

        # 実行ボタン
        self.run_button = ttk.Button(self.run_frame, text="実行", command=self.run_thread)
        self.run_button.pack(side="right", pady=(1, 2), padx=(2, 3)) # ボタンの周囲にパディングを設定

        # 終了ボタン
        self.e_button = ttk.Button(self.run_frame, text="終了", command=self.end_thread)
        #self.e_button.pack(side="right", padx=3, pady=3)
        self.e_button.pack(side="right", pady=(1, 2), padx=(2, 3)) # ボタンの周囲にパディングを設定

    #-----------------------------------------------------------#
    # 「参照ボタン（csv）押下時」の処理
    #-----------------------------------------------------------#
    def file_dialog_csv_clicked(self):
        #------------------------------------#
        # ファイル選択用ダイアログの表示
        #------------------------------------#
        fTyp = [("", "csv")] #csvファイル指定
        iFile = os.path.abspath(os.path.dirname(__file__))
        iFilePath = filedialog.askopenfilename(filetype = fTyp, initialdir = iFile)
        self.csv_entry.set(iFilePath)

    # -----------------------------------------------------------#
    # 「参照ボタン（Excel）押下時」の処理
    # -----------------------------------------------------------#
    def file_dialog_excel_clicked(self):
        #------------------------------------#
        # ファイル選択用ダイアログの表示
        #------------------------------------#
        fTyp = [("", "xlsx")] #Excelファイル指定
        iFile = os.path.abspath(os.path.dirname(__file__))
        iFilePath = filedialog.askopenfilename(filetype = fTyp, initialdir = iFile)
        self.excel_entry.set(iFilePath)

    # -----------------------------------------------------------#
    # 「参照ボタン（出力）押下時」の処理
    # -----------------------------------------------------------#
    def dir_dialog_clicked(self):
        #------------------------------------#
        # フォルダ選択用ダイアログの表示
        #------------------------------------#
        iDir = os.path.abspath(os.path.dirname(__file__))
        iDirPath = filedialog.askdirectory(initialdir = iDir)
        self.output_entry.set(iDirPath)

    # -----------------------------------------------------------#
    # 「終了ボタン（出力）押下時」の処理
    # -----------------------------------------------------------#
    def end_thread(self):
        threading.Thread(target=self.end_clicked, daemon=True).start()
    def end_clicked(window, sele=None):
        #---------------------------------------------#
        # 確認メッセージ表示処理（はい・いいえ）
        #---------------------------------------------#
        ret = messagebox.askyesno('確認', '終了しますか？')
        if ret == True:
            #-------------------------------#
            # アプリ終了処理
            #-------------------------------#
            window.tk.quit()

    # -----------------------------------------------------------#
    # 実行ボタン押下時の処理をスレッドで行う（プログレスバーを動かすため）
    # -----------------------------------------------------------#
    def run_thread(self):
        #---------------------------------------------#
        # 確認メッセージ表示処理（はい・いいえ）
        #---------------------------------------------#
        ret = messagebox.askyesno('確認', '実行しますか？')
        if ret == True:
            #-------------------------------#
            # プログレスバー表示開始処理
            #-------------------------------#
            threading.Thread(target=self.run_clicked, daemon=True).start()

    # -----------------------------------------------------------#
    # 「実行ボタン押下時」の処理
    # -----------------------------------------------------------#
    def run_clicked(self):
        self.set_progress_widgets()

        #-----------------------------------------------#
        # 各種未入力チェック処理
        #-----------------------------------------------#
        #ファイル、フォルダのパスが指定されているか確認
        #-----------------------------------------------#
        alert_text = self.check_file_path()
        if alert_text == "":
            #入力OK時(未入力なし)
            self.merge_file()                                  # ファイル結合(マージ)処理
            self.delete_progress()                             # プログレスバー削除処理
            messagebox.showinfo("info", "処理が完了しました")   # 終了メッセージ表示処理
        else:
            #入力NG時(未入力あり)
            self.delete_progress()                             # プログレスバー削除処理
            messagebox.showinfo("info", alert_text)            # 終了メッセージ表示処理

    #---------------------------------------------#
    # 処理中のラベルとプログレスバーを設置する
    #---------------------------------------------#
    def set_progress_widgets(self):
        #------------------------------------#
        # 処理中のラベルを設置処理
        #------------------------------------#
        self.process = ttk.Label(self.run_frame, text="処理中・・・")
        self.process.pack(side=LEFT)
        self.process.update()

        #------------------------------------#
        # 処理中のプログレスバーを設置処理
        #------------------------------------#
        var = tk.IntVar()
        self.pb=ttk.Progressbar(self.run_frame,maximum=100,mode="indeterminate",variable=var)
        self.pb.pack(side=LEFT)
        self.pb.start(interval=10)

    #---------------------------------------------#
    # 各種未入力チェック処理
    #---------------------------------------------#
    def check_file_path(self):
        alert_text = ""

        # パスが設定されているか確認する
        csv_path = self.csv_entry.get()
        excel_path = self.excel_entry.get()
        output_path = self.output_entry.get()
        if csv_path == '':
            alert_text += "csvファイル" + "\n"
        if excel_path == '':
            alert_text += "excelファイル" + "\n"
        if output_path == '':
            alert_text += "出力フォルダ" 
        if alert_text:
            alert_text = "以下のファイルの指定がありません" + "\n" + alert_text
        return alert_text

    #---------------------------------------------#
    # csvとexcelの結合(マージ)処理
    #---------------------------------------------#
    def merge_file(self):

        # 入力テキストより、対象ファイルパスを取得
        csv_path = self.csv_entry.get()
        excel_path = self.excel_entry.get()

        # 対象ファイル読込み
        csv_df = pd.read_csv(csv_path)        
        excel_df = pd.read_excel(excel_path)

        # ファイル結合(マージ)実行
        join_df = pd.merge(csv_df, excel_df, on=["ID"], how="left")

        # ファイル結合(マージ)結果出力
        output_dir = self.output_entry.get() + "\出力.xlsx"
        join_df.to_excel(output_dir,index=FALSE)

    #---------------------------------------#
    # ラベルとプログレスバーの削除
    #---------------------------------------#
    def delete_progress(self):
        self.process.destroy()
        self.pb.destroy()

#---------------------------------------#
# 主処理
#---------------------------------------#
def main():
    root = tk.Tk()                     # TkinterのTKフレーム起動(ウィンドウ画面オープン)
    app = Application(master=root)     # Applicationクラスを実行する・・・・・・・・・TkinterのTKフレームウィジェット(GUI)の動的作成
    app.mainloop()                     # Applicationクラスの無限ループを宣言する・・・Tkinterの破棄・生成が永遠と実行される

#---------------------------------------#
# 起動方法の指定
#---------------------------------------#
if __name__ == "__main__":
    # 主処理
    main()

