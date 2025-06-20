from functions.run_python import run_python_file

def test():
    print("Testing run_python_file.py...")
    
    result = run_python_file("calculator", "main.py", "3 + 5")
    print("Result of running main.py...")
    print(result)

    result = run_python_file("calculator", "tests.py")
    print("Result of running tests.py...")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print("Result of running ../main.py...")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    print("Result of running nonexistent.py...")
    print(result)

    result = run_python_file("calculator", "lorem.txt")
    print("Result of running lorem.txt...")
    print(result)

if __name__ == "__main__":
    test()