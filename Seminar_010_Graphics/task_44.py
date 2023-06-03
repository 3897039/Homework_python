import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
df = pd.DataFrame({'whoAmI':lst})


df.loc[df['whoAmI'] == 'robot', 'number'] = '0'
df.loc[df['whoAmI'] == 'human', 'number'] = '1'

df.head()

