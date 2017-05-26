import os
import pandas as pd
from sklearn import tree
import pydot
import io

os.getcwd()

titanic_train = pd.read_csv("train.csv")
titanic_train.info()
#we need to define x trian and y train as two parameters

#X_train = [['Pclass','Sex','Embarked','Fare']]
#y_train = ['Survived']

#now i need to use sklearn pakacges to build a tree
#pre processing work 
'''
as algorithm has limitation it can work on numerical data only so we are converting.
as we have categorical varibles convert them dummy variables
one-hot-coding
Pclass varible as 3 values
so remove pclass and convert to three variables and given 1's  n 0's 
similar for all category colo
pandas pakcage has method to do this'''

#titanic_train1 = pd.get_dummies(titanic_train[['Pclass','Sex','Embarked','Fare']])
titanic_train1 = pd.get_dummies(titanic_train,columns=['Pclass','Sex','Embarked'])
titanic_train1.info()
titanic_train1.shape
titanic_train1.head(5)
#1 is for column level 0 for rowlevel
X_train = titanic_train1.drop(['Survived','Name','Age','Cabin','Ticket','PassengerId'],1)
y_train = titanic_train1['Survived']
dt = tree.DecisionTreeClassifier()
dt.fit(X_train,y_train)


#how to visualize visulaization is done by using pydot install dot.exe 
#pydot is interacting with dotexe file
#io package is input/output which file you want to write which place you want to write
#io can wrrite files,imaages,strings some medium to hold my image 
dot_data = io.StringIO() 
#what tree you want to export, we pass decision tree we tell which file you want to write
'''what tree
which file u want to write
what col m using in tree building'''
tree.export_graphviz(dt, out_file = dot_data,feature_names= X_train.columns)
#this export is done in xml form
graph = pydot.graph_from_dot_data(dot_data.getvalue())[0]
graph.write_pdf("dt2.pdf")

titanic_test = pd.read_csv("test.csv")
titanic_test.Fare[titanic_test['Fare'].isnull()] = titanic_test['Fare'].mean()
titanic_test1 = pd.get_dummies(titanic_test,columns=['Pclass','Sex','Embarked'])
titanic_test1.info()
titanic_test1.shape
X_test = titanic_test1.drop(['Name','Age','Cabin','Ticket','PassengerId'],1)
titanic_test["Survived"] = dt.predict(X_test)
titanic_test.to_csv("submission1.csv",columns=["PassengerId",'Survived'],index=False)

