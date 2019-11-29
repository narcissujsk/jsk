# -*- coding:utf-8 -*-
try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup
from codecs import open
from os import path

#版本号
VERSION = '0.0.1'

#发布作者
AUTHOR = "jsk"

#邮箱
AUTHOR_EMAIL = "narcissujsk@gmail.com"

#项目网址
URL = "https://github.com/narcissujsk/jsk"

#项目名称
NAME = "narcissujsk"

#项目简介
DESCRIPTION = "narcissujsk"

#LONG_DESCRIPTION为项目详细介绍，这里取README.md作为介绍
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

#搜索关键词
KEYWORDS = "jsk"

#发布LICENSE
LICENSE = "MIT"

#包
PACKAGES = ["jsk"]

#具体的设置
setup(
    name=NAME,
    version=VERSION,
    description=LONG_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',

    ],
    keywords=KEYWORDS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=PACKAGES,
    install_requires=[],#依赖的第三方包
    include_package_data=True,
    zip_safe=True,
)