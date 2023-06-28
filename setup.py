from setuptools import setup, find_namespace_packages


setup(name='home_work',
      version='1',
      description='sort files in folders code',
      url='https://github.com/Filip-Povidernyi/go-it_hw',
      author='Filip Povidernyi',
      author_email='p.poviderniy@gmail.com',
      license='MIT',
      packages=['home_work'],
      packages=find_namespace_packages(),
      install_requires=[],
      entry_points={'console_scripts': ['homework = home_work.HW1:homework']}
      )