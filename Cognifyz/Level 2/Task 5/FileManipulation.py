import string

def count_word_occurrences(file_path):
    word_count = {}

    with open(file_path, 'r') as file:
        for line in file:
            # Remove punctuation and convert to lowercase
            line = line.translate(str.maketrans('', '', string.punctuation))
            words = line.lower().split()
            
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    
    return word_count

def main():
    file_path = input("Enter the path to the text file: ")

    try:
        word_count = count_word_occurrences(file_path)
        
        print("Word Occurrences:")
        for word, count in sorted(word_count.items()):
            print(f"{word}: {count}")
    
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
