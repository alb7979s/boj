
#1
b = '({[<'
c = ')}]>'


def solution(a):
    cnt = 0
    st = [[] for _ in range(4)]  # (), {}, [], <>
    for i in range(len(a)):
        if a[i] in b:
            st[b.index(a[i])].append(1)
        elif a[i] in c:
            try:
                st[c.index(a[i])].pop()
                cnt += 1
            except:
                return -1
    for i in range(4):
        if len(st[i]) != 0: return -1
    return cnt

#2
def cmp(ans, a1, a2):
    overlap_max_len = 0
    sus_cnt = 0
    temp = 0
    for i in range(len(ans)):
        if a1[i] == a2[i]:
            if ans[i] == a1[i]:
                overlap_max_len = max(overlap_max_len, temp)
                temp = 0
            else:
                sus_cnt += 1
                temp += 1
                overlap_max_len = max(overlap_max_len, temp)
        else:
            overlap_max_len = max(overlap_max_len, temp)
            temp = 0
    return sus_cnt + overlap_max_len ** 2


def solution(answer_sheet, sheets):
    res = 0
    ls = len(sheets)
    for i in range(ls - 1):
        for j in range(i + 1, ls - 1):
            res = max(res, cmp(answer_sheet, sheets[i], sheets[j]))
    return res

#4
hash_table = list([None for i in range(8)])


def get_key(data):
    return hash(data)


def hash_function(key):
    return key % 8


def save_data_hash_table(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != None:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([index_key, value])
    else:
        hash_table[hash_address] = [[index_key, value]]


def get_data_hash_table(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != None:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None


# hash table 코드 출처: https://www.fun-coding.org/Chapter09-hashtable.html#7.2.-Linear-Probing-%EA%B8%B0%EB%B2%95
# save_data_hash_table('David', '01032221111')
# get_data_hash_table('Dave')
def cal(d, prev, v):
    if d == 'S':
        return str(prev + v)
    else:
        return str(prev - v)


def solution(snapshots, transactions):
    visit = [0] * (10 ** 5)
    answer = []
    name_list = []
    for i in range(len(snapshots)):
        name_list.append(snapshots[i][0])
        save_data_hash_table(snapshots[i][0], snapshots[i][1])
    for i in range(len(transactions)):
        if visit[int(transactions[i][0])]: continue
        visit[int(transactions[i][0])] = 1
        try:
            save_data_hash_table(transactions[i][2], cal(transactions[i][1][0], int(get_data_hash_table(transactions[i][2])), int(transactions[i][3])))
        except:  # 없는 경우
            name_list.append(transactions[i][2])
            save_data_hash_table(transactions[i][2], cal(transactions[i][1][0], 0, int(transactions[i][3])))
    name_list.sort()
    for i in range(len(name_list)):
        answer.append([name_list[i], get_data_hash_table(name_list[i])])
    return answer

#5
ll=[]               #링크드 리스트 10개
for i in range(10):
    ll.append([-1,'ZZZZZZZZZZZ'])   #prev, value(태그포함개수, 문서이름), next

def solution(dataSource, tags):
    global ll
    answer = []
    for i in range(len(dataSource)):
        name = dataSource[i][0]
        cnt=0
        for x in dataSource[i][1:]:
            for t in tags:
                if x == t: cnt+=1       #문자열 더 빠르게 못하나.. KMP 열심히 공부할걸..
        if cnt==0: continue
        f=0
        for j in range(len(ll)):
            if ll[j][0] <= cnt:
                ll.append([cnt, name])
                f=1
                break
        if f:
            ll = sorted((sorted(ll, key = lambda x: x[1])), reverse = True, key = lambda x: x[0])
            ll.pop()
    for ll_cnt, ll_name in ll:
        if ll_cnt==-1: break
        answer.append(ll_name)
    return answer
