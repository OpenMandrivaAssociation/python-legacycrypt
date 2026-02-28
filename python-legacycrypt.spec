Name:		python-legacycrypt
Version:	0.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/l/legacycrypt/legacycrypt-%{version}.tar.gz
Summary:	Wrapper to the POSIX crypt library call and associated functionality.
URL:		https://pypi.org/project/legacycrypt/
License:	GPL
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(flit)
BuildRequires:	python%{pyver}dist(flit-core)
BuildSystem:	python
BuildArch:	noarch

%description
Wrapper to the POSIX crypt library call and associated functionality.

%prep -a
# Force the backend to use 'flit_core' which is the standard
sed -i 's/flit.buildapi/flit_core.buildapi/g' pyproject.toml

%files
%{py_sitedir}/legacycrypt.py
%{py_sitedir}/legacycrypt-*.*-info
%{py_sitedir}/__pycache__/*
