import random

frags = ["A", "C", "T", "G"]


def generate(num):
    dna_seq = []
    for i in range(num):
        dna_seq.append(random.choice(frags))
    return dna_seq


def splitter(dna_list, num):
    frags = []
    left = list(dna_list)
    right = list(dna_list)
    left_rand = 1
    right_rand = 1
    while left != [] or right != []:
        while left_rand == right_rand:
            left_rand = random.randint(num, num * 2)
            right_rand = random.randint(num, num * 2)
        frags = list_rand_element(left_rand, left, frags)
        frags = list_rand_element(right_rand, right, frags)
    return [x for x in frags if x]


def list_rand_element(rand, list_to_split, frags):
    temp = []
    for i in range(rand):
        try:
            temp.append(list_to_split.pop())
        except:
            pass
    frags.append(temp[::-1])
    return frags
