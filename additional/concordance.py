from collections import Counter, defaultdict
import re


# TASK: compute the word frequencies in the below text
#       list the top-3 words in the below text
text = '''
Searching and waiting, not wanting anything,
Loving and yearning, but losing everything.
Admiring the beauty, with my eyes being shot,
Perceive what no one saw, nobody knows it’s what,
Awed by the harmony, amazed by the secret,
Picturing in my mind, though have not seen it.
Adoring and loving everything that is clean,
The wind, white clouds, the snow and my dream;
To do what’s proper surely not for heaven,
Not for another world, but getting paid for them.
Knowing there is no goal, knowing there is no God,
I am scared that perhaps there’s no One who will be just.
Knowing the mind is poor, the willpower frail,
I am controlled by chance; life will do what it may.
But hoping stubbornly, I am still, still believing,
The work of my lifetime amounts to something.
I can welcome now the final peacefulness,
That cures all worldly pain, and our last due: death.
'''

# Without removal of stop words:
words = text.lower().split()
word_count = Counter(words)
print(f"3 Most frequent, regardless of nature: {word_count.most_common()[:3]}")

# including some data-cleaning

regex = re.compile('[^a-z]')
words_alphab = regex.sub('', text.lower()).split()
print(f"{words_alphab=}")
STOP_WORDS = set('''
    the and not my no what is i
    but by that for am it 
'''.strip().split())

words_clean = [w for w in words_alphab if w not in STOP_WORDS]
word_count_clean = Counter(words_clean)
print(f"3 Most frequent, stripped: {word_count.most_common()[:3]}")

# TASK: use the below Scrabble-style scoring dictionary
#       and compute the top highest aggregate scores
#       (i.e., find the max by frequency × word-score)
tile_scores = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4,
               'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3,
               'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4}


# scores = dict.fromkeys(word_count, 0)
#
# for w in words:
#     for c in w:
#         scores[w] += tile_scores.get(c, 0)
#
# # print(f"{scores=}")
# sorted_by_score = sorted(scores)
# print(f"{sorted_by_score=}\n\n\n\n")
#
# [print(key, value) for (key, value) in sorted(scores.items(), key=lambda x: x[1], reverse=True)]


