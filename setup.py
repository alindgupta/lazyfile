from setuptools import setup


def readme() -> str:
    with open('README.rst') as f:
        return f.read()


setup(name='lazyfile',
      version='0.1',
      description='Lazy function application for processing text files line by line',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='functional lazy file input',
      url='http://github.com/fushitarazu/lazyfile',
      author='fushitarazu',
      author_email='',
      license='MIT',
      packages=['lazyfile'],
      install_requires=[
      ],
      include_package_data=True,
      zip_safe=False)