import operator
from collections import Counter
english_freq = [
    ('E', 12.02),
    ('T', 9.10),
    ('A', 8.12),
    ('O', 7.68),
    ('I', 7.31),
    ('N', 6.95),
    ('S', 6.28),
    ('R', 6.02),
    ('H', 5.92),
    ('D', 4.32),
    ('L', 3.98),
    ('U', 2.88),
    ('C', 2.71),
    ('M', 2.61),
    ('F', 2.30),
    ('Y', 2.11),
    ('W', 2.09),
    ('G', 2.03),
    ('P', 1.82),
    ('B', 1.49),
    ('V', 1.11),
    ('K', 0.69),
    ('X', 0.17),
    ('Q', 0.11),
    ('J', 0.10),
    ('Z', 0.07)
]

text = open('ciphertext.txt').read().strip().lower()
letters = text.replace(' ', '')

text_count = {}
for letter in letters:
    text_count[letter] = 1 + text_count.get(letter, 0)
length = len(letters)
text_freq = {k: ((10000 * v) / length) / 100.0 for k, v in text_count.items()}
sorted_text_freq = sorted(text_freq.items(), key=operator.itemgetter(1))
sorted_text_freq.reverse()

deciph = {}
"""
for idx, pair in enumerate(english_freq):
   deciph[sorted_text_freq[idx][0]] = pair[0]
"""

original = deciph.copy()
deciph['g'] = 'T'
deciph['b'] = 'H'
deciph['n'] = 'E'
deciph['j'] = 'N'
deciph['x'] = 'F'
deciph['s'] = 'A'
deciph['d'] = 'S'
deciph['q'] = 'L'
deciph['e'] = 'U'
deciph['r'] = 'O'
deciph['f'] = 'C'

final_text = ''.join([deciph.get(text_letter, text_letter)
                      for text_letter in text])
blocks = final_text.split(' ')

doubles_filtered = filter(lambda (idx, letter): letter == text[idx - 1], 
                          enumerate(text))
doubles_mapped = map(lambda (idx, letter): letter + letter, doubles_filtered)
double_counts = Counter(doubles_mapped)

trigrams = {}
for block in blocks:
    for idx in range(3):
        trigram = block[idx: idx + 3]
        trigrams[trigram] = 1 + trigrams.get(trigram, 0)

common_trigrams = filter(lambda (k, v): v > 3, trigrams.items())
