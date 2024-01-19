def maximumSumSubarray (self,K,Arr,N):
        if K>N or K<0:
            return -1
        sum = 0
        for i in range(K):
            sum+=Arr[i]
        start = 0
        max_sum = sum
        
        for j in range(K,N):
            sum = sum + Arr[j] - Arr[start]
            start+=1
            max_sum = max(max_sum,sum)
        return max_sum
