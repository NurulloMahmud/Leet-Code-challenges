"""
https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
"""

def miniMaxSum(arr:list):
    values = []
    arr.sort()
    for i in range(len(arr)):
        temp = arr.pop(i)
        values.append(sum(arr))
        arr.append(temp)
        arr.sort()
    print(min(values), max(values))