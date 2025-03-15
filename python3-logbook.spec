#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

%define		module		logbook
Summary:	A logging replacement for Python
Summary(pl.UTF-8):	Zamiennik biblioteki logging dla Pythona
Name:		python3-%{module}
Version:	1.8.0
Release:	0.1
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/logbook/
Source0:	https://files.pythonhosted.org/packages/source/l/logbook/logbook-%{version}.tar.gz
# Source0-md5:	d15918a5745349eefab327661454527d
Patch0:		no-network.patch
URL:		https://pypi.org/project/Logbook/
BuildRequires:	python3 >= 1:3.8
BuildRequires:	python3-Cython
BuildRequires:	python3-devel >= 1:3.8
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-brotli
BuildRequires:	python3-pytest >= 6
BuildRequires:	python3-pytest-rerunfailures
%endif
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
# already installed package for metadata
#BuildRequires:	python3-logbook
BuildRequires:	sphinx-pdg-3
# >= 5
%endif
Requires:	python3-modules >= 1:3.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Logbook is a nice logging replacement.

%description -l pl.UTF-8
Logbook to przyjemny zamiennik biblioteki logging.

%package apidocs
Summary:	API documentation for Python Logbook module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona Logbook
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for Python Logbook module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona Logbook.

%prep
%setup -q -n logbook-%{version}
%patch -P 0 -p1

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytest_rerunfailures" \
PYTHONPATH=$(echo $(pwd)/build-3/lib.linux-*) \
%{__python3} -m pytest tests
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE README.md
%dir %{py3_sitedir}/logbook
%attr(755,root,root) %{py3_sitedir}/logbook/_speedups.cpython-*.so
%{py3_sitedir}/logbook/*.py
%{py3_sitedir}/logbook/__pycache__
%{py3_sitedir}/Logbook-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,api,*.html,*.js}
%endif
