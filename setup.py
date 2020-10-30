from setuptools import find_packages, setup

setup(
    name='ranked_game_predictor',
    packages=find_packages("src", exclude=["test"]),
    package_dir={"": "src"},
    version='0.1.0',
    description="Machine Learning Project to predict ranked games",
    author='ffaheroes',
    license='Unknown',
)
