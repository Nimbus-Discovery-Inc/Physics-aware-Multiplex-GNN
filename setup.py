from setuptools import setup, find_packages

setup(
    name='pamnet',
    version='0.1.0',
    description='PAMNet: A Universal Framework for Accurate and Efficient Geometric Deep Learning of Molecular Systems',
    author='leelasd',
    author_email='your.email@example.com',
    url='https://https://github.com/Nimbus-Discovery-Inc/Physics-aware-Multiplex-GNN',
    packages=find_packages(),
    install_requires=[
        'torch>=1.7.0',
        'torch_geometric',
        'numpy',
        'glob2',
        # Add other dependencies from requirements.txt here
    ],
    include_package_data=True,
    package_data={
        # Include any data files here
        '': ['data/*', 'save/*'],
    },
    entry_points={
        'console_scripts': [
            # Add command line scripts here
        ],
    },
)