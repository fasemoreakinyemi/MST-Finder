#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import os
import sys
import argparse
from Bio.Blast.Applications import NcbiblastnCommandline

parser = argparse.ArgumentParser()
parser.add_argument("-q", "--query_sequence", help="Path to query sequence")
parser.add_argument("-o", "--output_name", help="Name of output file")
parser.add_argument("-d", "--db_directory", help="Path to MST database files")
parser.add_argument("-mt", "--mst_type", nargs='+', help="MST type to predict")
args = parser.parse_args()

if os.path.exists(args.db_directory):
    for i in range(1, 31):
        db_file = "mst" + str(i) + ".fasta"
        if not os.path.isfile(args.db_directory/db_file):
            print("Missing database file {}".format(db_file))
else:
    print("{} is not a valid database directory".format(args.db_directory))
    sys.exit()

mst_type = args.mst_type
tmp_path = "tmp"
os.mkdir(tmp_path)
if "".join(mst_type) == "all":
    for i in range(1, 31):
        db_file = "mst" + str(i) + ".fasta"
        tmp_out = "mst" + str(i) + ".tab"
        if not os.path.isfile(args.db_directory/db_file):
            print("Missing database file {}".format(db_file))
            sys.exit()
        else:
            query = NcbiblastnCommandline(query=args.query_sequence, 
                                          db=args.db_directory/db_file,
                                          evalue=0.001,
                                          outfmt=6,
                                          out=tmp_path/tmp_out,
                                          ungapped=True)
else:
    for i in mst_type:
        if int(i) not in list(range(1,31)):
            print("Invalid argument MST type {}".format(i))
        else:
            db_file = "mst" + str(i) + ".fasta"
            tmp_out = "mst" + str(i) + ".tab"
            if not os.path.isfile(args.db_directory/db_file):
                print("Missing database file {}".format(db_file))
                sys.exit()
            else:
                query = NcbiblastnCommandline(query=args.query_sequence, 
                                              db=args.db_directory/db_file, 
                                              evalue=0.001,
                                              outfmt=6,
                                              out=tmp_path/tmp_out,
                                              ungapped=True)






