%define		module		logbook
Summary:	A logging replacement for Python
Name:		python3-%{module}
Version:	1.6.0
Release:	1
License:	ISC
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/logbook/
Source0:	https://files.pythonhosted.org/packages/source/l/logbook/Logbook-%{version}.tar.gz
# Source0-md5:	78029e508a4e8a5e6d6fd4df752b84ae
URL:		https://pypi.org/project/Logbook/
BuildRequires:	python3 >= 1:3.7
BuildRequires:	python3-Cython
BuildRequires:	python3-devel >= 1:3.7
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Logbook is a nice logging replacement.

%prep
%setup -q -n Logbook-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE README.md
%{py3_sitedir}/%{module}
%{py3_sitedir}/Logbook-%{version}-py*.egg-info
