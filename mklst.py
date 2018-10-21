import pandas as import pd
from janome.tokenizer import Tokenizer

def s2wakati(texts):
    t = Tokenizer()
    wakatis=[]
    for s_pre in texts:
        #文中の改行を削除
        s=''.join(s_pre.splitlines())
        tokens=t.tokenize(s)
        wakati_lst=[]
        for token in tokens:
            #単語だけwakati_lstに格納
            wakati_lst.append(token.surface)
            #単語を並べて間にスペースを入れる
            wakati=" ".join(wakati_lst)
        wakatis.append(wakati)
    return wakatis

def lern_lst(label_lst,wakati_lst):
    label_wakati=[]
    for label,text in zip(label_lst,wakati_lst):
        label_wakati.append("__label__"+str(label)+","+text)

    return label_wakati

def main():
    df=pd.read_csv("事前に作成した.csv")
    texts=df.text
    e_wakati=s2wakati(texts)
    e_label=df.label
    elements=learning_lst(e_wakati,e_label)

    f=open("list.txt","w")
    for e in elements:
        f.write(e+"\n")
    f.close()

if __name__ == '__main__':
    main()
