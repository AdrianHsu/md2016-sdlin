 #-*- coding: UTF-8 -*- 

import viterbi
import numpy as np


# 1 x 37, 每個都 1/37
pi = np.array([[0.6, 0.4]]).T
# 37 * 37, f00, f01...f036 總和為1, e.g. f[0] = [f[0][0], f[0][1]...]
trans = np.array([
    [0.7, 0.3], \
    [0.6, 0.4]])
# 37 * 37, p00, p01...p036 總和為1
obs = np.array([[0.5, 0.4, 0.1], \
                [0.1, 0.3, 0.6]])
# size 看字串多長，吃進來後轉成 index 0~36
data = [[0, 1, 2]]
d = viterbi.Decoder(pi, trans, obs)
print d.Decode(data[0])
