# README.md
This is a simple demonstration of using a Python package hosted on Github

The package itself can be seen here [github_pipenv_package_example](https://github.com/chrisguest75/github_pipenv_package_example)

# Usage:
I've left the package uninstalled by default so different mechanisms can be used. 

```
export PIPENV_VENV_IN_PROJECT=1
pipenv install --three
```

# Installing package from local directory
```
pipenv install -e ../github_pipenv_package_example
```

# Installing package from github
```
pipenv install git+https://github.com/chrisguest75/github_pipenv_package_example#egg=github_pipenv_package_example
```

# Installing package from private github
```
pipenv install git+ssh://git@github.com/chrisguest75/github_pipenv_package_example.git#egg=github_pipenv_package_example 
```

# Uninstalling package 

```
pipenv uninstall github_pipenv_package_example
```


# Troubleshooting Pipenv Installation
Use the --verbose flag.

```
pipenv install -e ../github_pipenv_package_example --verbose
```
