"""Installing with setuptools."""
import setuptools

with open("README.md", "r", encoding="utf8") as fh:
  long_description = fh.read()

setuptools.setup(
    name="game_helper",
    version="0.0.1",
    packages=setuptools.find_packages(),
    package_data={'game_helper': [
    ]},
    python_requires=">=3.6",
    install_requires=[
        "pyautogui==1.14.0",
        "pysocks==1.7.1",
    ],
    license="Apache License 2.0",
    url="https://github.com/ychy00001/game_helper",
    description="A Tool for Game to Auto Operation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Rain",
    author_email="ychy00001@163.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Development Status :: 1 - Pre-Alpha",
        "Operating System :: OS Independent",
        "Topic :: Game :: Script",
    ]
)
