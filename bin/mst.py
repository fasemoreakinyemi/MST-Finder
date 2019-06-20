#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import os
import argparse
from Bio.Blast.Applications import NcbiblastnCommandline

parser = argparse.ArgumentParser()
parser.add_argument("--q", "--query_sequence")
parser.add_argument("--o", "--output_name")
parser.add_argument("--d", "--db_directory")


