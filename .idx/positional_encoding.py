import numpy as np

def positional_encoding():
    empty_array = get_array()
    return create_encoding(empty_array)

def get_array():
    a_sentence = input("Sentence to encode:")
    sentence_size = len(a_sentence.split())
    encoding_size = int(input("Word encoding dimensionality:"))
    return np.zeros((sentence_size, encoding_size))

def create_encoding(empty_array):
    encoding_array = np.copy(empty_array)
    sentence_size = encoding_array.shape[0]
    encoding_size = encoding_array.shape[1]
    for word in range(sentence_size):
        for iterator in range(encoding_size // 2):
            encoding_array[word, 2*iterator] = np.sin(word / (10000 ** (2*iterator / encoding_size)))
            encoding_array[word, 2*iterator+1] = np.cos(word / (10000 ** (2*iterator / encoding_size)))
    return encoding_array


def main():
    encoding_matrix = positional_encoding()
    print("This is the matrix:\n", encoding_matrix)

if __name__ == "__main__":
    main()