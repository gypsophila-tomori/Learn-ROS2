class PersonNode:
    def __init__(self, name:str, age:int) -> None:
        print("PersonNode init 方法被调用了")
        self.name = name
        self.age = age
    
    def eat(self, food_name:str):
        print(f"我叫{self.name}，我今年{self.age}岁，我正在吃{food_name}")


def main():
    node = PersonNode("tomori", 18)
    node.eat("苹果")

if __name__ == "__main__":
    main()