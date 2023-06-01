import fugashi as fu
import pandas as pd
from nltk.translate.bleu_score import sentence_bleu,SmoothingFunction


org = open('data/org.txt').read().splitlines()
matis = open('data/matis.txt').read().splitlines()
google = open('data/google.txt').read().splitlines()


numsens = len(org)

print("The number of sentences of your file...")
print("org.txt", "matis.txt", "google.txt")
print((len(org), len(matis), len(google)))


tagger = fu.Tagger()

b_matis = []
b_google = []

for i in range(numsens):
    
    orgword = [word.surface for word in tagger(org[i])]
    mword = [word.surface for word in tagger(matis[i])]
    gword = [word.surface for word in tagger(google[i])]
    
    b_matis.append(round(sentence_bleu([orgword], mword, smoothing_function=SmoothingFunction().method4,), 2))
    b_google.append(round(sentence_bleu([orgword], gword, smoothing_function=SmoothingFunction().method4,), 2))


df = pd.DataFrame(list(zip(b_matis, b_google)), columns=["BLEU_MATIS", "BLEU_GOOGLE"])
df.to_csv('data/bleu.csv', sep=',')
