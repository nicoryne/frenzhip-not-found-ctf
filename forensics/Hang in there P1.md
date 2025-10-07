# 🐱 Meow Meow 1: Hang in there

## 📁 Challenge Info
- **Challenge Name:** Meow Meow 1 (Hang in there)
- **Category:** Forensics
- **Points:** ???

---

## 🎯 Objective
Find out the Flag by taking a look of the picture

---

## 🧠 Initial Thoughts

shii this was easy, because I love that picoCTF problem "red" that was unexpectedly hiding data using the colors and stuff

---

## 🔍 Investigation / Analysis / Solution

### Initial Discovery
- I used this tool: **[StegOnline](https://www.georgeom.net/StegOnline/)** to find the flag
- the data exists on the **RGB 0** (which are the first channels) but in **LSB**
- boom I found it (but it failed obviously because for some reason the CTF thingy has an issue, adrian got stuck to it lol).

### Red Herrings & Confusion
- and yaur I got stuck on a red-herring because I thought the flag was just the clue
- I used **zsteg** to check, I got **NOTHING**, I was stuck with another red-herring because when using zsteg to the file it found a file (**OpenPGP format**) so I was like **HUH???**
- but nonetheless I stopped, until my groupmate "found" the solution, inputted it, and boom, the flag works...
- I actually also thought that in order to solve the 2nd problem, I have to extract the OpenPGP key here because when using zsteg on that other file, it said like something encrypted (I know it's stupid, but trust me, leads are leads when you doubt yourself...)

---

## 🧪 Tools & Techniques Used
- **`StegOnline`** - Web-based steganography analysis tool
- **`zsteg`** - Command-line steganography detection tool

---

## 🚩 Solution

**Method 1: Using StegOnline**
1. Tweak Steg to only choose the colors that have data on it (it looks static) which is **R, G and B 0**
2. Change from **MSB** to **LSB**

**Method 2: Using zsteg**
- You can also use zsteg and pipe it with GREP to reveal the flag, use `-a` to reveal everything to it

---

## 📌 Flag

```
CITU{LSBEmbedOnBlue_Channel}
```

---

## 📝 Notes / Lessons Learned
- the shit was not my fault, fuck I rlly did doubt myself because entering the flag didn't work
- **if it doesn't work??? Try again in a few minutes** (this tip is mostly overlooked, but shii it actually works)