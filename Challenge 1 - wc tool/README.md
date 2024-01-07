# **Challenge 1 - WC tool**

wc is a command in Linux and Unix systems which returns the number of characters, words, lines and bytes in a file. The main aim of the challenge was to create our own version of the wc command at cmd level.

It's a pretty good one for starters. Using a Python library specialized in creating CLI apps called Click, I was able to learn how CLI apps work and operate and the nuances that come with file operations.

The source of the challenge is from the Coding Challenges website by John Crickett :  [https://codingchallenges.fyi/challenges/challenge-wc](https://codingchallenges.fyi/challenges/challenge-wc)

## **Tools used**

Language : Python 3.11.6

Libraries : Click

## Features

Get the number of bytes, characters, words, lines in a file by calling

```
python wc_tool.py test.txt <insert options or not>
```

or by using the pipe command to input file content directly into the program

```
insert options or notcat test.txt | python wc_tool.py <insert options>
```

Options include

| Options | Explanation                           |
| ------- | ------------------------------------- |
| -c      | Return number of bytes in a file      |
| -w      | Return numbe of words in a file       |
| -l      | Return number of lines in a file      |
| -m      | Return number of characters in a file |
