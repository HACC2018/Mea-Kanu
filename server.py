from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO
import os
import base64
import chardet
import socket
from tensorflow.python.keras.models import model_from_json
import numpy as np
import os,cv2
from tensorflow.python.keras.utils import np_utils
import csv
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        sumplant = []
        #obtain the length of the message being sent
        content_length = int(self.headers['Content-Length'])
        print('content')
        print(content_length)
        #parse the information
        body = self.rfile.read(content_length)
        payload = json.loads(body)
        print('json')
        print(body)

        image = list(payload.values())
        body = image[0]
        print(type(body))
        print('body =========')
       # print(body[17:-2])
        #confirm successful request
        self.send_response(200)
        self.end_headers()
        
        #determine what type of encoding the file is in by calling
        print(type(body))
        #decode the file and download into pwd
        decode = base64.b64decode(body)
        output_file = open("new_img.jpg", "wb")
        output_file.write(decode)
        output_file.close()

        NETp = '../MeaKanu'
        Best_weightsp = 'Best-weights-PLANT'
        #'NewOrchBestPLANT'
        data_listp = []
        print(type(cv2.imread('./new_img.jpg')))
        input_imgp =cv2.imread('./new_img.jpg')
        input_imgp_resize=cv2.resize(input_imgp,(224,224))
        data_listp.append(input_imgp_resize)
        img_datap = np.array(data_listp)
        img_datap = img_datap.astype('float32')
        img_datap = img_datap/255
        #print (img_datap.shape)
        json_filep = open('./' + 'model.json', 'r')
        loaded_model_json = json_filep.read()
        json_filep.close()
        modelp = model_from_json(loaded_model_json)
        # load weights into new model
        modelp.load_weights('./' + Best_weightsp +'.hdf5')
        # evaluate loaded model on test data
        modelp.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        ##### IMPORTANT: OUTPUT ALL ##########
        outputp = modelp.predict(img_datap)
        for i in range(0,100): 
            sumplant.append(sum(outputp[:,i]))
        else:
            for i in range(0,100): 
                sumplant.append(0)
        ###########################################################################
                numbTILES = 1
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
        #print(ClassPlantPred)
        percentages = []
        for percent in ClassPlantPred:
            percentages.append(round(percent * 100, 2))
        print(percentages)

        data = {
            "PNO": Z,
            "Percents" : percentages
        }
        
        json_string = json.dumps(data)
        print(json_string)
        self.wfile.write(json_string.encode('utf-8'))
        
        
        #self.send_response(200, "Success")
        #self.end_headers()


httpd = HTTPServer(('', 8081), SimpleHTTPRequestHandler)
httpd.serve_forever()