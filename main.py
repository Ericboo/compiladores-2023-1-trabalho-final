from lexico import LexicalAnalyzer
from sintatico import Parser
from tradutor import translate_to_python


source_code = """
    fun a1(a) { return a*2; }
    fun a2(b) { return a/2; }

    print a1(4) * a2(10); print a2(5) / a1(50);
    var c = nil;
    if(a1(4) > 5) { print "ok"; }
    c = 40; print c;

    """

tokens = LexicalAnalyzer(source_code)
parser = Parser(tokens)
code = parser.parse()
#print(code)
print(translate_to_python(code))


