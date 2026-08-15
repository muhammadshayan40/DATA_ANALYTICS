#Concatenate & Merge DataFrames (JOINs)
import pandas as pd

data1={
    'ID':[101,102,103],
    'Name' : ["Shayan", "Ali", "Sara"]
}
data2={
    'ID':[101,102,103,104],
    'Score':[89, 92, 78, 95]
}

d1=pd.DataFrame(data1)
d2=pd.DataFrame(data2)

print(pd.concat([d1,d2],axis=0)) #top on top/ vertical concatenation
print(pd.concat([d1,d2],axis=1)) #side by side/ horizontal

#merge bhi hn likin wo gpt se krlegy