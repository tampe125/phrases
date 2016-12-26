import argparse
from datetime import date


class Phrases:
    def __init__(self):
        self.version = '1.0.0'

        # Let's parse some CLI options
        parser = argparse.ArgumentParser()
        parser.add_argument('-o', '--outfile', help='Output file')
        parser.add_argument('-w', '--words', help='Number of words for each row', default=4)

        arguments = parser.parse_args()

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

try:
    obj = Phrases()
    obj.run()
except KeyboardInterrupt:
    print("Operation aborted")
