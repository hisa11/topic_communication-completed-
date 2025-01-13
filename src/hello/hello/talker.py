import rclpy
from hello_interfaces.msg import MyString
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy
from pyPS4Controller.controller import Controller
import os
import subprocess
class MyController(Controller, Node):
  def __init__(self, **kwargs):
    Controller.__init__(self, **kwargs)
    Node.__init__(self, 'ps4_controller_node')
    qos_profile = QoSProfile(depth=10, reliability=ReliabilityPolicy.RELIABLE)
    self.publisher_ = self.create_publisher(MyString, 'chatter', qos_profile)
    self.timer = self.create_timer(0.02, self.timer_callback)  # 20msごとにコールバック

  def timer_callback(self):
    self.listen(timeout=5)

  def on_circle_press(self):  # ●off
    msg = MyString()
    msg.data = "circle"
    for _ in range(3):
      self.publisher_.publish(msg)
    self.get_logger().info("Published: " + msg.data)

  def on_x_release(self):  # :x_黒太字:off
    msg = MyString()
    msg.data = "croOFF"
    for _ in range(3):
      self.publisher_.publish(msg)
    self.get_logger().info("Published: " + msg.data)

  def on_square_press(self):  # ■on
    msg = MyString()
    msg.data = "squareON"
    for _ in range(3):
      self.publisher_.publish(msg)
    self.get_logger().info("Published: " + msg.data)

  def on_square_release(self):  # ■off
    msg = MyString()
    msg.data = "squareOFF"
    for _ in range(3):
      self.publisher_.publish(msg)
    self.get_logger().info("Published: " + msg.data)

  def on_circle_release(self):  # ●on
    msg = MyString()
    msg.data = "circOFF"
    for _ in range(3):
      self.publisher_.publish(msg)
    self.get_logger().info("Published: " + msg.data)

  def on_x_press(self):  # :x_黒太字:on
    msg = MyString()
    msg.data = "cross"
    for _ in range(3):
      self.publisher_.publish(msg)
    self.get_logger().info("Published: " + msg.data)

  def on_triangle_press(self):  # ▲on
    msg = MyString()
    msg.data = "triangleON"
    for _ in range(3):
      self.publisher_.publish(msg)
    self.get_logger().info("Published: " + msg.data)

  def on_triangle_release(self):  # ▲off
    msg = MyString()
    msg.data = "triangleOFF"
    for _ in range(3):
      self.publisher_.publish(msg)
    self.get_logger().info("Published: " + msg.data)
  # ジャンプ機構

  def on_L1_press(self):  # L1on
    msg = MyString()
    msg.data = "L1ON"
    for _ in range(3):
      self.publisher_.publish(msg)
    self.get_logger().info("Published: " + msg.data)

  def on_L1_release(self):  # L1off
    msg = MyString()
    msg.data = "L1OFF"
    for _ in range(3):
      self.publisher_.publish(msg)
    self.get_logger().info("Published: " + msg.data)

  def on_R1_press(self):  # R1on
    msg = MyString()
    msg.data = "R1ON"
    for _ in range(3):
      self.publisher_.publish(msg)
    self.get_logger().info("Published: " + msg.data)

  def on_R1_release(self):  # R1off
    msg = MyString()
    msg.data = "R1OFF"
    for _ in range(3):
      self.publisher_.publish(msg)
    self.get_logger().info("Published: " + msg.data)
def main(args=None):
  rclpy.init(args=args)
  controller = MyController(interface="/dev/input/js0",
                            connecting_using_ds4drv=False)
  rclpy.spin(controller)  # コントローラーとROS2ノードを同時に実行
  # コントローラが停止したら、ノードを破棄してROS通信をシャットダウンする
  controller.destroy_node()
  rclpy.shutdown()
if __name__ == "__main__":
  main()
