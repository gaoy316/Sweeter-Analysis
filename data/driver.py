from singlepage import single_page
import pandas as pd

i=20001
print i
df1 = single_page(i)
df1 = df1()
i=i+1

while(i<=25000):
    df2 = single_page(i)
    df1 = df1.append(df2())
    print i
    i=i+1
    
df1.to_csv('example5.csv')