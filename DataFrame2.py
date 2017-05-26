"""import pandas as pd
import os

#return current working directory
os.getcwd()
os.chdir("E:/DATASCIENCE/DATASETS")
titanic_train = pd.read_csv("train.csv")
type(titanic_train)
print (titanic_train)
titanic_train.shape
titanic_train.info
titanic_train.tail()
titanic_train.describe()
titanic_train[0:3]
titanic_train.iloc[0:2,[0,1]]
titanic_train.groupby('Survived').size()
titanic_train.groupby(['Sex','Survived']).size()



titanic_test = pd.read_csv("test.csv")
titanic_test.shape
titanic_test.info
titanic_test['Survived'] = 0
titanic_test.to_csv("submission.csv",columns = ['PassengerId','Survived'],index=False)"""   

#we import pandas to use the method to read csv file
import pandas as pd
#to set os path at once so that we dont need to provide the same path again and again
import os

os.getcwd()
#chdir method is used to change the current working directory
os.chdir("E:/DATASCIENCE/DATASETS")
#we will read the file using pandas and will assign to some varible
titanic_train=pd.read_csv("train.csv")
print(titanic_train)
#shape is used to see the no of coloums and rows of the loaded data
titanic_train.shape
#describe() will describe only for only numbers for string it wont show
titanic_train.describe()

titanic_train.groupby(['Survived']).size()

#want to grouby data based ons sex and survival and also want to c the count
titanic_train.groupby(['Sex','Survived']).size()

#titanic_train.loc[titanic_train.Sex=='Female','Survived']=1

#now will use test data to apply our login of making all female as survived

#to load test data use panda csv and save it to label titanic_test

titanic_test=pd.read_csv("test.csv")

#As there is no coloum survived in this we will add one coloum with label Survived

#to add column we can use loc

titanic_test['Survived'] =0
            
titanic_test.shape   
print(titanic_test)         
#now we are trying to set value sex to 1 when its female to a column survived
titanic_test.loc[titanic_test.Sex=='female','Survived'] = 1
#we are trying to print it we are using [[]]  because as frame is a list and inside we are dealing multiple columns which again bcome list               
print(titanic_test[['PassengerId','Survived']])                
#to write that to csv file first we need to give csv file with name separted by commo and folowed by colums we want to display
#where we should use = operator and index should be false as by default index will be created as keggle accepts without index 
titanic_test.to_csv("submission.csv",columns=['PassengerId','Survived'],index='False')


titanic_test.to_csv("submission3.csv",columns=['PassengerId','Survived'],index=False)

titanic_test.describe()
                 
                 





    
