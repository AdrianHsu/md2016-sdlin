 #-*- coding: UTF-8 -*- 

import viterbi
import numpy as np

pi = np.array([[0.6, 0.4]]).T
trans = np.array([
    [0.7, 0.3], \
    [0.6, 0.4]])
obs = np.array([[0.5, 0.4, 0.1], \
                [0.1, 0.3, 0.6]])
data = [[0, 1, 2]]
d = viterbi.Decoder(pi, trans, obs)
print d.Decode(data[0])
