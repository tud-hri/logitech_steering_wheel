from setuptools import setup

setup(
    name='logitech_steering_wheel',
    version='1.0',
    packages=['logitech_steering_wheel'],
    url='',
    license='',
    author='O. Siebinga',
    author_email='o.siebinga@tudelft.nl',
    description='',
    data_files=[(
        'lib\\site-packages\\logitech_steering_wheel\\lib\\x64', [".\\lib\\x64\\LogitechSteeringWheelEnginesWrapper.dll"]),(
        'lib\\site-packages\\logitech_steering_wheel\\lib\\x86', [".\\lib\\x86\\LogitechSteeringWheelEnginesWrapper.dll"]
    )]
)
