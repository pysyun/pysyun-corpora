from setuptools import setup

setup(
    name='pysyun_corpora',
    version='1.2',
    description='Syun\'s Python SDK for time series analysis. Text corpora for segmenting textual time-series by '
                'domains.',
    author='Py Syun',
    author_email='pysyun@vitche.com',
    py_modules=['pysyun.corpora.blockchain', 'pysyun.corpora.crypto.exchanges', 'pysyun.corpora.web3.uniswap'],
    install_requires=['web3', 'requests']
)
