#!/usr/bin/python3

import os
import sys
import json
import re
import bleach

contentLength=int(os.environ['CONTENT_LENGTH'])
content=sys.stdin.read(contentLength)

myjson=json.loads(content);

search=myjson["search"];

fin=open("stories/index.txt","r")
titles=[];
for line in fin:
	title=line.split(" ",2)
	if title[0]!='*' and (not search or title[2].lower().find(search.lower())!=-1):
		titles.append({"id":title[0],"timestamp":title[1],"title":bleach.clean(title[2].strip())}) 
fin.close()

response={"status":"OK","titles":titles};

myjson=json.dumps(response)

print("content-type:application/json\r\n\r\n")

print(myjson)
