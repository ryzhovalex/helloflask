import os


def get_abs_path(rel_path: str) -> str:
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, rel_path)