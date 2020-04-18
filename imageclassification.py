import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
%matplotlib inline
# using pandas to store database stored in same folder
data=pd.read_csv('mnist.csv')
# viewing column heads
data.head()
# rashaping the extracted data into a reasonable size
a=a.reshape(28,28),astype('uint8')
plt.imshow(a)
# preparing the data and seperating labels and data values
df_x=data.iloc[:,1:]
df_y=data.iloc[:,0]
# creating test and table sizes
x_train, x_test, y_train, y_test=train_test_split(df_x, df_y, test_size=0.2, random_state=4)
# call rf classifier
rf = RandomForestClassifier(n_estimators=100)
# fit the model
rf.fit(x_train, y_train)
# prediction on test data
pred rf.predict(x_test)
s=y_test.values
# calculation of no. of correctly predicted values
count = 0
for i in range(len(pred)):
  if pred(i) == s(i)
     count += 1
 l=len(pred)
 # accuracy level
 accuracy = count/l
 
