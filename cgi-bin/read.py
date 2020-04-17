#!/usr/bin/python3

import os
import sys
import json
import re

contentLength=int(os.environ['CONTENT_LENGTH'])
content=sys.stdin.read(contentLength)

myjson=json.loads(content);

search=myjson["search"];

fin=open("stories/index.txt","r")
titles=[];
for line in fin:
	title=line.split(" ",1)
	if not search or title[1].lower().find(search.lower())!=-1:
		titles.append({"id":title[0],"title":title[1].strip()}) 
fin.close()

response={"status":"OK","titles":titles};

myjson=json.dumps(response)

print("content-type:application/json\r\n\r\n")

print(myjson)
