from robolink import * #Api RoboDk
from robodk import * #Calling basic matrix operation on RoboDK #Pemanggilan matrik basic operasi di RoboDk
print("------------------------------------------------------------------------------------------------------\n")

nameprogram = "PyndoBot (Python Indo Bot)"
version = "Version: 1.0"
devby = "Ananda Rauf Maududi"
devdate = "16 March 2021"

print(nameprogram)
print(version)
print(devby)
print(devdate)

print("------------------------------------------------------------------------------------------------------\n")

Roblink = Robolink() #Variable contain calling Api RoboDk #Ini variable berising memanggil api RoboDk

#Calling robot name brand items : #Memanggil nama model robot dari brand perusahaan orang lain

robotitem = Roblink.Item('KUKA KR 6 R900 sixx')

#Create home and target moving robots and also moving welding gun targets : #Membuat kontrol gerak dari berand(semula) ke target

homes = Roblink.Item('Home')
target = Roblink.Item('Target 1')

#Pose robots to target (4x4 matrik) : #Membuat pose robot berada di posisi target dengan 4x4 matrik

poser = target.Pose()

# Moving robots from condition home to the center : #Mengontrol robot dari posisi semula (Beranda) ke target

robotitem.MoveJ(homes)
robotitem.MoveJ(target)
nvertexs = mbox(' Enter number of vertexs',entry=True) # Create Message Box alert to fill command #Membuat kotak pesan perintah

#Create Hexagon on the center : #Membuat bangunan hexagon

#You can change whatever you wanna create. #Bebas tidak ada terpaksaan untuk membuat pergerakan robot harus membuat bangunan hexagon

for i in range(nvertexs+1):
    angl = i*2*pi/nvertexs # Calculation for create angle from i,nvertexs and math formula is Phi = 3,14 #angle is 0,60,120 .... #Kalkulasi membuat angle kontrol robot dengan rumus matematika Phi #Angle yang dibuat ialah 0,60,120,...
    poseti = poser*rotz(angl)*transl(300,0,0)*rotz(-angl) #variable pose position robots #Ini variable pose posisi angle untuk pergerakan membuat bangunan hexagon.
#calling variable poseti #Memanggil variable poseti
    robotitem.MoveL(poseti)  

# Moving control back from target 1 to home : #Mengembalikan pergerakan robot dari target ke tempat semula (Beranda).

robotitem.MoveJ(target)
robotitem.MoveJ(homes)
    
