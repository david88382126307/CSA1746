def sort_sentence(sentence):
    # Split the sentence into words and convert to lowercase
    words = sentence.split()
    # Sort the words in alphabetical order
    sorted_words = sorted(words, key=str.lower)
    # Join the sorted words back into a sentence
    sorted_sentence = ' '.join(sorted_words)
    return sorted_sentence

# Test the function
sentence = "Hello world this is a test sentence"
print("Original Sentence:")
print(sentence)
print("\nSorted Sentence:")
print(sort_sentence(sentence))
