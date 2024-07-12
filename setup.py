from setuptools import setup, find_packages

setup(
    name='praktika_task',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'django',
        'flake8',
        'radon',
        'bandit',
        'coverage'
    ],
    test_suite='test_app'
)
