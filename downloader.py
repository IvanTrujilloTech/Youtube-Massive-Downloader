import yt_dlp
import scrapetube
import os
import time
import re

def run_downloader(channel_url):
    print(f"\n[🔍] Analizando canal: {channel_url}")
    
    # 1. Obtener ID y Nombre del canal
    channel_id = None
    channel_name = "Descargas_Youtube"
    try:
        ydl_opts_info = {
            'extract_flat': True, 
            'quiet': True, 
            'no_warnings': True,
            'extractor_args': {'youtube': {'player_client': ['ios']}}
        }
        with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
            info = ydl.extract_info(channel_url, download=False)
            channel_id = info.get('id')
            channel_name = info.get('uploader') or info.get('channel') or "Canal_Desconocido"
    except Exception as e:
        print(f"[⚠️] No se pudo obtener metadatos extendidos: {str(e)}")

    if not channel_id:
        print("[❌] No se pudo obtener el ID del canal. Abortando.")
        return

    # Crear carpeta del canal
    folder_name = re.sub(r'[\\/*?:"<>|]', "", channel_name) # Limpiar nombre para Windows
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    print(f"[✅] Canal: {channel_name} ({channel_id})")
    print(f"[📂] Carpeta de destino: {os.path.abspath(folder_name)}")

    # 2. Obtener metadatos con Scrapetube
    print(f"[⚙️] Extrayendo metadatos de los videos...")
    videos_data = []
    try:
        vids = scrapetube.get_playlist("UU" + channel_id[2:])
        for v in vids:
            videos_data.append({
                'id': v['videoId'],
                'title': v['title']['runs'][0]['text']
            })
    except Exception as e:
        print(f"[⚠️] Error al listar videos: {str(e)}")

    total = len(videos_data)
    if total == 0:
        print("[❌] No se encontraron videos.")
        return

    print(f"[🚀] {total} videos detectados. Iniciando descarga en ALTA CALIDAD...\n")

    # 3. Configuración de descarga de alta calidad
    count = 1
    for video in videos_data:
        v_url = f"https://www.youtube.com/watch?v={video['id']}"
        clean_title = re.sub(r'[\\/*?:"<>|]', "", video['title']).strip()
        # Ruta dentro de la carpeta del canal
        filepath = os.path.join(folder_name, f"{clean_title}_{video['id']}.%(ext)s")
        
        print(f"[{count}/{total}] >> {video['title']}")
        
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best', # Forza la mejor calidad disponible
            'merge_output_format': 'mp4',
            'outtmpl': filepath,
            'quiet': True,
            'no_warnings': True,
            'nocheckcertificate': True,
            'ignoreerrors': True,
            'extractor_args': {
                'youtube': {
                    'player_client': ['android'],
                    'player_skip': ['webpage', 'configs', 'initial_data'],
                }
            },
            'http_headers': {
                'User-Agent': 'com.google.android.youtube/19.05.36 (Linux; U; Android 14; en_US; Pixel 8 Pro; Build/UQ1A.240205.002; Cronet/121.0.6167.71)',
            }
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                error_code = ydl.download([v_url])
                if error_code != 0:
                    print(f"   [⚠️] El video no se pudo bajar (posible bloqueo o falta de FFmpeg)")
        except Exception as e:
            print(f"   [❌] Error crítico: {str(e)}")
        
        count += 1

    print(f"\n\n[🏁] Proceso completado. Revisa la carpeta: {folder_name}")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*50)
    print("   YOUTUBE MASSIVE DOWNLOADER       ")
    print("             By @ivan_trujillo_tech        ")
    print("="*50)
    
    url = input("\n🔗 URL del Canal: ").strip()
    if url:
        run_downloader(url)
