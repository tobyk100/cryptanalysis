import operator
import collections

text = open('ciphertext.txt').read().strip().lower()

# Decipher
deciph = collections.OrderedDict([
    ('a', 'N'),
    ('b', 'H'),
    ('c', 'J'),
    ('d', 'S'),
    ('e', 'U'),
    ('f', 'G'),
    ('g', 'T'),
    ('i', 'D'),
    ('h', 'C'),
    ('j', 'R'),
    ('k', 'K'),
    ('l', 'I'),
    ('m', 'V'),
    ('n', 'E'),
    ('o', 'Y'),
    ('p', 'B'),
    ('q', 'L'),
    ('r', 'O'),
    ('s', 'A'),
    ('t', 'P'),
    ('u', 'M'),
    ('v', 'X'),
    ('w', 'Z'),
    ('x', 'F'),
    ('y', 'W'),
    ('z', 'Q')
])

final_text = ''.join([deciph.get(text_letter, text_letter)
                      for text_letter in text])
blocks = text.split(' ')
final_blocks = final_text.split(' ')

def ngram(count, text):
    ngram = [text[index:index + count] for index in range(len(text) - count)]
    ngram = filter(lambda gram: ' ' not in gram, ngram)
    return Counter(ngram)

def blocks_with(letter, blocks):
    return filter(lambda block: letter in block, blocks)

doubles = filter(lambda ((x, y), _): x == y, ngram(2, final_text).items())
doubles = sorted(doubles, key=operator.itemgetter(1), reverse=True)

deciphered = [final_blocks[i::20] for i in range(20)]
deciphered[19].append(deciphered[0].pop())  # Fixes edge case

for line in deciphered:
    print line
