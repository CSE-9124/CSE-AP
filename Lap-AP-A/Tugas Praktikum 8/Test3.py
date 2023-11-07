import re

def IP6(teks):
    patternIPv6 = r"(([1-9a-fA-F]|0?){1,4}:){7}([1-9a-fA-F]|0?){1,4}"
    hasil = re.search(patternIPv6,teks)
    
    if hasil:
        return True
    else : return False
    
def IP4(teks):
    patternIPv4 = r"((1[0-9]?[0-9]?|2[0-4]?[0-9]?|25[0-5])\.){3}(0|1[0-9]?[0-9]?|2[0-4]?[0-9]?|25[0-5])"
    hasil = re.search(patternIPv4,teks)

    if hasil:
        return True
    else : return False

def IPCheck(teks,n):
    teks1 = teks.split("\n")
    hasil = ""
    for i in range(n):
        if IP4(teks1[i]):
            hasil += "IPv4"
        elif IP6(teks1[i]):
            hasil += "IPv6"
        else: hasil += "Bukan IP Address"
        if i != n-1 :
            hasil+="\n"
    print(hasil)



teks1 ="""This line has trailing whitespace
121.203.197.20
2001:0db8:0000:0000:0000:ff00:0042:8329"""
teks2="""213.214.111.564
444.444.444.444 not an ip address
1050:0:0a:0:5:600:300c:326b"""
IPCheck(teks1,n = 3)
print("\n")
IPCheck(teks2,n = 3)

teks = '523.203.197.205'
print(IP4(teks))