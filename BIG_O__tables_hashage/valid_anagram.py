from collections import defaultdict 

# Idée A : 
def anagram_A(mot_1:str, mot_2:str) -> bool: 
    return sorted(mot_1.lower()) == sorted(mot_2.lower())

# Idée B : 
def count_letters(word:str)->dict: 
    dicto = defaultdict(int)
    for letter in word:
        dicto[letter] = dicto.get(letter, 0) + 1
    return dicto

def anagram_B(mot_1:str, mot_2:str) -> bool:
    mot_1, mot_2 = mot_1.lower(), mot_2.lower()
    if len(mot_1) != len(mot_2):
        return False
    return count_letters(mot_1) == count_letters(mot_2)

if __name__ == '__main__':
    cases = [
        ("listen", "silent", True), 
        ("rat", "car", False),
        ("Listen", "Silent", True),   
        ("a", "ab", False),          
        ("", "", True),               
        ("aab", "abb", False),        
    ]

    for a, b, expected in cases: 
        assert anagram_A(a, b) == expected, ("sort", a, b)
        assert anagram_B(a, b) == expected, ("count", a, b)

    print("Tous les tests sont passés")
