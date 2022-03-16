# 최대 100개의 자연수가 키로 입력
# 최대 힙

def enq(n):
    global last
    last += 1
    tree[last] = n  # 완전이진트리 유지
    c = last
    p = c//2
    while p >= 1 and tree[p] < tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2


def deq():
    global last
    tmp = tree[1]
    tree[1] = tree[last]
    last -= 1
    # 부모 > 자식 규칙 유지
    p = 1
    c = p * 2  # 왼쪽 자식
    while c <= last:    # 왼쪽 자식이 존재
        if c + 1 <= last and tree[c] < tree[c+1]:   # 오른쪽 자식이 크면
            c += 1   # 오른쪽 자식으로 선택
        if tree[p] < tree[c]:
            tree[p], tree[c] = tree[c], tree[p]
            p = c
            c = p*2
        else:
            break
    return tmp
# 포화이진트리의 정점번호
tree = [0]*101
last = 0
enq(3)
enq(4)
enq(6)
enq(1)
enq(7)
print(tree[1])
while last>0:
    print(deq(), tree[1])


