from setuptools import setup

setup(
    name="indian-name-generator",
    version="0.1.0",
    py_modules=["name_generator", "cli"],
    include_package_data=True,
    package_data={
        "": ["data/*.csv"],
    },
    install_requires=[
        "pandas>=1.3.0",
    ],
    python_requires=">=3.7",
    author="Ankit Kumar",
    description="A Python package to generate Indian names",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ankitprasad81/indian-name-generator",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: CC BY-NC-SA 4.0",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points={
        'console_scripts': [
            'generate-indian-name=cli:main',
        ],
    },
)
