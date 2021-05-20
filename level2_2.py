"""
프로그래머스 레벨 2 2번째 문제
quadtree 모방하여 압축하기
"""

# def solution(arr):
#     answer = []
#     quadSize = len(arr[0]) // 2
#     quadNum = 2
#     tempSum = 0
#     arr[:quadSize][:]
#
#     first = arr[:quadSize][:quadSize]
#     second = arr[:quadSize][quadSize:]
#     third = arr[quadSize:][:quadSize]
#     fourth = arr[quadSize:][quadSize:]
#     while quadSize >= 2:
#         if sum(first) == 0:
#
#         quadSize /= 2
#     return answer


# def findnum(arr):
#     if len(arr) == 4 and sum(arr) == 0:
#
#     elif sum(arr) == 1:

arr = [[a for a in range(8)] for y in range(8)]
quadSize = len(arr[0])//2
first  = arr[:quadSize][:quadSize]
second = arr[:quadSize][quadSize:]
third  = arr[quadSize:][:quadSize]
fourth = arr[quadSize:][quadSize:]
print(arr)
print(first)
