#!/usr/bin/python3
hid = __import__('hidden_4')
if __name__ == "__main__":
    for i in dir(hid):
        if i[0:2] != "__":
            print("{}".format(i))
