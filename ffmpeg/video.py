from moviepy.editor import *
import subprocess

title2 = '这究竟是什么猫啊？！'
title3 = '这究竟是什么猫啊？！'
titles = '这究竟是什么猫啊？！-已剪辑'

video_path = f'D:\\B站视频\\{title2}\\{title3}.mp4'

video_clip0 = VideoFileClip(video_path)

# 定义剪辑的起始和结束时间（以秒为单位）
start_time = 5
end_time = 20

# 对视频进行剪辑
clipped_video = video_clip0.subclip(start_time, end_time)

new_video = clipped_video.crop(x1=10, y1=50, x2=500, y2=940)
print(new_video)
video_path_1 = f'D:\\B站视频\\{title2}\\{titles}.mp4'

try:
    new_video.write_videofile(video_path_1, audio=True)
    print("裁剪并导出成功！")
except Exception as e:
    print(f"裁剪或导出失败：{e}")

#
# cmd = f'ffmpeg -i {video_path_1} -i {audio_path_1} -acodec copy -vcodec copy {video_path_1}'
# aa = subprocess.call(cmd, shell=True)


