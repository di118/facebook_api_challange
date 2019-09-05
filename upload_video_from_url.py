import json
import facebook
import requests


def main():
    token = 'EAAitbEFpFSQBADsgUyhwDN8wCg26XNRQc5MgPblHqjXDrQj13BkQgHaU3WbisvEw72Rvu0s4JBb988uKLVbW5jgNCjhzUAim6uhq6M92SZAPDnyY4d7P3I5ieXg7Cq0bb6rGY9rAhSNcpMCZB3bE7uFLlQn0NI4UI5L7K0bGgjHBcgXjiESlZCCyLpFMLrz4JIPi9iePgZDZD'
    # graph = facebook.GraphAPI(token)
    # fields = ['id, email']
    # profile = graph.get_object('me', fields=fields)
    # print(json.dumps(profile, indent=4))
    file_url = 'https://www.pexels.com/video/854713/download/?search_query=cars&tracking_id=ojbpy4ztzse'
    title = 'This is my first video upload using facebookAPI'
    caption = "This is my first video upload using facebookAPI"
    video_path = 'merc.mp4'
    fburl = 'https://graph-video.facebook.com/v2.3/311633592587517/videos?access_token=' + str(token)

    payload = {'title': '%s' % (title), 'description': '%s' % (caption), 'file_url': '%s' % (file_url)}
    flag = requests.post(fburl, data=payload).text
    print(flag)
    fb_res = json.loads(flag)

if __name__ == "__main__":
    main()