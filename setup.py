from setuptools import setup


def read(fname):
    import os
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='pdtweak',
      version='0.1.0',
      description='pandas utility functions',
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      url='http://github.com/kmedian/pdtweak',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='MIT',
      packages=['pdtweak'],
      install_requires=[
          'setuptools>=40.0.0',
          'pandas>=0.25.3'],
      python_requires='>=3.6',
      zip_safe=False)
