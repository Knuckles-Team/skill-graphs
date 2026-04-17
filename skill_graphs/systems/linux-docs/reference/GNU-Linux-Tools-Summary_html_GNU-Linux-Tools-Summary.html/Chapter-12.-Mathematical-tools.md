#  Chapter 12. Mathematical tools
![Note](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/note.gif) | **num-utils homepage**
---|---
| The “num-utils” homepage,

units

Convert units of measurement between different scales. For example, centimeters to inches, litres to gallons.
Simply run the program, I recommend running it as follows:
```
units --verbose
```

---
This will run the program and it will tell you exactly what it is doing.
Example: you enter “60 meters” then you want it worked out in “kilometers”. The first line will tell you what this evaluates to.
If you wanted the conversion rate for “meters” to “kilometers” read the second line of the output (which will tell you meters/1000).
![Note](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/note.gif) | **To exit**
---|---
| Press **CTRL** -**D** (end-of-file key) when you are finished using _units_.

python

Python is a very powerful, easy to learn, general purpose, interpreted programming language. And it makes a great calculator! If you don't have a calculator installed then simply type _python_ , then hit [Enter].
This will execute the Python interpreter in interactive mode. Type your sums just like you would use a calculator. Note that if you want to work out fractions make sure you use a decimal point and a zero to obtain the correct answer (otherwise it will use integer division).
To start python in interactive mode, simply type:
```
python
```

---
Once python is started you can use it to add up sums or maybe do some python programming.
Use **CTRL** -**D** (end-of-file key) to exit the Python interpreter.

numgrep

A little bit like grep only this is designed for numbers only.
Use '/' (forward slashes) to contain each expression.
Use m<n> to find multiples of the number n and use f<n> to find factors of the number n.
Use commas to separate expressions and .. (two dots) to represent a range.
For example, to input from standard input you could simply type:
```
numgrep
```

---
To input from a file and look for numbers between 1 and 1000 you could type:
```
numgrep /1..1000/ file_name
```

---
![Note](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/note.gif) | **This tool comes from the num-utils package**
---|---
| Please note that this tool is part of the num-utils package.
* * *
