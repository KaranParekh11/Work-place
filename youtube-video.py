
from pytube import YouTube

# link of the video to be downloaded
link="https://www.youtube.com/watch?v=b6GMwT35I38&list=PLAwxTw4SYaPk8_-6IGxJtD3i2QAu5_s_p&index=44"
yt = YouTube(link)

try:
	yt.streams.filter(progressive=True,file_extension="mp4").first().download(output_path="E:\KARAN PY",
															 filename="github.mp4")
except:
	print("Connection Error")
print('Task Completed!')
