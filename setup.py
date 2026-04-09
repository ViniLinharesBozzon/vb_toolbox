from setuptools import setup, find_packages

setup(
    name="vb-toolbox"
 ,  version="0.1.1"
 ,  package_dir={"":"src"}
 ,  packages=find_packages(where="src")

    # Dependências Globais
    install_requires=[
        "pandas"
      , "requests"
    ]

    # Dependências Por módulo
    extras_require=
    {
        "CV":[
                "tensorflow >=2.0.0"
            ,   "pillow"
        ],
        "ML":[
                "matplotlib"
            ,   "seaborn"
        ]
    }
)