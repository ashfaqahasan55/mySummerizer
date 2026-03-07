import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

    __version__ = "0.0.0"

    REPO_NAME = "mySummerizer"
    AUTHOR_USER_NAME = "ashfaqahasan55"
    SRC_REPO = "mySummerizer"
    AUTHOR_EMAIL = "ashfaqahasan55@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/ashfaqahasan55/mySummerizer",
    project_urls={
        "Bug Tracker": f"https://github.com/ashfaqahasan55/mySummerizer/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)