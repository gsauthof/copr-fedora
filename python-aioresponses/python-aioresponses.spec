%global         srcname  aioresponses
%global         desc     Aioresponses is a helper to mock/fake web requests in the python\
aiohttp package. The purpose of this package is to provide an\
easy way  to test asynchronous HTTP requests.

Name:           python-%{srcname}
Version:        0.6.0
Release:        1%{?dist}
Summary:        Mock out requests made by ClientSession from aiohttp package

License:        MIT
URL:            https://github.com/pnuckowski/aioresponses
Source0:        %pypi_source

BuildArch:      noarch

# required for py3_build macro
BuildRequires:  python3-devel

# from setup.py
BuildRequires: python3-pbr
BuildRequires: python3-aiohttp

## for tests
BuildRequires: python3-watchdog
BuildRequires: python3-pytest
BuildRequires: python3-pytest-cov
BuildRequires: python3-ddt
BuildRequires: python3-asynctest

%{?python_enable_dependency_generator}

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build


%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*-py*.egg-info/


%changelog

* Tue Mar 26 2019 Georg Sauthoff <mail@gms.tf> - 0.6.0-1
- initial packaging
