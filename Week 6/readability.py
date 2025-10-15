a = input("Enter a sentence: ")

sentences = sum(1 for c in a if c in ".!?")

b = a.split()

word_num = len(b)

letters = 0
for char in a:
    if char.isalpha(): 
        letters += 1

L = (letters / word_num) * 100
S = (sentences / word_num) * 100

grade = round(0.0588 * L - 0.296 * S - 15.8)
if grade < 0:
    print("Before Grade 1")
elif grade > 16:
    print("Grade 16+")
else:
    print("Grade " + str(grade))