import argparse
import string
from datetime import date


class Phrases:
    def __init__(self):
        self.version = '1.0.0'

        # Let's parse some CLI options
        parser = argparse.ArgumentParser()
        parser.add_argument('-o', '--outfile', help='Output file')
        parser.add_argument('-w', '--words', help='Number of words for each row', default=4, type=int)
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
        # Try to touch the output file. If anything goes wrong, let's make the exception bubble up
        with open(self.args.outfile, 'ab') as handle:
            pass

    def run(self):
        self.banner()

        # Perform some sanity checks
        try:
            self.checkenv()
        except Exception as error:
            print '[!]' + error.message
            return

        previous_data = ''
        output_handle = open(self.args.outfile, 'ab')
        out_buffer = []
        read = 0

        while True:
            read += 64
            data = self.args.text.read(1024 * 64)

            print "[*] Read %d Kb" % read

            if not data:
                print "[*] EOF reached"

                if len(out_buffer):
                    output_handle.write('\n'.join(out_buffer))

                output_handle.close()

                break

            # Remove any newlines
            data = data.replace("\r", "")
            data = data.replace("\n", " ")

            # Remove any extra space
            while '  ' in data:
                data = data.replace('  ', ' ')

            # Do I have any leftover from previous iterations?
            if previous_data:
                data = previous_data + data
                previous_data = ''

            chars = list(data)

            # Initialise some flags that will be used during the loop
            start = None
            spaces = 0
            phrase = ''
            i = 0

            # Ok, let's iterate over the string one char at time
            while i < len(chars):
                cur_char = chars[i]
                i += 1

                # Did we hit a space? If so let's
                if cur_char == ' ':
                    spaces += 1

                    # If I don't have a "start" mark, let's save it now
                    if not start:
                        start = i

                elif cur_char not in (string.ascii_letters + string.digits):
                    # Not a alphanum char? Let's skip it
                    continue

                # Got enough words? So let's get back to the last space we detected
                if spaces >= self.args.words:
                    out_buffer.append(phrase)

                    if len(out_buffer) >= 500:
                        output_handle.write('\n'.join(out_buffer))
                        out_buffer = []

                    # Reset all the flags for the next iteration
                    spaces = 0
                    phrase = ''
                    i = start
                    start = None

                    continue

                phrase += cur_char

            if phrase:
                previous_data = phrase


try:
    obj = Phrases()
    obj.run()
except KeyboardInterrupt:
    print("Operation aborted")
