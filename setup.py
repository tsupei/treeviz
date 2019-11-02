from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'treeviz',
  packages = ['treeviz'],
  version = '1.1',
  license='MIT',
  description = 'Print tree in bash manner',
  author = 'Chen Tsu Pei',
  author_email = 'a5560648@gmail.com',
  url = 'https://github.com/tsupei/treeviz',
  download_url="https://github.com/tsupei/treeviz/archive/v1.0.tar.gz",
  long_description=long_description,
  long_description_content_type="text/markdown",
  keywords = ['tree', 'treeviz'],
  classifiers = [],
)