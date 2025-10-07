# 🪆 Matryoshka

## 📁 Challenge Info
- **Challenge Name:** Matryoshka
- **Category:** Web
- **Points:** ???

---

## 🎯 Objective
Find the flag by looking at the website

---

## 🧠 Initial Thoughts
well, the website was basic, I rlly thought the website is bulletproof and has nothing

---

## 🔍 Investigation / Analysis

### Initial Reconnaissance
- I tried looking where typical flags hide: **inspect element**, **cookies**, **local storage**, **CSS**, **sources** (we'll talk about this later), the **robots.txt** and checked every files, **NADA** no comments, nothing, it looks normal to me ???
- I even looked if maybe that youtube telemetry crap has anything, I was desperate to look for the flag...

### The Eureka Moment
- I rlly thought about it and searched online what a **Matryoshka** and when I saw it, **OHHH** it's that thing where you dig deeper you'll see another doll
- and it clicked on me, "ohh maybe it's something like nested and shii

### HTML Investigation
- I checked HTML again, **NOTHING**, didn't rlly give me anything
- Then I checked sources again, and I noticed... **THE IMAGES ARE STORED IN A NESTED MANNER!!!**

### Directory Traversal Discovery
- I checked and I noticed that the last photo is like inside, I rlly expected it like **WOO** maybe this is it???
- but the photo is a red-herring, but I was actually close because when I actually removed the `/subthing/` I forgot what it was, but when I removed it, I realized it's this **apache thing** where if there's no document??? it would actually present you with the contents of the directory
- then I tried it again, but this time, I opened the photo in a new tab, removed the photo and **BOOM!!!**

### Binary Path Navigation
- the actual directory actually showed **2 folders 0 and 1** and if you're at the wrong path, it would show you a file called **NO** with **0KB** which means it has nothing on it
- and actually, **frenz** pointed out to me "hey that shi is **binary**!!" but I disregarded it, I just bruteforced my way but I got confused because it's **REALLY REALLY NESTED**

### Using Burp Suite Site Mapper
- But I remembered what **matt** used when snooping around AIMS to find all pages in the site (the **site mapper of burp**)
- and **YES** it came useful because when I got lost? it will actually show me where I haven't opened yet, and there it was, I found **flag.html**

---

## 🧪 Tools & Techniques Used

- **`Burp Suite`** - Site mapper for directory enumeration and navigation tracking

---

## 🚩 Solution

**Step-by-step:**
1. Browse a folder without HTML to reveal its directory contents (I think this only works on **apache**??? yaur)
2. Navigate through the nested binary directory structure (0s and 1s)
3. Use Burp Suite's site mapper to track visited paths and find unexplored directories
4. Continue until you find `flag.html`

---

## 📌 Flag

```
CITU{ano_nemotto_ippai_matte_choudai_karinka_marinka_gen_o_hajiite}
```

---

## 📝 Notes / Lessons Learned
- **Search things up when you don't understand its meaning**, it might be a hint about what to look for.