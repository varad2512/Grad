from pyspark import SparkContext
from operator import add
import sys
import itertools
support = sys.argv[2]
num_partitions = sys.argv[3]
sc = SparkContext(appName = "inf553")
def Apriori_Phase1(iterable, s):
       	chunk1,chunk2 = itertools.tee(iterable) 
        result_ones  = []
        result_pairs = []
        sc1 = SparkContext(appName = "inf553_1")
    	local_ones = sc1.parallelize(chunk1)
        local = local_ones.flatMap(lambda x : map(int, x.encode('ascii','ignore').split(',')))
        local = local.map(lambda x:(x,1))
        local = local.reduceByKey(add)
    	local = local.filter(lambda x: x[1] >= s).map(lambda x: x[0])
        local = local.collect()
        for x in local:
                result_ones.append((x,1))
    	local_pairs = sc1.parallelize(chunk2)
        local_pairs = local_pairs.flatMap(lambda x: generate_combinations_Phase1(x, local, 1))
        local_pairs = local_pairs.map(lambda x:(x,1)).reduceByKey(add).filter(lambda x:x[1] >= s).map(lambda x:x[0])
        for x in local_pairs.collect():
                result_pairs.append((x,1))
        phase1Result = result_ones + result_pairs
        sc1.stop()
        return phase1Result
def generate_combinations_Phase1(s, ones = [], bool = 0):
        l = map(int, s.split(','))
        l = list(itertools.combinations(l, 2))
        candidate_pairs = []	
        if bool:
            for x in l:
                if x[0] in ones and x[1] in ones:
                        candidate_pairs.append(x)
        	return candidate_pairs
        else:
            return l
def Eliminate(x):
        for i in frequentCandidates:
            if x == i[0]:
                return True
        return False
def Phase2(iterable):
        chunk1,chunk2 = itertools.tee(iterable)
        sc2 = SparkContext(appName = "inf553_2")
        local_ones = sc2.parallelize(chunk1)
        local = local_ones.flatMap(lambda x : map(int, x.encode('ascii','ignore').split(',')))
        local = local.filter(lambda x: Eliminate(x))
        local = local.map(lambda x:(x,1))
        local = local.reduceByKey(add)
        local_pairs = sc2.parallelize(chunk2)
        local_pairs = local_pairs.flatMap(lambda x: generate_combinations_Phase1(x, 0))
        local_pairs = local_pairs.filter(lambda x: Eliminate(x))
        local_pairs = local_pairs.map(lambda x:(x,1)).reduceByKey(add)
        Result = local.collect() + local_pairs.collect()
        sc2.stop()
        return Result
phase1 = sc.textFile(sys.argv[1], num_partitions)
phase1 = phase1.mapPartitions(lambda x : Apriori_Phase1(x, support/num_partitions)).distinct()
frequentCandidates = sorted(phase1.collect(), key = lambda x:x[0])
phase2 = sc.textFile(sys.argv[1], num_partitions)
phase2 = phase2.mapPartitions(lambda x : Phase2(x)).coalesce(1).reduceByKey(add).filter(lambda x: x[1] >= support)
print sorted(phase2.collect(), key = lambda x: x[0])

	
