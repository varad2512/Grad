from pyspark import SparkContext
from operator import add
from collections import defaultdict
import itertools
sc = SparkContext(appName = 'INF551')
threshold_support = 5
false_positives_list = []
a=1
b=1
N=7
def create_map(l):
    for x in l:
        map1[x[0]] = int(x[1])
def generate_combinations(s, a, b, N):
	l = map(int, s.split(','))
	l = list(itertools.combinations(l, 2))
	res = []
	for x in l:
		hash_function = (a*int(x[0]) + b*int(x[1])) % N
		res.append((hash_function, x))
	return res
     
def gen_pairs(l):
	temp = list(itertools.combinations(map(int, l.split(',')),2))
	result = []
	pruned = []
	for x in temp:
		if freq_table[(x[0]*a + x[1]*b) % N] == 1 and map1[x[0]] == 1 and map1[x[1]] == 1:
			result.append(x)
		elif freq_table[(x[0]*a + x[1]*b) % N] != 1 and map1[x[0]] == 1 and map1[x[1]] == 1:
			pruned.append(x)
	with open('candidates_pruned.txt','w') as fw:
		for x in pruned:
			fw.write(str(x)+"\n")

	return result

lines = sc.textFile('baskets_PCY_test.txt')
lines = lines.flatMap(lambda x:x.split(',')).map(lambda x: (int(x.encode('ascii','ignore')), 1))
count_table = lines.reduceByKey(add)
map1 = defaultdict(int)
create_map(count_table.collect())
for x,y in map1.iteritems():
    if y >= threshold_support:
        map1[x] = 1
    else:
        map1[x] = 0
lines1 = sc.textFile('baskets_PCY_test.txt')
lines1 = lines1.flatMap(lambda x: generate_combinations(x, a, b, N))
freq_table = lines1.countByKey()
for x,y in freq_table.iteritems():
    if y >= threshold_support and x!=6:
        freq_table[x] = 1
    else:
        freq_table[x] = 0
lines2 = sc.textFile('baskets_PCY_test.txt')
lines2 = lines2.flatMap(lambda x:gen_pairs(x))
lines2 = lines2.map(lambda x : (x,1))
lines2 = lines2.reduceByKey(add)
false_positives_list = lines2.filter(lambda x: x[1] < threshold_support).collect()
true_positives_list  = lines2.filter(lambda x: x[1] >= threshold_support).collect()
print len(false_positives_list)
print len(sorted(true_positives_list, key = lambda x:x[0]))
