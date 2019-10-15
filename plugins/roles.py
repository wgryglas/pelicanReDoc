import re


def lorem_text_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    from loremGeneration import random_words_as_string
    # import docutils.nodes as nodes
    # for some reason returning Text node element produces 'rawsource' attribute error
    # therfore I had to wrap this node around
    # return [nodes.Text(random_words_as_string(int(text)), rawtext)], []
    from nodes import inlinetext
    return [inlinetext(random_words_as_string(int(text)), rawtext)], []


_integer_number_with_decimals_regex_ = re.compile(r'^[-+]?[0-9]+\.0+$')
_integer_number_regex_ = re.compile(r'^[-+]?[0-9]+$')


def read_number_string(text):
    if text.endswith('d'):
        return int(text[:-1])
    elif text.endswith('f'):
        return float(text[:-1])
    elif _integer_number_with_decimals_regex_.match(text):  # try to format as integer
        return int(text.split('.')[0])
    elif _integer_number_regex_.match(text):
        return int(text)
    else:
        return float(text)


def vector_input_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    from nodes import vector
    print 'making vector role', rawtext
    values = map(read_number_string, text.split())
    return [vector(values[0], values[1], values[2], True, rawtext)], []


def input_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    from nodes import input
    return [input(read_number_string(text), rawtext)], []


def id_number(name, rawtext, text, lineno, inliner, options={}, content=[]):
    from nodes import number
    return [number(text)], []


def register():
    from docutils.parsers.rst import roles
    roles.register_local_role("lorem", lorem_text_role)
    roles.register_local_role("vector", vector_input_role)
    roles.register_local_role("input", input_role)
    roles.register_local_role("number", id_number)
