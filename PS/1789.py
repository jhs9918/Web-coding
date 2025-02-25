# s = int(input())
# cnt = 1

# while(True) :
#     lst = [i for i in range(1,cnt+1)]
#     total = sum(lst)
#     if(total==s) : 
#         print(len(lst))
#         break
#     else :
#         if total-s>0 and total-s<lst[-1] :
#             print(len(lst)-1)
#             break
#     cnt+=1

def max_natural_sum_count(s):
    # 이진 탐색을 활용하여 최대 k 찾기
    low, high = 1, s
    best_k = 0
    
    while low <= high:
        mid = (low + high) // 2
        total_sum = mid * (mid + 1) // 2  # 1부터 mid까지의 합
        
        if total_sum <= s:
            best_k = mid  # 조건을 만족하는 k 업데이트
            low = mid + 1  # 더 큰 k를 찾아봄
        else:
            high = mid - 1  # 너무 크면 줄이기
    
    # 최종적으로 best_k를 사용한 합이 s보다 크다면 조정
    total_sum = best_k * (best_k + 1) // 2
    diff = total_sum - s  # 초과된 값
    
    if diff > 0:  # 초과한 경우, 해당 숫자 제거하여 보정
        return best_k - 1
    return best_k

# 실행 코드
s = int(input())
print(max_natural_sum_count(s))
