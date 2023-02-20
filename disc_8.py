import re
import os
import unittest

def read_file(filename):
    """ Return a list of the lines in the file with the passed filename """
    
    # Open the file and get the file object
    source_dir = os.path.dirname(__file__) #<-- directory name
    full_path = os.path.join(source_dir, filename)
    infile = open(full_path,'r', encoding='utf-8')
    
    # Read the lines from the file object into a list
    lines = infile.readlines()
    
    # Close the file object
    infile.close()
    
    # return the list of lines
    return lines

def find_num_words(string_list):
    """ Return a list of words that contain three-digit numbers in the middle. """

    # initialize an empty list

    # define the regular expression

    # loop through each line of the string list 

    # find all the words that match the regular expression in each line
    
    # loop through the found words and add the words to your list 

    # return the list

    pass


def find_days(string_list):
    """ 
    Return a list of days from the list of strings
    The dates in the text are formatted as: MM/DD/YYYY
    Note: The month and date can one or two digits (ie: 01 or 1)
    """  

    # initialize an empty list

    # define the regular expression

    # loop through each line of the string list
    
    # find all the dates that match the regular expression in each line
    
    # loop through the found dates and only add the days to your list 
    
    #return the list of days
    pass

def find_domains(string_list):
    """ 
    Return a list of web address domains from the list of strings. 
    The web address may or may not have a www. and the protocol can either be http or https
    Example output: ['si.umich.edu', 'google.com']
    """

    # initialize an empty list

    # define the regular expression

    # loop through each line of the string list

    # find all the domains that match the regular expression in each line

    # loop through the found domains

    # get the domain name by pulling out the part of the string after the '//'
    # you'll also have to strip the 'www.' from domains where applicable

    # add the domains to your  list
    
    #return the list of domains
    pass

class TestAllMethods(unittest.TestCase):

    def setUp(self):
        self.string_list = read_file('alice_ch_1.txt')
        self.word_list = find_num_words(self.string_list)
        self.days_list = find_days(self.string_list)
        self.domain_list = find_domains(self.string_list)

    def test_find_num_words(self):
        # read the lines from the file into a list of strings
        self.assertEqual(len(self.word_list),4)

        test_list = ['for tes123t', 'for test123 t456est', 'number 123' ]
        self.assertEqual(find_num_words(test_list), ['tes123t', 't456est'])
    
    
    def test_find_days(self):
        # read the lines from the file into a list of strings
        self.assertEqual(self.days_list,['23', '12', '31', '4', '1', '4'])

        test_list = ['test date 3/1/2020', 'test another date: 12/30/2000']
        self.assertEqual(find_days(test_list), ['1', '30'])
    

    def test_domains(self):
        # read the lines from the file into a list of strings
        self.assertEqual(self.domain_list,['pythex.org', 'si.umich.edu', 'sabapivot.com', 'stars.chromeexperiments.com', 'theofficestaremachine.com', 'regex101.com'])

        test_list = ['test domain https://runestone.academy', 'test another domain: https://www.stackoverflow.com']
        self.assertEqual(find_domains(test_list), ['runestone.academy', 'stackoverflow.com'])



def main():
	# Use main to test your function. 
    # Run unit tests, but feel free to run any additional functions you need
	unittest.main(verbosity = 2)

if __name__ == "__main__":
	main()