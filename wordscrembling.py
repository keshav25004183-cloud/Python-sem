import random

words = ["apple","banana","computer","python","school","keyboard","internet","program","science","library"]
word = random.choice(words)
scrambled = ''.join(random.sample(word, len(word)))
print("Unscramble the word:", scrambled)
guess = input("Your guess: ")
if guess.lower() == word:
    print("Correct! ✌️")
else:

    print("Wrong! The word was:", word)

