# Quantum Scrambler – Reverse Engineering

**Author:**  Nicolo  
**Challenge Link:** https://play.picoctf.org/practice/challenge/479  
**Date:** 2025-10-08  
**Category:** Reverse Engineering  

## 🧠 Challenge Description

We invented a new cipher that uses "quantum entanglement" to encode the flag. Do you have what it takes to decode it?

## 📁 Provided Files / Access

- `ciphered_flag.txt` from the challenge instance
- `quantum_scrambler.py` (challenge source)
- `quantum_descrambler.py` (our solution)

## 🧪 Approach & Strategy

### Goal

Retrieve the ciphered flag from the challenge instance, analyze the scrambling logic, and recover the ASCII flag.

### Key Insight

The scrambler repeatedly:
- Concatenates adjacent sublists: `A[i-2] += A.pop(i-1)`
- Appends a slice of the earlier portion: `A[i-1].append(A[:i-2])`

This builds a deeply nested list-of-lists that still preserves the original data order at the outer-most level. Therefore, instead of fully reversing every mutation, we can:
1) Remove any nested list elements from each sublist, then
2) Flatten one level to recover a clean list of hex strings, and
3) Convert hex → ASCII.

### Tools / Techniques

- Python: `ast.literal_eval` for safe parsing of the cipher text
- List processing: nested list checks, single-level flattening


## 🛠️ Step-by-step Solution

```bash
# Step 1: Retrieve the cipher from the instance
nc verbal-sleep.picoctf.net 61220 | tee ciphered_flag.txt

# Step 2: Inspect the scrambler
# See `quantum_scrambler.py` – it starts from [['0x..'], ['0x..'], ...]
# and progressively merges/embeds earlier pieces into later ones.

# Step 3: Descramble strategy (implemented in `quantum_descrambler.py`)
# - Parse the text into a Python list with ast.literal_eval
# - For every sublist, drop any elements that are lists (keep only '0x..' strings)
# - Flatten one level across the outer list
# - Convert each hex string to a character and join

# Step 4: Run the descrambler
auth python3 quantum_descrambler.py
```

If everything is wired correctly, it will print the flag.

## 🏴 Flag

```
picoCTF{............}
```

## 💡 Key Takeaways

- **Understand structure before coding**: Mapping the data shape (and how it evolves) often reveals simpler recovery paths than naively reversing every operation.
- **Flatten strategically**: When transformations preserve order but add nesting, selective pruning + one-level flattening can be enough.
- **Parse safely**: Use `ast.literal_eval` to safely turn text representations into Python objects. 
