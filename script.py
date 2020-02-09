from datetime import datetime

file_object = open('/opt/python/test/sample.txt', 'a')

while True:
    now = datetime.now()
    dateString = now.strftime("%m/%d/%Y, %H:%M:%S ")
    file_object.write(dateString)
 
file_object.close()