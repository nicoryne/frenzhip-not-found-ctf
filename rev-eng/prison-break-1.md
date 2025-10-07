# Prison Break Level 1 – Python Jailbreak – I forgot

**Author:**  Porter, Nicolo
**Challenge Link:** [https://github.com/slaee/CITU-CTFd-event/tree/main/prison-break-lvl-1]
**Date:** July 31, 2025  
**Category:** Explotation / Python Jailbreak

---

## 🧠 Challenge Description

> *Find the hidden flag*  

---

## 📁 Provided Files / Access

- `jail.py`
- `Dockerfile`
- `nc ipadd 10014`

---

## 🧪 Approach & Strategy

### Goal

Go through the provided python script to find vulnerabilities. Using a payload, extract the flag from the server.

### Tools / Techniques

List tools or concepts used. For example:

- `ChatGPT to help with building payload`
- [PyJail Cheatsheet](https://shirajuki.js.org/blog/pyjail-cheatsheet/)

---

## 🛠️ Step-by-step Solution

### Step 1: Download the file

`downloaded jail.py`

### Step 2: Inspect the file

`nvim jail.py`

### Step 3: Understand the code

Right off the bat, it is evident that our user input has limited sanitation which is vulnerable.

`hax = input(">" )`

Furthermore, stdin is closed right after the input so this prevents interactive input
once the code is running, meaning we cannot use input() if necessary.

The variable `hax` has the following checks:

1. Must not be more than 1024 characters in length.
2. Must not contain a string that matches with one of the confiscated tools.

The confiscated tools are: ['os', 'import', 'flag', 'system']

Once the `hax` string is filtered, it is reassigned to the variable `code`.

`code` wraps the user input in a triple-quoted string, which basically
allows for multi-line input.

Additionally, it also applies strip to remove any leading or trailing whitespaces, including
newlines.

After this, `code` is passed
to the Python interpreter using:

`os.execv(sys.executable, [sys.executable, '-c', code])`

This line basically replaces the current process with a new one that runs the Python interpreter with the provided code.

### Step 4: Find flag location

I am not really familiar with Python, so I was not really sure how to find where the flag is.
I relied on the Dockerfile that was provided to find the flag.txt.

`COPY flag.txt /srv/app/`

With this in mind, we can assume that the flag is located at the current working directory.

Usually, we can also list the contents of the directory using listdir if possible.

### Step 5: Solution

To put it simply, we just need to inject a short line of code that will print the flag given our limitations.

Fortunately, we still have access to open which we will be using to read the flag file.

The payload I used to inject is:

```python
print(open('fla' + chr(103) + '.txt').read())
```

Where I get the flag:

`
CITU{th1s_1s_jus7_4n_ez_0n3_w4rd3n_1s_c4r3l3ss}`
