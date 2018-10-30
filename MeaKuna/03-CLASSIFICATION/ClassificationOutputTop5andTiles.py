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

ClassPlantPred =[]
PlantPredClass=[]
TilesPlant=[]
Z=[]

for j in range(1,6):
 ClassPlantPred.append(sorted(set(sumplant))[-j])
 PlantPredClass.append(sumplant.index(ClassPlantPred[j-1]))
 Z = [x for _,x in sorted(zip(ClassPlantPred,PlantPredClass), reverse=True)]

print(Z)
