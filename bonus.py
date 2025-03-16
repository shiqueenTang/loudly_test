import os

import cv2
import librosa
from moviepy.editor import VideoFileClip, AudioFileClip


audio_path = "src/loudly.mp3"

video_out_path = "output_opencv.avi"
final_out_path = "final_with_audio.mp4"
fps = 10
frame_size = (320, 240)

# === GET BEAT TIME ===
y, sr = librosa.load(audio_path)
onsets = librosa.onset.onset_detect(y=y, sr=sr, backtrack=True)
onset_times = librosa.frames_to_time(onsets, sr=sr)

# === GET EACH FRAME ===
img_path_list = []
for i in range(2):
    for j in range(4):
        img_path_list.append(f"src/{i+1}_{j+1}.jpg")

img_list = []
for img_path in img_path_list:
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"Image file not found: {img_path}")
    img = cv2.imread(img_path)
    img_list.append(cv2.resize(img, frame_size))

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
writer = cv2.VideoWriter(video_out_path, fourcc, fps, frame_size)

if not writer.isOpened():
    raise ValueError("VideoWriter failed to open. Check the codec and output path.")

total_duration = librosa.get_duration(y=y, sr=sr)
total_frames = int(total_duration * fps)

# === ARRANGE FRAMES ===
onset_frames = [int(t * fps) for t in onset_times]
onset_frames.append(total_frames + 1)

current_img = img_list[0]
idx = 0
for f in range(total_frames):
    if f >= onset_frames[idx]:
        idx += 1
        if idx < 5:
            if idx == 1:
                current_img = img_list[0]
            elif idx == 2:
                current_img = img_list[1]
            elif idx == 3:
                current_img = img_list[2]
            elif idx == 4:
                current_img = img_list[3]
        elif idx % 4 == 1:
            current_img = img_list[4]
        elif idx % 4 == 2:
            current_img = img_list[5]
        elif idx % 4 == 3:
            current_img = img_list[6]
        elif idx % 4 == 0:
            current_img = img_list[7]
    writer.write(current_img)
writer.release()

# === ADD MUSIX ===
video_clip = VideoFileClip(video_out_path)
audio_clip = AudioFileClip(audio_path)
final_clip = video_clip.set_audio(audio_clip)
final_clip.write_videofile(final_out_path, fps=fps)
