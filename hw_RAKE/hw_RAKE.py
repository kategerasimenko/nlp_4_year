import RAKE
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

with open('Bitcoin.txt','r',encoding='utf-8-sig') as f:
    text = f.read()

print('Базовый вариант')
Rake = RAKE.Rake(RAKE.SmartStopList())
res = Rake.run(text, maxWords = 3)
for r in res[:15]:
    print(r[0],'-',r[1])

print()

print('Продвинутый вариант')
wn_lemmatizer = WordNetLemmatizer()
tokens = word_tokenize(text)
lemmas = []
for token in tokens:
    lemma = wn_lemmatizer.lemmatize(token)
    if lemma == token:
        lemma = wn_lemmatizer.lemmatize(token,'v')
    lemmas.append(lemma)
lemmatized_text = ' '.join(lemmas)
res = Rake.run(lemmatized_text, maxWords = 3)
for r in res[:15]:
    print('minFreq 1:',r[0],'-',r[1])
print()
res = Rake.run(lemmatized_text, maxWords = 3, minFrequency = 2)
for r in res[:15]:
    print('minFreq 2:',r[0],'-',r[1])

print()

with open('Bitcoin_rus.txt','r',encoding='utf-8-sig') as f:
    text = f.read()

print('Базовый вариант - русский')
stop_words = stopwords.words('russian')
stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', '—', 'к', 'на'])
Rake = RAKE.Rake(stop_words)
res = Rake.run(text, maxWords = 3)
for r in res[:15]:
    print(r[0],'-',r[1])
