import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class KeyboardHRI(Node):

    def __init__(self):

        super().__init__('keyboard_hri')

        self.publisher = self.create_publisher(
            String,
            '/mission_command',
            10
        )

        self.get_logger().info(
            'Keyboard HRI started.'
        )

        self.get_logger().info(
            'Commands: START, STOP, RESET, QUIT'
        )

    def send_command(self, command):

        message = String()
        message.data = command

        self.publisher.publish(message)

        self.get_logger().info(
            f'Sent command: {command}'
        )


def main(args=None):

    rclpy.init(args=args)

    node = KeyboardHRI()

    print()
    print('======================================')
    print(' Warehouse Robot Keyboard HRI')
    print('======================================')
    print('START - Start mission')
    print('STOP  - Stop mission')
    print('RESET - Reset mission')
    print('QUIT  - Exit HRI')
    print('======================================')

    try:

        while rclpy.ok():

            command = input(
                'Enter command: '
            ).strip().upper()

            if command in [
                'START',
                'STOP',
                'RESET'
            ]:

                node.send_command(command)
                rclpy.spin_once(node, timeout_sec=0.1)

            elif command == 'QUIT':

                break

            else:

                print(
                    'Invalid command. '
                    'Use START, STOP, RESET or QUIT.'
                )

    except KeyboardInterrupt:
        pass

    finally:

        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()