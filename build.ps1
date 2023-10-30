Write-Host "Pyqt5 build..." -ForegroundColor green

# pyrccc
pyrcc5.exe ./resource/resource.qrc -o resource_rc.py

# designer
# designer.exe .\View\main_window\main.ui

# compile
pyuic5.exe ./View/main_window/main.ui -o ./View/main_window/ui_main.py -x
pyuic5.exe ./View/tab_unit/tab_unit.ui -o ./View/tab_unit/ui_tab_unit.py -x
pyuic5.exe ./View/tab_dev/tab_dev.ui -o ./View/tab_dev/ui_tab_dev.py -x
pyuic5.exe ./View/sub_parse_index/parse_index.ui -o ./View/sub_parse_index/ui_parse_index.py -x
pyuic5.exe ./View/help_widget/help.ui -o ./View/help_widget/ui_help.py -x

# language
pylupdate5 .\View\main_window\ui_main.py ./View/tab_unit/ui_tab_unit.py ./View/tab_dev/ui_tab_dev.py ./View/sub_parse_index/ui_parse_index.py ./View/help_widget/ui_help.py -ts .\resource\i18n\ptool.zh_CN.ts
# linguist.exe .\resource\i18n\ptool.zh_CN.ts 
lrelease .\resource\i18n\ptool.zh_CN.ts

python PTool.py

