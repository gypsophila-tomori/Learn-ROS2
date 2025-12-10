from demo_python_pkg.person_node import PersonNode

class WriterNode(PersonNode):
    def __init__(self, name:str, age:int, book:str) -> None:
        super().__init__(name, age)
        print("WriterNode init 方法被调用了")
        self.book = book

def main():
    node = WriterNode("tomori", 18, "Learn ROS2")
    node.eat("苹果")