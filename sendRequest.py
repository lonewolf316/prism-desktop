import requests, time

def sendRGB(host, rgbTuple):
    requestString = "/setColor?r="+str(rgbTuple[0])+"&g="+str(rgbTuple[1])+"&b="+str(rgbTuple[2])+"&w=0"
    host = "http://" + host + ":5000" + requestString
    print(host)
    print(requests.post(host, data=""))

#Test Loop
if __name__ == "__main__": 
    host = str(input("Host Address:"))
    while True:
        sendRGB(host, (255,0,0))
        time.sleep(.1)
        sendRGB(host, (0,255,0))
        time.sleep(.1)
        sendRGB(host, (0,0,255))
        time.sleep(.1)