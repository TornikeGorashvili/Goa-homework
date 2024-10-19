def is_palindrome(text):
    return text == text[::-1]

result1 = is_palindrome("wow")
result2 = is_palindrome("hello")

print(result1)  # დაბეჭდავს True
print(result2)  # დაბეჭდავს False
