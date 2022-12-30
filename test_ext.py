import cgitb
cgitb.enable(format="text")
import os
result = os.popen(r"E:\vision\label\dist\__main__\__main__.exe")
print(result.read())