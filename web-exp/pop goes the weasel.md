# 🎵 Pop Goes the Weasel

## 📁 Challenge Info
- **Challenge Name:** Pop Goes the Weasel
- **Category:** Web
- **Points:** ???

---

## 🎯 Objective
Just to take a look at the website and find the flag

---

## 🧠 Initial Thoughts

I got into a bit of trauma about that **"Please Don't Break Me"** Message on the site because I still haven't solved **SSTI2** in picoCTF and I thought that was it *yikes*

---

## 🔍 Investigation / Analysis

### Initial Discovery
- **NGL** I just inspected the element and there, it was encoded though in **hex**, and tbh my first thought was it was jumbled or something, so I did the "right" way by just tripping that flag

### URL Parameter Attempts
- I forgot how I did it, I think I messed with the **URL parameter**, adding **CITU** or something but the alert message lead me to jibberish

### The Solution
- Then **frenz** told me just to grab that **hex encoded thing** in **flagArray**
- Pasted it in a **Hex to ASCII converter** (I am not good with cyberchef, I ahve a vendetta to it for some odd reason due to that **vault-doors** problem in picoCTF, I got mad by it because I somehow can't make it work properly, but overall, it's a good tool, twas a human error, not cyberchef's problem so I just dodged it to not use up too much time figuring out)
- **boom** the flag is there

---

## 🧪 Tools & Techniques Used

- **Generic hex to ASCII converter online** - For decoding the hex-encoded flag
- **Browser Developer Tools** - For inspecting elements

---

## 🚩 Solution

**Step-by-step:**
1. **Inspect the Element** using browser dev tools
2. **Grab that Hex encoded Array** from the flagArray variable
3. **Convert it to ASCII** using any hex-to-ASCII converter

---

## 📌 Flag

```
CITU{easy_lamang_viewsource}
```

---

## 📝 Notes / Lessons Learned
- Sometimes the simplest approach (inspect element) is all you need
- Don't overthink web challenges - check the source first!
