import argparse
from datetime import date


class Phrases:
    def __init__(self):
        self.version = '1.0.0'

        # Let's parse some CLI options
        parser = argparse.ArgumentParser()
        parser.add_argument('-o', '--outfile', help='Output file')
        parser.add_argument('-w', '--words', help='Number of words for each row', default=4)
        parser.add_argument('text', help='Original text from where we should create the phrases',
                            type=argparse.FileType('r'))

        self.args = parser.parse_args()

        if not self.args.outfile:
            self.args.outfile = 'phrases.txt'

    def banner(self):
        print("Phrases " + self.version + " - Short story long...")
        print("Copyright (C) " + str(date.today().year) + " FabbricaBinaria - Davide Tampellini")
        print("===============================================================================")
        print("Phrases is Free Software, distributed under the terms of the GNU General")
        print("Public License version 3 or, at your option, any later version.")
        print("This program comes with ABSOLUTELY NO WARRANTY as per sections 15 & 16 of the")
        print("license. See http://www.gnu.org/licenses/gpl-3.0.html for details.")
        print("===============================================================================")

    def checkenv(self):
        pass

    def run(self):
        self.banner()

        # Perform some sanity checks
        try:
            self.checkenv()
        except Exception as error:
            print error
            return

        while True:
            data = self.args.text.read(1024 * 64)

            if not data:
                print "[*] EOF reached"
                break

            # Remove any newlines
            data = data.replace("\r", "")
            data = data.replace("\n", " ")

            # Remove any extra space
            while '  ' in data:
                data = data.replace('  ', ' ')

            longest = ''
            i = 0
            for char in data:
                if i == self.args.words:
                    break

                # Let's get the longest string for the current position
                if char == ' ':
                    i += 1
                else:
                    longest += char

try:
    obj = Phrases()
    obj.run()
except KeyboardInterrupt:
    print("Operation aborted")
