def texto_para_morse(texto):
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.'
    }

    morse_texto = ''
    caracteres_invalidos = ''

    for char in texto:
        char_maiusculo = char.upper()
        
        if char_maiusculo == ' ':
            morse_texto += ' '
        elif char_maiusculo in morse_dict:
            morse_texto += morse_dict[char_maiusculo] + ' '
        else:
            caracteres_invalidos += char + ' '

    if caracteres_invalidos:
        raise ValueError(f"Caracteres inválidos encontrados: '{caracteres_invalidos}'")

    return morse_texto.strip()


def main():
    mensagem = input("Digite a mensagem para traduzir para código Morse: ")

    try:
        morse = texto_para_morse(mensagem)
        print("Código Morse:", morse)
    except ValueError as e:
        print("Erro:", e)


if __name__ == "__main__":
    main()
