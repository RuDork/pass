#!/usr/bin/env python3
def connect(ip,port):
    print("IP:",ip)
    print("Port:",port)
    ip = '10.10.10.1'
    port.append(8080)
if __name__=="__main__":
    ip = '192.168.1.1'
    port = [22,23,24]
    print("before call")
    print("IP:",ip)
    print("Port:",port)
    print("in connect")
    connect(ip,port)
    print("after call")
    print("IP:",ip)
    print("Port:",port)

