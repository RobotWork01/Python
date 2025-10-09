# アプリ名「PythonCSV＿AI」（パイソン・シーエスブイ＿エーアイ）

### アプリ概要
このアプリでは、CSVファイル読込み・検索（GUI）することが出来ます。　※FreeSimpleGUI、pandas
<table>
<tr>
  <td><img width="735" height="826" alt="image" src="https://github.com/user-attachments/assets/596490f9-0b15-46e5-abc6-e61d94a2c953"  style="width: 120%; height: auto;" /></td>
  <td><img width="942" height="591" alt="image" src="https://github.com/user-attachments/assets/53700239-7f01-4a1e-a44d-ff4a9f07ddb7"  style="width: 70%; height: auto;" /></td>
</tr>
</table>
このアプリは <a href="https://github.com/RobotWork01/Python/blob/main/PythonCSV_AI/%E5%8F%82%E8%80%83%EF%BC%BFAI%E3%81%A7%E3%81%AE%E5%9B%9E%E7%AD%94.txt">AIの回答</a> を参考にいたしました。

### アプリ機能説明
```
１．このアプリを起動すると、入力待ちの状態になります。
　　予め決めたフォーマットでリストボックスに列名（ヘッダー）が表示されています。

２．ファイル参照ボタンをクリックすると、ファイル選択ダイアログボックスが表示されます。
　　そのファイル選択ダイアログボックスを使用してファイルを選択すると、選択したファイルのフルパスがテキストボックス「CSVファイル名」に表示されて、
  　リストボックスに選択したファイルの全データが表示されます。
　　※GitHubでは、サンプルCSVファイル用意されています。

　　留意点：
　　どのようなファイルレイアウトを読んでも、予め用意されたファイルレイアウトに合うようにファイルが読み込まれます。
　　ファイルの１行目は列タイトル行と判断し、２行目以降が毎回読み込まれます。

　　例えば、ファイルレイアウトの列数が１０列でも２０列でも１００列だとしても、予め用意された列数だけが読み込まれます。
　　列名は変更することが出来ません。

３．検索キーワードに検索条件を入力した後に「検索」ボタンをクリックすると検索条件にマッチしたレコードが抽出されます。

４．全件表示ボタンをクリックすると、全データが表示されます。

５．終了ボタンをクリックすると、確認メッセージ「終了しますか？」が表示され「はい」を選択するとアプリが終了します。

```

# License
The source code is licensed MIT. The website content is licensed CC BY 4.0,see LICENSE.

