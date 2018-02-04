from setuptools import setup


def readme() -> str:
    with open('README.rst') as f:
        return f.read()


setup(name='lazyfile',
      version='1.0',
      description=('Lazy function application for'
                   'processing text files line by line'),
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6.0',
        'Topic :: Text Processing',
      ],
      keywords='functional lazy file input',
      url='http://github.com/alindgupta/lazyfile',
      author='alindgupta',
      author_email='',
      license='MIT',
      packages=['lazyfile'],
      install_requires=[],
      include_package_data=True,
      zip_safe=False)
