def two_sum_naive(liste:list[int], target:int)->tuple[int, int]:
    for i in range(len(liste)):
        start = i 
        for j in range(start+1, len(liste)): 
            if liste[i] + liste[j] == target: 
                return (i, j)
    return (0, 0)

def two_sum_opt(liste:list[int], target:int) -> tuple[int, int]:
    seen = {} # Espace : O(1) / Temps : O(1)

    for i, n in enumerate(liste): # Temps : O(n) / Espace : O (n)
        complement = target - n  # Temps : O(1) / Espace : O(1)
        if complement in seen:  # Temps O (1) / Espace : O(1)
            return (seen[complement], i) 
        seen[n] = i # Temps : O(1) / Espace : O(n)
    return (0, 0)


# Complexité finale
# Temps : O(n) en moyenne
# Espace : O(n)
    
if __name__ == '__main__':
    cases = [
        ([2, 7, 11, 15], 9, (0, 1)),
        ([3, 2, 4], 6, (1, 2)),
        ([3, 3], 6, (0, 1)),
        ([-1, -2, -3, -4], -6, (1, 3)),
        ([0, 4, 3, 0], 0, (0, 3))
    ]

    for a, b, expected in cases:
        assert two_sum_naive(a, b) == expected, ("naive", a, b)
        assert two_sum_opt(a, b) == expected , ("opt", a, b)

    print("Tous les test sont passés")