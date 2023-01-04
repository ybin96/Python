f = open('./Data/kma.txt', 'r', encoding='utf-8')
lines = f.readlines()
for line in lines:
    print(line.strip())

