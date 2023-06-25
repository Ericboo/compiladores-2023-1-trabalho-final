from lexico import LexicalAnalyzer
from sintatico import Parser
from tradutor import translate_to_python


source_code = """
    fun getSum(a, b) {
      return a + b;
      var x = 1;
    }

    var sum = getSum(4, 5);

    if(sum > 10) {
    print "yes";
    } else if(sum > 20) {
    print "maybe";
    } else {
    print "no";
    }

    """

tokens = LexicalAnalyzer(source_code)
parser = Parser(tokens)
code = parser.parse()
print(code)
print(translate_to_python(code))


