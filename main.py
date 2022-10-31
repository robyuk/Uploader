# Uploads a file to http://cgi-lib.berkeley.edu/ex/fup.html
#
import requests

url="http://cgi-lib.berkeley.edu/ex/fup.cgi"
filename="sentences.txt"

file=open(filename, 'rb')

# To obtain the contents of the files={} dictionary, point your browser at the page, right click on (or near) the "Choose file" button, select "Inspect element" and look for the input type="file" tag.  The dictionary key is the name entry for this tag.  eg. for this page:
#      <input type="file" name="upfile">
# So in this case the dictionary key is "upfile"
# The text for the "upfile" key is the file object we opened above
req=requests.post(url, files={"upfile":file})
print(req.text)