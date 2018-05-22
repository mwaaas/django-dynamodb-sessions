from setuptools import setup, find_packages
import dynamodb_sessions

long_description = open('README.rst').read()

major_ver, minor_ver, minor_minor_ver = dynamodb_sessions.__version__
version_str = '%s.%s.%s' % (major_ver, minor_ver, minor_minor_ver)

setup(
    name='dj-dynamodb-sessions',
    version=version_str,
    packages=find_packages(),
    description="A Django session backend using Amazon's DynamoDB",
    long_description=long_description,
    author='Gregory Taylor',
    author_email='gtaylor@gc-taylor.com',
    license='BSD License',
    url='https://github.com/gtaylor/django-dynamodb-sessions',
    platforms=["any"],
    install_requires=['django', "boto3>=1.1.4"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Web Environment',
    ],
)
