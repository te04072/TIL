# def merge_sort(ls):
#     length = len(ls)
#     global cnt
#     if length == 1:
#         return ls
#     else:
#         mid = length // 2
#         left = merge_sort(ls[:mid])
#         right = merge_sort(ls[mid:])
#         if left[-1] > right[-1]:
#             cnt += 1
#         merged = []
#         i = 0
#         j = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 merged.append(left[i])
#                 i += 1
#             else:
#                 merged.append(right[j])
#                 j += 1
#         merged += left[i:]
#         merged += right[j:]
#         return merged
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     target = list(map(int, input().split()))
#     cnt = 0
#     target = merge_sort(target)
#     print(f"#{tc} {target[N//2]} {cnt}")


# def quicksort(ls, l, r):
#     if l < r:
#         s = partition(ls, l, r)
#         quicksort(ls, l, s-1)
#         quicksort(ls, s+1, r)
#
#
# def partition(ls, left, right):
#     mid = (left+right)//2
#     pivot = ls[mid]
#     ls[left], ls[mid] = ls[mid], ls[left]
#     i = left + 1
#     j = right
#     while i <= j:
#         while i <= j and ls[i] <= pivot:
#             i += 1
#         while i <= j and ls[j] >= pivot:
#             j -= 1
#         if i < j:
#             ls[i], ls[j] = ls[j], ls[i]
#     ls[left], ls[j] = ls[j], ls[left]
#     return j
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     target = list(map(int, input().split()))
#     quicksort(target, 0, N-1)
#     print(target)
#     print(f"#{tc} {target[N//2]}")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    list_A = list(map(int, input().split()))
    list_B = list(map(int, input().split()))
    output = 0
    for i in range(M):
        target = list_B[i]
        l = 0
        r = N-1
        m = (l+r)//2
        status_L = False
        status_R = False
        while l <= r:
            if target == list_A[m]:
                break
            elif target > list_A[m]:
                l = m + 1
                status_R = True
            else:
                r = m - 1
                status_L = True
            m = (l+r) // 2
        if target == list_A[m]:
            output += 1
        elif target == list_A[r] and status_R and status_L:
            output += 1
    print(f"#{tc} {output}")
