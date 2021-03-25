import sys
import requests
import socket
import json

if len(sys.argv) < 2 :
    print("Usage "+ sys.argv[0] + "<url>")
    sys.exit(1)

req = requests.get("https://"+sys.argv[1])
print("\n"+str(req.headers))

gethostby_ = socket.gethostbyname(sys.argv[1])
print("\n The IP Address of "+sys.argv[1] + " is " + gethostby_+"\n")


#ipinfo.io


req_two = requests.get("https://ipinfo.io/"+gethostby_+"/json")
response_ = json.loads(req_two.text)

print("location: "+response_["loc"])
print("region: "+response_["region"])
print("city: "+response_["city"])
print("country: "+response_["country"])
print("asn:" +response_["asn"])