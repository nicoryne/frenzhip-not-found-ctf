# Prison Break Level 2 – Python Jailbreak – I forgot

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
- `nc ipadd 10015`

---

## 🧪 Approach & Strategy

### Goal

Go through the provided python script to find vulnerabilities. Using a payload, extract the flag from the server.

### Tools / Techniques

List tools or concepts used. For example:

- `ChatGPT to help with building payload`
- [PyJail Cheatsheet](https://shirajuki.js.org/blog/pyjail-cheatsheet/)
- [Text Decorator](https://fancy-generator.com/)

---

## 🛠️ Step-by-step Solution

### Step 1: Download the file

`downloaded jail.py`

### Step 2: Inspect the file

`nvim jail.py`

### Step 3: Understand the code

Similar with our first level Jailbreak, we just need to take note of the limitations and bypass the filters to get extract the flag.

The variable `hax` has the following checks:

1. Must not be more than 512 characters in length.
2. Must not contain a string that matches with one of the confiscated tools.

The confiscated tools are: ['sys', 'import', 'flag', 'open', '/', 'sh', 'bin', 'eval', 'exec', 'os', 'read', 'system', 'builtins', '**builtins**']

Once the `hax` string is filtered, it is reassigned to the variable `code`.

Similar to Jailbreak 1, `code` wraps our `hax` variable in a multi-line triple-quoted f-string.

But now we know that it is also importing os alongside our function.

After this, `code` is passed
to the Python interpreter using:

`os.execv(sys.executable, [sys.executable, '-c', code])`

This line basically replaces the current process with a new one that runs the Python interpreter with the provided code.

### Step 4: Find flag location

I relied on the Dockerfile that was provided to find the location of the flag.txt.

`COPY flag.txt /srv/app/`

### Step 5: Solution

This time we cannot use open anymore and read so we need to find an alternate payload.

We can actually make use of text decorating generators to bypass the filters.

For example, since our previous implementation for Jailbreak 1 made use of
open and read which are now confiscated, we can decorate those texts to bypass the filter.

If we were to italicize open and read, we can make use of the functions while bypassing the filters.

The payload I used to inject is:

```python
print(𝘰𝘱𝘦𝘯('fla' + chr(103) + '.txt').𝘳𝘦𝘢𝘥())
```

Where I get the flag:
`
CITU{0k_g00d_y0u_escaped_lvl_2_ret_has_a_message_for_you_in_the_next_level}`
