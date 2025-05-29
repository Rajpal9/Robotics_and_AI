import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('turltsim_move_publisher')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.move_cmd_callback)
        self.i = 0

    def move_cmd_callback(self):
        """
        Callback function.
        """
        # Twist is geometry_msgs for linear and angular velocity 
        move_cmd = Twist() 
        # Linear speed in x in meters/second is + (forward) or 
        #    - (backwards) 
        move_cmd.linear.x = 0.3   # Modify this value to change speed 
        # Turn at 0 radians/s 
        move_cmd.angular.z = 0.3
        self.publisher_.publish(move_cmd)

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()
    try:
        rclpy.spin(minimal_publisher)
        
    except KeyboardInterrupt:
        print("KeyboardInterrupt: Move Command Publisher Thread\n")

    except Exception as e:
        print(f"Unexpected error: Move Command Publisher Thread: {e}\n")

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()

    # Shutdown ROS client library if not already shut down
    if rclpy.ok():  # Check if the context is still active
        rclpy.shutdown()


if __name__ == '__main__':
    main()