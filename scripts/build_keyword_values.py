#!/usr/bin/env python

"""Script to build a keyword popularity dictionary using a list of TMDB id's and the TMDB API
"""

from __future__ import print_function
import os
import sys
import argparse
import requests 
import pandas as pd

def main(arguments):
    
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="File path of TMDB ID's", type=str)
    parser.add_argument('outfile', help="File path to save result", type=str)

    args = parser.parse_args(arguments)

    path_to_movie_title_csv = args.infile
    path_to_write_result = args.outfile

    print("Infile: {}, Outfile: {}".format(path_to_movie_title_csv, path_to_write_result))

    # we need a list of movie titles to use
    movie_titles = pd.read_csv(path_to_movie_title_csv)
    # movie_titles = movie_titles
    # go through the list

        # run through the keywords for the title
        # if not in the dict, add it and set value to 1
        # else if its in the dict, increment the value
        # at the end print out a dict 




if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))