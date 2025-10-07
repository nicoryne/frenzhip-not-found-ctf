# Me Love Cookie

**Author:** Repunte, Frenz Nicole

**Challenge Link:** [Me Love Cookie](https://github.com/slaee/CITU-CTFd-event/tree/main/me-love-cookie)

**Date:** July 31, 2025

**Category:** Web Exploitation

---

## 🧠 Challenge Description

> *Find the hidden flag in the website*  

---

## 📁 Provided Files / Access

*Me Love Cookie Website*

---

## 🧪 Approach & Strategy

### Goal

Go through the website and find vulnerabilities that could reveal the flag.

### Tools / Techniques

- `HTTP Cookies`
- `DevTools`

---

## 🛠️ Solution

### The Website
The website is filled with cookies, as well as cookie monster himself.

![](/images/me-love-cookie-1.png) 

My assumption leads to the concept of HTTP Cookies and how it stores data.
Using Devtools, I checked the provided Storage tab:

![](/images/me-love-cookie-2.png)

Thus, the flag is stored as a cookie key-value pair.

![](/images/me-love-cookie-3.png)

### Flag
`
CITU{cookie_pasta}
`
