from setuptools import setup
setup(
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=["pypi"],
    package_dir={"": "src/main/resources/src"}
)
