# 💻 Networking with my Friend

## 📁 Challenge Info
- **Challenge Name:** Networking with my Friend
- **Category:** Network Forensics
- **Points:** 250

---

## 🎯 Objective
Find the flag by reading the network traffic in USB protocol

---

## 🧠 Initial Thoughts

- It was my first time seeing **USB protocol** in a pcap file
- kind of regretted not learning USB protocol filters and tools and shii
- I rlly couldn't let **matt** down on this shii **HAHAHA**

---

## 🔍 Investigation / Analysis / Solution

### Initial AI Consultation
- I actually asked the AI on what tools in wireshark I used to analyze a USB protocol like TCP and UDP. The response was okay but nothing stick to me, because the prompt was vague and it thought that I was planning on capturing packets, not reading them (my fault lol)

### Wireshark Exploration
- I tried right clicking the USB packet and checked if I can use **follow** to follow it, but no
- I checked the USB protocol and it was clean
- I tried using **conversations** in the statistics, and it's only one sided, I thought like there's gonna be noise but no, it was clean and one sided

### Pattern Recognition Attempts
- I was trying to scroll through every packet and I thought I found the pattern, there's this part of the frame and in the ascii side of things, it changed alot, I was like "**oh shi this might be it**" but it was just a timestamp **URB sec** and **URB usec**
- I actually cycled through other questions because I rlly thought it's hard but looked again, cycled through the packets again and I noticed something

### The Discovery
- at the last part of the frame field: **Unused Setup Header**, I was like, there's like **00:00** and when I scrolled I do notice there's data in it, and I checked again, **THERE IS!!!** because in my first thought, there wasn't any because it doesn't show anything in the ascii part, but when I looked closer I did find data, but what was it???
- and yea it also crossed my mind that it says **Unused Setup Header** might not be it because "Header" meaning it's not the data??? but I tried because it checks out being a data being wrapped around **frame -> protocol -> the headers -> (Unused Setup Header)** (I'm not accurate about this but yea while snooping around, the format is always like data are gonna be inside of a header, header being inside the protocol, etc. etc.)

### Research Phase
- I looked up the internet on how to rip up like data from USB protocol, or like something along the lines
- I actually found a writeup about how to extract the data from the keyboard using **tshark command** and I was like "**ohhh this might be it**" but no since the tshark command won't work on the file because the packets are malformed, but I checked again and a theory brewed up on my mind because the suspicious part of the frame (the **Unused Setup Header**) matched to what the writeup was grabbing (**exactly 8 bytes**), it's just not labeled because the packet was malformed

### The Hint & Breakthrough
- Until the hint showed and presented me (**It's a keyboard parser**)
- and then I searched for it, found a **github page** and **BOOM**, **YES** my suspicion was correct, those **8 bytes MUST be the key**
- but my issue is, I only know what to grab, I'm not some wizardly person who knows commands, I just know in the high level that I **NEED TO GRAB THAT LAST 8 bytes of the frame**

### ChatGPT to the Rescue
- when I received a message that I can use AI for that particular type of problem, I whipped up **chatGPT** to make me a command that will rip out the last 8 bytes of that frame and format it the same as what the keyboard parser wanted as an input

**THIS COMMAND:**
```bash
tshark -r network1.pcap -T fields -e frame[40:8] -E header=n -E occurrence=f | tr -d '\\'
```
*(It just means to rip out that part of the frame and then just remove the backslash, and I forgot to pipe it to a file, I be like a caveman copy pasting shii like that 'ooga booga')*

### Final Steps
- I actually tried the command that was given in the github, tweaked it? but it didn't work because for some odd reason, when I tried using the actual field "**Unused Setup Header**", it just prints out **1** over and over which was stupid, I don't know why maybe the command lacked something and I just did it in the hard way by actually doing the **low level filter** and it solved my problem...
- I put it in the text file and **badabim badaboom**, the flag was there

---

## 🧪 Tools & Techniques Used

- **`tshark`** - Command-line network protocol analyzer
- **[USB Keyboard Parser](https://github.com/TeamRocketIst/ctf-usb-keyboard-parser)** - GitHub tool for parsing USB keyboard data
- **`Wireshark`** - Network protocol analyzer GUI
- **`ChatGPT`** - For generating the tshark extraction command

---

## 🚩 Solution

**Step-by-step:**
1. **Clean up the packet** by keeping the last 8 bytes of the frame (the data)
2. **Extract using tshark:** `tshark -r network1.pcap -T fields -e frame[40:8] -E header=n -E occurrence=f | tr -d '\\'`
3. **Feed the output** to a USB Keyboard parser

---

## 📌 Flag

```
CITU{Keyb0ard_p4rsing}
```

---

## 📝 Notes / Lessons Learned
- **Try and learn things that you think you might need because you will...**
- USB protocol analysis requires specialized tools and understanding
- Sometimes malformed packets still contain the data you need, just in unexpected places
- Also my explanation might be rough, but it's because I'm mostly into patterns, not names