from setuptools import setup, find_packages

setup(
    name="instasele",
    version = '0.0.1',
    packages=['instasele'],
    author="Al-Saeed Hasan",
    license='MIT',
    author_email="Sa3ed7asanOfficial@gmail.com",
    description="Simple Instagram Accounts Controller Using Selenium",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sa3ed7asan/instasele",
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: Indonesian',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3 :: Only'
  ],
    python_requires='>=3.9',
    install_requires=[
        "selenium==4.9.1",
        "webdriver-manager"
    ],
    keywords=['instagram-scraper', 'instagram-bot', 'instasele', 'instagram-bot-using-selenium'],
)
