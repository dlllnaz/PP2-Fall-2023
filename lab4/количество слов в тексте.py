def count_uni_w(text):
    words = text.split()
    uni_w = set(words)
    return len(uni_w) 
num_l = int(input())

text = ""
for i in range(num_l):
    line = input()
    text += line + " "

unique_word_count = count_uni_w(text)

print(unique_word_count)