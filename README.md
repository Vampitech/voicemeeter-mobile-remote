# Voicemeeter Mobile Remote

PWA móvil para controlar Voicemeeter mediante el backend WebSocket de [MeeterLink / voicemeeter-web-remote](https://github.com/Loewe111/voicemeeter-web-remote).

## Probar en el móvil

1. Ejecuta MeeterLink en el PC con Voicemeeter.
2. Copia el contenido de `mobile/` en `web/mobile/` dentro de MeeterLink.
3. Abre `http://IP-DEL-PC:8080/mobile/` en Chrome Android.
4. Introduce la IP si hace falta y pulsa **Conectar**.
5. Usa **Instalar aplicación** para añadirla a la pantalla de inicio.

## Funciones

- Escenas rápidas.
- Faders táctiles.
- Mute, solo y mono.
- Ruteos A/B.
- Medidores.
- Reconexión automática.
- PWA instalable.

La aplicación utiliza el protocolo WebSocket existente de MeeterLink y delega el control final a la API nativa de Voicemeeter.
