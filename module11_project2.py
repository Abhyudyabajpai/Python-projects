import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
 df = pd.read_csv('WorldCupMatches.csv')
print(df.head())
df['Total Goals']= df['Home Team Goals']+df['Away Team Goals']
sns.set_style('whitegrid')
sns.set_context('poster',font_scale=1.5)
f,ax = plt.subplots(figsize=(12,7))
ax =sns.barplot(x='Year',y='Goals')
plt.show()
ax.set_title('Football')
df_goals = pd.read_csv('goals.csv')
print(df_goals.head())
sns.set_context('notebook',font_scale = 1.25)
f,ax2=plt.subplots(figsize=(12,7))
sns.boxplot(data=df_goals,x='year',y='goals',palette='Spectral')
ax2.set_title('Football2')
plt.show()
