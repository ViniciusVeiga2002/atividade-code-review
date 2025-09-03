def sao_anagramas(string1, string2):
    s1 = ''.join(sorted(string1.replace(" ", "").lower()))
    s2 = ''.join(sorted(string2.replace(" ", "").lower()))
    return s1 == s2
