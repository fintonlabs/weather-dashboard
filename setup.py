from setuptools import setup, find_packages

setup(
    name='weather_dashboard',
    version='0.1.0',
    description='A Python Flask web application that fetches weather data from OpenWeatherMap API',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'Flask==1.1.2',
        'requests==2.25.1'
    ],
)