import librosa
from datetime import datetime
import os
from moviepy.editor import *

media_file = input("Kéo thả file nhạc hoặc video vào đây: ")

media_rm_quotes = media_file.replace('"','')

audio_file = media_rm_quotes

if os.path.splitext(os.path.basename(media_rm_quotes))[1] in {".mp4", ".avi", ".mov", ".wmv", ".flv", ".mkv", ".mpeg", ".webm"} : 
    # nhận dạng file video
    print("Phát hiện video! Sẽ tự động chuyển sang .mp3")
    video_file = media_rm_quotes
    audio_file = os.path.splitext(video_file)[0] + ".mp3"
    video = VideoFileClip(video_file)
    video.audio.write_audiofile(audio_file)


audio_file_name = os.path.basename(media_rm_quotes)
output_file_name = os.path.splitext(audio_file_name)[0] + '_output.tsv'
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
output_path = os.path.join(desktop_path, output_file_name)


y, sr = librosa.load(audio_file)
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

# Tạo danh sách các thời điểm beat
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# Mở file tệp tsv để ghi dữ liệu
output_file = open(output_path, 'w')

# Ghi dữ liệu vào tệp tsv
for i in range(len(beat_times) - 1):
    start_time = datetime.utcfromtimestamp(beat_times[i]).strftime('%H:%M:%S,%f')[:-3]
    end_time = datetime.utcfromtimestamp(beat_times[i + 1]).strftime('%H:%M:%S,%f')[:-3]
    line = f"{start_time}\t{end_time}\t\n"
    output_file.write(line)

# Đóng tệp tsv
output_file.close()
print(f"Đã xuất ra file .tsv | Đường dẫn: {output_path}")







