# 완전이진트리에서의 순회

def pre_order(v):
    global last
    if v <= last:   # 마지막 정점번호 아래면 존재하는 것
        print(v)        # visit(v)
        pre_order(v*2)     # 왼쪽 자식정점 방문
        pre_order(v*2+1)     # 오른쪽 자식정점 방문
