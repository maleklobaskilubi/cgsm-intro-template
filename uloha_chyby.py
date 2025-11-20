# ============================================
# Súbor: uloha_chyby.py
# Úloha: Každá funkcia obsahuje jednoduchú chybu,
#        ktorú musíš opraviť a commitnúť.
# ============================================


# 1. Funkcia: súčet dvoch čísel
# Chyba: vracia nesprávnu operáciu
def sucet(a, b):
    return a - b   


# 2. Funkcia: skontroluje, či je číslo párne
# Chyba: podmienka je opačne
def je_parne(n):
    if n % 2 == 1:   
        return True
    return False


# 3. Funkcia: obvod štvorca
# Chyba: zlý vzorec
def obvod_stvorca(s):
    return s * 2   


# 4. Funkcia: priemer zo zoznamu
# Chyba: chýba delenie počtom prvkov
def priemer(zoznam):
    suma = sum(zoznam)
    return suma   


# 5. Funkcia: zistí, či text obsahuje písmeno 'a'
# Chyba: kontroluje nesprávne písmeno
def obsahuje_a(text):
    return 'b' in text   
