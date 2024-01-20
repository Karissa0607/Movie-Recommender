from setuptools import setup

AUTHOR_NAME = 'Karissa Dubreuil'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name = SRC_REPO,
    version = '0.0.1',
    author = AUTHOR_NAME,
    author_email = 'karissadubreuil@gmail.com',
    description = 'Package for Movie Recommendation System',
    long_description = "Movie Recommendation System",
    long_description_content_type = 'text/markdown',
    package = [SRC_REPO],
    python_requires = '>=3.9',
    install_requires = LIST_OF_REQUIREMENTS,
)