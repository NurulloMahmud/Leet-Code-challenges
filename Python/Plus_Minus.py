"""
https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true
"""
def plusMinus(arr):
    positives = negatives = zeros = 0
    for i in arr:
        if i == 0:
            zeros += 1
        elif i > 0:
            positives += 1
        else:
            negatives += 1
    print("{:.6f}".format(positives/len(arr)))
    print("{:.6f}".format(negatives/len(arr)))
    print("{:.6f}".format(zeros/len(arr)))
