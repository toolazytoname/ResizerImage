import os
import Image
import string

inFile = 'OrangeDragon.png'
sizeArray = ['57','29','72','50','32','40','1024','60','76']

for outSize in sizeArray: 
	fileName = os.path.splitext(inFile)[0]
	im = Image.open(inFile)

	outFile =  fileName + '_' + outSize + 'x' + outSize + '.png'
	outImage = im.resize((string.atoi(outSize),string.atoi(outSize)),Image.ANTIALIAS)
	outImage.save(outFile)

	outFile2x = fileName + '_' + outSize + 'x' + outSize + '@2x' +'.png'
	outImage2x = im.resize((string.atoi(outSize) * 2,string.atoi(outSize) * 2),Image.ANTIALIAS)
	outImage2x.save(outFile2x)

