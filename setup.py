from setuptools import find_packages, setup

package_name = 'unity_lidar_transformer'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='alianlbj23',
    maintainer_email='alianlbj23@gmail.com',
    description='This is a simple ROS2 node that republishes Lidar scan messages with an updated timestamp. It listens to Lidar scan messages on the `/scan_tmp` topic, updates the timestamp of the message, and republishes it to the `/scan` topic.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'lidar_transformer_node = unity_lidar_transformer.lidar_transformer_node:main'
        ],
    },
)
