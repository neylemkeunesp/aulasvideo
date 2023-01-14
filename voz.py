import argparse
from gtts import gTTS
import os
import nltk

def fixed_digits(number, num_digits):
    # convert the number to a string
    number_str = str(number)
    # get the number of digits in the number
    num_digits_in_number = len(number_str)
    
    # if the number of digits in the number is less than the desired number of digits,
    # add leading zeros
    if num_digits_in_number < num_digits:
        number_str = '0' * (num_digits - num_digits_in_number) + number_str
    
    # print the number with the fixed number of digits
    return(number_str)

def num_digits(number):
    if number == 0:
        return 1
    # convert the number to a string
    number_str = str(number)
    # return the length of the string
    return len(number_str)

def savevoice():
    # Cria um parser
    parser = argparse.ArgumentParser()

    # Adiciona um argumento opcional '--mensagem'
    parser.add_argument('--file', help='arquivo a ser transformado em voz')
    parser.add_argument('--say', help='reproduz o som')
    parser.add_argument('--language', help='define a linguagem')
    parser.add_argument('--tokenize', help='separa em frases')

    # Analisa os argumentos da linha de comando
    args = parser.parse_args()

    # Imprime a mensagem, se foi passada
    if args.file:
        filename=args.file
        with open(filename, 'r') as f: #open the file
            contents = f.read()
        if args.tokenize=='yes':
            tokens = nltk.sent_tokenize(contents)
            for token in zip(tokens,range(len(tokens))):
                print(fixed_digits(token[1],num_digits(len(tokens))))

                soundfilename=filename[:-4]+fixed_digits(token[1],num_digits(len(tokens)))+".mp3"
                tts = gTTS(text=token[0], lang=args.language)
                tts.save(soundfilename)
        else:
            tts = gTTS(text=contents, lang=args.language)
            soundfilename=filename[:-4]+".mp3"
            tts.save(soundfilename)

        if args.say=='yes':
            os.system("mpg123 "+soundfilename)
        else:
            print("Arquivo criado: "+soundfilename)
    else:
        print("Nenhum arquivo informado")
    
    #tokenize a string using nltk?
        
if __name__=="__main__":
    savevoice()


    