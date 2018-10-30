from keras.models import model_from_json
import numpy as np
import os,cv2
from keras.utils import np_utils
import csv

#################################################################
## PLANT

# Define data path
data_pathp = 'D:/MeaKuna/01-SEGMENTATION/plant/a'
img_listp = sorted(os.listdir(data_pathp))
sumplant=[]

if len(img_listp)>0:
 ### PLANT ARCHITECTURE
 Archp = 'ResNet18'
 NETp = '03-CLASSIFICATION/01-PLANT/'+ Archp
 Best_weightsp = 'Best-weights-PLANT'
 #'NewOrchBestPLANT'
 data_listp = []
 for k in img_listp:
  input_imgp=cv2.imread(data_pathp + '/' + k)
  input_imgp_resize=cv2.resize(input_imgp,(224,224))
  data_listp.append(input_imgp_resize)
 img_datap = np.array(data_listp)
 img_datap = img_datap.astype('float32')
 img_datap = img_datap/255
 #print (img_datap.shape)
 json_filep = open('D:/MeaKuna/' + NETp + '/' + 'model.json', 'r')
 loaded_model_json = json_filep.read()
 json_filep.close()
 modelp = model_from_json(loaded_model_json)
 # load weights into new model
 modelp.load_weights('D:/MeaKuna/' + NETp + '/' + Best_weightsp +'.hdf5')
 # evaluate loaded model on test data
 modelp.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
 ##### IMPORTANT: OUTPUT ALL ##########
 outputp = modelp.predict(img_datap)
 for i in range(0,100): sumplant.append(sum(outputp[:,i]))
else:
 for i in range(0,100): sumplant.append(0)
###########################################################################

numbTILES = 3
FINAL =[]

#######################################################################
### FLOWER TEMPORARY Classes
tempclassf=[]
tempclassf.append(0)
tempclassf.append(1)
tempclassf.append(4)
tempclassf.append(5)
tempclassf.append(7)
tempclassf.append(8)
tempclassf.append(9)
tempclassf.append(11)
tempclassf.append(13)
tempclassf.append(14)
tempclassf.append(15)
tempclassf.append(17)
tempclassf.append(19)
tempclassf.append(21)
tempclassf.append(22)
tempclassf.append(25)
tempclassf.append(26)
tempclassf.append(28)
tempclassf.append(29)
tempclassf.append(34)
tempclassf.append(35)
tempclassf.append(36)
tempclassf.append(37)
tempclassf.append(39)
tempclassf.append(41)
tempclassf.append(44)
tempclassf.append(45)
tempclassf.append(46)
tempclassf.append(47)
tempclassf.append(48)
tempclassf.append(49)
tempclassf.append(50)
tempclassf.append(51)
tempclassf.append(52)
tempclassf.append(53)
tempclassf.append(54)
tempclassf.append(55)
tempclassf.append(57)
tempclassf.append(58)
tempclassf.append(59)
tempclassf.append(60)
tempclassf.append(63)
tempclassf.append(65)
tempclassf.append(67)
tempclassf.append(68)
tempclassf.append(71)
tempclassf.append(73)
tempclassf.append(75)
tempclassf.append(76)
tempclassf.append(77)
tempclassf.append(78)
tempclassf.append(79)
tempclassf.append(80)
tempclassf.append(81)
tempclassf.append(82)
tempclassf.append(83)
tempclassf.append(84)
tempclassf.append(87)
tempclassf.append(88)
tempclassf.append(89)
tempclassf.append(93)
tempclassf.append(94)
tempclassf.append(96)
tempclassf.append(97)
tempclassf.append(98)
tempclassf.append(99)
###########################

ClassPlantPred =[]
PlantPredClass=[]
FlowerPredClass=[]
TilesPlant=[]
Z=[]

for j in range(1,6):
 ClassPlantPred.append(sorted(set(sumplant))[-j])
 PlantPredClass.append(sumplant.index(ClassPlantPred[j-1]))
 Z = [x for _,x in sorted(zip(ClassPlantPred,PlantPredClass), reverse=True)]

print(Z)
