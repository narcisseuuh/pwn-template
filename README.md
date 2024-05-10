# pwn-template

A simple tool to generate python pwntools script written in python.
What the script does is checking if there is a libc in our pwn environment, checking the binary name, and ip/port to have everything setup and then just focus on pwn.

# Adding it to the zshrc

I use environment variables to precise wether I want to debug with gdb or to exploit locally.
```bash
export DBG='NO'
export LOCAL='YES'
```
Then I create an alias to just use `generate_pwn` when I created a directory containing my environment in CTF.
```bash
alias generate_pwn='cp /path/to/solve.py . && python3 /path/to/generate_script.py'
```
