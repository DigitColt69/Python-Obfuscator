# Python-Obfuscator

One night I got bored of writing good code, so I made good code to make bad code.

### **DONT USE IN PRODUCTION**

**I just made this because it was interesting to me. I do plan on making this more official in the future, but currently don't have the time!**


## Installing

```
pip install python-obfuscator
```

## Quickstart

Print out obfuscated code
```
pyobfuscate -i your_file.py
```

Apply changes to the input file
```
pyobfuscate -i your_file.py -r True
```

## More Detailed Documentation

You can use this as a module if you want
```
import python_obfuscator
obfuscator = python_obfuscator.obfuscator()

code_to_obfuscate = "print('hello world')"
```

You can also exclude certain techniques applied for obfuscation
```
import python_obfuscator
from python_obfuscator.techniques import add_random_variables
obfuscator = python_obfuscator.obfuscator()

code_to_obfuscate = "print('hello world')"
obfuscated_code = obfuscator.obfuscate(code_to_obfuscate, remove_techniques[add_random_variables])
```
Find a list of all techniques [here](https://github.com/davidteather/python-obfuscator/blob/210da2d3dfb96ab7653fad869a43cb67aeb0fe67/python_obfuscator/techniques.py#L87)

## Example Obfuscated Code

Input
```
y = input("what's your favorite number")

user_value = int(y)
print("{} that's a great number!".format(user_value))
```

[With `pyobfuscate -i file.py`](https://gist.github.com/davidteather/b6ff932140d8c174b9c6f50c9b42fdaf)


[With `--one-liner True`](https://gist.github.com/davidteather/75e48c04bf74f0262fe2919239a74295)

## Authors

* **Rdimo0** - *Initial work* - [Rdimo0](https://github.com/Rdimo0)

See also the list of [contributors](https://github.com/davidteather/python-obfuscator) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
