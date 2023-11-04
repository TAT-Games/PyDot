
def singleton(cls):
    instances = {}
    
    def get_instance(*args, **kwargs):
        print(*args, **kwargs)
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        
        return instances[cls]
    
    return get_instance()


def main():
    pass


if __name__ == "__main__":
    main()