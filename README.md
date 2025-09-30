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
```
Python 3.9.1
```
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

### 参考本：シゴトがはかどるPython自動処理の教科書
<a href="https://www.google.co.jp/books/edition/_/XEYUEAAAQBAJ?hl=ja&sa=X&ved=2ahUKEwja0OaLwIGQAxU9klYBHY7BNywQ8fIDegQIGBAF">
<img width="126" height="162" alt="image" src="https://github.com/user-attachments/assets/2c1605ab-2f6c-43c7-b7de-18f8c014b14e" />
</a>
