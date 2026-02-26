<div align="center">

  # Username Generator Pro

  Smart, fast and customizable username generator for 2 / 3 / 4‑character handles.

  <!-- Screenshot -->
  <p>
    <img
      alt="Username Generator Pro Screenshot"
      src="https://github.com/vv1ck/Generator_usernames/raw/main/Screenshot%202026-02-26%20062249.png"
      style="max-width: 900px; border-radius: 10px; box-shadow: 0 8px 20px rgba(0,0,0,0.25);"
    >
  </p>

  <!-- Badges -->
  <p>
    <img alt="Python" src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white">
    <img alt="Platform" src="https://img.shields.io/badge/Platform-Windows%20%7C%20CLI-4D4D4D?style=for-the-badge&logo=windows&logoColor=white">
    <img alt="Type" src="https://img.shields.io/badge/Type-Username%20Generator-8A2BE2?style=for-the-badge&logo=terminal&logoColor=white">
  </p>

  <img alt="Preview" src="https://img.shields.io/badge/UI-Colored%20CLI%20%7C%20Progress%20Bar-00C853?style=flat-square">

</div>

---

## Overview

**Username Generator Pro** is a powerful and ultra‑fast command‑line tool that generates clean, unique usernames with lengths of **2**, **3**, or **4** characters.  
It is designed for scenarios where you need **huge lists of unique handles** with strict formatting rules and file‑based persistence.

The tool:
- Generates usernames using **lowercase English letters**, **digits**, `_` and `.`
- Enforces **no duplicates** across runs for each output file
- Respects strict rules for the `.` character
- Offers **advanced modes** for repeated‑letter usernames
- Provides a **modern, colored CLI** with a **progress bar** and **timing information**

---

## Features

- **4 main generation modes** (2 / 3 / 4 chars + mixed)
- **Dot‑safety rules**:
  - Usernames **never start** with `.`
  - Usernames **never end** with `.`
  - `.` is only allowed in the **middle** of the username
- **No duplicates**:
  - New usernames are guaranteed to be unique within a run
  - Existing usernames from the target file are loaded, and duplicates are avoided
- **Advanced modes** for 3‑ and 4‑character usernames:
  - Repeated letters only
  - Fully random alphanumeric + `_` + `.`
- **File‑based storage**:
  - Each mode has its own output file
  - New results are **appended** (old data is preserved)
- **Modern CLI UX**:
  - Colored sections and status messages
  - Inline **progress bar** while generating
  - Execution **time summary** per generation

---

## Username Rules

- Allowed characters:
  - `a`–`z` (lowercase English letters)
  - `0`–`9` (digits)
  - `_` and `.`
- Dot rules:
  - Username **cannot start** with `.`
  - Username **cannot end** with `.`
  - `.` can appear **only in the middle** (e.g. `a.b`, `h_.9`, `x.yz`)
- Duplicates:
  - The tool loads all usernames from the target output file
  - Newly generated usernames **must not** exist in that set

---

## Menu & Options

When you run the script, you get a colored main menu like:

- **[1] Generate 2-character usernames**
- **[2] Generate 3-character usernames**
- **[3] Generate 4-character usernames**
- **[4] Generate random usernames (2, 3, and 4 characters)**
- **[5] Exit**

### Option 1 – 2‑Character Usernames

- Generates usernames of length **2** (e.g. `we`, `l7`, `_u`, `j_`)
- Uses letters, digits and `_` (no leading/trailing `.`)
- Output file: **`usernames_2_chars.txt`**

### Option 2 – 3‑Character Usernames

After choosing **3‑character** mode, an **advanced mode** menu appears:

- **[1] Repeated letters only**  
  Examples: `wee`, `uud`, `qqq`, `pee`

- **[2] Fully random mix (letters, digits, `_`, `.`)**  
  Examples: `iwb`, `_uw`, `u.i`, `oq3`, `a_7`

Output file: **`usernames_3_chars.txt`**

### Option 3 – 4‑Character Usernames

Same advanced mode as above:

- **[1] Repeated letters only**  
  Examples: `iiid`, `hhee`, `qqqu`

- **[2] Fully random mix (letters, digits, `_`, `.`)**  
  Examples: `iwhh`, `jf.u`, `9h_q`, `as.5`

Output file: **`usernames_4_chars.txt`**

### Option 4 – Mixed Length (2 / 3 / 4)

- Randomly selects the length for each username: **2**, **3** or **4**
- Uses the full allowed character set with the same `.` rules
- Output file: **`usernames_random_2_3_4.txt`**

---

## Installation

1. **Clone the repository** (or download the source):

   ```bash
   git clone https://github.com/vv1ck/Generator_usernames.git
   cd Generator_usernames
   ```

2. Make sure you have **Python 3.x** installed and available in your `PATH` (for the Python versions).

3. No external dependencies are required (only Python standard library).

---

## Usage

### 1. PC (Windows / Linux / macOS) – Python script

From the project root:

```bash
python Generator_PC.py
```

### 2. Phone (Android with Termux / mobile Python)

From your Python‑enabled terminal on the phone:

```bash
python Generator_phone.py
```

### 3. Windows – Standalone EXE

- Run `Generator.exe` directly (double‑click) or from `cmd` / PowerShell:

  ```bash
  .\Generator.exe
  ```

---

After launching any version:

1. Choose one of the options from **1 to 4**.
2. Enter how many usernames you want to generate.
3. (For options 2 and 3) choose the **advanced mode**:
   - `1` – repeated letters only  
   - `2` – fully random mix
4. Watch the **progress bar** and wait for the summary.

At the end, you will see:
- How many usernames were generated
- Which file they were saved to
- Total time taken
- A small **preview** of generated usernames

---

## Output Files

The tool writes to these files (appending if they already exist):

- `usernames_2_chars.txt` – 2‑character usernames  
- `usernames_3_chars.txt` – 3‑character usernames  
- `usernames_4_chars.txt` – 4‑character usernames  
- `usernames_random_2_3_4.txt` – mixed (2 / 3 / 4) usernames  

You can safely re‑run the generator multiple times:  
each new run will **append** more unique usernames while checking against existing ones in the same file.

---

## Notes & Performance

- Designed to be **fast and smooth**, even for large counts (e.g. tens of thousands of usernames).
- The generator uses a **maximum attempts limit** per batch to avoid infinite loops if the space becomes saturated.
- Colorized output and progress bar are optimized for **Windows terminals** that support ANSI escape sequences.

---

## Author & Links

- **Platform**: [Cathack.io](https://cathack.io)  
- **Instagram**: [@221298](https://instagram.com/221298)

If you use this tool, feel free to share results or suggestions via Instagram or the platform. 🚀

