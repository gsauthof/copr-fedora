%global         srcname  inema
%global         desc     This is a python module for interfacing the "Internetmarke" API provided by the\
German postal company "Deutsche Post". It implements V3 of this API.\
\
The Internetmarke API allows you to buy online franking for national and\
international postal products like post cards and letters of all weight\
classes and service classes (normal, registered, ...).

Name:           python-%{srcname}
Version:        0.8
Release:        1%{?dist}
Summary:        A Python interface to the Deutsche Post Internetmarke Online Franking

License:        AGPLv3+
URL:            http://git.sysmocom.de/python-inema/
Source0:        %pypi_source

BuildArch:      noarch

# required for py3_build macro
BuildRequires:  python3-devel

# from setup.py
BuildRequires: python3-pytz
BuildRequires: python3-zeep

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
sed -i '1,1s@^#!.*$@@' inema/frank.py inema/inema.py
%py3_build


%install
%py3_install

%files -n python3-%{srcname}
%{_bindir}/frank
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*-py*.egg-info/


%changelog

* Sun Jul 14 2019 Georg Sauthoff <mail@gms.tf> - 0.8-1
- Update to latest upstream version
* Wed Mar 27 2019 Georg Sauthoff <mail@gms.tf> - 0.6-1
- initial packaging
