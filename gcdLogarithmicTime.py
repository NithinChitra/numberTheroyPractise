def gcd(a,b):
    # i=2
    # hcf = 0
    # while i<=a:
    #     if a%i==0 and b%i==0:
    #         if i>hcf:
    #             print(hcf)
    #             hcf = i
    #     i+=1
    # return hcf
    if b==0:
        return a
    else:
        return gcd(b,a%b)
res = gcd(10,20)
print(res)
