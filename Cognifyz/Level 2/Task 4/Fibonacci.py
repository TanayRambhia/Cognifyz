def generate_fibonacci_sequence(terms):
    fibonacci_sequence = [0, 1]  # Initial terms of the sequence
    
    while len(fibonacci_sequence) < terms:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    
    return fibonacci_sequence

def main():
    try:
        num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
        
        if num_terms <= 0:
            print("Please enter a positive integer.")
            return
        
        fibonacci_sequence = generate_fibonacci_sequence(num_terms)
        
        print("Fibonacci Sequence:")
        for term in fibonacci_sequence:
            print(term, end=" ")
        
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
