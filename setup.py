from setuptools import setup, find_packages


setup(
    name="Gastos-dos-Politicos",
    version="0.1.0.dev",
    description="Gastos dos políticos brasileiros.",
    author="Thiago J. Barbalho",
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "coverage>=5.2.1",
        "Flask>=1.1.2",
        "Flask-Caching>=1.9.0",
        "Flask-SQLAlchemy>=2.4.3",
        "Flask-WTF>=0.4.13",
        "mysqlclient>=2.0.1",
        "pytest>=5.4.3",
        "python-dotenv>=0.13.0",
        "requests>=2.24.0",
    ],
)
