#!/usr/bin/python3
import sys
processing = __import__('1-batch_processing')

try:
    processing.batch_processing(50)
except BrokenPipeError:
    sys.stderr.close()
