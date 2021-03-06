#
# Conditional build:
%bcond_with	tests	# do not perform "make test"

Summary:	App that corrects your previous console command
Name:		thefuck
Version:	3.2
Release:	1
License:	MIT
Group:		Applications/Shells
Source0:	https://github.com/nvbn/thefuck/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b2012c223a0ae15cecaa384aa8bbae32
URL:		https://github.com/nvbn/thefuck
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-pip
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	python3-colorama
BuildRequires:	python3-decorator
BuildRequires:	python3-mock
BuildRequires:	python3-psutil
BuildRequires:	python3-pytest
BuildRequires:	python3-six
%endif
Requires:	python3
Requires:	python3-colorama
Requires:	python3-psutil
Requires:	python3-six
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# provided by python3.spec
%define	_noautoreq_py3egg pathlib

%description
This application corrects your previous console command.

See README.md how to setup for your shell.

%prep
%setup -q

sed -i -e '/^#!\//, 1d' *.py

%build
%py3_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE.md
%attr(755,root,root) %{_bindir}/thefuck
%attr(755,root,root) %{_bindir}/fuck
%attr(755,root,root) %{_bindir}/thefuck-alias
%{py3_sitescriptdir}/thefuck
%{py3_sitescriptdir}/thefuck-%{version}-*egg-info
