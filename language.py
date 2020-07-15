"""
Script: language.py
Version: 1.0.0
Name: James Pinder (https://github.com/3NiGMa404)
Date: 2020-07-15
"""
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
# Let's go!
dataset = loadtxt('words.csv', delimiter=',')
dataset2 = loadtxt('testdata.csv', delimiter=',')
x2 = dataset2[:, 0:520]
y2 = dataset2[:, 520:522]
X = dataset[:, 0:520]
y = dataset[:, 520:522]
print(X.shape)

model = Sequential()
model.add(Dense(520, input_dim=520, activation='relu'))
model.add(Dense(260, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy'])
model.fit(X, y, epochs=20, batch_size=1, verbose=1)
# evaluate the keras model
_, accuracy = model.evaluate(x2, y2, verbose=1)
print(accuracy)
alph = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
inputs = [input('>: ').lower(), 'a']
while 'exit' not in inputs:
    newlines = []
    for line in inputs:
        curline = ''
        for letter in line:
            letternum = alph.index(letter)
            curline = curline + (letternum * '0,') + '1' + \
                ((25 - letternum) * ',0,')
        curline = curline + ((20 - len(line)) * 26 * '0,')
        if curline[-1] == ',':
            curline = curline[0:-1]
        newlines.append(
            curline.replace(
                ',,',
                ',').replace(
                '00',
                '0,0').replace(
                '01',
                '0,1').replace(
                    '10',
                    '1,0').replace(
                        '11',
                '1,1'))
    newlines2 = []
    op = open('user input.csv', 'w+')
    op.write('\n'.join(newlines))
    op.close()
    dataset3 = loadtxt('user input.csv', delimiter=',')
    x3 = dataset3[:, 0:520]
    prediction = model.predict(x3)[0]
    if prediction[0] > 0.5:
        print('i am {}% sure that "{}" is english'.format(
            round(float(prediction) * 100, 2), inputs[0]))
    else:
        print('i am {}% sure that "{}" is italian'.format(
            round(float((1 - prediction)) * 100, 2), inputs[0]))
    inputs = [input('>: ').lower(), 'a']
