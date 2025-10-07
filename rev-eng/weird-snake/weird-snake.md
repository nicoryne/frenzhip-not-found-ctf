# Weird Snake – Reverse Engineering

**Author:** Nicolo

**Challenge Link:** https://play.picoctf.org/practice/challenge/428 

**Date:** 2025-10-05  

**Category:** Reverse Engineering

## 🧠 Challenge Description

I have a friend that enjoys coding and he hasn't stopped talking about a snake recently
He left this [file](./snake) on my computer and dares me to uncover a secret phrase from it. Can you assist?


## 📁 Provided Files / Access

- Disassembled python bytecode: [snake](./snake)


## 🧪 Approach & Strategy

### Goal

Reconstruct the actual snake.py file and run it to get the flag

### Tools / Techniques

List tools or concepts used. For example:

- https://www.geeksforgeeks.org/python/ (refresher on functions I can use and how they)


## 🛠️ Step-by-step Solution

```bash
# Step 1: Download the file
curl -O https://artifacts.picoctf.net/c_titan/124/snake

# Step 2: Inspect file (I opened with vim)
nvim snake

# Step 3: Analyze the Python bytecode
# The file contains disassembled Python bytecode.

# - Lines 1-82: Creates a list of 40 integers (input_list)
# - Lines 84-118: Builds a key string step by step:
#   * Line 2: key_str = 'J'
#   * Line 3: key_str = '_' + key_str = '_' + 'J' = '_J'
#   * Line 4: key_str = key_str + 'o' = '_J' + 'o' = '_Jo'
#   * Line 5: key_str = key_str + '3' = '_Jo' + '3' = '_Jo3'
#   * Line 6: key_str = 't' + key_str = 't' + '_Jo3' = 't_Jo3'
# - Lines 120-132: Defines a list comprehension function that converts string to ASCII values
# - Lines 134-160: Extends the key list to match the length of input_list
# - Lines 162-180: XORs input_list with key_list
# - Lines 182-200: Converts the result to characters and prints

# Step 4: Reconstruct the Python code
# Based on the bytecode analysis, reconstructed the original snake.py:


input_list = [4, 54, 41, 0, 112, 32, 25, 49, 33, 3, 0, 0, 57, 32, 108, 23, 48, 4, 9, 70, 7, 110, 36, 8, 108, 7, 49, 10, 4, 86, 43, 106, 123, 89, 87, 18, 62, 47, 10, 78]

key_str = "t_Jo3"

def listcomp(s):
    key_list = [ord(c) for c in s]
    
    while len(key_list) < len(input_list):
        key_list.extend(key_list)
    
    return key_list

key_list = listcomp(key_str)

result = [a ^ b for a, b in zip(input_list, key_list)]
# This line performs XOR decryption:
# - zip(input_list, key_list) pairs each encrypted byte with its corresponding key byte
# - a ^ b performs XOR operation between each pair
# - XOR is reversible: if encrypted = plaintext ^ key, then plaintext = encrypted ^ key
# - Example: if input_list[0] = 4 and key_list[0] = 116 (ASCII for 't'), then 4 ^ 116 = 112
# - The result is a list of ASCII values that represent the decrypted characters

result_text = ''.join(map(chr, result))

print(result_text)


# Step 5: Run the reconstructed code
python3 snake.py
```

## 🏴 Flag

```
picoCTF{weird_snake_1mb_187c5dbf}
```

## 💡 Key Takeaways

- **Python bytecode analysis**: Understanding how Python bytecode works helps in reverse engineering
- **XOR encryption**: The challenge used simple XOR encryption with a repeating key
- **List comprehensions**: The code used list comprehensions for efficient data processing
- **String manipulation**: Converting between strings and ASCII values using `ord()` and `chr()`
