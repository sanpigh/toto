from setuptools import setup, find_packages


with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content]


setup(name='toto',
    description="Paquete test",
    packages=find_packages(), #(toto + tests)     packages=["toto"],
    install_requires=requirements,
    scripts=['scripts/toto-run']
)
