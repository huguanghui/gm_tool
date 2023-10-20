Write-Host "Pyqt5 build..." -ForegroundColor green

# pyrccc
pyrcc5.exe ./resource/resource.qrc -o ./common/resource.py

# designer
# designer.exe .\View\main_window\main.ui

# compile
pyuic5.exe ./View/main_window/main.ui -o ./View/main_window/ui_main.py -x
# pyuic5.exe ./View/page01/page01.ui -o ./View/page01/ui_page01.py -x
# pyuic5.exe ./View/page02/page02.ui -o ./View/page02/ui_page02.py -x

# language
pylupdate5 .\View\main_window\ui_main.py -ts .\resource\i18n\ptool.zh_CN.ts
# linguist.exe .\resource\i18n\ptool.zh_CN.ts 
lrelease .\resource\i18n\ptool.zh_CN.ts

python PTool.py

