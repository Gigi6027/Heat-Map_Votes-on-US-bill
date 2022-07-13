!pip install pandas
import pandas as pd

#Creating a data frame using pandas
Df=pd.read_csv('Book2.csv')
Df.head()

#Creating the two columns of the data frame
myOrd1=Df['Party']
myOrd2=Df['VotePosition']

#Creating a cross table with the values
CrossTable=pd.crosstab(myOrd2,myOrd1)
CrossTable

#Updating the table to remove non voting cadidates
up=CrossTable.drop('Not Voting')
up
up.style.background_gradient(cmap='GnBu')


#Creating the heat map
import seaborn as sns
sns.heatmap(up,annot=True,cmap='GnBu')