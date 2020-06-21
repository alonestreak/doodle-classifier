import numpy as np
from PIL import Image

train_path= 'data/train_set/'
test_path='data/test_set/'
data= np.load('cloud.npy')
total=len(data)
test=int(total*0.01)
train=total-test
print(train)
for i in range(total):
    x= np.reshape(data[i],(28,28))
    img=Image.fromarray(x)
    img=img.convert('L')
    if(i<train):
        img.save(train_path+"cloud/cloud"+str(i)+".png")
    else:
        img.save(test_path+"cloud/cloud"+str(i-train)+".png")
print('done')

