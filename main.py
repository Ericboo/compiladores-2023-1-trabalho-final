from lexico import LexicalAnalyzer
from sintatico import Parser

source_code = """
    // Programa de exemplo 4
var x = true;
var y = 100;

if(10 > y or x) {
  print "1";
} else {
  if(10 < y and !x) {
    print "2";
  } else {
    print "3";
  }
}
"""

tokens = LexicalAnalyzer(source_code)
parser = Parser(tokens)
print(parser.parse())


