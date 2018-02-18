from pyspark import SparkContext
from operator import add
import sys
import itertools
from collections import defaultdict
from pprint import pprint
support = 4
num_partitions = 2
sc = SparkContext(appName = "inf553")
def Apriori_Phase1(iterable, s):
        list_iterable = list(iterable)[:]
        number_pass = 2
        results = []
        sc1     = SparkContext(appName = "inf553_1")
    	local   = sc1.parallelize(list_iterable)
        local   = local.flatMap(lambda x : map(int, x.encode('ascii','ignore').split(',')))
        local   = local.map(lambda x:(x,1))
        local   = local.reduceByKey(add)
    	local   = local.filter(lambda x: x[1] >= s).map(lambda x: x[0])
        temp    = sorted(local.collect())[:]
        while(len(list(itertools.combinations(temp, number_pass))) > 0):
            temp1        = list(itertools.combinations(temp, number_pass)) #MONOTONICITY
            local_pairs  = sc1.parallelize(list_iterable)
            local_pairs  = local_pairs.flatMap(lambda x: generate_combinations_Phase1(x, temp1, number_pass, 1))
            local_pairs  = local_pairs.map(lambda x:(x,1)).reduceByKey(add).filter(lambda x:x[1] >= s).map(lambda x:x[0])
            for x in local_pairs.collect():
                results.append((x,1))
            temp         = list(set(list(itertools.chain(*local_pairs.collect()))))[:]
            number_pass += 1
        
        final =  results + local.map(lambda x:(x,1)).collect()
        sc1.stop()
        return final  
def generate_combinations_Phase1(s, ones, parts, bool = 0):
        l = map(int, s.split(','))
        if bool:
            l = list(itertools.combinations(l, parts))
            candidate_pairs = []
            for x in l:
                if x in ones:
                        candidate_pairs.append(x)   
            return candidate_pairs
        else:
            candidate_pairs = []
            for i in range(1,len(l)):
                candidates = list(itertools.combinations(l, i+1))
                candidate_pairs.append(candidates)
            return list(itertools.chain.from_iterable(candidate_pairs))
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
        local_pairs = local_pairs.flatMap(lambda x: generate_combinations_Phase1(x, [], 0, 0))
        local_pairs = local_pairs.filter(lambda x: Eliminate(x)).map(lambda x:(x,1)).reduceByKey(add)
        final = local.collect() + local_pairs.collect()
        sc2.stop()
        return final
phase1 = sc.textFile('baskets_test_SON.txt',2)
phase1 = phase1.mapPartitions(lambda x : Apriori_Phase1(x,2)).distinct()
frequentCandidates = sorted(phase1.collect(), key = lambda x:x[0])
phase2 = sc.textFile('baskets_test_SON.txt',2)
phase2 = phase2.mapPartitions(lambda x : Phase2(x)).coalesce(1).reduceByKey(add).filter(lambda x: x[1] >= support)
pprint(sorted(phase2.collect(), key = lambda x: x[0]))

	
