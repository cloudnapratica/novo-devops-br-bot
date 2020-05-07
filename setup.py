import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="novo_devops_br_bot",
    version="0.0.1",

    description="Um bot para o grupo Novo DevOps BR no Telegram",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="fgoncalves-io",

    package_dir={"": "novo_devops_br_bot"},
    packages=setuptools.find_packages(where="novo_devops_br_bot"),

    install_requires=[
        "aws-cdk.core==1.37.0",
        "aws_cdk.aws_events==1.37.0",
        "aws_cdk.aws_events_targets==1.37.0",
        "aws_cdk.aws_lambda==1.37.0",
        "aws_cdk.aws_ssm==1.37.0",
        "autopep8==1.5.2",
        "moto==1.3.14",
        "pytest-env==0.6.2",
        "requests==2.23.0",
        "requests-mock==1.8.0"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
