# Python
Python(パイソン)

### Python開発環境を作ってみよう（インストール手順）
参考サイト：
https://dropoutgs.com/python-install/

★Python用IDEのJetBrains社のPython開発環境
『PyCharm』（パイチャーム）をインストールする方法
https://www.jetbrains.com/pycharm/download/#section=windows

★無料版
https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC
```
日本語変換ツール(お勧め出来ないです、ごめんなさい！
どうしてかというとPython用IDE『PyCharm』（パイチャーム）が起動出来なくなってしまい解決できなかったので、
仕方なく、Python用IDE『PyCharm』（パイチャーム）をアンインストールして再度インストールして解決いたしました((+_+))
「日本語でなくても当面はいいかなぁ」と思って『PyCharm』（パイチャーム）の日本語化を諦めた次第ですー($・・)/~~~)
　https://mergedoc.osdn.jp/
　↓　↓　↓
　Preparing to download Eclipse Pleiades plugin
　https://ftp.jaist.ac.jp/pub/mergedoc/pleiades/build/stable/pleiades-win.zip
```
### Pytho(パイソン)のバージョンを確認！する方法
py -V
Python 3.9.1

### pyinstaller(3.9)をアンインストールする方法
py -3.9 -m pip uninstall pyInstaller

### pyinstaller(3.9)をインストールする方法
py -3.9 -m pip install pyinstaller
```
c:\Python39\Lib\site-packages>py -3.9 -m pip install pyinstaller
Requirement already satisfied: pyinstaller in c:\python39\lib\site-packages (4.10)
Requirement already satisfied: setuptools in c:\python39\lib\site-packages (from pyinstaller) (49.2.1)
Requirement already satisfied: pywin32-ctypes>=0.2.0; sys_platform == "win32" in c:\python39\lib\site-packages (from pyinstaller) (0.2.0)
Requirement already satisfied: pefile>=2017.8.1; sys_platform == "win32" in c:\python39\lib\site-packages (from pyinstaller) (2021.9.3)
Requirement already satisfied: pyinstaller-hooks-contrib>=2020.6 in c:\python39\lib\site-packages (from pyinstaller) (2022.3)
Requirement already satisfied: altgraph in c:\python39\lib\site-packages (from pyinstaller) (0.17.2)
Requirement already satisfied: future in c:\python39\lib\site-packages (from pefile>=2017.8.1; sys_platform == "win32"->pyinstaller) (0.18.2)
```
### freesimpleguiをインストールする方法
C:\WINDOWS\system32>pip install freesimplegui
```
WARNING: Ignoring invalid distribution -p (c:\python310\lib\site-packages)
WARNING: Ignoring invalid distribution -sa (c:\python310\lib\site-packages)
WARNING: Ignoring invalid distribution -ip (c:\python310\lib\site-packages)
WARNING: Ignoring invalid distribution - (c:\python310\lib\site-packages)
WARNING: Ignoring invalid distribution -p (c:\python310\lib\site-packages)
WARNING: Ignoring invalid distribution -sa (c:\python310\lib\site-packages)
WARNING: Ignoring invalid distribution -ip (c:\python310\lib\site-packages)
WARNING: Ignoring invalid distribution - (c:\python310\lib\site-packages)
Collecting freesimplegui
  Downloading freesimplegui-5.2.0.post1-py3-none-any.whl (733 kB)
     ---------------------------------------- 733.6/733.6 kB 11.5 MB/s eta 0:00:00
WARNING: Ignoring invalid distribution -p (c:\python310\lib\site-packages)
WARNING: Ignoring invalid distribution -sa (c:\python310\lib\site-packages)
WARNING: Ignoring invalid distribution -ip (c:\python310\lib\site-packages)
WARNING: Ignoring invalid distribution - (c:\python310\lib\site-packages)
Installing collected packages: freesimplegui
WARNING: Ignoring invalid distribution -p (c:\python310\lib\site-packages)
WARNING: Ignoring invalid distribution -sa (c:\python310\lib\site-packages)
WARNING: Ignoring invalid distribution -ip (c:\python310\lib\site-packages)
WARNING: Ignoring invalid distribution - (c:\python310\lib\site-packages)
Successfully installed freesimplegui-5.2.0.post1
WARNING: Ignoring invalid distribution -p (c:\python310\lib\site-packages)
WARNING: Ignoring invalid distribution -sa (c:\python310\lib\site-packages)
WARNING: Ignoring invalid distribution -ip (c:\python310\lib\site-packages)
WARNING: Ignoring invalid distribution - (c:\python310\lib\site-packages)

[notice] A new release of pip available: 22.3.1 -> 25.2
[notice] To update, run: python.exe -m pip install --upgrade pip
```

### PyCharm IDE利用：freesimpleguiの実行結果
C:\Python39\python.exe C:/Users/XXXXX/開発技術/Python（パイソン）/PythonGUI/main.py
Process finished with exit code 0

※参考：https://teratail.com/questions/s3zojfvst32yit
PySimpleGUI パッケージは商用利用が有償化されて
個人利用もライセンス登録が必要になりました。
```
　参考：
　Python2年生 デスクトップアプリ開発のしくみ 体験してわかる！会話でまなべる！ ダウンロード｜翔泳社の本
　https://www.shoeisha.co.jp/book/download/9784798174990/detail
　PySimpleGUI パッケージの代替として、FreeSimpleGUI パッケージの利用を勧めています。
```

＜＜コンパイル＞＞
```
１．コンパイルしたいパイソンの配下に移動する。
    cd C:\Users\XXXXX\test\

２．コンパイルを実行してexeファイルを作成する。
    py -m  PyInstaller main.py --onefile
```
＜＜コンパイル＆exeファイルを作成結果＞＞
```
100 DEPRECATION: Running PyInstaller as admin is not necessary nor sensible. Run PyInstaller from a non-administrator terminal. PyInstaller 7.0 will block this.
522 INFO: PyInstaller: 6.16.0, contrib hooks: 2025.9
523 INFO: Python: 3.10.5
556 INFO: Platform: Windows-10-10.0.19044-SP0
556 INFO: Python environment: C:\Python310
560 INFO: wrote C:\Users\XXXXX\開発技術\Python（パイソン）\PythonGUI\main.spec
581 INFO: Module search paths (PYTHONPATH):
['C:\\Users\\XXXXX\\開発技術\\Python（パイソン）\\PythonGUI',
 'C:\\Python310\\python310.zip',
 'C:\\Python310\\DLLs',
 'C:\\Python310\\lib',
 'C:\\Python310',
 'C:\\Users\\XXXXX\\AppData\\Roaming\\Python\\Python310\\site-packages',
 'C:\\Python310\\lib\\site-packages',
 'C:\\Users\\XXXXX\\開発技術\\Python（パイソン）\\PythonGUI']
1537 INFO: checking Analysis
1549 INFO: Building because C:\Users\XXXXX\開発技術\Python（パイソン）\PythonGUI\main.py changed
1550 INFO: Looking for Python shared library...
1551 INFO: Using Python shared library: C:\Python310\python310.dll
1552 INFO: Running Analysis Analysis-00.toc
1553 INFO: Target bytecode optimization level: 0
1553 INFO: Initializing module dependency graph...
1559 INFO: Initializing module graph hook caches...
1685 INFO: Analyzing modules for base_library.zip ...
4381 INFO: Processing standard module hook 'hook-heapq.py' from 'C:\\Python310\\lib\\site-packages\\PyInstaller\\hooks'
4619 INFO: Processing standard module hook 'hook-encodings.py' from 'C:\\Python310\\lib\\site-packages\\PyInstaller\\hooks'
9859 INFO: Processing standard module hook 'hook-pickle.py' from 'C:\\Python310\\lib\\site-packages\\PyInstaller\\hooks'
13829 INFO: Caching module dependency graph...
13962 INFO: Analyzing C:\Users\XXXXX\開発技術\Python（パイソン）\PythonGUI\main.py
15478 INFO: Processing standard module hook 'hook-_ctypes.py' from 'C:\\Python310\\lib\\site-packages\\PyInstaller\\hooks'
15710 INFO: Processing standard module hook 'hook-platform.py' from 'C:\\Python310\\lib\\site-packages\\PyInstaller\\hooks'
16097 INFO: Processing standard module hook 'hook-sysconfig.py' from 'C:\\Python310\\lib\\site-packages\\PyInstaller\\hooks'
16938 INFO: Processing pre-find-module-path hook 'hook-tkinter.py' from 'C:\\Python310\\lib\\site-packages\\PyInstaller\\hooks\\pre_find_module_path'
16945 INFO: TclTkInfo: initializing cached Tcl/Tk info...
18017 INFO: Processing standard module hook 'hook-_tkinter.py' from 'C:\\Python310\\lib\\site-packages\\PyInstaller\\hooks'
18805 INFO: Processing standard module hook 'hook-difflib.py' from 'C:\\Python310\\lib\\site-packages\\PyInstaller\\hooks'
19457 INFO: Processing module hooks (post-graph stage)...
19472 INFO: Processing standard module hook 'hook-_tkinter.py' from 'C:\\Python310\\lib\\site-packages\\PyInstaller\\hooks'
19510 INFO: Performing binary vs. data reclassification (923 entries)
27230 INFO: Looking for ctypes DLLs
27307 INFO: Analyzing run-time hooks ...
27311 INFO: Including run-time hook 'pyi_rth_inspect.py' from 'C:\\Python310\\lib\\site-packages\\PyInstaller\\hooks\\rthooks'
27322 INFO: Including run-time hook 'pyi_rth__tkinter.py' from 'C:\\Python310\\lib\\site-packages\\PyInstaller\\hooks\\rthooks'
27335 INFO: Including run-time hook 'pyi_rth_pkgutil.py' from 'C:\\Python310\\lib\\site-packages\\PyInstaller\\hooks\\rthooks'
27442 INFO: Creating base_library.zip...
27495 INFO: Looking for dynamic libraries
28390 INFO: Extra DLL search directories (AddDllDirectory): []
28391 INFO: Extra DLL search directories (PATH): []
30139 INFO: Warnings written to C:\Users\XXXXX\開発技術\Python（パイソン）\PythonGUI\build\main\warn-main.txt
30226 INFO: Graph cross-reference written to C:\Users\XXXXX\開発技術\Python（パイソン）\PythonGUI\build\main\xref-main.html
30338 INFO: checking PYZ
30343 INFO: Building because toc changed
30343 INFO: Building PYZ (ZlibArchive) C:\Users\XXXXX\開発技術\Python（パイソン）\PythonGUI\build\main\PYZ-00.pyz
31001 INFO: Building PYZ (ZlibArchive) C:\Users\XXXXX\開発技術\Python（パイソン）\PythonGUI\build\main\PYZ-00.pyz completed successfully.
31089 INFO: checking PKG
31098 INFO: Building because toc changed
31098 INFO: Building PKG (CArchive) main.pkg
39423 INFO: Building PKG (CArchive) main.pkg completed successfully.
39494 INFO: Bootloader C:\Python310\lib\site-packages\PyInstaller\bootloader\Windows-64bit-intel\run.exe
39494 INFO: checking EXE
39501 INFO: Building because toc changed
39502 INFO: Building EXE from EXE-00.toc
39508 INFO: Copying bootloader EXE to C:\Users\XXXXX\開発技術\Python（パイソン）\PythonGUI\dist\main.exe
39645 INFO: Copying icon to EXE
39723 INFO: Copying 0 resources to EXE
39724 INFO: Embedding manifest in EXE
39803 INFO: Appending PKG archive to EXE
40738 INFO: Fixing EXE headers
42391 INFO: Building EXE from EXE-00.toc completed successfully.
42425 INFO: Build complete! The results are available in: C:\Users\XXXXX\開発技術\Python（パイソン）\PythonGUI\dist
```

### Windows10開発環境『MSDOSプロンプト』で、
### コンパイルした後にexeファイルを作成する方法

＜＜シナリオ１＞＞
```
１．コンパイルしたいパイソン3.9の配下に移動する。
cd C:\Python39\Lib\site-packages

２．コンパイルを実行してexeファイルを作成する。
py -m PyInstaller C:\Users\XXXXX\test\main.py
```

＜＜シナリオ１のexeファイル実行結果＞＞
C:\Python39\Lib\site-packages\main\dist\main>C:\Python39\Lib\site-packages\main\dist\main\main
Hi, PyCharm

＜＜シナリオ２＞＞
```
１．コンパイルしたいパイソンの配下に移動する。
    cd C:\Users\XXXXX\test\

２．コンパイルを実行してexeファイルを作成する。
    py -m  PyInstaller main.py --onefile

    最後に「INFO: Building EXE from EXE-00.toc completed successfully.」と出ていればexe作成は成功です。
    (*'▽')(*'▽')(*'▽')(*'▽')(*'▽')(*'▽')(*'▽')(*'▽')(*'▽')(*'▽')(*'▽')(*'▽')(*'▽')
```

＜＜シナリオ２のコンパイル実行結果＞＞
```
cd C:\Users\XXXXX\test\
C:\Users\XXXXX\test>py -m  PyInstaller main.py --onefile
1203 INFO: PyInstaller: 4.10
1203 INFO: Python: 3.9.1
1203 INFO: Platform: Windows-10-10.0.19041-SP0
1219 INFO: wrote C:\Users\XXXXX\test\main.spec
1234 INFO: UPX is not available.
1250 INFO: Extending PYTHONPATH with paths
['C:\\Users\\XXXXX\\PycharmProjects\\test']
2738 INFO: checking Analysis
2738 INFO: Building Analysis because Analysis-00.toc is non existent
2753 INFO: Initializing module dependency graph...
2759 INFO: Caching module graph hooks...
2854 INFO: Analyzing base_library.zip ...
16062 INFO: Processing pre-find module path hook distutils from 'C:\\Python39\\lib\\site-packages\\PyInstaller\\hooks\\pre_find_module_path\\hook-distutils.py'.
16072 INFO: distutils: retargeting to non-venv dir 'C:\\Python39\\lib'
28867 INFO: Caching module dependency graph...
29901 INFO: running Analysis Analysis-00.toc
29963 INFO: Adding Microsoft.Windows.Common-Controls to dependent assemblies of final executable
  required by C:\Python39\python.exe
32675 INFO: Analyzing C:\Users\XXXXX\test\main.py
32697 INFO: Processing module hooks...
32697 INFO: Loading module hook 'hook-difflib.py' from 'C:\\Python39\\lib\\site-packages\\PyInstaller\\hooks'...
32697 INFO: Loading module hook 'hook-distutils.py' from 'C:\\Python39\\lib\\site-packages\\PyInstaller\\hooks'...
32713 INFO: Loading module hook 'hook-distutils.util.py' from 'C:\\Python39\\lib\\site-packages\\PyInstaller\\hooks'...
32729 INFO: Loading module hook 'hook-encodings.py' from 'C:\\Python39\\lib\\site-packages\\PyInstaller\\hooks'...
33130 INFO: Loading module hook 'hook-heapq.py' from 'C:\\Python39\\lib\\site-packages\\PyInstaller\\hooks'...
33145 INFO: Loading module hook 'hook-lib2to3.py' from 'C:\\Python39\\lib\\site-packages\\PyInstaller\\hooks'...
33345 INFO: Loading module hook 'hook-multiprocessing.util.py' from 'C:\\Python39\\lib\\site-packages\\PyInstaller\\hooks'...
33361 INFO: Loading module hook 'hook-pickle.py' from 'C:\\Python39\\lib\\site-packages\\PyInstaller\\hooks'...
33361 INFO: Loading module hook 'hook-sysconfig.py' from 'C:\\Python39\\lib\\site-packages\\PyInstaller\\hooks'...
33377 INFO: Loading module hook 'hook-xml.etree.cElementTree.py' from 'C:\\Python39\\lib\\site-packages\\PyInstaller\\hooks'...
33377 INFO: Loading module hook 'hook-xml.py' from 'C:\\Python39\\lib\\site-packages\\PyInstaller\\hooks'...
33599 INFO: Loading module hook 'hook-_tkinter.py' from 'C:\\Python39\\lib\\site-packages\\PyInstaller\\hooks'...
34649 INFO: checking Tree
34649 INFO: Building Tree because Tree-00.toc is non existent
34665 INFO: Building Tree Tree-00.toc
35120 INFO: checking Tree
35120 INFO: Building Tree because Tree-01.toc is non existent
35120 INFO: Building Tree Tree-01.toc
35539 INFO: checking Tree
35539 INFO: Building Tree because Tree-02.toc is non existent
35545 INFO: Building Tree Tree-02.toc
35608 INFO: Looking for ctypes DLLs
35693 INFO: Analyzing run-time hooks ...
35708 INFO: Including run-time hook 'C:\\Python39\\lib\\site-packages\\PyInstaller\\hooks\\rthooks\\pyi_rth_subprocess.py'
35724 INFO: Including run-time hook 'C:\\Python39\\lib\\site-packages\\PyInstaller\\hooks\\rthooks\\pyi_rth_pkgutil.py'
35746 INFO: Including run-time hook 'C:\\Python39\\lib\\site-packages\\PyInstaller\\hooks\\rthooks\\pyi_rth_multiprocessing.py'
35777 INFO: Including run-time hook 'C:\\Python39\\lib\\site-packages\\PyInstaller\\hooks\\rthooks\\pyi_rth_inspect.py'
35808 INFO: Looking for dynamic libraries
36865 INFO: Looking for eggs
36865 INFO: Using Python library C:\Python39\python39.dll
36865 INFO: Found binding redirects:
[]
36881 INFO: Warnings written to C:\Users\XXXXX\test\build\main\warn-main.txt
37097 INFO: Graph cross-reference written to C:\Users\XXXXX\test\build\main\xref-main.html
37250 INFO: checking PYZ
37250 INFO: Building PYZ because PYZ-00.toc is non existent
37250 INFO: Building PYZ (ZlibArchive) C:\Users\XXXXX\test\build\main\PYZ-00.pyz
39758 INFO: Building PYZ (ZlibArchive) C:\Users\XXXXX\test\build\main\PYZ-00.pyz completed successfully.
39821 INFO: checking PKG
39821 INFO: Building PKG because PKG-00.toc is non existent
39821 INFO: Building PKG (CArchive) main.pkg
56581 INFO: Building PKG (CArchive) main.pkg completed successfully.
56596 INFO: Bootloader C:\Python39\lib\site-packages\PyInstaller\bootloader\Windows-64bit\run.exe
56596 INFO: checking EXE
56612 INFO: Building EXE because EXE-00.toc is non existent
56612 INFO: Building EXE from EXE-00.toc
56612 INFO: Copying bootloader EXE to C:\Users\XXXXX\test\dist\main.exe.notanexecutable
56797 INFO: Copying icon to EXE
56797 INFO: Copying icons from ['C:\\Python39\\lib\\site-packages\\PyInstaller\\bootloader\\images\\icon-console.ico']
56881 INFO: Writing RT_GROUP_ICON 0 resource with 104 bytes
56881 INFO: Writing RT_ICON 1 resource with 3752 bytes
56881 INFO: Writing RT_ICON 2 resource with 2216 bytes
56897 INFO: Writing RT_ICON 3 resource with 1384 bytes
56897 INFO: Writing RT_ICON 4 resource with 37019 bytes
56897 INFO: Writing RT_ICON 5 resource with 9640 bytes
56897 INFO: Writing RT_ICON 6 resource with 4264 bytes
56897 INFO: Writing RT_ICON 7 resource with 1128 bytes
56997 INFO: Copying 0 resources to EXE
57013 INFO: Emedding manifest in EXE
57013 INFO: Updating manifest in C:\Users\XXXXX\test\dist\main.exe.notanexecutable
57029 INFO: Updating resource type 24 name 1 language 0
57051 INFO: Appending PKG archive to EXE
66557 INFO: Building EXE from EXE-00.toc completed successfully.
```

### JetBrains社のPython開発環境『PyCharm』（パイチャーム）で、
### Terminalウィンドウ（ターミナル・ウィンドウ）でのコンパイルを実施する場合

＜＜シナリオ＞＞
```
cd C:\Python39\Lib\site-packages
py -m PyInstaller C:\Users\XXXXX\test\main.py
```

＜＜実行結果＞＞
```
PS C:\Python39\Lib\site-packages> py -m PyInstaller C:\Users\XXXXX\test\main.py
563 INFO: PyInstaller: 4.10
563 INFO: Python: 3.9.1
563 INFO: Platform: Windows-10-10.0.19041-SP0
594 INFO: wrote C:\Python39\Lib\site-packages\main\main.spec
612 INFO: UPX is not available.
614 INFO: Extending PYTHONPATH with paths
['C:\\Users\\XXXXX\\PycharmProjects\\test']
1609 INFO: checking Analysis
1609 INFO: Building Analysis because Analysis-00.toc is non existent
1609 INFO: Initializing module dependency graph...
1625 INFO: Caching module graph hooks...
1710 INFO: Analyzing base_library.zip ...
13494 INFO: Processing pre-find module path hook distutils from 'C:\\Python39\\Lib\\site-packages\\PyInstaller\\hooks\\pre_find_module_path\\hook-distutils.py'.
13513 INFO: distutils: retargeting to non-venv dir 'C:\\Python39\\lib'
23082 INFO: Caching module dependency graph...
24269 INFO: running Analysis Analysis-00.toc
24285 INFO: Adding Microsoft.Windows.Common-Controls to dependent assemblies of final executable
  required by C:\Python39\python.exe
25689 INFO: Analyzing C:\Users\XXXXX\test\main.py
25705 INFO: Processing module hooks...
25705 INFO: Loading module hook 'hook-difflib.py' from 'C:\\Python39\\Lib\\site-packages\\PyInstaller\\hooks'...
25705 INFO: Loading module hook 'hook-distutils.py' from 'C:\\Python39\\Lib\\site-packages\\PyInstaller\\hooks'...
25705 INFO: Loading module hook 'hook-distutils.util.py' from 'C:\\Python39\\Lib\\site-packages\\PyInstaller\\hooks'...
25720 INFO: Loading module hook 'hook-encodings.py' from 'C:\\Python39\\Lib\\site-packages\\PyInstaller\\hooks'...
26137 INFO: Loading module hook 'hook-heapq.py' from 'C:\\Python39\\Lib\\site-packages\\PyInstaller\\hooks'...
26146 INFO: Loading module hook 'hook-lib2to3.py' from 'C:\\Python39\\Lib\\site-packages\\PyInstaller\\hooks'...
26375 INFO: Loading module hook 'hook-multiprocessing.util.py' from 'C:\\Python39\\Lib\\site-packages\\PyInstaller\\hooks'...
26375 INFO: Loading module hook 'hook-pickle.py' from 'C:\\Python39\\Lib\\site-packages\\PyInstaller\\hooks'...
26391 INFO: Loading module hook 'hook-sysconfig.py' from 'C:\\Python39\\Lib\\site-packages\\PyInstaller\\hooks'...
26391 INFO: Loading module hook 'hook-xml.etree.cElementTree.py' from 'C:\\Python39\\Lib\\site-packages\\PyInstaller\\hooks'...
26406 INFO: Loading module hook 'hook-xml.py' from 'C:\\Python39\\Lib\\site-packages\\PyInstaller\\hooks'...
26607 INFO: Loading module hook 'hook-_tkinter.py' from 'C:\\Python39\\Lib\\site-packages\\PyInstaller\\hooks'...
27247 INFO: checking Tree
27247 INFO: Building Tree because Tree-00.toc is non existent
27247 INFO: Building Tree Tree-00.toc
27663 INFO: checking Tree
27663 INFO: Building Tree because Tree-01.toc is non existent
27663 INFO: Building Tree Tree-01.toc
28127 INFO: checking Tree
28127 INFO: Building Tree because Tree-02.toc is non existent
28127 INFO: Building Tree Tree-02.toc
28207 INFO: Looking for ctypes DLLs
28296 INFO: Analyzing run-time hooks ...
28296 INFO: Including run-time hook 'C:\\Python39\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks\\pyi_rth_subprocess.py'
28311 INFO: Including run-time hook 'C:\\Python39\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks\\pyi_rth_pkgutil.py'
28327 INFO: Including run-time hook 'C:\\Python39\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks\\pyi_rth_multiprocessing.py'
28349 INFO: Including run-time hook 'C:\\Python39\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks\\pyi_rth_inspect.py'
28380 INFO: Looking for dynamic libraries
28966 INFO: Looking for eggs
28966 INFO: Using Python library C:\Python39\python39.dll
28966 INFO: Found binding redirects:
[]
28982 INFO: Warnings written to C:\Python39\Lib\site-packages\main\build\main\warn-main.txt
29174 INFO: Graph cross-reference written to C:\Python39\Lib\site-packages\main\build\main\xref-main.html
29237 INFO: checking PYZ
29237 INFO: Building PYZ because PYZ-00.toc is non existent
29237 INFO: Building PYZ (ZlibArchive) C:\Python39\Lib\site-packages\main\build\main\PYZ-00.pyz
31462 INFO: Building PYZ (ZlibArchive) C:\Python39\Lib\site-packages\main\build\main\PYZ-00.pyz completed successfully.
31509 INFO: checking PKG
31509 INFO: Building PKG because PKG-00.toc is non existent
31515 INFO: Building PKG (CArchive) main.pkg
31616 INFO: Building PKG (CArchive) main.pkg completed successfully.
31631 INFO: Bootloader C:\Python39\Lib\site-packages\PyInstaller\bootloader\Windows-64bit\run.exe
31631 INFO: checking EXE
31631 INFO: Building EXE because EXE-00.toc is non existent
31631 INFO: Building EXE from EXE-00.toc
31839 INFO: Copying icon to EXE
31839 INFO: Copying icons from ['C:\\Python39\\Lib\\site-packages\\PyInstaller\\bootloader\\images\\icon-console.ico']
31847 INFO: Writing RT_GROUP_ICON 0 resource with 104 bytes
31847 INFO: Writing RT_ICON 1 resource with 3752 bytes
31847 INFO: Writing RT_ICON 2 resource with 2216 bytes
31847 INFO: Writing RT_ICON 3 resource with 1384 bytes
31847 INFO: Writing RT_ICON 4 resource with 37019 bytes
31847 INFO: Writing RT_ICON 5 resource with 9640 bytes
31847 INFO: Writing RT_ICON 6 resource with 4264 bytes
31857 INFO: Writing RT_ICON 7 resource with 1128 bytes
31949 INFO: Copying 0 resources to EXE
31949 INFO: Emedding manifest in EXE
31949 INFO: Updating manifest in C:\Python39\Lib\site-packages\main\build\main\main.exe.notanexecutable
31959 INFO: Updating resource type 24 name 1 language 0
32137 INFO: Appending PKG archive to EXE
35369 INFO: Building EXE from EXE-00.toc completed successfully.
35400 INFO: checking COLLECT
35400 INFO: Building COLLECT because COLLECT-00.toc is non existent
35400 INFO: Building COLLECT COLLECT-00.toc
36775 INFO: Building COLLECT COLLECT-00.toc completed successfully.
```

最後に「INFO: Building EXE from EXE-00.toc completed successfully.」と出ていれば完了です。
(*'▽')

<img width="1223" height="639" alt="image" src="https://github.com/user-attachments/assets/6d0dc960-215f-4ca7-a685-f9a69f0e5ed3" />

### 参考本：
data:image/jpeg;base64,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
