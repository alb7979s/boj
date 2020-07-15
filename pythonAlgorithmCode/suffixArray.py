#Suffix Array

from collections import defaultdict     #초기값 리스트나 set으로 저장가능
def SA_ManberMyers(_str):
    res = []
    def sort_bucket(_str, bucket, order=1):
        d = defaultdict(list)
        for i in bucket:
            key = _str[i: i+order]
            d[key].append(i)
        #d의 key로 정렬해준 값들 가지고 진행
        for k, v in sorted(d.items()):      #같은 그룹인애들 다시 정렬해줌
            print(k, v)
            if len(v) > 1:
                sort_bucket(_str, v, order*2)
            else:                           #그룹 정리 끝난애들 저장
                res.append(v[0])
        return res
    return sort_bucket(_str, (i for i in range(len(_str))))

a=input()
sa = SA_ManberMyers(a)
for x in sa:
    print(a[x:])
    
#출처: https://github.com/benfulton/Algorithmic-Alley/blob/master/AlgorithmicAlley/SuffixArrays/sa.py
