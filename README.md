# Phrases generator
How can we create password candidates for passphrases?  
Well, [we can scrape Twitter](https://github.com/tampe125/hashtag-scraper) to harvest some slang words, but what if the user was using quotes from a text (a book or a movie)?  
For example, what if the user chose a password like this:  
`godcreatedtheheaven`

20 chars are simply too many for a brute-force attempt. What if we start to create phrases containing N words, based on a specific text?  
For example, using a wordlist based on the Bible and with phrases containing from 4 to 7 words lead to these craked passwords:
```
25 withhisstripeswearehealed
23 amnotashamedofthegospel
22 rejoiceinthelordalways
21 wonderswithoutnumbers
20 theearthisthelords11
20 lordofheavenandearth
20 fearnotiwillhelpthee
20 andthewordwaswithgod
19 onehourwiththebeast
19 hardennotyourhearts
```

### Requirements
No external libraries are required.

### Usage
`python phrases.py [OPTIONS] original_file.txt`  
The script will start to crawl the original text and output phrases with the selected amount of words, one per line.  
For example, running the following command on the Bible, will produce something like this:
```
python phrases.py -w 4 -o bible4words.txt bible.txt

In the beginning God
the beginning God created
beginning God created the
God created the heaven
created the heaven and
the heaven and the
heaven and the earth
```
From this base text, you can tweak the final output using Hashcat rules.

### Options
Phrases Generator has some options for fine tuning:
```
-o OUTFILE --outfile OUTFILE  Output file (default to phrases.txt)
-w WORDS   --words   WORDS    Number of words for each row (default to 4)
```

### Bug report
Feel free to open an issue and, if confirmed, create a Pull Request!
