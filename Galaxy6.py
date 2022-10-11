def galaxy(n):
    if n==0:
        return
    else:
        galaxy(n-1)
        print("*"*n)
n = int(input())
galaxy(n)