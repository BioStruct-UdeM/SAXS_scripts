#!/usr/bin/env python3
# -*- coding: utf8 -*-

'''
- Author: Normand Cyr
- Email: normand.cyr@umontreal.ca
- Description: Script to strip the first row of the CSV file provided by the SAXS user, which contains headers to facilitate readability, but that cannot be parsed by the operating software of the SAXS system.

- Notes: Probably unnecessarily complex.
'''

import csv
import argparse

def parse_arguments():

    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True, help="input filename")
    ap.add_argument("-o", "--output", required=True, help="output filename")
    args = vars(ap.parse_args())

    return(args)

def parse_csv(args):

    csv_data_in = []
    with open(args['input'], 'r') as csvfile_in:
        csv_data = csv.reader(csvfile_in, delimiter = ',')
        for row in csv_data:
            csv_data_in.append(row)

    return(csv_data_in)

def save_csv(args, csv_data_in):

    with open(args['output'], 'w') as csvfile_out:
        csv_data_out = csv.writer(csvfile_out, delimiter = ',')
        for row in csv_data_in[1:]:
            csv_data_out.writerow(row)

    return(csv_data_out)

def main():

    args = parse_arguments()

    csv_data_in = parse_csv(args)

    print('Reading the file "{}" and stripping the header line.\n'.format(args['input']))

    csv_data_out = save_csv(args, csv_data_in)

    print('Writing the file "{}" with the appropriate format for the SAXS system.\n'.format(args['output']))

    print('Done.\n')
    
if __name__ == '__main__':
    main()
