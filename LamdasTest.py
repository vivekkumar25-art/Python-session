is_passing = lambda mark: mark > 40

print(is_passing(60))




## HOME WORK 

words = ["apple", "banana", "watermelon", "mango", "pineapple"]

longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word:", longest_word)
