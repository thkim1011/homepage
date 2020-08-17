import argparse
import os
import sys
from homepage.render import JinjaRenderer, MarkdownRenderer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source_dir", type=str, required=True)
    parser.add_argument("--output_dir", type=str, required=True)
    params = vars(parser.parse_args())

    source_dir = params["source_dir"]
    output_dir = params["output_dir"]

    if not os.path.isdir(source_dir) or not os.path.isdir(output_dir):
        print("Source or output directory does not exist")
        sys.exit(1)

    JinjaRenderer(source_dir, output_dir).render()

if __name__ == "__main__":
    main()
