# -*- coding: utf-8 -*-
"""
    pygments.lexers._mapping
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Lexer mapping definitions. This file is generated by itself. Everytime
    you change something on a builtin lexer definition, run this script from
    the lexers folder to update it.

    Do not alter the LEXERS dictionary by hand.

    :copyright: Copyright 2006-2014 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from __future__ import print_function

LEXERS = {
    'PythonLexer': ('pygments.lexers.python', 'Python', ('python', 'py', 'sage'), ('*.py', '*.pyw', '*.sc', 'SConstruct', 'SConscript', '*.tac', '*.sage'), ('text/x-python', 'application/x-python')),
}

if __name__ == '__main__':  # pragma: no cover
    import sys
    import os

    # lookup lexers
    found_lexers = []
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
    for root, dirs, files in os.walk('.'):
        for filename in files:
            if filename.endswith('.py') and not filename.startswith('_'):
                module_name = 'pygments.lexers%s.%s' % (
                    root[1:].replace('/', '.'), filename[:-3])
                print(module_name)
                module = __import__(module_name, None, None, [''])
                for lexer_name in module.__all__:
                    lexer = getattr(module, lexer_name)
                    found_lexers.append(
                        '%r: %r' % (lexer_name,
                                    (module_name,
                                     lexer.name,
                                     tuple(lexer.aliases),
                                     tuple(lexer.filenames),
                                     tuple(lexer.mimetypes))))
    # sort them to make the diff minimal
    found_lexers.sort()

    # extract useful sourcecode from this file
    with open(__file__) as fp:
        content = fp.read()
    header = content[:content.find('LEXERS = {')]
    footer = content[content.find("if __name__ == '__main__':"):]

    # write new file
    with open(__file__, 'w') as fp:
        fp.write(header)
        fp.write('LEXERS = {\n    %s,\n}\n\n' % ',\n    '.join(found_lexers))
        fp.write(footer)

    print ('=== %d lexers processed.' % len(found_lexers))
