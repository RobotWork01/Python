#----------------------------------------------------------------------------------------#
# ＜＜  RobotWork01 ＞＞
#    アプリ画面(GUI)＋データベース更新アプリ
#
#    参考サイト：
#      https://www.w3resource.com/python-exercises/tkinter/python-tkinter-file-operations-and-integration-exercise-12.php
#      Python Tkinter CRUD application with SQLite
#
# ●環境構築：
#  py -3.9 -m pip install pyinstaller
#  pip install pandas
#
# ●コンパイル＆exeファイル「PythonCSVExcel_MERGE.exe」作成方法
#  cd C:\Users\XXXXX\OneDrive\ドキュメント\GitHub\Python\PythonSQLLite
#  py -m  PyInstaller PythonSQLLite.py --onefile
#
# ●実行方法
#  cd C:\Users\XXXXX\OneDrive\ドキュメント\GitHub\Python\PythonSQLLite\dist
#  PythonSQLLite.exe
#
#----------------------------------------------------------------------------------------#

import tkinter as tk            #Pythonに同梱される「標準ライブラリ」(ティーケーインター)
from tkinter import *           # モジュール内で定義されているメソッドや変数をまとめてインポート
from tkinter import ttk         # ttkを使うと、tkよりも見た目が良く、クロスプラットフォームで一貫したスタイルを持つウィジェット作成出来ます
import sqlite3                  #Pythonに同梱される「データベース」(エスキューエル・ライト)
from tkinter import messagebox  #メッセージボックス作成ツール
from tkinter import font        # 文字書式（カスタムフォントを作成）

#--------------------------------------#
#     Applicationクラス
#--------------------------------------#
class Application(tk.Frame):
    def __init__(self,master):                                    
        super().__init__(master)                              # フレームの親ウィジェットを定義
        self.pack(fill="both", expand=True)                   # pack(パック)・・・・・・・・・ TKオブジェクトの起動(フレームをウィンドウ全体に広げる)
        
        #--------------------------------------#
        #     ウィンドウ作成
        #--------------------------------------#
        self.master.title("RobotWork　[CRUD Application]")    # タイトル       ウィンドウ・タイトルの設定
        self.master.geometry('750x600')                       # ジオメトリー   画面サイズ（幅x高さ)
        self.master.configure(bg="ivory", padx=10, pady=10)   # コンフィギュア 画面背景色、X軸枠、Y軸枠

        #--------------------------------------#
        #     school.dbデータベース接続
        #--------------------------------------#
        self.master.conn = sqlite3.connect("school.db")
        self.master.cursor = self.master.conn.cursor()

        #--------------------------------------#
        #     studentsテーブル作成
        #--------------------------------------#
        self.master.cursor.execute('''CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            stclass TEXT,
            marks REAL
        )''')
        self.master.conn.commit()

        # カスタムフォントを作成
        custom_font = font.Font(family="Helvetica", size=10, weight="bold")  # フォント書式名、文字サイズ、太字を指定
   
        # フレーム
        self.main_frame = ttk.Frame(self, padding=10)   # TTKフレーム作成　第一引数：ルート　第二引数：オプション
        self.main_frame.grid(row=0, column=1, sticky=E) # グリッド枠 オプション：stickyではウィジェットを寄せる方向を指定できます。寄せる方向は英語の方角（North、South、East、West）の頭文字を指定します。

        # 画面タイトル
        title_memo = "【Python】GUI画面＋データベース更新出来るアプリ"
        self.head_title = ttk.Label(self.main_frame,text=title_memo,padding=(5, 5),foreground='linen',background='lightslategray',font=custom_font) # カスタムフォント 
        self.head_title.pack(side=TOP)

        # フレーム
        self.main_frame2 = ttk.Frame(self, padding=10)   # TTKフレーム作成　第一引数：ルート　第二引数：オプション
        self.main_frame2.grid(row=2, column=1, sticky=E) # グリッド枠 オプション：stickyではウィジェットを寄せる方向を指定できます。
                                                         #寄せる方向（North、South、East、West）の頭文字を指定します。
        #--------------------------------------#
        #           名前欄の作成
        #--------------------------------------#
        # 項目ラベル
        self.name_label = ttk.Label(self.main_frame2, text="名前:", padding=(10, 10))
        self.name_label.pack(side=LEFT)

        # テキストボックス
        self.name_entry = StringVar()
        self.name_entry = ttk.Entry(self.main_frame2, textvariable=self.name_entry, width=30)
        self.name_entry.pack(side=LEFT)

        #--------------------------------------#
        #           役職欄の作成
        #--------------------------------------#
        # 項目ラベル
        self.position_label = ttk.Label(self.main_frame2, text="役職:", padding=(2, 2))
        self.position_label.pack(side=LEFT)

        # テキストボックス
        self.stclass_entry = StringVar()
        self.stclass_entry = ttk.Entry(self.main_frame2, textvariable=self.stclass_entry, width=60)
        self.stclass_entry.pack(side=LEFT)

        # フレーム
        self.main_frame3 = ttk.Frame(self, padding=10)   # TTKフレーム作成　第一引数：ルート　第二引数：オプション
        self.main_frame3.grid(row=3, column=1, sticky=E) # グリッド枠 オプション：stickyではウィジェットを寄せる方向を指定できます。
                                                         #寄せる方向（North、South、East、West）の頭文字を指定します。
        #--------------------------------------#
        #           備考メモの作成
        #--------------------------------------#
        # 項目ラベル
        self.salary_label = ttk.Label(self.main_frame3, text="備考メモ:", padding=(10, 10))
        self.salary_label.pack(side=LEFT)

        # テキストボックス
        self.marks_entry = StringVar()
        self.marks_entry = ttk.Entry(self.main_frame3, textvariable=self.marks_entry, width=70)
        self.marks_entry.pack(side=LEFT)

        # フレーム
        self.main_frame4 = ttk.Frame(self, padding=10)   # TTKフレーム作成　第一引数：ルート　第二引数：オプション
        self.main_frame4.grid(row=4, column=1, sticky=E) # グリッド枠 オプション：stickyではウィジェットを寄せる方向を指定できます。
                                                         #寄せる方向（North、South、East、West）の頭文字を指定します。
        # 追加登録ボタン
        self.add_button = ttk.Button(self.main_frame4, text="追加登録", command=self.add_student)
        self.add_button.pack(side=LEFT)

        #--------------------------------------#
        #       リストボックス作成
        #--------------------------------------#
        # フレーム
        self.main_frame5 = ttk.Frame(self, padding=10)   # TTKフレーム作成　第一引数：ルート　第二引数：オプション
        self.main_frame5.grid(row=6, column=1, sticky=E) # グリッド枠 オプション：stickyではウィジェットを寄せる方向を指定できます。
                                                         #寄せる方向（North、South、East、West）の頭文字を指定します。
        # 項目ラベル
        self.salary_label = ttk.Label(self.main_frame5, text="データベース「students」テーブル参照:", padding=(10, 10))
        self.salary_label.pack(side=TOP)

        # リストボックス
        self.student_listbox = tk.Listbox(self.main_frame5, width=70)  # TTKフレーム作成　第一引数：ルート　第二引数：オプション
        self.student_listbox.bind('<<ListboxSelect>>', self.list_selected)  # リストボックス選択時をバインド
        self.main_frame5.columnconfigure(0, weight=3)
        self.student_listbox.pack(side=LEFT)               # グリッド枠 オプション：stickyではウィジェットを寄せる方向を指定できます。
                                                           # 寄せる方向（North、South、East、West）の頭文字を指定します。

        #--------------------------------------#
        #         画面項目の再表示
        #--------------------------------------#
        self.load_students()

        #--------------------------------------#
        #          更新ボタン作成
        #--------------------------------------#
        # フレーム
        self.main_frame6 = ttk.Frame(self, padding=10)   # TTKフレーム作成　第一引数：ルート　第二引数：オプション
        self.main_frame6.grid(row=7, column=1, sticky=E) # グリッド枠 オプション：stickyではウィジェットを寄せる方向を指定できます。
                                                         #寄せる方向（North、South、East、West）の頭文字を指定します。
        self.update_button = ttk.Button(self.main_frame6, text="更新", command=self.update_student)
        self.update_button.pack(side=LEFT)

        #--------------------------------------#
        #          削除ボタン作成
        #--------------------------------------#
        self.delete_button = ttk.Button(self.main_frame6, text="削除", command=self.delete_student)
        self.delete_button.pack(side=LEFT)

        # 終了ボタン
        self.e_button = ttk.Button(self.main_frame6, text="終了", command=self.end_clicked)
        self.e_button.pack(side="right", pady=(1, 2), padx=(2, 3))   # ボタンの周囲にパディングを設定

    #-------------------------------#
    #      レコード追加登録処理
    #-------------------------------#
    def add_student(self):
        #画面項目「テキストボックス」の値を取得する
        name = self.name_entry.get()
        stclass = self.stclass_entry.get()
        marks = self.marks_entry.get()

        if name and stclass and marks:
            #画面項目「テキストボックス」の値がすべて入力されていた場合
            self.master.cursor.execute("INSERT INTO students (name, stclass, marks) VALUES (?, ?, ?)", (name, stclass, marks))
            self.master.conn.commit()
            self.load_students()
            self.clear_entries()
            messagebox.showinfo("info", "レコード追加登録しました！")  # 終了メッセージ表示処理
        else:
            #画面項目「テキストボックス」の値が1つでも未入力がある場合
            #messagebox.showwarning("Warning", "Please fill in all fields.")
            messagebox.showwarning("確認", "全ての画面項目に入力してください")

    #-------------------------------#
    #     画面項目の再表示処理
    #-------------------------------#
    def load_students(self):
        #画面項目「リストボックス」のクリア
        self.student_listbox.delete(0, tk.END)
        
        #全レコード取得
        self.master.cursor.execute("SELECT * FROM students")
        students = self.master.cursor.fetchall()
        for row in students:
            #画面項目「リストボックス」に表示する
            self.student_listbox.insert(tk.END, f"{row[0]}. {row[1]}, {row[2]}, {row}")

    #-------------------------------#
    #    画面項目のクリア処理
    #-------------------------------#
    def clear_entries(self):
    
        #画面項目のクリア
        self.name_entry.delete(0, tk.END)
        self.stclass_entry.delete(0, tk.END)
        self.marks_entry.delete(0, tk.END)

    #-------------------------------#
    #      リストボックス選択時
    #-------------------------------#
    def list_selected(self, event):

        #画面項目「リストボックス」の値を取得する
        selected_index = self.student_listbox.curselection()
        if selected_index:

           #画面項目「リストボックス」の値を取得
           selected_module = self.student_listbox.get(selected_index)
            
           #配列に分割
           result1 = selected_module.split(",", 6)
           
           #配列の要素を取得
           student_id = result1[2]
           name = result1[3]
           stclass = result1[4]
           marks = result1[5]
           
           #不要な文字「'」を除去
           o_name = name.replace("'", "")
           o_stclass = stclass.replace("'", "")
           o_marks = marks.replace("'", "")
           
           #不要な文字「)」を除去
           o_student_id = student_id[2:len(student_id)]  #2文字目から文字桁分を取得
           ret = o_marks[1:len(o_marks)-1]  #1文字目から文字桁ー１文字分を取得
           
           #テキストボックスのクリア
           self.clear_entries()
           
           #テキストボックスに値を設定
           self.name_entry.insert(0,o_name)
           self.stclass_entry.insert(0,o_stclass)
           self.marks_entry.insert(0,ret)

        #else:
        #   messagebox.showwarning("警告", "リストボックス何も選択されていません削除対象データを選択ください")

    #-------------------------------#
    #      レコード更新処理
    #-------------------------------#
    def update_student(self):

        #画面項目「テキストボックス」に選択されたリストボックスの値を取得する
        selected_index = self.student_listbox.curselection()

        if selected_index:

           #画面項目「リストボックス」の値を取得
           selected_module = self.student_listbox.get(selected_index)
            
           #配列に分割
           result1 = selected_module.split(",", 6)
        
           #配列の要素を取得
           student_id = result1[2]

           #不要な文字「(」を除去
           o_student_id = student_id[2:len(student_id)]  #2文字目から文字桁分を取得

           ret = messagebox.askyesno('確認', '本当に更新しますか？')
           if ret == True:

              #選択されている「リストボックス」の値からIDを取得する
              name = self.name_entry.get()
              stclass = self.stclass_entry.get()
              marks  = self.marks_entry.get()
              
              #メッセージ
              messagebox.showinfo("確認", f"UPDATE students SET name={name}, stclass={stclass}, marks={marks} WHERE id={o_student_id}")

              if name and stclass and marks:
              #画面項目「テキストボックス」の値が１つでも入力されていた場合
                  #レコード更新の実行
                  self.master.cursor.execute("UPDATE students SET name=?, stclass=?, marks=? WHERE id=?", (name, stclass, marks, o_student_id))
                  self.master.conn.commit()
                  
                  #画面の再表示
                  self.load_students()
                  
                  #画面のクリア
                  self.clear_entries()
                  
                  messagebox.showinfo("確認", "レコード更新しました！")
              else:
                  messagebox.showwarning("確認", "リストボックス「更新対象データ」を選択してください")
           else:
              messagebox.showinfo("確認", "更新キャンセルしました！")

    #-------------------------------#
    #      レコード削除処理
    #-------------------------------#
    def delete_student(self):
    
        #画面項目「テキストボックス」に選択されたリストボックスの値を取得する
        selected_index = self.student_listbox.curselection()

        messagebox.showinfo("確認", "削除ボタン開始！")

        if selected_index:

           #画面項目「リストボックス」の値を取得
           selected_module = self.student_listbox.get(selected_index)

           #配列に分割
           result1 = selected_module.split(",", 6)

           #配列の要素を取得
           student_id = result1[2]

           #不要な文字「(」を除去
           o_student_id = student_id[2:len(student_id)]  #2文字目から文字桁分を取得

           ret = messagebox.askyesno('確認', f"本当に削除しますか？DELETE FROM students WHERE id={o_student_id}") 
           if ret == True:
              #レコード削除の実行
              self.master.cursor.execute("DELETE FROM students WHERE id=?", (o_student_id,))
              #self.master.cursor.execute("UPDATE students SET name=?, stclass=?, marks=? WHERE id=?", (name, stclass, marks, o_student_id))
              self.master.conn.commit()

              #画面の再表示
              self.load_students()

              #画面のクリア
              self.clear_entries()

              messagebox.showinfo("確認", "レコード削除しました！")
           else:
              messagebox.showinfo("確認", "削除キャンセルしました！")
        else:
           messagebox.showwarning("確認", "リストボックス「削除対象データ」を選択してください")

    #-------------------------------#
    #     データベース切断処理
    #-------------------------------#
    def __del__(self):
        #self.conn.close()
        self.master.conn.close()

    # -----------------------------------------------------------#
    # 「終了ボタン（出力）押下時」の処理
    # -----------------------------------------------------------#
    def end_clicked(window, sele=None):
        if messagebox.askyesno('確認', '本当に終了しますか？'):window.tk.quit()

#-------------------------------#
#          アプリ主処理
#-------------------------------#
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)  
    root.mainloop()
