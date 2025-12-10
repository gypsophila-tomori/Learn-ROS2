import rclpy
from rclpy.node import Node

class PersonNode(Node):
    def __init__(self, node_name:str, name:str, age:int) -> None:
        super().__init__(node_name)
        print("PersonNode init 方法被调用了")
        self.name = name
        self.age = age

    def eat(self, food_name:str):
        self.get_logger().info(f"我叫{self.name}，我今年{self.age}岁，我正在吃{food_name}")

def main():
    rclpy.init()
    node = PersonNode("person_node", "tomori", 18)
    node.eat("苹果")
    rclpy.spin(node)
    rclpy.shutdown()