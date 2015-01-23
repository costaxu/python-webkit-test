#!/usr/bin/python
#coding: utf-8

import ghost
import logging
import sys

ipad_user_agent = "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"

#video_url = "http://www.iqiyi.com/v_19rrh1tfkg.html"
#video_url = "http://www.iqiyi.com/v_19rrifvjnz.html"

video_url = "http://v.qq.com/cover/c/c5j3rggftlgseti.html"
#video_url = "http://v.qq.com/cover/c/c5j3rggftlgseti/f0012kzjrt5.html"

#video_url = "http://v.youku.com/v_show/id_XNjU0MzUzODE2.html?x"
#video_url = "http://v.youku.com/v_show/id_XNTgzNDM3ODg4.html?x"

#video_url = "http://www.letv.com/ptv/vplay/2196674.html"
#video_url = "http://www.letv.com/ptv/vplay/2221743.html"

#video_url = "http://pad.tv.sohu.com/20131229/n392592429.shtml"

logging_handler = logging.StreamHandler(sys.stdout)
ghost.ghost.logger.addHandler(logging_handler)

def GetHostNameFromUrl(url):
    splits = url.split('/')
    if len(splits) >= 3:
        return splits[2]
    else:
        return ''

ghost_object = ghost.Ghost(user_agent = ipad_user_agent, 
        wait_timeout=120,
        download_images=False,
        log_level = logging.DEBUG)

page, resources = ghost_object.open(video_url)

host_name = GetHostNameFromUrl(video_url)
print "host " + host_name
if host_name.find('sohu.com') != -1:
    ghost_object.wait_for_selector('div[class="x-init-play-btn"]')
    ghost_object.evaluate("document.getElementsByClassName('x-init-play-btn')[0].click()")

ghost_object.wait_for_selector('video')
#for resource in resources:
#    if resource.url == video_url:
#        print resource.url
#        print resource.http_status
#        break
print "%d resources downloaded" % (len(resources))
result, resources = ghost_object.evaluate( "document.getElementsByTagName('video')[0].getAttribute('src');")
print "视频播放url:"
print result



