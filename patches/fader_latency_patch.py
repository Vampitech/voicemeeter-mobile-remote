"""Parche exacto para MeeterLink.

Aplica estos tres cambios en main.py:

1) Fast-path para updates que solo cambian gain.
2) No tocar denoiser si la app no envia ese parametro.
3) Reducir polling_interval en config.toml.
"""

FAST_PATH_STRIP = '''
async def rec_strips(ws, data):
    try:
        strip = server['vm'].strip[data['index']]

        if set(data['values'].keys()) == {'gain'}:
            strip.gain = data['values']['gain']
            return
'''

FAST_PATH_BUS = '''
async def rec_busses(ws, data):
    try:
        bus = server['vm'].bus[data['index']]

        if set(data['values'].keys()) == {'gain'}:
            bus.gain = data['values']['gain']
            return
'''

DENOISER_FIX = '''
# ANTES:
# if hasattr(strip, 'denoiser'):
#     strip.denoiser.knob = data['values'].get('denoiser', strip.denoiser)

# DESPUÉS:
if hasattr(strip, 'denoiser') and 'denoiser' in data['values']:
    strip.denoiser.knob = data['values']['denoiser']
'''

CONFIG_FIX = '''
[general]
polling_interval = 0.05

[levels]
polling_interval = 0.05
'''
