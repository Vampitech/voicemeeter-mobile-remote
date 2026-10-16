"""Patch para MeeterLink: servir la PWA móvil en /mobile/.

Reemplaza el bloque final de main.py de MeeterLink por este bloque,
o aplica los cambios indicados en PATCH.md.
"""

PATCH = r"""
# Busca este bloque al final de main.py:
#
# if __name__ == '__main__':
#     app = web.Application()
#     app.router.add_get('/', index)
#     app.router.add_get('/ws', websocket_handler)
#     app.router.add_static('/', path=os.path.join(FILE_DIR, 'web'), name='web')
#
# Y reemplázalo por:

if __name__ == '__main__':
    app = web.Application()

    async def mobile_index(request):
        return web.FileResponse(os.path.join(FILE_DIR, 'web', 'mobile', 'index.html'))

    app.router.add_get('/', index)
    app.router.add_get('/mobile', mobile_index)
    app.router.add_get('/mobile/', mobile_index)
    app.router.add_get('/ws', websocket_handler)
    app.router.add_static('/', path=os.path.join(FILE_DIR, 'web'), name='web')
"""
