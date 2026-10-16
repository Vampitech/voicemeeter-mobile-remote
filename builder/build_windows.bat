@echo off
setlocal

where python >nul 2>nul
if errorlevel 1 (
  echo Python no esta instalado o no esta en PATH.
  pause
  exit /b 1
)

python -m pip install --upgrade pip
python -m pip install -r builder/requirements-build.txt

if not exist meeterlink (
  git clone https://github.com/Loewe111/voicemeeter-web-remote.git meeterlink
)

cd meeterlink
git pull
cd ..

if not exist meeterlink\web\mobile mkdir meeterlink\web\mobile
xcopy /E /I /Y mobile meeterlink\web\mobile

cd meeterlink
pyinstaller --noconfirm --clean ..\builder\meeterlink_mobile.spec
cd ..

echo.
echo EXE generado en:
echo meeterlink\dist\MeeterLinkMobile.exe
pause
