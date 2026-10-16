# Generar un EXE único

Este empaquetado crea `MeeterLinkMobile.exe`: un ejecutable de Windows que incluye el backend de MeeterLink y la PWA móvil.

## Requisitos

- Windows 10 u 11.
- Python 3.11 o 3.12 en PATH.
- Git.
- Voicemeeter instalado.

## Build automático

Desde la raíz de este repositorio:

```bat
builder\build_windows.bat
```

El script:

1. Instala PyInstaller.
2. Clona o actualiza MeeterLink.
3. Copia `mobile/` a `meeterlink/web/mobile/`.
4. Compila `MeeterLinkMobile.exe`.

El resultado queda en:

```text
meeterlink\dist\MeeterLinkMobile.exe
```

## Parche obligatorio

Antes de compilar, aplica el parche de [`PATCH.md`](../PATCH.md) al archivo:

```text
meeterlink\main.py
```

Sin ese parche, la ruta `/mobile/` dará `403 Forbidden` y los faders pueden seguir con el error de `StripDenoiser`.

## Ejecutar

1. Copia `MeeterLinkMobile.exe` donde quieras.
2. Ejecútalo.
3. Acepta el firewall de Windows para redes privadas.
4. En el móvil abre:

```text
http://IP-DEL-PC:8080/mobile/
```

## Nota sobre un solo archivo

PyInstaller `--onefile` extrae temporalmente los recursos al ejecutar el programa. El arranque puede tardar unos segundos más que una carpeta normal, pero el resultado es un único `.exe` fácil de copiar o distribuir.

## Antivirus

Los ejecutables de PyInstaller a veces generan falsos positivos. Si vas a distribuirlo, considera compilar sin UPX o firmar el binario.
