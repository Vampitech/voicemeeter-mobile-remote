# Solución al error `Forbidden`

El error ocurre porque MeeterLink usa `aiohttp.static` para servir la carpeta `web/`. Ese servidor no entrega automáticamente `index.html` cuando abres una ruta de directorio como:

```text
http://IP:8080/mobile/
```

Por eso devuelve `403 Forbidden`.

## Solución rápida

Abre directamente el archivo:

```text
http://IP-DE-TU-PC:8080/mobile/index.html
```

Eso debería cargar la PWA sin modificar MeeterLink.

## Solución definitiva

Edita `main.py` de MeeterLink y localiza este bloque al final:

```python
if __name__ == '__main__':
    app = web.Application()
    app.router.add_get('/', index)
    app.router.add_get('/ws', websocket_handler)
    app.router.add_static('/', path=os.path.join(FILE_DIR, 'web'), name='web')
```

Reemplázalo por:

```python
if __name__ == '__main__':
    app = web.Application()

    async def mobile_index(request):
        return web.FileResponse(
            os.path.join(FILE_DIR, 'web', 'mobile', 'index.html')
        )

    app.router.add_get('/', index)
    app.router.add_get('/mobile', mobile_index)
    app.router.add_get('/mobile/', mobile_index)
    app.router.add_get('/ws', websocket_handler)
    app.router.add_static('/', path=os.path.join(FILE_DIR, 'web'), name='web')
```

Guarda, reinicia MeeterLink y abre:

```text
http://IP-DE-TU-PC:8080/mobile/
```

La ruta `/mobile/index.html` también seguirá funcionando.
