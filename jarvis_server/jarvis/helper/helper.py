import logging as log


_WORD_TO_NUM = {
   "one":   1,
   "on":    1,
   "two":   2,
   "to":    2,
   "toe":   2,
   "three": 3,
   "four":  4,
   "for":   4,
   "five":  5,
   "six":   6,
   "seven": 7,
   "eight": 8,
   "nine":  9,
   "nein":  9,
   "ten":  10,
}

def word_to_num( word ):
   try:
      return _WORD_TO_NUM[ word ]
   except:
      log.info( f"Helper Word2Num: \"{word}\" not found." )
      return None


def is_int( word ):
   try:
      int(word)
      return True
   except:
      return False
