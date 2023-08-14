from functools import reduce
def solution(clothes):
    answer = 0
    cloth_dict = {}
    for [cloth_item, cloth_type] in clothes:
        if cloth_type not in cloth_dict:
            cloth_dict[cloth_type] = []
        cloth_dict[cloth_type].append(cloth_item)
    item_nums = [len(f)+1 for f in cloth_dict.values()]
    answer = reduce(lambda x, y: x * y, item_nums) - 1
    return answer

# def solution(clothes):
#     from collections import Counter
#     from functools import reduce
#     cnt = Counter([kind for name, kind in clothes])
#     answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
#     return answer
