mot = input("Entrez le premier mot: ")
mot_2 = input("Entrez le second mot: ")

# Idée A : 
def anagram_A(mot_1:str, mot_2:str) -> bool: 
    if sorted(mot_1.lower()) == sorted(mot_2.lower()):
        return True 
    else: 
        return False 

if anagram_A(mot, mot_2):
    print(f"{mot} et {mot_2} sont des Anagrammes.")
else: 
    print(f"{mot} et {mot_2} ne sont pas des anagrammes.")

# Idée B : 
dicto_1 = {}
dicto_2 = {}

def anagram_B(mot:str, dicto:dict) -> dict:
    for letter in mot:
        dicto[letter] = dicto.get(letter, 0) + 1
    return dicto

dicto_1 = anagram_B(mot, dicto_1)
dicto_2 = anagram_B(mot_2, dicto_2)

if dicto_1 == dicto_2:
    print(f"{mot} et {mot_2} sont des anagrammes.")
else:
    print(f"{mot} et {mot_2} ne sont pas des anagrammes.")
