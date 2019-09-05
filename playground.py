import json
import facebook
import requests

# command to run
# adding overlay : -i logo.png -f lavfi -i anullsrc -filter_complex "[0:v]scale=1024:-1,setpts=PTS-STARTPTS[bg];[1:v]scale=120:-1,setpts=PTS-STARTPTS[fg];[bg][fg]overlay=W-w-10:10,format=yuv420p[out]" -map "[out]" -map 2:a
# ffmpeg -re -stream_loop -1 -i merc.mp4 -i logo.png -f lavfi -i anullsrc -filter_complex "[0:v]scale=1024:-1,setpts=PTS-STARTPTS[bg];[1:v]scale=120:-1,setpts=PTS-STARTPTS[fg];[bg][fg]overlay=W-w-10:10,format=yuv420p[out]" -map "[out]" -map 2:a -codec:v libx264 -pix_fmt yuv420p -preset veryfast -b:v 3000k -g 60.0 -codec:a aac -b:a 128k -ar 44100 -maxrate 3000k -bufsize 1500k -strict experimental -f flv  "rtmps://live-api-s.facebook.com:443/rtmp/777255016025370?s_bl=0&s_ps=1&s_sw=0&s_vt=api-s&a=AbyoMafpkIVJieTkKb4"
# ffmpeg -loglevel error -re -stream_loop -1 -i big_buck_bunny_480p_h264.mov -i logo.png -f lavfi -i anullsrc -filter_complex "[0:v]scale=1024:-1,setpts=PTS-STARTPTS[bg];[1:v]scale=120:-1,setpts=PTS-STARTPTS[fg];[bg][fg]overlay=W-w-10:10,format=yuv420p[out]" -map "[out]" -map 2:a -codec:v libx264 -pix_fmt yuv420p -preset veryfast -b:v 500k -g 48.0 -codec:a aac -b:a 128k -ar 44100 -maxrate 500k -bufsize 250k -strict experimental -f flv  "rtmps://live-api-s.facebook.com:443/rtmp/777255016025370?s_bl=0&s_ps=1&s_sw=0&s_vt=api-s&a=AbyoMafpkIVJieTk8Rk"

def main():
    token = 'EAAitbEFpFSQBAIUMJKlmJNFZAPbybvodLVTJxyVyxtlhQQyJoaD8ZBsfVnt3PmPsnB5n2nBS5G6ti2JZCEsZAp9GEskSse0rG2ZAcZBl8ZA734U2VFh0r2hqajyP3k95Ut3TZCf7Wu06Idr3UERwSgFk0mMm52cZA4onvjJzlhnjmATkQj2bha4iXE4aZCZA15MZAbUZD'
    # graph = facebook.GraphAPI(token)
    # fields = ['id, email']
    # profile = graph.get_object('me', fields=fields)
    # print(json.dumps(profile, indent=4))
    file_url = 'https://www.pexels.com/video/854713/download/?search_query=cars&tracking_id=ojbpy4ztzse'
    title = 'This is my first video upload using facebookAPI'
    caption = "This is my first video upload using facebookAPI"
    video_path = open('merc.mp4', 'r')
    fburl = 'https://graph-video.facebook.com/v2.3/311633592587517/live_videos?access_token=' + str(token)

    payload = {'title': '%s' % (title), 'description': '%s' % (caption), 'live_encoders': '%s' % (video_path)}
    flag = requests.post(fburl, data=payload).text
    print(flag)
    fb_res = json.loads(flag)

if __name__ == "__main__":
    main()