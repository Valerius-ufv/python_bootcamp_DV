# Check the type of a string
default_string = b"default string"
<<<<<<< HEAD
default_string = 5
print(str(default_string))
numero= "55"
print(int(numero)+default_string)
=======
print(str(default_string))

>>>>>>> 5705a7dc37d499f79f44907cb6d86ca6471e90a7

print(type(default_string))  # Output: <class 'str'>

# Check the type of a string
clearly_unicode = "你好 chinese string"
print(type(clearly_unicode))  # Output: <class 'str'>!!!

# Show that a string in Python 3 supports Unicode
unicode_string = "你好, мир, hello"
print(unicode_string)  # Output: 你好, мир, hello

# Confirm that str is Unicode by default
is_unicode = isinstance(unicode_string, str)
print("Is unicode_string of type str (Unicode)?:", is_unicode)  # Output: True

# Compare with bytes
<<<<<<< HEAD
byte_string = b"default string"
=======
byte_string = b" default string 2 "
>>>>>>> 5705a7dc37d499f79f44907cb6d86ca6471e90a7
print(byte_string)  # Output: <class 'bytes'>

# Show the difference between str and bytes
try:
    combined_string = default_string + byte_string  # This should raise a TypeError
except TypeError as e:
    print("TypeError when trying to combine str and bytes:", e)

<<<<<<< HEAD
print(combined_string)
=======
print(combined_string)
>>>>>>> 5705a7dc37d499f79f44907cb6d86ca6471e90a7
