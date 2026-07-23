from collections import Counter

def solution(nums):
    answer = 0
    
    pokemon = Counter(nums)
    len_nums = len(nums)/2
    len_pokemon = len(pokemon)
    
    
    if len_nums > len_pokemon:  
        return len_pokemon
    
    
    return len_nums