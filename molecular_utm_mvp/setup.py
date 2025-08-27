from setuptools import setup, find_packages

setup(
    name="molecular_utm_mvp",
    version="0.1.0",
    description="Molecular Universal Turing Machine MVP using pylua_bioxen_vm_lib",
    author="Research Team",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pylua_bioxen_vm_lib>=0.1.18",
        "asyncio",
        "numpy",
        "networkx",
        "matplotlib",
        "pyyaml",
        "click",
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-asyncio",
            "black",
            "flake8",
            "mypy",
        ]
    },
    entry_points={
        "console_scripts": [
            "molecular-utm=molecular_utm_mvp.cli:main",
        ]
    },
    python_requires=">=3.7",
)
