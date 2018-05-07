from random import randint
import pprint
import sys
import pickle
import os
from termcolor import colored, cprint

#no_dupes = [x for n, x in enumerate(rand_list) if x not in rand_list[:n]]
#if output of below statement is less than 5000 then there exists a duplicate itemin rand_list.
#print("Non duplicate numbers....",len(no_dupes))


def allot_pass(randict):
	name=input("Enter the name of person whom you want to allot the pass : ")
	start=int(input("Input starting serial number "))
	end=int(input("Input ending serial number "))

	for key,values in randict.items():
		
		if values[1] in range(start,end+1):
			if randict[key][2]=='dummy-name':
				randict[key][2]=name
				print("Pass {0} is alloted to {1}".format(randict[key][1],randict[key][2]))

			else :				
				confirm = input("You still want to allot the pass to %s"%name,"[yes/no]")
				if confirm=='yes' or confirm=='y':
					randict[key][2]=name
				elif confirm=='no' or confirm=='n':
					continue
				else :
					print("Wrong option ,continuing without alloting the pass {} to {}".format(randict[key][1],name))
	
	save_dict(randict)
	print("Done.")


def default_dict():
	with open("final-barcode.txt","r") as bfile:
		bfile_list=bfile.read().splitlines()
	if len(bfile_list)==len(range(1,5001)):
		randict = {key:[0,num,"dummy-name"] for num,key in zip(range(1,5001),bfile_list)}
	else:
		print("length not same")
	return randict



def save_dict(data):
	if not os.path.exists('bardata'):
		os.makedirs('bardata')
	with open('bardata/bardata'+'.pkl','wb') as bd:
		pickle.dump(data,bd,pickle.HIGHEST_PROTOCOL)


def load_dict():
	with open('bardata/bardata.pkl','rb') as bd:
		return pickle.load(bd)

def menu():
	print("\n"*3)
	w="(without quotes)."
	print("[1]To start scanning from scratch type 'start'",w)
	print("[2]To start scanning from saved data type 'load_data'",w)
	print("[3]To stop scanning type 'stop'",w)
	print("[4]To allot pass type 'allot'",w)
	print("[5]To repeat this menu type 'help'",w)
	print("\n"*3)

def scan(randict):
	print("\n"*2)
	print("Scanning Started".center(50,"="))
	print("\n"*2)
	while 1:

		print("\n"*2)
		line = sys.stdin.readline().rstrip()
		if line in randict.keys():
			print("PASS NUMBER ",randict[line][1])
			if randict[line][0] == 0:
				
				print(colored("PASS SCANNED.", 'green',attrs=['reverse']))
			
			elif randict[line][0] > 0:
				print("Pass already scanned.")
				cprint('Duplicate pass!', 'red', 'on_white',attrs=['reverse','blink'])
				print("Scanned :",randict[line][0]+1,"times")
		
			print("PASS ALLOTTED BY ",colored(randict[line][2], 'yellow',attrs=['reverse']))
			randict[line][0] += 1
			save_dict(randict)

		elif line=='stop' or line=='3':
			break

		elif line=='help' or line=='2':
			menu()

		elif line=="allot" or line=='3':
			print("First you have to stop the scan in progress.(press 3 to stop).")

		else:
			print("Barcode {} not found.".format(line))

		
def main():
	#print(default_dict(),sep="\n",end='\n')

	#for keys,val in randict.items():
	#	print(keys,val)
	print("\n"*3)
	print("Barcode Scanner".center(8,"="))

	for i in range(100):
		menu()
		command = sys.stdin.readline().rstrip()
		if command == "start" or command=='1':
			randict = default_dict()
			scan(randict)
		
		elif command == "load_data" or command=='2':
			randict = load_dict()
			scan(randict)

		elif command == "stop" or command=='3':
			break

		elif command == 'help' or command=='5':
			menu()

		elif command == 'allot' or command=='4':
			print("You want to allot pass in saved data ?")
			y=input("yes OR no ")
			if y=="y" or y=="yes":
				randict=load_dict()
				allot_pass(randict)

			elif y=='no' or y=='n':
				print("names entered will be in default database")
				randict=default_dict()
				allot_pass(randict)

			

		else:
			print("Bad option.")
			continue



if __name__=="__main__":
	main()

