%define 	module	generateDS
Summary:	Generate Python data structures and XML parser from Xschema
Summary(pl.UTF-8):	-
Name:		python-%{module}
Version:	2.3b
Release:	0.1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/g/generateDS/%{module}-%{version}.tar.gz
# Source0-md5:	272e04c47abc8110fac7589917015bd0
URL:		http://pypi.python.org/pypi/generateDS/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
#Requires:		python-libs
Requires:	python-modules
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
generateDS.py generates Python data structures (for example, class
definitions) from an XML Schema document. These data structures
represent the elements in an XML document described by the XML Schema.
It also generates parsers that load an XML document into those data
structures. In addition, a separate file containing subclasses (stubs)
is optionally generated. The user can add methods to the subclasses in
order to process the contents of an XML document.

%prep
%setup -q -n %{module}-%{version}

%build
# CFLAGS is only for arch packages - remove on noarch packages
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README tutorial
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/lib%{module}/*.py[co]
%{py_sitescriptdir}/lib%{module}/gui
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
