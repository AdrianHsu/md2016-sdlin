#!/usr/bin/env python3
 #-*- coding: UTF-8 -*- 

# "隱含"state的list （S，代表現在healthy or sick。注意hmm的state都是"hidden"，因為只能從observations中推斷）
states = ('Healthy', 'Fever')

# 測資，丟進去的observation序列（V，HMM才有這個）
observations = ('normal', 'cold', 'dizzy')
# 結果：(0.01512, ['Healthy', 'Healthy', 'Fever']) 
# 0.6 * 0.5 * 0.7 * 0.4 * 0.3 * 0.6 = 0.01512

observations_2 = ('normal', 'cold', 'normal')
# 結果：(0.0294, ['Healthy', 'Healthy', 'Healthy'])
observations_3 = ('dizzy', 'cold', 'normal')
# 結果：(0.01344, ['Fever', 'Healthy', 'Healthy'])

# 初始化（pi節點）的機率 （一個人在今天算起是健康or生病？所以特別把邊界條件抓出來）
start_probability = {'Healthy': 0.6, 'Fever': 0.4}

# 轉態機率（每條邊aij的條件機率）現在在state = 健康，下次state = 健康的機率為0.7
transition_probability = { 
   'Healthy' : {'Healthy': 0.7, 'Fever': 0.3},
   'Fever' : {'Healthy': 0.4, 'Fever': 0.6},
   }

# 噴出這種observation的條件機率。現在在state = 健康，當下噴出的observation = dizzy的機率為0.1
# 表示每天病人感覺的可能性。假如他是健康的，50%會感覺正常。如果他發燒了，有60%的可能感覺到頭暈。
emission_probability = {
   'Healthy' : {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
   'Fever' : {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6},
   }

# Helps visualize the steps of Viterbi.
def print_dptable(V):
    print "    ",
    for i in range(len(V)): print "%7d" % i,
    print

    for y in V[0].keys():
        print "%.5s: " % y,
        for t in range(len(V)):
            print "%.7s" % ("%f" % V[t][y]),
        print

# 噴出來的observation 不知道是從哪一個state噴出來的
# 看到一個觀察序列 o 1 o 2 ...... o T ，
# 但是看不到狀態序列 s 1 s 2 ...... s T 的情況下，
# 從所有可能的路徑當中，找出機率最大的一條路徑，以及其機率。e.g.結果：(0.01512, ['Healthy', 'Healthy', 'Fever']) 
def viterbi(obs, states, start_p, trans_p, emit_p):
	V = [{}]
	path = {}

	# 初始化base cases (時間t = 0)
	for y in states:
		V[ 0 ][ y ] = start_p[ y ] * emit_p[y][obs[0]]
		path[y] = [y]
	
	# 跑 Viterbi alg. for時間 t > 0
	for t in range(1, len(obs)):
		V.append({})
		newpath = {}

		for y in states:
			(prob, state) = max([(V[t - 1][ y0 ] * trans_p[ y0 ][ y ] * emit_p[ y ][ obs[t] ], y0) for y0 in states])
			V[t][y] = prob
			newpath[y] = path[state] + [y]

        # 不需要記得剛剛走哪一條線（不用管上一筆轉態機率）
        path = newpath

	print_dptable(V)
	(prob, state) = max( [( V[len( obs ) - 1][ y ], y) for y in states] )
	return (prob, path[state])


def main():
    return viterbi(observations,
                   states, 
                   start_probability, 
                   transition_probability,
                   emission_probability)  
print main()