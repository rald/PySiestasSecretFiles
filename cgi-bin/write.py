#!/usr/bin/python3

import os
import sys
import json
import re

contentLength=int(os.environ['CONTENT_LENGTH'])
content=sys.stdin.read(contentLength)

myjson=json.loads(content);

title=myjson["title"];
story=myjson["story"];

fin=open("stories/id.txt","r")
id=int(fin.readline());
fin.close()

fout=open("stories/index.txt","a")
fout.write("%d %s\r\n" % (id,title))
fout.close()

fout=open("stories/%d.html" % id,"w")
fout.write(story)
fout.close()

id+=1
fout=open("stories/id.txt","w")
fout.write("%d\r\n" % id);
fout.close()

print("content-type:application/json\r\n\r\n")

print('{"status":"OK"}')
