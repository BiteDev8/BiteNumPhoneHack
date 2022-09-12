from colorama import Fore, init; init()
import random,time

x=0
a = "AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn1234567890."
h = "1234567890"
cookie= ''.join(random.choice(a)for i in range(111))

def gen_ip():
    first  = ''.join((random.choice(h)for i in range(2)))
    second = ''.join((random.choice(h)for i in range(2)))
    third  = ''.join((random.choice(h)for i in range(2)))
    four   = ''.join((random.choice(h)for i in range(2)))
    ipres  = first + "." + second + "." + third +"." + four
    return ipres

def gen_cc():
    first  = ''.join((random.choice(h)for i in range(4)))
    second = ''.join((random.choice(h)for i in range(4)))
    third  = ''.join((random.choice(h)for i in range(4)))
    four   = ''.join((random.choice(h)for i in range(4)))
    ccres  = first + "." + second + "." + third +"." + four
    return ccres

def gen_token():
    first  = ''.join((random.choice(a)for i in range(24)))
    second = ''.join((random.choice(a)for i in range(6)))
    third  = ''.join((random.choice(a)for i in range(27)))

    result = first + "." + second + "." + third

    return result

def gen_num():
	bite   = "76"
	debut  = ''.join((random.choice(bite)for i in range(1)))
	first  = ''.join((random.choice(h)for i in range(2)))
	two    = ''.join((random.choice(h)for i in range(2)))
	tri    = ''.join((random.choice(h)for i in range(2)))
	four   = ''.join((random.choice(h)for i in range(2)))
	result = debut + " " + first + " " + two + " " + tri + " " + four

	return result

ip    = gen_ip()
cc    = gen_cc()
token = gen_token()

print(f"{Fore.GREEN}qui trouvé numero phone ?:")
input()


while x <= 3000 :
	num = gen_num()
	print(f"{Fore.RED}0{num}")
	x+=1


print(f"0{num} {Fore.GREEN}<== True") 

print(f"{Fore.WHITE}Do we hack : 0{num} ? y/n")
lol=str(input())

if lol == "y":
	print("hack en cours...")
	time.sleep(3)
	print("tokens hack...")
	time.sleep(5)
	print("initialisation...")
	time.sleep(2)

	print(f"{Fore.GREEN}Token : {token}")
	print(f"IP : {ip}")
	print(f"Cookie roblox : {cookie}")
	print(f"Credit Cart : {cc} Data : {random.randint(1,12)}/{random.randint(23,25)}  CAP : {random.randint(100,999)}" )
else :
	pass
	
input()
