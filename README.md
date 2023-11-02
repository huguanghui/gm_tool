
## 打包

```
$ pyinstaller.exe --onefile --icon=.\resource\images\logo\logo.ico --name=PTool -Fw .\PTool.py
$ pyinstaller.exe PTool.spec --noconfirm
```

pylupdate5 .\View\main_window\ui_main.py .\View\page01\ui_page01.py -ts .\resource\i18n\ptool.zh_CN.ts
lrelease.exe .\resource\i18n\ptool.zh_CN.ts

pip freeze > requirements.txt

## 文档

$ pandoc.exe --standalone .\doc\Readme.md -o .\Readme.html
