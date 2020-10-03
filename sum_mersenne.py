"""Sum of all mersenne numbers present in an array Given an array of integers arr[], the
task is to nd the sum of all the Mersenne numbers from the array. A number is a
Mersenne number if it is greater than 0 and is one less than some power of 2. First few
Mersenne numbers are 1, 3, 7, 15, 31, 63, 127, …
Examples:
Input: arr[] = {17, 6, 7, 63, 3}
Output: 73
Only 7, 63 and 3 are Mersenne numbers i.e. 7 + 63 + 3 = 73
Input: arr[] = {1, 3, 11, 45}
Output: 4
Sample Input:
5
17 6 7 63 3
Sample Output:
73
"""

def sum_mersenne(arr):
    sum=0
    for i in range(len(arr)):
        num=arr[i]+1
        
        count=0
        while num!=0:
            num=num//2
            #print(num)
            count+=1
        #print(arr[i],count-1)
        if (2**(count-1)-arr[i])==1:
            sum+=arr[i]
    return sum
print(sum_mersenne([17, 6, 7, 63, 3]))
