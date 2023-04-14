import setuptools

setuptools.setup(
    name="spam-check",
    version="0.0.25",
    author="Suhghosh D J ",
    description="",
    url="https://github.com/Sughosh-D-J/Learn_django.git",
    url="https://github.com/Sughosh-D-J/Learn_django.git",
    install_requires=open('requirements.txt').read().split('\n'),
    include_package_data=True,
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
       classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)