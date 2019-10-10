import docutils.frontend, docutils.parsers.rst, docutils.utils, docutils.nodes



class YoutubeDirective(docutils.parsers.rst.Directive):
    required_arguments = 1
    optional_arguments = 100000
    has_content = True

    def run(self):
        from nodes import youtube
        return [youtube(link=self.arguments[0], title=" ".join(self.arguments[1:]), description = self.content)]


# class loremipsum
class NoteDirective(docutils.parsers.rst.Directive):
    required_arguments = 0
    optional_arguments = 0
    has_content = True

    def run(self):
        from nodes import note
        texts = []
        line = ''
        for t in self.content[1:]:
            if len(t) == 0:
                texts.append(line)
                line = ''
            else:
                line += ' '+t
        if len(line) > 0:
            texts.append(line)

        # children = self.state.inline
        return [note(title=self.content[0], content=texts)]
        # return [note(title=self.content[0], content=texts, rawsource='',  )]

# class NoteDirective2(docutils.parsers.rst.Directive):
#     required_arguments = 0
#     optional_arguments = 0
#     has_content = True
#
#     def run(self):
#         from nodes import note
#         import docutils.nodes as nodes
#         texts = []
#         line = ''
#         for t in self.content[1:]:
#             if len(t) == 0:
#                 texts.append(line)
#                 line = ''
#             else:
#                 line += ' '+t
#         if len(line) > 0:
#             texts.append(line)
#
#         title_text =
#         node = note(note(title=self.content[0], content=texts))
#         textnodes, messages = self.state.inline_text(title_text,
#                                                      self.lineno)
#         title = nodes.title(, '', *textnodes)
#         title.source, title.line = (self.state_machine.get_source_and_line(self.lineno))
#         self.state.nested_parse(self.content, self.content_offset, node)
#         return []
        # return [note(title=self.content[0], content=texts, rawsource='',  )]


class LoremIpsumDirective(docutils.parsers.rst.Directive):
    required_arguments = 2
    optional_arguments = 0
    has_content = True

    def run(self):
        from docutils.nodes import TextElement, paragraph
        amount = int(self.arguments[0])
        if self.arguments[1] == "words":
            from loremGeneration import random_words_as_string
            return [paragraph(text=random_words_as_string(amount))]
        elif self.arguments[1] == "sentences":
            from loremGeneration import random_sentences_as_string
            return [paragraph(text=random_sentences_as_string(amount))]
        elif self.arguments[1] == "paragraphs":
            from loremGeneration import random_sentences
            return [paragraph(text=p) for p in random_sentences(amount)]
        else:
            self.directive_error(3, "The lorem parameter %s is unknown, use words|sentences|paragraphs" % self.arguments[1])


def register():
    from docutils.parsers.rst.directives import register_directive
    register_directive("lorem", LoremIpsumDirective)
    register_directive("youtube", YoutubeDirective)
    # register_directive("note", NoteDirective)


if __name__ == "__main__":
    ipsum = LoremIpsumDirective("lorem", ["5", "words"], [], "", "", 0, "", 0, 0)
    print ipsum.run()[0].astext()
