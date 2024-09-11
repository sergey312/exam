import sys
from io import StringIO


class File:
    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def my_decorator(self, func):
        def wrapper(*args, **kwargs):
            old_stdout = sys.stdout
            new_stdout = StringIO()
            sys.stdout = new_stdout

            try:
                result = func(*args, **kwargs)
            finally:

                sys.stdout = old_stdout

            with open(self.file_path, 'a', encoding='utf-8') as f:
                f.write(new_stdout.getvalue())
            return result
        return wrapper
