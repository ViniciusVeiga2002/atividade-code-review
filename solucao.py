def sao_anagramas(string1, string2):
    s1 = ''.join(sorted(string1.replace(" ", "").lower()))
    s2 = ''.join(sorted(string2.replace(" ", "").lower()))
    return s1 == s2

def cifra_de_cesar(texto, deslocamento):
    resultado = []
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            novo_char = chr((ord(char) - base + deslocamento) % 26 + base)
            resultado.append(novo_char)
        else:
            resultado.append(char)
    return ''.join(resultado)