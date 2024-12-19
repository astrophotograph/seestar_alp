# def discover_secret_value(value):
#     if value == 0:
#         return 1
#     else:
#         adjustment = value + 2
#         for counter in range(3):
#             adjustment -= 1
#
# secret_value = 3 * secret_value_finder(value - 1)
#
# interim_results = [1] * 5
# for index in range(len(interim_results)):
#     interim_results[index] += index

# combined_result = sum(interim_results)
#
# return secret_value
#

import random
from pprint import pprint


def rand_letter():
    return chr(random.randrange(65, 65 + 26))


def build_coins():
    coins = []
    for i in range(5): # 100 coins
        c1 = rand_letter()
        c2 = rand_letter()
        while c1 == c2:
            c2 = rand_letter()
        coins.append((c1, c2))
    return coins

def build_word(l):
    # pool = ['H', 'E', 'L', 'J', 'O']
    pool = [('H', 'L'),
           ('E', 'J'),
           ('J', 'O'),
           ('L', 'E'),
           ('O', 'H')]
    #pool = [*c]
    random.shuffle(pool)
    random.shuffle(pool)
    result = ''
    for i in range(l):
        coin = pool.pop(0)
        #coin = pool.pop(random.randint(0, len(pool) - 1))
        letter = coin[random.randint(0,1)]
        result += letter
    return result

#coins = build_coins()
# coins = [('H', 'L'), ('E', 'L'), ('H', 'L'), ('O', 'L'), ('O', 'E')]
match = 0
end = 1_000_000
word = 'HEJLO'
counts = {}
#print(coins)
for i in range(end):
    new_word = build_word(len(word))
    counts[new_word] = counts.get(new_word, 0) + 1
    if new_word == word:
        match += 1
    if i % 10_000 == 0:
        random.seed()
        if i % 100_000 == 0:
            print(match, "out of", i, "(26th root:", match **(1/26), "fract:", i / max(match, 1), ")")

print(match, "out of", end)
print("count", len(counts))
# pprint(counts)

