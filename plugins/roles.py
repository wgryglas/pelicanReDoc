
def lorem_text_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    from docutils.nodes import Text
    from loremGeneration import random_words_as_string
    return [Text(random_words_as_string(int(text)))], []


def read_number_string(text):
    if text.endswith('d'):
        return int(text[:-1])
    elif text.endswith('f'):
        return float(text[:-1])
    else:
        return float(text)


def vector_input_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    from nodes import vector
    values = map(read_number_string, text.split())
    return [vector(values[0], values[1], values[2], True)], []


def register():
    from docutils.parsers.rst import roles
    roles.register_local_role("lorem", lorem_text_role)
    roles.register_local_role("vector", vector_input_role)