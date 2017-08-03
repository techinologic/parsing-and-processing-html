# Example parsing and processing HTML

from HTMLParser import HTMLParser
metacount = 0;
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):

    #function to handle openning tag in the doc
    # this will be called when the closing ">" of the tag is reached
    def handle_starttag(self, tag, attrs):
        pos = self.getpos()
        print "At line: ", pos[0], " position ", pos[1]
        if attrs.__len__ > 0:
            print "\tAttributes:"
            for a in attrs:
                print "\t", a[0], "=", a[1]

    # method to handle the processing of HTML comments
    def handle_endtag(self, tag):
        print "Encountered an end tag:", tag
        pos = self.getpos()
        print "At line: ", pos[0], " position ", pos[1]

    # function to handle character and text data (tag contents)
    def handle_comment(self, data):
        print "Encountered comment: ", data
        pos = self.getpos()
        print "At line: ", pos[0], " position ", pos[1]

def main():
    #instantiate the parser and feed it HTML
    parser = MyHTMLParser()

    # open the sample HTML file and read it
    f = open("samplehtml.html")

    if f.mode == "r":
        contents = f.read() # read entire file
        parser.feed(contents)

if __name__ == '__main__':
    main()