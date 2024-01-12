import string


simplechr="!#%&'()*+,-./:;<=>?[]^_`{|}~"+string.ascii_lowercase + string.ascii_uppercase + string.digits
escapemap={
    "\a":r"\a",
    "\b":r"\b",
    "\t":r"\t",
    "\v":r"\v",
    "\f":r"\f",
    "\r":r"\r",
    '\"':r'\"',
    "\\":r"\\",
    "\n":r"\n"

}

def bytes2c_allx(data:bytes):
    output=[]
    for d in data:
        output.append(r"\x"+ f"{d:02X}")
    return  "".join(output)

def bytes2c_adobe(data:bytes):
    output=[]
    for d in data:
        if chr(d) in simplechr:
            output.append(chr(d))
        elif chr(d) in escapemap:
            output.append(escapemap[chr(d)])
        else:
            output.append(r"\x"+ f"{d:02X}")
    return  "".join(output)
