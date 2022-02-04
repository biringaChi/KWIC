'''
Original Author:
    Alexander J. Moulton
    Github: @moul-10

Second Author:
    Grady Landers
    Github: @GradXL49

Usage:
    circ_shift = CircularShifter()
    list_of_shifted_strings = circ_shift.shift("This is my input string")
'''


class CircularShifter:

    # variable for holding 'dictionary' of uninteresting words
    blacklist = ["a", "an", "the", "for", "and", "nor", "but", "or", "yet", "so", "aboard", "about", "above", "across",
                 "after", "against", "along", "amid", "among", "anti", "around", "as", "at", "before", "behind",
                 "below", "beneath", "beside", "besides", "between", "beyond", "but", "by", "concerning", "considering",
                 "despite", "down", "during", "except", "excepting", "excluding", "following", "for", "from", "in",
                 "inside", "into", "like", "minus", "near", "of", "off", "on", "onto", "opposite", "outside", "over",
                 "past", "per", "plus", "regarding", "round", "save", "since", "than", "through", "to", "toward",
                 "towards", "under", "underneath", "unlike", "until", "up", "upon", "versus", "via", "with", "within",
                 "without"]

    # Only used to keep Object-Oriented, no attributes needed
    # This could be made static by removing class def
    def __init__(self):
        pass

    # Input string, output a list of indexes where a circular shift could start
    def shift(self, line):
        # initialize output
        out = []

        # split line into words, then loop through to do calculation
        words = line.split()
        i = 0
        for word in words:
            if self.interesting(word):
                out.append(i)
            i += 1

        # return result
        return out

    # Input string, return whether it is an interesting word as boolean
    def interesting(self, word):
        return word.lower() not in self.blacklist
