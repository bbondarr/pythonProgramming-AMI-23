# Calculate the number of ways in which a bunny with a maximal step of K 
# can get on Nth stair

def calcWays(K, N):        
    temp = 0
    res = [1]  
      
    for currStair in range(1, N + 1): 
        i = currStair - K - 1

        # Window Sliding technique: as soon as we get to i>=K,
        # we start substracting first elements to maintain the scope K,
        # which we need for answer, because res[N] = sum(res[N-1], res[N-2], ...,res[N-K])
        if (i >= 0): 
            temp -= res[i]              
        temp += res[currStair - 1]  

        res.append(temp)  

    return res[N]  

print('-' * 90)
print('This programm counts the number of ways to get on Nth stair with the maximal step K')
print('-' * 90)
n = int(input('Enter N value: '))
assert 1 <= n and n <= 300
print('-' * 90)
k = int(input('Enter K value: '))
assert 1 <= k and k <= 300 and k <= n
print('-' * 90)

print('You can get on %dth stair with maximal step of %d in %d ways' 
    % (n, k, calcWays(k, n)))