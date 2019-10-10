import docutils.nodes as nodes


class input(nodes.Inline, nodes.Element):
    def __init__(self, value, rawsource='', *children, **attributes):
        textnode = nodes.Text('{}'.format(value))
        nodes.Element.__init__(self, rawsource, textnode, *children, **attributes)
        self.value = value


class vector(nodes.Inline, nodes.Element):
    def __init__(self, x, y, z, inline=False, rawsource='', *children, **attributes):
        nodes.Element.__init__(self, rawsource, input(x), input(y), input(z))
        self.inline = inline


class youtube(nodes.Inline, nodes.Element):
    def __init__(self, link, title, description='', rawsource='', *children, **attributes):
        from docutils.nodes import Text
        nodes.Element.__init__(self, rawsource)
        self.attributes['link'] = link
        self.attributes['title'] = title
        self.append(Text(description))


class note(nodes.Element):
    def __init__(self, title, content='', rawsource='', *children, **attributes):
        nodes.Element.__init__(self, rawsource, *children, **attributes)
        self.attributes['title'] = title
        self.text = content
        # from docutils.nodes import Text
        # self.append(Text('\n'.join(content)))


class number(nodes.Inline, nodes.Element):
    def __init__(self, value, rawsource='', *children, **attributes):
        nodes.Element.__init__(self, rawsource)
        self.number = int(value)
