# Standard library imports
import os
import sys

# Constants

def parse_ref(current_ref):
    if not current_ref.startswith("ref/tags/"):
        raise Exception(f"Invalid ref `{current_ref}`!")

    tag_name = current_ref.replace("ref/tags/", "")
    sys.stdout.write(f'{tag_name}')


if __name__ == "__main__":
    current_ref = os.environ.get("GITHUB_REF")
    parse_ref(current_ref)
