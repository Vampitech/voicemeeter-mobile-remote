# Corrección: faders lentos y error `StripDenoiser`

Hay dos problemas distintos:

## 1. Error `float() argument must be a string or a real number, not 'StripDenoiser'`

Es un bug del `rec_strips` de MeeterLink. Aunque la app no envíe `denoiser`, esta línea intenta asignar el objeto completo como valor:

```python
strip.denoiser.knob = data['values'].get('denoiser', strip.denoiser)
```

### Corrección

En `main.py` de MeeterLink, busca:

```python
if hasattr(strip, 'denoiser'):
    strip.denoiser.knob = data['values'].get('denoiser', strip.denoiser)
```

Y reemplázalo por:

```python
if hasattr(strip, 'denoiser') and 'denoiser' in data['values']:
    strip.denoiser.knob = data['values']['denoiser']
```

## 2. Actualización de ganancia casi en tiempo real

Para que un movimiento de fader que solo cambia `gain` no pase por todo el bloque de actualización —ni por el bug del denoiser—, añade este bloque al inicio de `rec_strips`, justo después de `strip = server['vm'].strip[data['index']]`:

```python
if set(data['values'].keys()) == {'gain'}:
    strip.gain = data['values']['gain']
    return
```

El bloque debe quedar así:

```python
async def rec_strips(ws, data):
    try:
        strip = server['vm'].strip[data['index']]

        if set(data['values'].keys()) == {'gain'}:
            strip.gain = data['values']['gain']
            return

        strip.label = data['values'].get('label', strip.label)
        # ... el resto sigue igual
```

Haz lo mismo para `rec_busses`, después de obtener el bus:

```python
async def rec_busses(ws, data):
    try:
        bus = server['vm'].bus[data['index']]

        if set(data['values'].keys()) == {'gain'}:
            bus.gain = data['values']['gain']
            return

        bus.label = data['values'].get('label', bus.label)
        # ... el resto sigue igual
```

## 3. Revisar `config.toml`

Abre `config.toml` de MeeterLink y busca `polling_interval`. Para que la interfaz reciba el estado con más frecuencia, usa:

```toml
[general]
polling_interval = 0.05
```

Y, si existe:

```tomn
[levels]
polling_interval = 0.05
```

Esto mejora la frecuencia de refresco de estado y medidores; la corrección del `gain` es la que elimina la espera al aplicar el volumen.

## Después del cambio

1. Guarda `main.py` y `config.toml`.
2. Cierra MeeterLink completamente.
3. Vuelve a ejecutarlo.
4. Recarga la PWA en el móvil, idealmente borrando datos del sitio para invalidar el service worker.
