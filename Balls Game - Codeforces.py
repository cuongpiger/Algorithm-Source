#https://codeforces.com/problemset/problem/430/B
'''
Comment
'''
n = 0
k = 0
x = 0
balls = []

def cntBall(pos):
    l = r = pos
    cnt = 0

    while balls[l] == balls[r]:
        tmp = 2

        while l > 0 and balls[l - 1] == balls[l]:
            l -= 1
            tmp += 1

        while r < n - 1 and balls[r + 1] == balls[r]:
            r += 1
            tmp += 1

        l -= 1
        r += 1

        if tmp < 3:
            break

        cnt += tmp

        if l < 0 or r >= n:
            break
        
    return cnt - 1

if __name__ == "__main__":
    n, k, x = map(int, input().split())
    balls = list(map(int, input().split()))
    res = 0
    
    for i in range(n):
        if balls[i] == x:
            res = max(res, cntBall(i))

    print(res)