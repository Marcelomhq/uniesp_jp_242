# Contador de Vogais e Consoantes:
# Contexto: Crie um programa que peça ao usuário uma frase e conte o número de 
# vogais e consoantes presentes nela. Utilize um loop para percorrer cada caractere 
# da frase e realizar a contagem.
def count(phrase):
    vowel_count = 0
    consonant_count = 0
    for i in phrase:
        if i.lower() in vowels:
            vowel_count += 1
        if i.lower() in consonants:
            consonant_count += 1
    return vowel_count, consonant_count

if __name__ == "__main__":
    vowels = 'aeiou'
    consonants = 'qwrtypsdfghjklzxcvbnm'
    phrase = input('Digite a fras meu consagrated: ')
    vowel,consonant = count(phrase)
    print(f"vogais {vowel} consoantes {consonant}")

