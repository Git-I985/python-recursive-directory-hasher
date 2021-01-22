import argparse

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to folder")
    parser.add_argument("--table", action="store_true", help="print table in console")
    return parser.parse_args()