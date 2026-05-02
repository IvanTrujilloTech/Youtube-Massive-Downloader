# 🚀 YouTube Massive Downloader

![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)
![FFmpeg](https://img.shields.io/badge/FFmpeg-Required-red.svg)
![Status](https://img.shields.io/badge/status-Stable-green.svg)

**YouTube Massive Downloader** es una herramienta de ingeniería inversa diseñada para la descarga masiva de canales completos. Utiliza una arquitectura de **"Capa Híbrida Anónima"** que permite saltar las protecciones más agresivas de Google sin necesidad de cookies ni autenticación manual.

## 🛠️ ¿Por qué esta versión es única?

La mayoría de descargadores (incluyendo `yt-dlp` básico) fallan hoy en día con errores como *403 Forbidden* o *Sign in to confirm you're not a bot*. Este software soluciona esto dividiendo el proceso en dos fases aisladas:

1.  **Extracción de Metadatos (Scrapetube)**: Obtiene los IDs y Títulos mediante peticiones JSON puras de la API de YouTube, sin cargar scripts de rastreo ni interfaces web.
2.  **Entrega Blindada (yt-dlp + Android App Profile)**: Realiza el streaming simulando ser una aplicación oficial de **Android (Pixel 8 Pro)**, saltándose el renderizado de página que activa los bloqueos de "Reload page".

## ✨ Características Estrellas

*   **📁 Auto-Folder System**: Crea automáticamente carpetas con el nombre del canal y organiza los videos dentro.
*   **🎥 High Definition (1080p/4K)**: Prioriza la máxima calidad disponible (requiere FFmpeg).
*   **🛡️ Stealth Mode**: No requiere cookies del navegador, evitando el riesgo de baneo de cuentas personales.
*   **⚡ Bypass de Firma (PO Token)**: Utiliza perfiles de dispositivos móviles para saltar la validación de tokens de navegador.

## 📋 Requisitos Críticos

Este software es una "bestia", pero necesita sus herramientas:

1.  **Python 3.9+**
2.  **FFmpeg** (OBLIGATORIO para calidad >720p):
    *   Windows: `winget install ffmpeg`
    *   Linux: `sudo apt install ffmpeg`

## 🚀 Guía de Inicio Rápido

1.  **Instalar dependencias**:
    ```bash
    pip install yt-dlp scrapetube
    ```
2.  **Ejecutar el script**:
    ```bash
    python downloader.py
    ```
3.  **Introducir URL**: Pega el enlace del canal (ej: `https://www.youtube.com/@CanalEjemplo`) y disfruta.

## 🔧 Solución de Problemas

| Problema | Causa | Solución |
| :--- | :--- | :--- |
| **Baja Calidad (360p/720p)** | Falta FFmpeg | Ejecuta `winget install ffmpeg` y reinicia tu terminal. |
| **Error en metadatos** | Bloqueo de IP temporal | Reinicia tu router para obtener una nueva IP. |
| **No encuentra el canal** | URL incorrecta | Asegúrate de usar el formato `@nombreusuario`. |

## ⚠️ Nota Legal

Este proyecto tiene fines exclusivamente educativos y de copia de seguridad personal. El autor no se hace responsable del uso que se le dé a esta herramienta. Respeta siempre los derechos de autor y los términos de servicio de la plataforma.

---
**Desarrollado por @IvanTrujilloTech**
