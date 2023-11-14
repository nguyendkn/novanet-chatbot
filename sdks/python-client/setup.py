from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="chatbot-client",
    version="0.1.8",
    author="Chatbot",
    author_email="hello@chatbot.ai",
    description="A package for interacting with the Chatbot Service-API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nguyendkn/chatbot",
    license='MIT',
    packages=['chatbot_client'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests"
    ],
    keywords='chatbot nlp ai language-processing',
    include_package_data=True,
)
