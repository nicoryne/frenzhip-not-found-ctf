# [Challenge Name] – [Category] – [Points]

**Author:**  
**Challenge Link:** [CTF Platform or URL]  
**Date:** YYYY-MM-DD  
**Category:** (e.g., Web, Pwn, Crypto, Misc, Forensics)  

---

## 🧠 Challenge Description

> *(Paste the full challenge prompt here)*  
>
> Example:  
> You're given a service to interact with. Find the hidden flag!

---

## 📁 Provided Files / Access

- `example_file.txt`
- Service: `nc example.ctf.net 12345`
- Website: `https://example.ctf.net`

---

## 🧪 Approach & Strategy

### Goal

Briefly describe what the challenge is asking you to do.

### Tools / Techniques

List tools or concepts used. For example:

- `curl`, `nmap`, `wireshark`
- Steganography
- Encoding/Decoding (Base64, hex, etc.)
- Web fuzzing
- Logic or math

---

## 🛠️ Step-by-step Solution

```bash
# Step 1: Download the file
curl -O http://example.ctf.net/file.zip

# Step 2: Unzip and inspect
unzip file.zip
strings file.jpg | grep FLAG
