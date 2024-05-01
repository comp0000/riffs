#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Extract embedded MIDI data from a GarageBand loop AIF
and write it to a .MID file.

NB, this is a very basic script that can only handle
a single file with minimal error handling. Improving
file management is left as an exercise for the reader.
"""

import sys, os, os.path
import argparse

def extract_midi ( filename ):
    """
    Extract a new MIDI file from the specified loop AIF.
    If MIDI segment can't be found, this does nothing.
    Otherwise it is written out to a new file with the
    same base name as the original but extension changed to
    '.mid'.
    """
    with open(filename, 'rb') as ff:
        data = ff.read()
    
    start = data.find(b'MThd')
    if start >= 0:
        end = data.find(b'CHS') + 3
    
        midi = data[start:end]
        name = os.path.splitext(filename)[0] + '.mid'
        print(f'writing {len(midi)} bytes to {name}')
        
        with open(name, 'wb') as ff:
            ff.write(midi)
    else:
        print(f'no MIDI data found in {filename}')
    

def process_args():
    """
    Set up command line arguments. This is trivial here, but
    broken out for easy expansion later.
    """
    ap = argparse.ArgumentParser(description='Extract MIDI from a GarageBand loop AIF')
    ap.add_argument('file', help='input AIF file')
    return ap.parse_args()

if __name__ == '__main__':
    args = process_args()
    extract_midi(args.file)
