import stdlib

def testgood(name):
    print(f"'{name}': {getattr(stdlib, name)}")

def testbad(name):
    try:
        getattr(stdlib, name)
    except AttributeError as e:
        print(f'AttributeError: {e}')
    else:
        assert False

# Normal imports
testgood('argv')

# Builtins
testgood('dict')

# Deeply nested
testgood('ThreadPoolExecutor')

# Weird
testgood('__import__')

# Modules
testgood('futures')

# Special case renaming
testgood('ETree')

# Typo
testbad('ZipFil')

# Ambiguous
testbad('loads')
testbad('Future')

