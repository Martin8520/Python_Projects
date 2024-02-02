num_target = int(input())

n = int(input())

word_dist = []

for i in range(n):
    word = input().strip()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    word_value = sum(alphabet.index(letter) + 1 for letter in word)
    distance = abs(num_target - word_value)
    word_dist.append((word, distance))

for word, distance in word_dist:
    print(f"{word} {distance}")

avg_dist = sum(distance for i, distance in word_dist) / n
print(f"{avg_dist:.2f}")
