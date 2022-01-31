import math
class Solution: # countPrimes strictly less than n
    def countPrimes(self, n: int) -> int: # Sieve of Eratosthenes - complexity n*log(logn)
#         if n <= 2: return 0 
        
#         isPrime = [True] * (n+1) # it stores if i'th value is prime or not from 0 to N
#         isPrime[0] = False
#         isPrime[1] = False
        
#         # from 2 to sqrt(n) => coz after that those will already be marked if 11 => 22 will already be marked 
#         for i in range(2 , int(math.sqrt(n))+1): 
#             # if 2 is prime then 4,6,8.. will not be prime & 3 is prime then 6,9.. will not be prime
#             for index in range(i*i, n+1, i): # 6 will already be marked for 3 by 2 so we start from i*i
#                 isPrime[index] = False
                
#         return sum(isPrime) - sum([isPrime[len(isPrime)-1]]) # countPrimes strictly less than n

        if n==0 or n==1 or n==2: return 0
        PrimeTable=[True]*(n)
        p=2
        while p*p<=n-1:
            if PrimeTable[p]==True:
                for i in range(p**2,n,p): PrimeTable[i]=False
            p += 1
        return sum(PrimeTable)-2