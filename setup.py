from setuptools import setup, find_packages

setup(
    name="ad-creator-ai",
    version="0.1.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=open("requirements.txt").read().splitlines(),
    entry_points={
        "console_scripts": [
            "ad-creator=src.interface.gradio_app:main",
        ],
    },
)
