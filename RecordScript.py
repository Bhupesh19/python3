# Creator - Bhupesh
pointDict = {}
pointDict['Alexa'] = 0
pointDict['GAssist'] = 0
pointDict['Siri'] = 0
try:
    file = open('Record.txt', 'r+')
except:
    file = open('Record.txt', 'w+')
    for (key, value) in pointDict.items():
        file.write(key + ' = ' + str(value))
        file.write('\n')

for line in file:
    _lineList = line.split()
    _key = _lineList[0]
    _value = _lineList[2]
    if(_key in pointDict.keys()):
        pointDict[_key] = int(_value)

temp = \
    input('Who would you like to give points to? Alexa , GAssist or  Siri: '
          )
if temp in pointDict.keys():
    points = \
        int(input('How many points would you like to give to ' + temp + ' ?'))
    pointDict[temp] = pointDict[temp] + points
    for (key, value) in pointDict.items():
        file.write(key + ' = ' + str(value))
        file.write('\n')
    
else:
    print('That name is not valid')

file.close()

for (key, value) in pointDict.items():
    print( key + ' has now ' + str(value) + ' points') 
