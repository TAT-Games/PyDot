from pygame import Color
from inspect import currentframe, stack

def printErr(error: str, ErrorType: str = "ERROR", help: str = "", print_source: bool = True) -> None:
    """Print an error to the terminal"""
    stack_list: list = stack()
    calling_function_line = currentframe().f_back.f_lineno
    calling_frame = stack_list[len(stack_list) - 1]
    calling_function_filename = calling_frame[0].f_code.co_filename

    print(f"\n{ErrorType}: {error}")
    if print_source:
        print(f"Source: Line {calling_function_line} in \"{calling_function_filename}\"")
        
    if help != "":
        print(f"Help: {help}")
    
    print("\n")
    quit()

