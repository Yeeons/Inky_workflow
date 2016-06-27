import fileinput
import sys


name = raw_input("Section name: ")

headline = raw_input("Insert headline: ")
body1 = raw_input("Insert body content: ")

# Json file
def json_create(h1,b1):
  json_name = "./testing/" + name + ".json"
  json_fo = open(json_name, "wb")
  json_fo.write( '''{\n\t"headline": "'''+ h1 +'''",\n\t"body1": "'''+ b1 + '''"\n}''');
  
# html file
def html_template(h1,b1):
  html_name = name + ".html"
  html_fo = open(html_name, "wb")
  html_fo.write('<wrapper>\n\t<row class="footer">\n\t\t<columns>\n\t\t\t<h1>{{'+ name +'.headline}}</h1>\n\t\t\t<p>{{{'+ name +'.body2}}}</p>\n\t\t</columns>\n\t</row>\n</wrapper>\n<spacer></spacer>');
  
def mainfile():
  for line in fileinput.FileInput("./testing/default.html",inplace=1):
    if "<container>" in line:
      line=line.strip('\n')
      line=line.replace(line, line + "\n\t\t\t\t\t\t\t{{>" + name +"}}\n")
    sys.stdout.write(line)    

json_create(headline, body1)
html_template(headline, body1)
mainfile()