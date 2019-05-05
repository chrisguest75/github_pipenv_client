from github_pipenv_package_example import sample_class

if __name__ == '__main__':
    sc = sample_class.sample_class()
    package_test = sc.get()

    print(f"Hello World {package_test}")