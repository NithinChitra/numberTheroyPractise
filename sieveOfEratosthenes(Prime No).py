from math import *
N = 17
list = []
prime = [1]*(N+1)

for i in range(2,int(sqrt(N))+1):
    if prime[i]==1:
        j=i*i
        while j<=N:
            prime[j]=0
            j+=i

for i in range(2,N+1):
    if prime[i]==1:
        print(i,end=" ")