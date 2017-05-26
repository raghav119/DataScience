import pandas as pd
col1 = [10,20,30,40]
col2 = ['abc','def','xyz','pqr']
col3 = [0,0,0,0]



#Creating dataframe

df1 = pd.DataFrame({'pid': col1,'pname':col2,'survived':col3})
df1.shape
print(df1)
df1.describe


df2 = pd.DataFrame({'pid':col1,'pname': col2 ,'survived':col3})
df2.shape
df2.describe
df2.head(3)
df1.tail()

df1['col4'] = 1
   
#SELECTING A INDEX,COLUMN OR VALUE FROM DATAFRAME 
print(df1)
#for index we have to iloc and we provide the index postions
#within brackets witout comma seperation
print(df1.iloc[0][0])
#when trying to access the data with coloumn name we use 'loc'
print(df1.loc[0]['pid'])
#we can also use 'loc' using comma seperation to get the value of dataframe
print(df1.loc[0,'pid'])
print(df1.iloc[0,0])
#we can use get_value to get the data of particular index of dataframe
print(df1.get_value(0,'pid'))
df1.loc[1,'pname']= 3
print(df1.iloc[2])


#Selecting rows and columns of the Dataframe
print(df1.iloc[0])
print(df1.iloc[0,:])
print(df1.loc[1][:])

#adding index to a dataframe
print(df1.set_index('pid'))

   
#access frame content by column/columns

df1.pid
df1['pid']
df1[['pid','pname']]
df1[[0,1]]   

#dropping a column

df2 = df1.drop('pname',1)
print (df2)

#slicing rows of frame
df1[0:2]
df1[0:4]
df1[0:]
df1[:2]
df1[-2:]

#filtering rows of datasets by condition

type(df1.pid>20)
df1[df1.pid>20]

#selecting subsets of rows and coloumns
df1.iloc[0:2]
df1.iloc[[0,2]] 
df1.iloc[0:2,0] 
df1.iloc[0:2,[0,2]] 
df1.loc[0:2,['pname']] 
