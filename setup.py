from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='logitech_steering_wheel',
    version='1.0',
    packages=['logitech_steering_wheel'],
    license='MIT License',
    author='O. Siebinga',
    author_email='o.siebinga@tudelft.nl',
    description='A wrapper to use the Logitech Steering Wheel SDK in Python',
    long_description=long_description,
    url="https://github.com/tud-hri/logitech_steering_wheel",
    project_urls={
        "Bug Tracker": "https://github.com/tud-hri/logitech_steering_wheel/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
    ],
    data_files=[(
        'lib\\site-packages\\logitech_steering_wheel\\lib\\x64', [".\\lib\\x64\\LogitechSteeringWheelEnginesWrapper.dll"]),(
        'lib\\site-packages\\logitech_steering_wheel\\lib\\x86', [".\\lib\\x86\\LogitechSteeringWheelEnginesWrapper.dll"]
    )]
)
