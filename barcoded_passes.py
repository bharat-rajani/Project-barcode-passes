import barcode
from barcode.writer import ImageWriter
from random import randint
import os
from PIL import Image, ImageFont ,ImageDraw
import pickle

#RANDOM NUMBERS GENERATOR
random_number_digits = lambda x : randint(10**(x-1),(10**x)-1)
#random number file
rand_list = sorted([random_number_digits(13) for x in range(5000)])


data = {x:[0,"%04d"%y] for x,y in zip(rand_list,range(1,5001))}
#print(i for i in data.items())
if not os.path.exists('obj'):
	os.makedirs('obj')

def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


save_obj(data,"data")
w=load_obj('data')
for key,val in w.items():
	print(key,val)




rfile = open("rfile.txt","w")


main_dir = os.getcwd()

#directory for barcode images
barcode_images = os.path.join(main_dir,'barcode_images')
if not os.path.exists(barcode_images):
	os.makedirs(barcode_images)

#directory for pass images
pass_images = os.path.join(main_dir,'pass_images')
if not os.path.exists(pass_images):
	os.makedirs(pass_images)


#BARCODE WRITER OPTIONS AND BARCODE CLASS
options = dict(module_width=0.4,font_size=10,module_height=9,text_distance=2)
EAN = barcode.get_barcode_class('ean13')

#Change dir
font = ImageFont.truetype("DejaVuSans-Bold.ttf", 18,encoding="unic")




pass_design = os.getcwd()+'/TYFPASSES.jpg'



for i in range(5000):

	os.chdir(main_dir)

	barcode_number=str(rand_list[i])
	#barcode_number="000000000"+"%4d"%i
	print(barcode_number)
	print(type(barcode_number))
	
	rfile.write(barcode_number+"\n")

	ean = EAN(barcode_number,writer=ImageWriter())
	#saving barcode images in barcode_images directory 
	os.chdir(barcode_images)
	barcode_img = 'ean13_barcode_%s'%(i+1)
	print("[*] Barcode {} saved in {} ".format(i+1,"barcode_images"))

	barcode = ean.save(barcode_img,options)
	

	img_bcode = Image.open(barcode_img+'.png', 'r')
	img_w, img_h = img_bcode.size

	#print(img_w,img_h)
	#background = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))

	angle=90
	rot = img_bcode.rotate( angle, expand=1 )

	youthfest_pass = Image.open(pass_design,'r')

	bg_w, bg_h = youthfest_pass.size
	#print("youthfest pass size ",youthfest_pass.size)
	offset = ((bg_w - (img_h + 53)), (bg_h - img_w)//2)

	#offset1 = (int(str(y) for y in offset:)
	#offset1 = [int(y) for y in offset]
	#print(offset)
	youthfest_pass.paste(rot, offset)
	serial_num = "%04d"%(i+1)
	draw = ImageDraw.Draw(youthfest_pass)
	txt = draw.text((60, 0),serial_num,(255,255,255),font=font)
	#saving pass in pass images directory
	os.chdir(pass_images)
	youthfest_pass.save('pass%s.png'%(i+1))
	print("[*] Pass {} saved in {} ".format(i+1,"pass_images"))

	#closing all the pillow images
	img_bcode.close()
	youthfest_pass.close()

print("All numbers are written at rfile.txt")

#options = dict(compress=True)
	

	