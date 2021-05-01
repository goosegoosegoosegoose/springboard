"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, file):
        """
        Attributes
        -----------

        file: Text file to be read
        """
        
        lst = open(file)
        self.list = self.parse(lst)
        self.count_words()

    def parse(self, lst):
        return [word.strip() for word in lst]

    def count_words(self):
        """
        Make text file contents a list by line
        """

        print(f'{len(self.list)} words read')

    def random(self):
        """
        Return a random word inside list
        """

        return random.choice(self.list).rstrip()


class SpecialWordFinder(WordFinder):
    """
    Subclass of Wordfinder that does not return blank lines

    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def parse(self, lst):
        """
        use parse def name and make a list that doesn't include falsy elements
        """
        return [i.strip() for i in lst if i.strip() and not i.startswith("#")]

    
    


    #learn about parsing
    # return already inside brackets to make list, don't have to have empty list like in java remember that
    # if w.strip() means if w.strip() is truthy
    # and is &&
    # not is !=
    # startswith seems like a good method, only for strings returns boolean

# writing my own doctest is weird

#use strip() to remove newline from read string lines and for loop to iterate them into a list

# 2nd class doesn't need new init since its not changing any variables instance wise? ask question

# classes still confuse me as expected with contructors and instanced objects