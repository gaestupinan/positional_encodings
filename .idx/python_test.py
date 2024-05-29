import numpy as np

a_sentence = input("Sentence to encode:")
sentence_size = len(a_sentence.split())
encoding_size = int(input("Word encoding dimensionality:"))
an_empty_array = np.zeros((encoding_size, sentence_size))
print(an_empty_array)

an_empty_array[0, 0] = 1
print(an_empty_array.shape[-1])