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

        return [note(title=self.content[0], content=texts)]


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
    register_directive("note", NoteDirective)


if __name__ == "__main__":
    ipsum = LoremIpsumDirective("lorem", ["5", "words"], [], "", "", 0, "", 0, 0)
    print ipsum.run()[0].astext()
