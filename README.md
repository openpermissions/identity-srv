open-permissions-platform-identity-srv
======================================

This repository contains the Open Permissions Platform Coalition Identity Service

Running locally
===============
To run the service locally:

```
pip install -r requirements/dev.txt
python setup.py develop
python identity/
```

To show a list of available CLI parameters:

```
python identity/ -h [--help]
```

To start the service using test.service.conf:

```
python identity/ -t [--test]
```

Running tests and generating code coverage
==========================================
To have a "clean" target from build artifacts:

```
make clean
```

To run all unit tests and generate a HTML code coverage report along with a
JUnit XML report in tests/unit/reports:

```
make test
```

To run pyLint and generate a HTML report in tests/unit/reports:

```
make pylint
```

To run create the documentation for the service in _build:

```
make docs
```
