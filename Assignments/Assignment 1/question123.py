#question1
numbers = [15, 8, 22, 7, 31, 4, 17]


print("Even numbers:")
for num in numbers:
    if num % 2 == 0:
        print(num, end=" ")
        
squared_odds = [num**2 for num in numbers if num % 2 != 0]
print("\nSquared odd numbers:", squared_odds)

#question 2
sentence = "The book was interesting because the book covered many topics and the topics discussed in the book were engaging"

# Convert to lowercase and split
words = sentence.lower().split()

# Count word occurrences
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("Word counts:", word_counts)

#question 3
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

nums = [2, 4, 5, 10, 13, 17, 20, 23]
prime_numbers = [num for num in nums if is_prime(num)]
print("Prime numbers:", prime_numbers)