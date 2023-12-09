from inspect import stack
from constants_dict import constants


def generate_constants(constants: dict, path: str = "") -> None:
    if path == "":
        stack_list: list = stack()
        calling_frame = stack_list[len(stack_list) - 1]
        filename:str = calling_frame[0].f_code.co_filename
        filename = filename.replace("\\", "/")
        filename = filename[::-1]
        filename = filename[filename.find("/"):]    
        filename = filename[::-1]
        filename += "constants.py"
        path = filename
    
    constants_file = open(path, "w") 
    constant_count: int = 0
    constants_list: str
    
    # special_notification = "Easter_Egg"
    # constants_file.write("# Special Notification\n")
    # constants_file.write(f"{special_notification.upper()} = {constant_count}\n")
    
    for constants_list in constants:
        if constant_count >= 1:
            constants_file.write(f"\n# {constants_list}\n")
        
        else:
            constants_file.write(f"# {constants_list}\n")
            
        constant: str
        for constant in constants[constants_list]:
            constant = constant.upper()
            if len(constants_list.split(" ")) == 2:
                constants_file.write(
                    f"{constants_list.split()[1][:-1].upper()}_{constant}: int = {constant_count}\n")
            
            else:
                constants_file.write(f"{constant}: int = {constant_count}\n")
            
            constant_count += 1
            
    constants_file.close()

def main():
    generate_constants(constants)
    print("DONE")

if __name__ == "__main__":
    main()