# **TPython**
TPython a better python REPL.
### [Github](https://github.com/Techlord210/TPython) | [PyPi](https://pypi.org/project/TPython/)

## **config.jsonc changelog**
```jsonc
// Removed
{
        "error": {
            "internal": "red",
            "user": "red"
        }
}
```

## Features
- Built-in TimeIt, clear/cls
- Colors
- Update Notifier 
- Flexible

## Installation
```
$ pip install TPython
```

## Dependencies
```
colorama
```

## **Usage**

### **Run**
```
$ tpy
```
### or
```
$ python3 -m tpy
```
### or
```py
import tpy
tpy.main()
```

### **Built-in Commands**
|     Command     |          Function            |
| :-------------: | :--------------------------: |
|     version     |    Tells current version     |
| exit/quit/close |          Exits REPL          |
|    cls/clear    |     Clears the terminal      |
|     timeit      | Tells execution time of code |

### **Configuration**

#### **Create File**
**Windows:**
```
> mkdir %USERPROFILE%\.TPython
> curl https://raw.githubusercontent.com/Techlord210/TPython/main/config.jsonc -o %USERPROFILE%\.TPython\config.jsonc
```
**Mac OS/Linux/BSD:**
```
$ mkdir ~/.TPython
$ curl https://raw.githubusercontent.com/Techlord210/TPython/main/config.jsonc -o ~/.TPython/config.jsonc
```

#### **Instructions**
- File location: `~/.TPython/config.jsonc`
- Config file is case-sensetive.
- Do not use Spaces in values of config file.