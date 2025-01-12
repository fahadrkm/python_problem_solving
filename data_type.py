# s ='dsA17'
# for i in s:
#         if i .isalnum():
#              print(True)
#              break
#         else:
#               print(False)
#               break
# for i in s:
#         if i .isalpha():
#             print(True)
#             break
#         else:
#             print(False)
#             break
# for i in s:
#         if i .isdigit():
#             print(True)
#             break
#         else:
#             print(False)
#             break
# for i in s:
#         if i .islower():
#             print(True)
#             break
#         else:
#             print(False) 
# for i in s:
#         if i .isaupper():
#             print(True)
#             break
#         else:
#             print(False) 
#             break
s = input()

# Check for alphanumeric characters
print(any(c.isalnum() for c in s))

# Check for alphabetical characters
print(any(c.isalpha() for c in s))

# Check for digits
print(any(c.isdigit() for c in s))

# Check for lowercase characters
print(any(c.islower() for c in s))

# Check for uppercase characters
print(any(c.isupper() for c in s))
