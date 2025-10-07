# 🐱 Hang in there Part 2: The Meow Meow Thing

## 📁 Challenge Info
- **Challenge Name:** Hang in there Part 2, the Meow Meow thing
- **Category:** Forensics  
- **Points:** ???

---

## 🎯 Objective
Find the Hidden flag based on the image, same as the first one

---

## 🧠 Initial Thoughts

- A meow meow without the green color??? (because when I compared the 2 images, the 2nd one has no green, like it's background has like a reddish hue???)
- I thought this was the hard one due to this self doubt issue from the part one

---

## 🔍 Investigation / Analysis

### First Attempt
- It's a meow meow without the green channel (I actually didn't see the flag first because I was too stupid to just **LOOK DOWN!!!** like frfr, I've read this writeup: 
  - 📖 [Image Steganography - MicroCTF 2017](https://www.doyler.net/security-not-included/image-steganography-microctf-2017) from StegOnline
  - and I saw the guy using this tool **StegSolve by Caesum???**

### Using StegSolve
- so yea, I've used that tool to find the flag (I rlly didn't need it, the color plane was enough, again I **JUST DIDN'T LOOK DOWN!!!!**)
- so i scrolled through the color channels, tried extracting strings, nothing

### Second Attempt (Success!)
- and yea I left this and got back to it again and did the steps again, scrolled through the color channels, and this time, I looked down, and there it was... (but ngl I like StegSolve, it's a good tool!)

---

## 🧪 Tools & Techniques Used

- **`StegSolve by caesum`** - Main steganography analysis tool
- **`StegOnline`** - Online steganography tool for reference

---

## 🚩 Solution

**Step-by-step:**
1. Check the color planes or the color channels for each color 
2. **Don't forget to look everywhere and look down!!!**

---

## 📌 Flag

```
CITU{hidden_frame101}
```

---

## 📝 Notes / Lessons Learned
- Ayaw pag tanga tanga, kupal ka ba boss???