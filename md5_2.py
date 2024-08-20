import hashlib

# MD5 hash to compare
target_hash = 'aaedfac4a732ad7608d720886b69f289'

# List of words to test
words = [
    "Rickrolling has taught us to be wary of random links more than any cyber security courses ever has.",
    "Meme",
    "jpeg",
    "InfoSec Image",
    "meme.jpg",
    "meme.jpeg",
    "aGlkZGVuX2luX3RoZV9kZXRhaWxz; ",
    "aGlkZGVuX2luX3RoZV9kZXRhaWxz",
    "aGlkZGVuX2luX3RoZV9kZXRhaWxz;"
]

# Function to calculate MD5 hash of a given string
def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

# Check each word
for word in words:
    if md5_hash(word) == target_hash:
        print(f"Match found: {word}")
        break
else:
    print("No match found.")
