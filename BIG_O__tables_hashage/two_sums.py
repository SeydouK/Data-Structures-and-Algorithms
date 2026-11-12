def two_sum_naive(liste:list[int], target:int)->tuple[int, int]:
    for i in range(len(liste)):
        start = i 
        for j in range(start+1, len(liste)): 
            if liste[i] + liste[j] == target: 
                return (i, j)
    return (0, 0)

def two_sum_opt(liste:list[int], target:int) -> tuple[int, int]:
    seen = {} # memoire : O(1)

    for i, n in enumerate(liste): # temps: O(n)
        complement = target - n  # memoire O (n)
        if complement in seen:  # Memoire O (1)
            return (seen[complement], i)
        seen[n] = i 
    return (0, 0)


# Complexite finale 
# temps : O(1)
# memoire O(n)
    
if __name__ == '__main__':
    cases = [
        ([12,3,51,2], 14, (0, 3)),
        ([1,34,5,12], 16, (0, 0)),
        ([], 12, (0, 0)),
        ([5,-1,2], 4, (0, 1))
    ]

    for a, b, expected in cases:
        assert two_sum_naive(a, b) == expected, ("naive", a, b)
        assert two_sum_opt(a, b) == expected , ("opt", a, b)

    print("Tous les test sont passés")