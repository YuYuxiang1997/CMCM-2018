from PIL import Image
import numpy as np

#ambulance class with a int ID, int[][] targets, coordinate home
class ambulance:
    def __init__(self, ID, targets, home):
        self.ID = ID
        self.targets = targets
        self.home = home

amb_array = []

#iterate across all images in folder
for k in range(6):
    for l in range(6):
        try:
            path = "D:/Cornell/amb_data/" + str(k+1) + "," + str(l+1) + ".jpg"
            im = Image.open(path)
            rgb_im = im.convert('RGB')
            temp= np.zeros((30,30))
            grid_height = im.size[0]/32
            grid_width = im.size[1]/32
            #get numpy array representation of image
            for i in range(30):
                for j in range(30):
                    if rgb_im.getpixel(((i+2)*grid_height+10,(j+2)*grid_width+10))==(0,0,0):
                        temp[j][i] = 1
            amb = ambulance((k+1,l+1), temp, (k+1,l+1))
            amb_array.append(amb)
            #print("D:/Cornell/amb_data/" + str(k+1) + "," + str(l+1) + ".jpg")            
        except:
            #print("not found")
            pass

#print(amb_array[0].targets)