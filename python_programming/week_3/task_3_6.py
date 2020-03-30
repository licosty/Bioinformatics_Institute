''' 3.6 Дополнительные модули '''

# task 1
import requests

with open("E:/dataset_3378_2.txt") as rfile:
    r = requests.get(rfile.read().strip())
    print(len(r.text.splitlines()))

# task 2
import requests

with open("E:/dataset_3378_3.txt") as rfile:
    file_1 = requests.get(rfile.read().strip())
    while 1:
        s = file_1.text
        if 'We' == s.split()[0]:
            print(s.strip())
            break
        else:
            file_1 = requests.get('https://stepic.org/media/attachments/course67/3.6.3/'
                                  + file_1.text.strip())