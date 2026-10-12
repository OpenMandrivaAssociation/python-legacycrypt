Name:		python-legacycrypt
Version:	0.3
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/l/legacycrypt/legacycrypt-%{version}.tar.gz
Summary:	Wrapper to the POSIX crypt library call and associated functionality.
URL:		https://pypi.org/project/legacycrypt/
License:	GPL
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(pip)
Provides:	python%{pyver}dist(crypt)
BuildSystem:	python
BuildArch:	noarch

%description
Wrapper to the POSIX crypt library call and associated functionality.

%prep -a
# flit 4 no longer reads [tool.flit.metadata].
cat > pyproject.toml << 'EOF'
[build-system]
requires = ["flit_core >=3.2"]
build-backend = "flit_core.buildapi"

[project]
name = "legacycrypt"
description = "Wrapper to the POSIX crypt library call and associated functionality."
readme = "README.md"
requires-python = ">=3.5"
license = "PSF-2.0"
authors = [{name = "Christian Heimes", email = "christian@python.org"}]
dynamic = ["version"]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Programming Language :: Python :: 3 :: Only",
    "Operating System :: POSIX",
    "Topic :: Security :: Cryptography",
]

[tool.flit.module]
name = "legacycrypt"
EOF

%install -a
# Make "import crypt" great again
cd %{buildroot}%{py_sitedir}
ln -s legacycrypt.py crypt.py

%files
%{py_sitedir}/crypt.py
%{py_sitedir}/legacycrypt.py
%{py_sitedir}/legacycrypt-*.*-info
%{py_sitedir}/__pycache__/*
