from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
import os

def generate_launch_description():
    json_name = "test.json"

    # Declare launch arguments
    address_arg = DeclareLaunchArgument(
        'address',
        default_value="192.168.1.17",
        description='IP address of the mocap system'
    )
    json_file_arg = DeclareLaunchArgument(
        'json_file_name',
        default_value=json_name,  
        description='Path to the JSON file'
    )
    body_to_track_arg = DeclareLaunchArgument(
        'body_to_track',
        default_value="2",
        description='ID of the body to track'
    )

    # Use LaunchConfiguration to fetch argument values
    address = LaunchConfiguration('address')
    json_file = LaunchConfiguration('json_file_name')
    body_to_track = LaunchConfiguration('body_to_track')


    # MoCap Node with remapping
    phasespace_node = Node(
        package='phasespace_client',
        executable='phasespace_client_node',
        name='phasespace_client_node',
        output='screen',
        parameters=[{
            'address': address,
            'json_file': json_file,
            'body_to_track': body_to_track
        }],
        
    )

    return LaunchDescription([
        address_arg,
        json_file_arg,
        body_to_track_arg,
        phasespace_node
    ])
