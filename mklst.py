import pandas as pd
from janome.tokenizer import Tokenizer

df1=pd.read_csv("review1.csv")
df2=pd.read_csv("review2.csv")
df3=pd.read_csv("review3.csv")
df4=pd.read_csv("review4.csv")
df5=pd.read_csv("review5.csv")

df=df1.append(df2).reset_index(drop=True)
df=df.append(df3).reset_index(drop=True)
df=df.append(df4).reset_index(drop=True)
df=df.append(df5).reset_index(drop=True)

labels=df.score
texts=df.text
t = Tokenizer()
wakatis=[]
for s_pre in texts:
    s=''.join(s_pre.splitlines())
    tokens=t.tokenize(s)
    wakati_lst=[]
    for token in tokens:
        wakati_lst.append(token.surface)
        wakati=" ".join(wakati_lst)
    wakatis.append(wakati)

label_wakati=[]

for label,text in zip(labels,wakatis):
    label_wakati.append("__label__"+str(label)+","+text)

print(label_wakati)

f=open("list.txt","w")
for e in label_wakati:
    f.write(e+"\n")
f.close()
