# Prepara una copia de MeeterLink con la PWA movil incluida.

if (-not (Test-Path .\meeterlink)) {
    git clone https://github.com/Loewe111/voicemeeter-web-remote.git .\meeterlink
}

Set-Location .\meeterlink
git pull
Set-Location ..

if (-not (Test-Path .\meeterlink\web\mobile)) {
    New-Item -ItemType Directory -Path .\meeterlink\web\mobile | Out-Null
}

Copy-Item -Path .\mobile\* -Destination .\meeterlink\web\mobile\ -Recurse -Force

Write-Host "MeeterLink preparado en .\meeterlink"
Write-Host "Aplica el parche de PATCH.md a .\meeterlink\main.py antes de compilar."
