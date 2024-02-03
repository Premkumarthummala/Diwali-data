import pandas as pd
file_path = "/Users/premkumar/Downloads/Diwali Sales Data.csv"
data = pd.read_csv(file_path, encoding='ISO-8859-1')
df = pd.DataFrame(data)
print(df.head())

print(df.head())
print(df.info())
df.drop(["Status","unnamed1"], axis = 1 , inplace = True)
print(df.info())
print(pd.isnull(df))
print(pd.isnull(df).sum())
df.dropna(inplace=True)

df.rename(columns={"Marital_Status": "Relationship_status"},inplace=True)
print(df.columns)

print(df.info())
df['Amount']=df['Amount'].astype(int)
print(df['Amount'].dtype)

print(df.describe())

print(df[['Age', 'Amount', 'Orders']].describe())

import seaborn as sns
import matplotlib.pyplot as plt
a = sns.countplot(x='Gender',data=df)
plt.show()

a = sns.countplot(x = 'Gender',data= df)
for i in a.containers:
    a.bar_label(i)
plt.show()

sg = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by=['Amount'],ascending=False)
print(sg)

sg_graph = sns.barplot( x='Gender',y='Amount',data=sg)
for i in sg_graph.containers:
    sg_graph.bar_label(i)
plt.show()


ag = sns.countplot(x='Age Group',hue='Gender',data=df)
plt.show()
ag = sns.countplot(x='Age Group',hue='Gender',data=df)
for i in ag.containers:
    ag.bar_label(i)
plt.show()

Ga = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by= ['Amount'],ascending=False)
print(Ga)
ga_graph = sns.barplot(data=Ga,x='Age Group',y='Amount')
plt.show()

states = df.groupby(['State'], as_index= False)['Orders'].sum().sort_values(by='Orders', ascending = False).head(10)
print(states)
sns.set(rc={'figure.figsize':(15,5)})
states_graph = sns.barplot(data=states,x='State',y='Orders')
plt.show()


states = df.groupby(['State'], as_index= False)['Amount'].sum().sort_values(by='Amount', ascending = False).head(10)
print(states)
sns.set(rc={'figure.figsize':(15,5)})
states_graph = sns.barplot(data=states,x='State',y='Amount')
plt.show()


rs = sns.countplot(x ="Relationship_status",data=df)
sns.set({'figure.figsize':(6,2)})
for i in rs.containers:
    rs.bar_label(i)
plt.show()

rs = df.groupby(["Relationship_status"], as_index= False)['Amount'].sum().sort_values(by='Amount', ascending = False).head(10)
print(rs)
sns.set(rc={'figure.figsize':(5,2)})
sns.barplot(data=rs,x="Relationship_status",y='Amount',hue='Gender')
plt.show()



os = df.groupby(['Occupation'], as_index= False)['Orders'].sum().sort_values(by='Orders', ascending = False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=os,x='Occupation',y='Orders')
plt.show()

os = df.groupby(['Occupation'], as_index= False)['Amount'].sum().sort_values(by='Amount', ascending = False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=os,x='Occupation',y='Amount')
plt.show()

pc = sns.countplot(x ='Product_Category',data=df)
sns.set({'figure.figsize':(25,5)})
for i in pc.containers:
    pc.bar_label(i)
plt.show()

os = df.groupby(['Product_Category'], as_index= False)['Orders'].sum().sort_values(by='Orders', ascending = False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=os,x='Product_Category',y='Orders')
plt.show()

os = df.groupby(['Product_Category'], as_index= False)['Amount'].sum().sort_values(by='Amount', ascending = False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=os,x='Product_Category',y='Amount')
plt.show()


states = df.groupby(['Product_Category'], as_index= False)['Orders'].sum().sort_values(by='Orders', ascending = False).head(10)
print(states)
sns.set(rc={'figure.figsize':(15,5)})
states_graph = sns.barplot(data=states,x='Product_Category',y='Orders')
plt.show()


states = df.groupby(['Product_Category'], as_index= False)['Amount'].sum().sort_values(by='Amount', ascending = False).head(10)
print(states)
sns.set(rc={'figure.figsize':(15,5)})
states_graph = sns.barplot(data=states,x='Product_Category',y='Amount')
plt.show()


