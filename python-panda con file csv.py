import pandas as pd 
df = pd.read_csv('titanic')
df
df.imdex
df.info()
df.head()
df.mean()
df.sort_values('age', ascending=False).head(3)
df['age']
df['age'].mean()
df['sex'].value_counts()
df[df['pclass']<= 2]
df.loc['nome riga', 'nome colonna']
df['sex'].value_counts().plot(kind='pie')


df['pclass'].value_counts().plot(kind='bar')

df['survived'].value_counts().plot(kind='pie')

females=df[df['sex'] == 'females']
females['survived'].value_counts().plot(kind='pie')

males=df[df['sex'] == 'males']
males['survived'].value_counts().plot(kind='pie')

df.head()

df.plot()

df.plot(x='age', y= 'fare', kind ='scatter') #asseniazione nei due punti

tips = pd.read_csv('tips.csv')
tips.head()
tips.plot(x='total_bill', y= 'tip', kind ='scatter')

ufos = pd.read_csv('nuforc_2019.csv', parse_dates['date_time'])
ufos['date_time'].value_counts()

ufos['date_time'].dt.date.value_counts()