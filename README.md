![Python Boilerplate Social Image](./pysimplegui_boilerplate.png)
[![GitHub release](https://img.shields.io/github/release/johnnymillergh/pysimplegui_boilerplate.svg)](https://github.com/johnnymillergh/pysimplegui_boilerplate/releases)
[![Github Actions workflow status](https://github.com/johnnymillergh/pysimplegui_boilerplate/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/johnnymillergh/pysimplegui_boilerplate/actions)
[![GitHub issues](https://img.shields.io/github/issues/johnnymillergh/pysimplegui_boilerplate)](https://github.com/johnnymillergh/pysimplegui_boilerplate/issues)
[![GitHub forks](https://img.shields.io/github/forks/johnnymillergh/pysimplegui_boilerplate)](https://github.com/johnnymillergh/pysimplegui_boilerplate/network)
[![GitHub stars](https://img.shields.io/github/stars/johnnymillergh/pysimplegui_boilerplate)](https://github.com/johnnymillergh/pysimplegui_boilerplate)
[![GitHub license](https://img.shields.io/github/license/johnnymillergh/pysimplegui_boilerplate)](https://github.com/johnnymillergh/pysimplegui_boilerplate/blob/master/LICENSE)
[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/johnnymillergh/pysimplegui_boilerplate.svg?style=popout)](https://github.com/johnnymillergh/pysimplegui_boilerplate)
[![GitHub repo size](https://img.shields.io/github/repo-size/johnnymillergh/pysimplegui_boilerplate.svg)](https://github.com/johnnymillergh/pysimplegui_boilerplate)
[![Twitter](https://img.shields.io/twitter/url/https/github.com/johnnymillergh/pysimplegui_boilerplate?style=social)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2Fjohnnymillergh%2Fpython_kivymd_boilerplate)

# PySimpleGUI Boilerplate

**pysimplegui_boilerplate** is a boilerplate project for Python with PySimpleGUI. Based on template [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter).

## Features

Here is the highlights of **pysimplegui_boilerplate**:

1. Inherited from modern and the latest Python technologies:

   `Python` - [![Python](https://img.shields.io/badge/Python-v3.10.6-blue)](https://www.python.org/downloads/release/python-3106/)

   `Pipenv` is to build and compile the project.

   `PySimpleGUI` - [![PySimpleGUI](https://img.shields.io/badge/PySimpleGUI-v4.60.3-blue)](https://github.com/PySimpleGUI/PySimpleGUI/releases/tag/4.60.3)

2. [Event Bus](https://github.com/seanpar203/event-bus) to handle GUI events.

3. [PyInstaller](https://github.com/pyinstaller/pyinstaller) to build executable package for macOS and Windows platform.

4. Highly customizable data analysis with [pandas](https://pandas.pydata.org/), enhanced array operation with [NumPy](https://numpy.org/). Supports CSV, excel, JSON and so on.

5. Data persistence with [peewee](http://docs.peewee-orm.com/en/latest/), [SQLite3](https://sqlite.org/index.html) as local database.

6. Simple and flexible retry with [Tenacity](https://github.com/jd/tenacity).

7. Environment variable and configuration with [pyhocon](https://pythonhosted.org/pyhocon/_modules/pyhocon.html). Read `${ENVIRONMENT_VARIABLE}` when startup.

8. Sensible and human-friendly approach to creating, manipulating, formatting and converting dates, times and timestamps with [Arrow](https://pypi.org/project/arrow/).

9. Generate fake data with [Faker](https://pypi.org/project/Faker/).

10. Customized function decorator `@async_function` to enable function to run asynchronously; `@peewee_table` class decorator to register ORM tables; `@elapsed_time(level="INFO")` to profile a function elapsed time.

11. Testing with [pytest](https://docs.pytest.org/en/latest/), integrating [pytest-mock](https://pypi.org/project/pytest-mock/) for mocking, [pytest-cov](https://pypi.org/project/pytest-cov/) for code coverage analysis and [pyinstrument](https://github.com/joerick/pyinstrument) for Python stack profiler.

12. Formatting with [black](https://github.com/psf/black).

13. Import sorting with [isort](https://github.com/timothycrosley/isort).

14. Static typing with [mypy](http://mypy-lang.org/).

15. Linting with [flake8](http://flake8.pycqa.org/en/latest/).

16. Git hooks that run all the above with [pre-commit](https://pre-commit.com/).

17. Deployment ready with [Docker](https://docker.com/).

18. Continuous Integration with [GitHub Actions](https://github.com/features/actions).

19. [Loguru](https://github.com/Delgan/loguru) logging configuration. Log sample is like,

   ```
   2022-09-17 14:13:52.385 | ⚠️ WARNING  | 6860 | MainThread      | pysimplegui_boilerplate.repository.model.base_model.<module>:24 - SQLite database created. Path: [/Users/johnny/Projects/PyCharmProjects/pysimplegui_boilerplate/data/pysimplegui_boilerplate.db], <peewee.SqliteDatabase object at 0x1191e1390>
   2022-09-17 14:13:52.386 | ℹ️ INFO     | 6860 | MainThread      | pysimplegui_boilerplate.common.orm.peewee_table:16 - Registering peewee table: StartupLog
   2022-09-17 14:13:52.387 | 🐞 DEBUG    | 6860 | MainThread      | peewee.execute_sql:3185 - ('CREATE TABLE IF NOT EXISTS "startup_log" ("id" INTEGER NOT NULL PRIMARY KEY, "current_user" VARCHAR(50) NOT NULL, "host" VARCHAR(50) NOT NULL, "command_line" TEXT NOT NULL, "current_working_directory" TEXT NOT NULL, "startup_time" DATETIME NOT NULL, "created_by" VARCHAR(50) NOT NULL, "created_time" DATETIME NOT NULL, "modified_by" VARCHAR(50) NOT NULL, "modified_time" DATETIME NOT NULL)', [])
   2022-09-17 14:13:52.530 | ℹ️ INFO     | 6860 | MainThread      | pysimplegui_boilerplate.<module>:53 - Started pysimplegui_boilerplate in 0.117 seconds (117.26 ms)
   ```

## Usage

1. Clone or download this project.

   ```shell
   $ git clone https://github.com/johnnymillergh/python_kivymd_boilerplater.git
   ```

2. Build with newest PyCharm.

3. Click the green triangle to Run.

## Setup

1. Setup the development environment

   ```shell
   # Install pipx if pipenv and cookiecutter are not installed
   $ python3 -m pip install pipx
   $ python3 -m pipx ensurepath

   # Install pipenv using pipx
   $ pipx install pipenv
   ```

2. Install dependencies

   ```shell
   $ pipenv install --dev
   ```

3. Setup pre-commit and pre-push hooks

   ```shell
   $ pipenv run pre-commit install -t pre-commit
   $ pipenv run pre-commit install -t pre-push
   ```

## Useful Commands

### Run Python Module

```shell
$ python3 -m pysimplegui_boilerplate
```

### Run Python Script

**Append your project’s root directory to** `PYTHONPATH` — In any environment you wish to run your Python application such as Docker, vagrant or your virtual environment i.e. in bin/activate, run the below command:

> [How to Fix ModuleNotFoundError and ImportError](https://towardsdatascience.com/how-to-fix-modulenotfounderror-and-importerror-248ce5b69b1c)

```shell
$ PYTHONPATH="${PYTHONPATH}:/Users/johnny/Projects/PyCharmProjects/pysimplegui_boilerplate/pysimplegui_boilerplate" python3 pysimplegui_boilerplate/__main__.py
```

### Package with [PyInstaller](https://pyinstaller.org/en/latest/usage.html?highlight=pythonpath#using-pyinstaller)

> **WANRING**
>
> Need to call `freeze_support()` immediately when startup in `pysimplegui_boilerplate/__init__.py`
>
> ```python
> from multiprocessing import freeze_support
>
> freeze_support()
> ```
>
> - [Pyinstaller multiprocessing name of process is always "MainProcess" #3957](https://github.com/pyinstaller/pyinstaller/issues/3957#issuecomment-674579877)
> - [pyinstaller linux binary is getting restarted again and again #4190](https://github.com/pyinstaller/pyinstaller/issues/4190)

```shell
$ pipenv run pyinstaller --windowed --noconsole \
--add-data "setup.cfg:." \
--add-data "pysimplegui_boilerplate/resources/*:pysimplegui_boilerplate/resources" \
--name pysimplegui_boilerplate-main \
--clean --noconfirm pysimplegui_boilerplate/__main__.py
```

### Run Unit Tests

Run with pytest, analyze code coverage, generate HTML code coverage reports, fail the test if coverage percentage is unser 85%

```shell
$ pipenv run pytest --cov --cov-report html --cov-fail-under=85 --capture=no --log-cli-level=INFO
```

### Conventional Changelog CLI

1. Install global dependencies (optional if installed):

   ```shell
   $ npm install -g conventional-changelog-cli
   ```

2. This will *not* overwrite any previous changelogs. The above generates a changelog based on commits since the last semver tag that matches the pattern of "Feature", "Fix", "Performance Improvement" or "Breaking Changes".

   ```shell
   $ conventional-changelog -p angular -i CHANGELOG.md -s
   ```

3. If this is your first time using this tool and you want to generate all previous changelogs, you could do:

   ```shell
   $ conventional-changelog -p angular -i CHANGELOG.md -s -r 0
   ```

## CI (Continuous Integration)

- GitHub Actions is for building project and running tests.
- ~~[Travis CI](https://travis-ci.com/github/johnnymillergh/) is for publishing Docker Hub images of SNAPSHOT and RELEASE.~~

## Maintainers

[@johnnymillergh](https://github.com/johnnymillergh).

## Contributing

Feel free to dive in! [Open an issue](https://github.com/johnnymillergh/pysimplegui_boilerplate/issues/new).

### Contributors

This project exists thanks to all the people who contribute.

- Johnny Miller [[@johnnymillergh](https://github.com/johnnymillergh)]
- …


### Sponsors

Support this project by becoming a sponsor. Your logo will show up here with a link to your website. [[Become a sponsor](https://become-a-sponsor.org)]

## Credits

This package was created with Cookiecutter and the [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter) project template.

Inspired by [How to set up a perfect Python project](https://sourcery.ai/blog/python-best-practices/).

## License

[Apache License](https://github.com/johnnymillergh/pysimplegui_boilerplate/blob/master/LICENSE) © Johnny Miller

2022 - Present
