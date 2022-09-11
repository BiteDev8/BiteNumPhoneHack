from colorama import Fore, Back, Style, init
import random
import time

init()
a = "AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn1234567890."

cookie= ''.join(random.choice(a)for i in range(111))

def gen_ip():
    h = "1234567890"
    first = ''.join((random.choice(h)for i in range(2)))
    second = ''.join((random.choice(h)for i in range(2)))
    third = ''.join((random.choice(h)for i in range(2)))
    four = ''.join((random.choice(h)for i in range(2)))

    ipres = first + "." + second + "." + third +"." + four

    return ipres

ip = gen_ip()

def gen_cc():
    h = "1234567890"
    first = ''.join((random.choice(h)for i in range(4)))
    second = ''.join((random.choice(h)for i in range(4)))
    third = ''.join((random.choice(h)for i in range(4)))
    four = ''.join((random.choice(h)for i in range(4)))

    ccres = first + "." + second + "." + third +"." + four

    return ccres

cc = gen_cc()

def gen_token():
    a = "AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn1234567890"
    first = ''.join((random.choice(a)for i in range(24)))
    second = ''.join((random.choice(a)for i in range(6)))
    third = ''.join((random.choice(a)for i in range(27)))

    result = first + "." + second + "." + third

    return result

token = gen_token()


x=0

print(Fore.GREEN+"qui trouvé numero phone ?:")
input()


while x <= 3000 :
	def gen_num():
	    a = "123456789"
	    bite = "76"
	    debut = ''.join((random.choice(bite)for i in range(1)))

	    first = ''.join((random.choice(a)for i in range(2)))
	    two = ''.join((random.choice(a)for i in range(2)))
	    tri = ''.join((random.choice(a)for i in range(2)))
	    four = ''.join((random.choice(a)for i in range(2)))
	

	    result = debut + " " + first + " " + two + " " + tri + " " + four

	    return result

	num = gen_num()
	print(Fore.RED+"0"+num)
	x+=1


pop="0"+num
print(pop ,Fore.GREEN+"<== True") 

print(Fore.WHITE+"Do we hack :",pop," ? y/n")
lol=str(input())

if lol == "y" :
	
	print("hack en cours...")
	time.sleep(3)
	print("tokens hack...")
	time.sleep(5)
	print("initialisation...")
	time.sleep(2)

	print(Fore.GREEN+"")
	print("Token :",token)
	print("ip :",ip)
	print("cookie roblox :",cookie )
	print("credit cart :",cc ," date :08/24  cap :652" )
else :
	pass
	



input()
