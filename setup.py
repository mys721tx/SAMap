from setuptools import setup, find_packages

setup(
    name="samap",
    version="1.0.3",
    description="The SAMap algorithm",
    long_description="The Self-Assembling Manifold Mapping algorithm for mapping single-cell datasets across species.",
    long_description_content_type="text/markdown",
    author="Alexander J. Tarashansky",
    url="https://github.com/atarashansky/SAMap",
    author_email="tarashan@stanford.edu",
    keywords="scrnaseq analysis manifold reconstruction cross-species mapping",
    python_requires=">=3.7",
    install_requires=[
        "sam-algorithm>=0.8.1",
        "scanpy>1.7.0",
        "hnswlib",
        "dill",
        "numba==0.52.0",
        "h5py<=2.10",
        "leidenalg",
        "fast-histogram",
        "holoviews-samap"
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
