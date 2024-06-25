import random


def main():
    level=get_level()
    score=0
    problems_count=10
    for _ in range(problems_count):
        x=generate_integer(level)
        y=generate_integer(level)
        attempts = 3
        correct_answer=x+y
        while attempts>0:
            answer_input = input(f"{x} + {y} = ")
            try:
                if int(answer_input)==correct_answer:
                    score+=1
                    print("correct!")
                    break
                else:
                    print("EEE")
                    attempts-=1
            except ValueError:
                print("EEE")
            attempts-=1
        if attempts == 0:
            print(f"{x}+{y}={correct_answer}")
    print(f"{score}")



def get_level():
    while True:
        level=input("Level: ")
        if level in ['1','2','3']:
            return int(level)
        else:
            print("Please enter a valid level (1,2, or 3).")




def generate_integer(level):
    if level not in [1,2,3]:
        raise ValueError("level must be 1, 2, or 3")
    if level ==1:
        return random.randint(0,9)
    elif level ==2:
        return random.randint(10,99)
    elif level ==3:
        return random.randint(100,999)




if __name__ == "__main__":
    main()
