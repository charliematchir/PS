import time
l = [1, 2, 3, 4, 5, 6, 7, 8]
p = [1, 5, 8, 9, 10, 17, 17, 20]
n= len(l)


'''
First bruteForce Rod is 20 time slower than second
Time Complexity: O(2n) where n is the length of the price array.
Space Complexity: O(n) where n is the length of the price array.
'''
def Rod(curr, left, idx):

    if left == 0:
        return curr
    
    value = 0
    for i in range(idx, n):
        if left >=l[i]:
            value = max(Rod(curr+p[i], left-l[i],i), Rod(curr, left,i+1), value) 
    return value
'''
첫번째 코드는 DP의 Optimal substructure의 모습이 비교적 적음 

'''

def cutRod(index, n):
     
    if index == 0:
        return n*p[0]
     
    notCut = cutRod(index - 1,n)
    cut = float("-inf")
    #rod_length = index + 1
 
    #if (rod_length <= n):
    if l[index] <= n:
        cut = p[index]+cutRod(index,n - l[index])
   
    return max(notCut, cut)

def main():
    start = time.time()
    print(Rod(0, 8, 0))
    end = time.time()
    print("First Rod Took: ", (end-start)*10000)
    
    start = time.time()
    print(cutRod(n-1, n))
    end = time.time()
    print("Secodn Rod took: ", (end-start)*10000)




if __name__ == '__main__':
    main()


