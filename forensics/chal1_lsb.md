# Cat LSB Image

**Author:** Repunte, Frenz Nicole

**Challenge Link:** [Cat LSB - Blue Channel](https://github.com/slaee/CITU-CTFd-event/blob/main/misc/chal1_lsb.png)

**Date:** July 31, 2025

**Category:** Image Stenography

---

## 🧠 Challenge Description

> *Find the hidden flag in the image*  

---

## 📁 Provided Files / Access

 - *chal1_lsb.png*

---

## 🧪 Approach & Strategy

### Goal

Find the flag within the image.

### Tools / Techniques

- `LSB Steganography`
- [`zsteg`](https://github.com/zed-0xff/zsteg)

---

## 🛠️ Solution

### The Image
The image provided was nothing out of the oridinary.

![](/images/chal1-lsb-1.png) 

The title seemed to denote LSB, which meant something had to do with the least significant bits ie. LSB Stenography.

### The Command
Using zsteg, a tool for image stenography, I ran the command:

```
zsteg chal1-lsb.png -a | grep CIT
``` 
Which would search for instanced of "CIT" in all types of analyses with zsteg.

The result was a flag hidden within the LSB.

![](/images/chal1-lsb-2.png)

### Flag
`
CITU{LSBEmbedOnBlue_Channel}
`
