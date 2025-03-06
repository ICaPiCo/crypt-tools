from collections import Counter

def extract_bigrams(input_string):
    # Generate bigrams from the input string
    bigrams = [input_string[i:i+2] for i in range(len(input_string) - 1)]
    return bigrams

def extract_trigrams(input_string):
    # Generate trigrams from the input string
    trigrams = [input_string[i:i+3] for i in range(len(input_string) - 1)]
    return trigrams

def frequency_analysis(input_string):
    # Count the frequency of each character
    char_frequency = Counter(input_string)
    
    # Sort characters by frequency in descending order
    sorted_chars = sorted(char_frequency, key=char_frequency.get, reverse=True)
    
    # Join characters into a single string
    char_result = "".join(sorted_chars)
    
    # Extract bigrams and count their frequency
    bigrams = extract_bigrams(input_string)
    bigram_frequency = Counter(bigrams)
    
    # Extract bigrams and count their frequency
    trigrams = extract_trigrams(input_string)
    trigram_frequency = Counter(trigrams)

    # Sort bigrams by frequency in descending order, then by their appearance in the text
    sorted_bigrams = sorted(bigram_frequency, key=lambda x: (-bigram_frequency[x], input_string.find(x)))

    # Sort trigrams by frequency in descending order, then by their appearance in the text
    sorted_trigrams = sorted(trigram_frequency, key=lambda x: (-trigram_frequency[x], input_string.find(x)))
    
    # Return both character and bigram results
    return char_result, sorted_bigrams

def main():
    # Get input from the user
    input_string = input("Enter a string: ")
    
    # Perform frequency analysis and print the results
    char_result, common_bigrams = frequency_analysis(input_string)
    
    print("Characters sorted by frequency:", char_result)
    print("Most common bigrams (left to right):", common_bigrams)

if __name__ == "__main__":
    main()