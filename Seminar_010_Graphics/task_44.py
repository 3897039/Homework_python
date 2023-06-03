import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
df = pd.DataFrame({'whoAmI':lst})


df.loc[df['whoAmI'] == 'robot', 'robot'] = '1'
df.loc[df['whoAmI'] == 'human', 'robot'] = '0'
df.loc[df['whoAmI'] == 'robot', 'human'] = '0'
df.loc[df['whoAmI'] == 'human', 'human'] = '1'

df.head()

