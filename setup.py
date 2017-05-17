from setuptools import setup


extra_packages = {
    'testing': ['pytest', 'pytest-watch', 'pytest-cov']
}


setup(
    name="mailroom-madness",
    description="401 partner assignment to read and write text files.",
    version=0.1,
    author="Casey O'Kane" "Ronel Rustia",
    author_email="okanecasey@gmail.com" "fedstats@yahoo.com",
    license="MIT",
    py_modules=["mailroom"],
    package_dir={'': 'src'},
    install_requires=["ipython", "pytest"],
    extras_require=extra_packages,
)
