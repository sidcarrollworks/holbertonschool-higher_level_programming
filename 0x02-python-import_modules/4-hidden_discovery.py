#!/usr/bin/python3
import hidden_4 as hid
if __name__ == "__main__":
    for i in dir(hid):
        if i[0:2] != "__":
            print("{}".format(i))
