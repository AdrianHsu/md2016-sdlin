
# coding: utf-8

# In[87]:

#!/usr/bin/env python


import numpy as np
import pandas as pd
from sklearn import preprocessing


# In[88]:

probs = pd.read_csv("./valid/encode.bin", header=None,sep=" ") 
#A transition probability matrix and the B observation likelihood matrix


# In[89]:

#probs


# In[90]:

B_obs_llh = np.zeros((37, 37))
for i in probs.T:
    B_obs_llh[ probs.ix[i,0] ][ probs.ix[i,1] ] = probs.ix[i,2]


# In[91]:

B_obs_llh = preprocessing.normalize(B_obs_llh, norm='l1') # emission_probability, 37 * 37


# In[92]:

mydict = pd.read_csv("./valid/symbolToNum.dict", header=None, sep="\t")


# In[93]:

#mydict


# In[ ]:

test = pd.read_csv("./valid/test_copy.num", header=None, sep=" ")
#test = pd.read_csv("./valid/test.num", header=None, sep=" ")


# In[ ]:

#ans = pd.read_csv("./valid/ans_copy.num", header=None, sep=" ")
ans = pd.read_csv("./valid/ans.num", header=None, sep=" ")


# In[ ]:

_test = test.values.tolist()
a = _test[0]
b = _test[0][1:]
_list = [list(c) for c in zip(a,b)]


# In[ ]:

mybigram = np.zeros((37, 37))


# In[ ]:

for i in _list:
    mybigram[i[0], i[1]] += 1


# In[ ]:

print("done!")
A_trans_prob = preprocessing.normalize(mybigram, norm='l1') # transition_probability, 37 * 37 
#sum to be 1 (e.g. a probability distribution) 


# In[ ]:

B_obs_llh


# In[ ]:

A_trans_prob


# In[ ]:

'''
N: number of hidden states
'''
class Decoder(object):
    def __init__(self, initialProb, transProb, obsProb):
        self.N = initialProb.shape[0]
        self.initialProb = initialProb
        self.transProb = transProb
        self.obsProb = obsProb
        assert self.initialProb.shape == (self.N, 1)
        assert self.transProb.shape == (self.N, self.N)
        assert self.obsProb.shape[0] == self.N
        
    def Obs(self, obs):
        return self.obsProb[:, obs, None]

    def Decode(self, obs):
        trellis = np.zeros((self.N, len(obs)))
        backpt = np.ones((self.N, len(obs)), 'int32') * -1
                
        # initialization
        trellis[:, 0] = np.squeeze(self.initialProb * self.Obs(obs[0]))
                
        for t in range(1, len(obs)):
            trellis[:, t] = (trellis[:, t-1, None].dot(self.Obs(obs[t]).T) * self.transProb).max(0)
            backpt[:, t] = (np.tile(trellis[:, t-1, None], [1, self.N]) * self.transProb).argmax(0)
        # termination
        tokens = [trellis[:, -1].argmax()]
        for i in range(len(obs)-1, 0, -1):
            tokens.append(backpt[tokens[-1], i])
        return tokens[::-1]


# In[ ]:

pi = np.zeros((1, 37))
for i in range(0, len(pi[0])):
   pi[0][i] = (1.0 / 37.0)


# In[ ]:

d = Decoder(pi.T, A_trans_prob, B_obs_llh)


# In[ ]:

_test[0]


# In[ ]:
try_test = pd.read_csv("./valid/test.num", header=None, sep=" ")
try_list_test = try_test.values.tolist()

pred = d.Decode(try_list_test[0])


# In[ ]:

for i in pred:
   print(i),


# In[142]:

count = 0
total = len(pred)
for i in pred:
    if pred[i] == ans.ix[0,i]:
        count += 1
        


# In[143]:

err = count/total


# In[133]:

print("ERROR RATE: ")
print(err)


# In[ ]:



