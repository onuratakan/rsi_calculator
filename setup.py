from setuptools import setup


setup(name='rsi_calculator',
version='0.1.0',
description="""A library to calculating RSI.""",
long_description="""
# RSI Calculator
A library to calculating RSI.
# Install
```
pip3 install rsi-calculator
```
# Using
## In another script
```python
from rsi_calculator import rsi
# rsi(prices = None, periods = 14)
print(rsi([15, 20, 25, 30, 20, 15, 20, 25, 30, 20, 15, 20, 25, 30, 100]))
```
## In command line
```console
  -h, --help            show this help message and exit
  -pr PRICES [PRICES ...], --prices PRICES [PRICES ...]
                        Prices
  -pe PERIODS, --periods PERIODS
                        Periods
```
```console
rsi -pr 15 20 25 30 20 15 20 25 30 20 15 20 25 30 100
```
""",
long_description_content_type='text/markdown',
url='https://github.com/onuratakan/rsi_calculator',
author='Onur Atakan ULUSOY',
author_email='atadogan06@gmail.com',
license='MIT',
packages=["rsi_calculator"],
package_dir={'':'src'},
install_requires=[
  "numpy==1.21.1"
],
entry_points = {
    'console_scripts': ['rsi=rsi_calculator.rsi_calculator:rsi'],
},
python_requires=">= 3",
zip_safe=False)