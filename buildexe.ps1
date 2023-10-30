Write-Host "Package generate..." -ForegroundColor green

Copy-Item -Path ".\Readme.html" -Destination ".\dist\" -Force
Copy-Item -Path ".\version.md" -Destination ".\dist\" -Force
pyinstaller.exe --onefile --icon=.\resource\images\logo\logo.ico --add-data="Readme.html;." --name=PTool -Fw .\PTool.py
