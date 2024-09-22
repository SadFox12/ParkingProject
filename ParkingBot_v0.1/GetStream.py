import subprocess

# URL потока
stream_url = "https://cctv.tmpk.net/entuziastov.1512.parkovka.na.entuziastov-ccb5aca411/index.fmp4.m3u8?token=3.ihzhG497AAAAAAAAAAEABeMyAzO0Xs7qTEMli4PIvCR3v9lg-hgPvd8B"

# Путь к ffmpeg
ffmpeg_path = "F:/ffmpeg/ffmpeg-7.0.2-essentials_build/bin/ffmpeg.exe"

# Имя файла для скриншота
output_image = "screenshot.png"

# Команда для создания скриншота
command = [
    ffmpeg_path,
    '-y',                  # Автоматически перезаписывать выходной файл
    '-i', stream_url,
    '-ss', '00:00:05',    # Время, на котором нужно сделать скриншот (5 секунд)
    '-vframes', '1',      # Количество кадров для захвата
    output_image
]

# Выполняем команду
subprocess.run(command)

print(f"Скриншот сохранен как {output_image}.")
