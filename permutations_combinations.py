# # 순열
# def gen_permutations(arr, n): 
#     result = [] 
#     if n == 0: 
#         return [[]] 
    
#     for i, elem in enumerate(arr): 
#         for P in gen_permutations(arr[:i] + arr[i+1:], n-1): 
#             result += [[elem]+P] 
    
#     return result 
# arr = [0, 1, 2, 3, 4, 5] 


# 조합
def gen_combinations(arr, n): 
    result =[] 
    if n == 0: 
        return [[]] 
    for i in range(0, len(arr)):
        elem = arr[i] 
        rest_arr = arr[i + 1:] 
        for C in gen_combinations(rest_arr, n-1): 
            result.append([elem]+C) 
    return result
print(gen_combinations([1,2,3], 2))

