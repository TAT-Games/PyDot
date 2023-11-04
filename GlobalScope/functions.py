from pygame import Color
from inspect import currentframe, stack, getmodule

def printErr(error: str, ErrorType: str = "ERROR", help: str = ""):
    """Print an error to the terminal"""
    stack_list: list = stack()
    caller_line = currentframe().f_back.f_lineno
    caller_frame = stack_list[1]
    filename = caller_frame[0].f_code.co_filename
    
    line = caller_line
    
    if len(stack_list) >= 3:
        calling_frame = stack_list[2]
        calling_function_line = calling_frame[0].f_lineno
        line = calling_function_line
    
    
    print(f"\n{ErrorType}: {error}")
    print(f"Source: Line {line} in \"{filename}\"")
    if help != "":
        print(f"Help: {help}")
    
    print("\n")
    quit()
