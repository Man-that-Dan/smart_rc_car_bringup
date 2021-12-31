import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    config = os.path.join(
        get_package_share_directory('raspicam2'),
        'cfg',
        'params.yaml'
        )
    return LaunchDescription([
        Node(
            package='raspicam2',
            executable='raspicam2_node',
            name='raspicam2',
            parameters=[config]
        ),
        Node(
            package='smart_rc_car',
            namespace='smart_rc_car',
            executable='lane_detector',
            name='lane_detector'
        ),
        Node(
            package='xtrc_llc',
            namespace='xtrc_llc',
            executable='xtrc_controller',
            name='driver'
        ),
        Node(
            package='smart_rc_car',
            executable='dk_control',
            name='dk_control',
            remappings=[
                ('/dk_control/cmd_vel', '/cmd_vel')
            ]
        )
    ])