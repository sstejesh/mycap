import sys
print('python: {}'.format(sys.version))
import scipy
print('scipy: {}'.format(scipy.__version__))
import numpy
print('numpy: {}'.format(numpy.__version__))
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
import pandas
print('pandas: {}'.format(pandas.__version__))
import sklearn
print('sklearn: {}'.format(sklearn.__version__))

import pandas
from pandas read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.matrices import classification_report
from sklearn.matrices import confusion_matrix
from sklearn.matrices import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import model_selection
from sklearn.ensemble import VotingClassifier

#loading the data
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length','sepal-width','petal-length','petal-width,'class']
dataset = read_csv(url, names=names)

#dimensions of dataset
print(dataset.shape)
#take a peek at the data
print(dataset.head(20))
#statistical summary
print(dataset.describe())
#class distribution
print(dataset.groupby('class').size())
#univariate plots - box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()
#histogram of the variable
dataset.hist()
pyplot.show()
#multivariate plots
scatter_matrix(dataset)
pyplot.show()
#creating a validation dataset
#splitting dataset
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
X_train,X_validation,Y_train,Y_validation = train_test_split(X, Y, test_size=0.2, randon_state=1)

#building models
model = []
models.append(('LR",LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA',LinearDiscriminantAnalysis()))
models.append(('KNN',KNeighborsClassifier()))
models.append(('NB',GaussianNB()))
models.append(('SVM',SVC(gamma='auto)))
#evaluate the created models
results = []
names = []
for name, model in models:
  kfold=StratifiedKFold(n_splits=10, random_state=1)
  cv_results=cross_val_score(model,X_train,Y_train,cv=kfold,scoring='accuracy')
  results.append(cv_results)
  names.append(name)
  print('%s:%f(%f)' % (name,cv_results.mean(),cv_results.std()))
  
#compare the models
pyplot.boxplot(results,label=names)
pyplot.title('Algorithm Comparison')
pyplot.show()

#make predictions on svm
model=SVC(gamma='auto')
model.fit(X_train,Y_train)
predictions=model.predict(X_validation)
