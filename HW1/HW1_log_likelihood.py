from collections import Counter
from numpy import log
import re


def calculate_loglikelihood(md):
    test_est = md['test']['total'] * md['total']['word'] / md['total']['total']
    ref_est = md['ref']['total'] * md['total']['word'] / md['total']['total']
    ll = 2 * ((md['test']['word'] * log(md['test']['word'] / test_est)) + \
              (md['ref']['word'] * log(md['ref']['word'] / ref_est)))
    return ll


def get_loglikelihood(test_freq,test_N,ref_freq,ref_N):
    matrix_dict = {'test':
                   {'word':test_freq,
                    'other_words':test_N - test_freq,
                    'total': test_N},
                   'ref':
                   {'word':ref_freq,
                    'other_words':ref_N - ref_freq,
                    'total': ref_N},
                   'total':
                   {'word':test_freq + ref_freq,
                    'other_words':test_N + ref_N - test_freq - ref_freq,
                    'total': test_N + ref_N}
                   }
    return calculate_loglikelihood(matrix_dict)


def get_weirdness(test_freq,test_N,ref_freq,ref_N):
    w = (test_freq / test_N) / (ref_freq / ref_N)
    return w

                           

with open('court-V-N.csv','r',encoding='utf-8') as f:
    test_tokens = [x.strip(',') for sent in f.readlines()
                   for x in sent.strip().split() if x.strip(',')]
    test_N = len(test_tokens)
    test_wfs = Counter(test_tokens)

print('top-10 of SpecCorpus by freq')
for w in test_wfs.most_common(10):
    print(w[0])
print()

with open('Sc_part1.txt','r',encoding='cp1251') as f:
    ref_tokens = re.findall('\[(?:kw#+|NE#+)*(.+?)[.\]]',f.read())
    ref_N = len(ref_tokens)
    ref_wfs = Counter(ref_tokens)

scores = []
for word,test_freq in test_wfs.items():
    if word in ref_wfs:
        ll = get_loglikelihood(test_freq,test_N,ref_wfs[word],ref_N)
        w = get_weirdness(test_freq,test_N,ref_wfs[word],ref_N)
        scores.append((word,ll,w))
scores = sorted(scores,key=lambda x: x[1],reverse=True)

# for ranks
lls = {x:i+1 for i,x in enumerate(sorted(list(set([x[1] for x in scores])),reverse=True))}
ws = {x:i+1 for i,x in enumerate(sorted(list(set([x[2] for x in scores])),reverse=True))}

print('Top-10')
for w,ll,weird in scores[:10]:
    print(w,'тематическое',test_wfs[w],ref_wfs[w],
          ll,lls[ll],weird,ws[weird],sep='\t')

print()

print('Anti-top-10')
for w,ll,weird in scores[-10:]:
    print(w,'общеупотребительное',test_wfs[w],ref_wfs[w],
          ll,lls[ll],weird,ws[weird],sep='\t')
