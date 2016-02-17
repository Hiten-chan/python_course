try:
    foo()
except AssertionError:
    print('Caught AssertionError')
except MemoryError:
    print('Caught MemoryError')
except RuntimeError:
    print('Caught RuntimeError')
