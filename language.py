# first neural network with keras
import string
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
englen=998
italen=952
print(englen,italen)
newdata=open('words.csv','w+')
data_lines=english+italian
print(data_lines)
for line in data_lines:
    curline=''
    for letter in line:
        letternum=alph.index(letter)
        curline=curline+(letternum*'0,')+'1'+((25-letternum)*',0,')
    curline=curline+((20-len(line))*26*'0,')
    if curline[-1]==',':
        curline=curline[0:-1]
    newlines.append(curline.replace(',,',',').replace('00','0,0').replace('01','0,1').replace('10','1,0').replace('11','1,1'))

newlines2=[]
for line in newlines[0:englen]:
    newlines2.append(line+',1')
for line in newlines[englen+1:englen+italen]:
    newlines2.append(line+',0')
op=open('words.csv','w+')
op.write('\n'.join(newlines2))
op.close()
data_lines=open('test data.txt','w+').read().split('\n')
for line in data_lines:
    curline=''
    for letter in line:
        letternum=alph.index(letter)
        curline=curline+(letternum*'0,')+'1'+((25-letternum)*',0,')
    curline=curline+((20-len(line))*26*'0,')
    if curline[-1]==',':
        curline=curline[0:-1]
    newlines.append(curline.replace(',,',',').replace('00','0,0').replace('01','0,1').replace('10','1,0').replace('11','1,1'))

newlines2=[]
for line in newlines[0:englen]:
    newlines2.append(line+',1')
for line in newlines[englen+1:englen+italen]:
    newlines2.append(line+',0')
op=open('testdata.csv','w+')
op.write('\n'.join(newlines2))
op.close()
    ##Let's go!
dataset = loadtxt('words.csv', delimiter=',')
dataset2 = loadtxt('testdata.csv', delimiter=',')
x2=dataset2[:,0:520]
y2=dataset2[:,520:522]
X = dataset[:,0:520]
y = dataset[:,520:522]
print(X.shape)

model = Sequential()
model.add(Dense(520, input_dim=520, activation='relu'))
model.add(Dense(260, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=10, batch_size=10, verbose=0)
# evaluate the keras model
_, accuracy = model.evaluate(x2, y2, verbose=1)
print(accuracy)
inputs=[input('>: ').lower(),'a']
while not 'exit' in inputs:
    newlines=[]
    for line in inputs:
        curline=''
        for letter in line:
            letternum=alph.index(letter)
            curline=curline+(letternum*'0,')+'1'+((25-letternum)*',0,')
        curline=curline+((20-len(line))*26*'0,')
        if curline[-1]==',':
            curline=curline[0:-1]
        newlines.append(curline.replace(',,',',').replace('00','0,0').replace('01','0,1').replace('10','1,0').replace('11','1,1'))
    newlines2=[]
    for line in newlines[0:englen]:
        newlines2.append(line+',1')
    for line in newlines[englen+1:englen+italen]:
        newlines2.append(line+',0')
    newlines
    op=open('user input.csv','w+')
    op.write('\n'.join(newlines2))
    op.close()
    dataset3 = loadtxt('user input.csv', delimiter=',')
    x3=dataset3[:,0:520]
    prediction=model.predict(x3)[0]
    if prediction[0]>0.5:
        print('i am {}% sure that "{}" is english'.format(round(float(prediction)*100,2),inputs[0]))
    else:
        print('i am {}% sure that "{}" is italian'.format(round(float((1-prediction))*100,2),inputs[0]))
    inputs=[input('>: ').lower(),'a']

    '''
       Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
   '''
