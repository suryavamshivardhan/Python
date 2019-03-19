
def read_write():
    f_w = open('C:/MyDocs/Training/Python/WorkSpace/resources/input','w')
    f_w.write("Hello surya , How are you doing?")
    f_w.write("Hello Vamshi. I am doing great!!!")
    f_w.close()
    f_r = open('C:/MyDocs/Training/Python/WorkSpace/resources/input','r')
    for line in f_r:
        print(line)

read_write()