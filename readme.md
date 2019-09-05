### the challange
The reason of this challenge is to provide candidates with the opportunity to demonstrate their analytical skills when presented with a Research & Development challenge.
Objective:
The main objectives of this challenge are:
Stream a video file to Facebook on a 1/1 format including this a logo overlay on the top right corner using 100x100 pixels of the available video.
The file should not be pre-converted to any other format (i.e. the video should be converted at the same time that it’s streamed to Facebook)
The system should programmatically send the content to a Facebook page, using Facebook’s APIs, without any user interaction.

### the solution
This challenge was rather easy once I found the right libraries to work with. 
I initial found pylivestream 1.9.4 which a library that stream to one or multiple streaming sites simultaneously, using pure object-oriented Python (no extra packages) and FFmpeg.
Knowing that the library was based on ffmpeg I started looking for a way to add the logo overlay. After a few tries I managed to acomplish the task using the following comand
```python
ffmpeg -loglevel error -re -stream_loop -1 -i big_buck_bunny_480p_h264.mov -i logo.png -f lavfi -i anullsrc -filter_complex "[0:v]scale=1024:-1,setpts=PTS-STARTPTS[bg];[1:v]scale=120:-1,setpts=PTS-STARTPTS[fg];[bg][fg]overlay=W-w-10:10,format=yuv420p[out]" -map "[out]" -map 2:a -codec:v libx264 -pix_fmt yuv420p -preset veryfast -b:v 500k -g 48.0 -codec:a aac -b:a 128k -ar 44100 -maxrate 500k -bufsize 250k -strict experimental -f flv  "rtmps://live-api-s.facebook.com:443/rtmp/777255016025370?s_bl=0&s_ps=1&s_sw=0&s_vt=api-s&a=AbyoMafpkIVJieTk8Rk"

```
To run this yourself please install the required dependencies

```python
pip install -r "requirements.txt"
```

Also to get your own stremer key go to Facebook > Live  then click on the Connect tab