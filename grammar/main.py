from UMLParserEntry import UMLParserEntry
import sys

def main(argv):
    """Main method calling a single debugger for an input script"""
    parser = UMLParserEntry()
    parser.parse(argv)

if __name__ == '__main__':
    main(sys.argv)