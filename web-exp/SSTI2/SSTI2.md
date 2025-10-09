# SSTI2 – Web Exploitation

**Author:**  Frenz Nicole Repunte
**Challenge Link:** https://play.picoctf.org/practice/challenge/488
**Date:** 2025-10-10 
**Category:** Web Exploitation  

---

## 🧠 Challenge Description

> I made a cool website where you can announce whatever you want! I read about input sanitization, so now I remove any kind of characters that could be a problem :)

---

## 📁 Provided Files / Access

- Website: `http://shape-facility.picoctf.net:[port]/`

---

## 🧪 Approach & Strategy

### Goal

Find a way to execute remote code via Server-side Template Injection

### Tools / Techniques

List tools or concepts used. For example:

- SSTI
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)
- [Python SSTI](https://onsecurity.io/article/server-side-template-injection-with-jinja2/)

---

## 🛠️ Step-by-step Solution

1. First check on the website, you are presented with a form. Since it's SSTI-related, try checking what {{}} does.
   ![[ssti2_1.png]]
   ![[ssti2_2.png]]

2. Clearly some characters are being checked. Let's try an operation like {{7 * 7}}.
   ![[ssti2_3.png]]

3. Operations work. After finding [this repository](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md) that's related to all things payloads, we can analyze our specific injection.
   ![[ssti2_5.png]]
   Seeing that this website uses {{}}, we can see that it uses Jinja2 expression, which is for Python. Language acquired.

4. Going for a quick google search for "Python SSTI", we are lead to a fun site that explains payloads using Jinja2.
   ![[ssti2_4.png]]
   Looking through the site, you get a payload like this:
```python
{{request.application.__globals__.__builtins__.__import__('os').popen('id').read()}}
```

5. Well, we have a payload, but when we try it out on the site we get this.
   ![[ssti2_6.png]]
   So, what went wrong? Well we still have those characters that are being checked.

6. Through a bit of trial and error, you'll see [], . , __ being blocked and don't print. 
   ![[ssti2_7.png]]
   So that would mean we just have to find a payload that doesn't use that.

7. A couple of things you can do in Python: piping ( | ) still works and there are functions to retrieve class items/attributes. Furthermore, you can use hexcode to represent special characters like _ ( \x5f ). Using `attr` and `getitem` as our retrievers, we can make this payload:
```python
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('ls')|attr('read')()}}
```

8. Plugging that into the form, we can see the current folder has a flag file.
   ![[ssti2_8.png]]
   Just change the command to ```cat flag``` and:
   ![[ssti2_9.png]]
