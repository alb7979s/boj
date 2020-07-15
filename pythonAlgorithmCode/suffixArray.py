#Suffix Array
#https://www.acmicpc.net/problem/9248 시간초과남 화가난다!!!! 
from collections import defaultdict     #초기값 리스트나 set으로 저장가능
def SA_ManberMyers(_str):
    res = []
    def sort_bucket(_str, bucket, order=1):
        d = defaultdict(list)
        for i in bucket:
            key = _str[i: i+order]          #여기서 시간 잡아먹는듯, 개선하기
            d[key].append(i)
        #d의 key로 정렬해준 값들 가지고 진행
        for k, v in sorted(d.items()):      #같은 그룹인애들 다시 정렬해줌
            if len(v) > 1:
                sort_bucket(_str, v, order*2)
            else:                           #그룹 정리 끝난애들 저장
                res.append(v[0])
        return res
    return sort_bucket(_str, (i for i in range(len(_str))))
def LCP(_str):
    sa = SA_ManberMyers(_str)
    n=len(_str)
    lcp = [None]*n
    rank=[0]*n
    for i in range(n):
        rank[sa[i]] = i
    l=0
    for i in range(n):
        k = rank[i]
        if k:
            j = sa[k-1]
            while i+l < n and j+l < n and _str[j+l] == _str[i+l]:
                l+=1
            lcp[k] = l
            if l: l -= 1
    if n: lcp[0] = 'x'
    return sa, lcp
a=input()
sa, lcp = LCP(a)
for x in sa:
    print(x+1,end=' ')
print()
for x in lcp:
    print(x, end=' ')
#출처: https://github.com/benfulton/Algorithmic-Alley/blob/master/AlgorithmicAlley/SuffixArrays/sa.py
