# Chapter 1: What is Python & How to Set It Up?

---

## What Will You Learn?

- What Python is and why it matters
- How to install Python on Windows and Linux
- How to write and run your first program

---

## Read This First — Python Symbols Guide

Before diving into code, read the **[Python Symbols Guide](../reference/python_symbols_guide.md)**.

It explains when to use `( )`, `[ ]`, and `{ }` — three types of brackets that each
mean something different in Python. You will see them constantly from Chapter 2 onwards.
Knowing them upfront prevents a lot of early confusion.

---

## What is Python?

Python is a **high-level, general-purpose programming language** — meaning you can use it to build almost anything: websites, games, AI, data analysis tools, automation scripts, and more.

What makes Python special is its **readability**. Python code looks very close to plain English, which makes it one of the easiest languages to learn and also one of the most productive for experienced developers.

**Who uses Python?**
- Google, YouTube, Instagram — for their backends
- NASA — for space mission data analysis
- Netflix — for recommendation systems
- Data scientists and machine learning engineers worldwide

**A quick look at Python code:**

```python
name = "Alice"
print("Hello, " + name)
```

Compare that to Java doing the same thing — you'd need 6+ lines. Python gets it done in 2.

---

## How Python Works

When you write Python code and run it, here's what happens behind the scenes:

1. You write instructions in a `.py` file
2. The **Python interpreter** reads your file line by line
3. It converts each line into machine instructions the computer understands
4. The computer executes those instructions and shows you the result

This is why Python is called an **interpreted language** — it reads and runs your code directly, without needing a separate compilation step.

---

## Key Terms

| Term | What it Means |
|------|--------------|
| **Program** | A set of instructions written for a computer to execute |
| **Code / Source Code** | The text you write using a programming language |
| **Python** | The programming language we use in this course |
| **Interpreter** | The program that reads and runs your Python code |
| **Terminal / Command Prompt** | A text interface where you type commands to the computer |
| **IDE** | Integrated Development Environment — a smart editor for writing code |
| **Script** | A Python file, typically saved with the `.py` extension |
| **Syntax** | The rules of the language — how code must be written to be valid |

---

## Installation — Windows

### Step 1: Download Python
1. Open your browser and go to: **https://www.python.org/downloads/**
2. Click the large button that says **"Download Python 3.x.x"**

### Step 2: Install Python
1. Open the downloaded `.exe` file
2. **CRITICAL:** Check the box at the bottom that says **"Add Python to PATH"** before clicking Install
3. Click **"Install Now"**
4. Wait for installation to finish, then click "Close"

### Step 3: Verify installation
Open Command Prompt (`Windows key + R`, type `cmd`, press Enter) and run:
```
python --version
```
You should see something like: `Python 3.12.0`

### Step 4: Install VS Code (Recommended)
1. Download from: **https://code.visualstudio.com/**
2. Install and open it
3. Go to Extensions (left sidebar icon or `Ctrl+Shift+X`)
4. Search for **"Python"** (by Microsoft) and install it

---

## Installation — Linux (Ubuntu / Debian)

### Step 1: Open Terminal
Press `Ctrl + Alt + T`

### Step 2: Update package list
```bash
sudo apt update
```

### Step 3: Install Python
```bash
sudo apt install python3 python3-pip -y
```

### Step 4: Verify installation
```bash
python3 --version
```
Expected output: `Python 3.x.x`

### Step 5: Optional — Create a shortcut
On Linux, the command is `python3`. To use just `python`, add this to your `~/.bashrc`:
```bash
alias python=python3
```
Then run: `source ~/.bashrc`

### Step 6: Install VS Code (Optional)
```bash
sudo snap install code --classic
```

---

## Running Your First Program

### Method 1: Terminal
1. Create a file called `hello.py`
2. Write inside it: `print("Hello, World!")`
3. In the terminal, navigate to the file's folder and run:
   - Windows: `python hello.py`
   - Linux: `python3 hello.py`

### Method 2: VS Code
1. Open VS Code
2. Create a new file, save it as `hello.py`
3. Write your code
4. Press `F5` or click the Run button (▶) at the top right

---

## Python Interactive Mode

Python also has an **interactive mode** (called REPL — Read, Evaluate, Print, Loop) where you can type code and see results immediately without saving a file.

```bash
python3
>>> 2 + 2
4
>>> print("Hello!")
Hello!
>>> exit()
```

This is great for quick experiments and testing small ideas.

---

## Examples in This Chapter

| File | What it Does |
|------|-------------|
| [example_01_hello_world.py](example_01_hello_world.py) | Prints Hello World |
| [example_02_your_name.py](example_02_your_name.py) | Prints your name |
| [example_03_multiple_prints.py](example_03_multiple_prints.py) | Sequential print statements |
| [example_04_emojis.py](example_04_emojis.py) | Print with emojis |
| [example_05_ask_name.py](example_05_ask_name.py) | Ask and greet the user |
| [example_06_python_facts.py](example_06_python_facts.py) | Fun Python facts |
