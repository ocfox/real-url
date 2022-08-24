from setuptools import setup, find_packages

setup(
    name="real-url",
    version="0.1.0",
    description="A live url get tool",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.10, <4",
    entry_points={
        "console_scripts": [
            "real-url=real-url:main"
        ]
    },
)
