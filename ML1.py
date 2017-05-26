import os
import pandas as pd
#sklearn pakcage have tree 
#from -- sklearn is a big package having lot of submodules(tree is one apporoch) tree is subpackage
from sklearn import tree
import io
import pydot

os.chdir("E:/DATASCIENCE/DATASETS")
titanic_train=pd.read_csv("train.csv")

#EDA

titanic_train.shape
titanic_train.info()

#creating a variable and storing the data of Pclss and Survived col
X_train = titanic_train[['Pclass']]

Y_train = titanic_train['Survived']


#Building the decision tree model

dt = tree.DecisionTreeClassifier()
#tree into train  data x is features y is target  when calling fit method tree will be ready
#fit method builds tree link xcol to ycol n build a tree
dt.fit(X_train,Y_train)

#visulize the decision tree
dot_data = io.StringIO()
tree.export_graphviz(dt, out_file = dot_data,feature_names= X_train.columns)
graph = pydot.graph_from_dot_data(dot_data.getvalue())[0]
graph.write_pdf("dt2.pdf")

titanic_test = pd.read_csv("test.csv")
titanic_test.shape
X_test = titanic_test[["Pclass"]]
titanic_test['Survived'] = dt.predict(X_test)
titanic_test.to_csv("submission6.csv", columns=["Survived","PassengerId"],index=False)

                                 






