from lilypondlexer.lilypondlexer.lilypondlexer import lilypond

def setup(app):
    app.add_lexer("lilypond", lilypond.LilyPondLexer())
