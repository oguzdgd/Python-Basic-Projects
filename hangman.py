import random

# kelime listesini ve gerekli liste ve değişkenleri oluştur.
words_of_lists = ['kelebek','aslan','kaplumbağa','kedi','kirpi','zebra']
guessed_letters = []
lines=[]



# kelimeyi listeden seç ve uzunluğu kadar çizgi oluştur.
selected= random.choice(words_of_lists)
for _ in range(len(selected)):
    lines.append('_')

# print içinde kelimenin kaç harflı olduğunu bulmak için 
lengthOfSelected= len(selected)


while True:
    print('Choose one\nNew game: n\nQuit : q\nPress: ')
    choose=input()
    if(choose=='q'):
        break
    elif(choose=='n'):
        print('New game loading...\n')
        print(f"Lets guess this word: This word is an animal and consists of {lengthOfSelected} letters. You have 3 rights\n")
        numberOfGuessRight=3
    else:
        continue
    while True:
        guess=input('Guess a letter! : ')  
        if guess in selected:
            
            # bu kısım enumurate fonksiyonu sayesinde seçilen kelimeyi tek tek liste haline getiriyor ve onları indexliyor.Daha sonra letter tahmin edilen harfin içinde ise Tuple(liste çeşidi) dönüyor. Yani harflerin indexleri belirlenmiş oluyor.
            indices = [index for index, letter in enumerate(selected) if letter == guess]
            # bu kısım yukarıda liste içinde dönen kelimelerin  içine tahmin edilen kelimeye atıyor. Mesela kelime araba ise ve tahmin edilen kelime a ise tüm a lar yazılıyor.            
            for index in indices:
                lines[index] = guess
            print(f"Right! : {('').join(lines)}")
            if ('').join(lines)==selected:
                print(f'Congratulations. You won!')
                break

        else:
            numberOfGuessRight-=1
            if numberOfGuessRight!=0:
                print(f'Wrong! You left {numberOfGuessRight} guesses')
            else:
                print('Hangman!')
                print(f'The word was: "{selected}"')
                break


   