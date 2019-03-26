import random, subprocess, string
from pyfield import ffield


def padbin(s):
	return '0b'+s[2:].zfill(64)

def hex2str(str):
	padhexa(str)
	lst=[]
	for i in range(2,18,2):
		x=chr(int(str[i:i+2],16))
		lst.append(x)
	lst=''.join(lst);
	return lst

def output(outp): #reducing the output to usable form
	lst=['0x']
	for i in range(len(outp)):
		lst.append(hex(ord(outp[i])-ord('f'))[2])
	return ''.join(lst)

in1=''.join(random.choice(string.ascii_lowercase) for i in range(8))
args1="curl -H \"Content-Type: application/json\" --request POST --data \'{\"teamname\":\"team5\",\"password\":\"ayz11ospfc\", \"plaintext\":\""+in1+"\"}\' -k https://172.27.26.163:9000/eaeae"
out1=subprocess.check_output(args1,shell=True)
out1=out1.decode('utf-8').split('"')[3]
print(padbin(bin(int(output(out1),0))));
		
F=ffield.FField(7);
a=ord('a');
F.showpolynomial(a);