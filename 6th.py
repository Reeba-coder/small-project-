
word1="abcd"
word2="pqr"
merged=""
i ,j=0,0
# Merge characters one by one
while i < len(word1) and j < len(word2):
    merged += word1[i] + word2[j]
    i += 1
    j += 1
    # Append remaining characters from the longer string
while i < len(word1):
    merged += word1[i]
    i += 1

while j < len(word2):
    merged += word2[j]
    j += 1
print(merged)