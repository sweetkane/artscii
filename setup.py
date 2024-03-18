import setuptools

setuptools.setup(
    name="artscii",
    version="0.0.1",
    author="Kane Sweet",
    author_email="kanesweet11@gmail.com",
    description="This tool uses AI to generate ascii art from a given prompt.",
    requires=["requests"],
    entry_points={
        'console_scripts': [
            'artscii = artscii.__main__:main'
        ]
    }
)