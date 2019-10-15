from pelican.readers import PelicanHTMLTranslator, RstReader
import docutils.core, docutils.io


class SFHtmlTranslator(PelicanHTMLTranslator):
    """
    class for handling custom nodes provided by this plugin for translation rst to html
    """
    def __init__(self, document):
        PelicanHTMLTranslator.__init__(self, document)

    def endtag(self, tagname):
        return '</{}>'.format(tagname)

    def visit_vector(self, node):
        self.body.append(self.starttag(node, 'span' if node.inline else 'div', **{'class': 'vector-input'}))
        #self.body.append("[")

    def depart_vector(self, node):
        #self.body.append("]")
        self.body.append('<button class="vector-copy" style="padding:3px; border-radius:3px">copy</button>')
        self.body.append(self.endtag('span' if node.inline else 'div'))

    def visit_input(self, node):
        tag_string = self.starttag(node, 'span', **{'class': 'scalar-input'})
        self.body.append(tag_string)

    def depart_input(self, node):
        self.body.append(self.endtag('span'))

    # def visit_note(self, node):
    #     self.body.append(self.starttag(node, 'div', **{'class': 'note'}))
    #     self.body.append('<p class="note-title">{}</p>'.format(node.attributes['title']))
    #     self.body.append('<div class="note-content">')
    #     for t in node.text:
    #         self.body.append('<p>{}</p>'.format(t))
    #     self.body.append(self.endtag('div'))
    #
    # def depart_note(self, node):
    #     self.body.append(self.endtag('div'))

    def visit_inlinetext(self, node):
        pass
        # self.body.append(self.starttag(node, 'span'))

    def depart_inlinetext(self, node):
        pass

    # def visit_title(self, node):
    #     PelicanHTMLTranslator.visit_title(self, node)

    def visit_section(self, node):
        from docutils.nodes import section
        if not isinstance(node.parent, section):
            self.body.append('<button class="in-text scrolling next"></button>')
            self.body.append('<button class="in-text scrolling previous"></button>')
        PelicanHTMLTranslator.visit_section(self, node)

    def visit_number(self, node):
        self.body.append('<span class=id-number>{}</span>'.format(node.number))
        # self.body.append(self.starttag(node, 'span', **{'class':'id-number'}))
        # self.body.append(self.endtag('span'))

    def depart_number(self, node):
        pass


class SFRstReader(RstReader):
    """
    helper class for registering custom html translator
    """

    def _get_publisher(self, source_path):
        extra_params = {'initial_header_level': '2',
                        'syntax_highlight': 'short',
                        'input_encoding': 'utf-8'}
        user_params = self.settings.get('DOCUTILS_SETTINGS')
        if user_params:
            extra_params.update(user_params)

        pub = docutils.core.Publisher(destination_class=docutils.io.StringOutput)
        pub.set_components('standalone', 'restructuredtext', 'html')
        pub.writer.translator_class = SFHtmlTranslator
        pub.process_programmatic_settings(None, extra_params, None)
        pub.set_source(source_path=source_path)
        pub.publish()
        return pub


def add_reader(readers):
    readers.reader_classes['rst'] = SFRstReader


def register():
    from pelican import signals
    signals.readers_init.connect(add_reader)
