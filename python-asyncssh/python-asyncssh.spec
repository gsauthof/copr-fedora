%global         srcname  asyncssh
%global         desc     Python 3 library for asynchronous client and\
server-side SSH communication. It uses the Python asyncio module and\
implements many SSH protocol features such as the various channels,\
SFTP, SCP, forwarding, session multiplexing over a connection and more.

Name:           python-asyncssh
Version:        1.13.3
Release:        1%{?dist}
Summary:        Asynchronous SSH for Python

License:        EPL-1.0
URL:            https://github.com/ronf/asyncssh
Source0:        %pypi_source
#sha256(Source0) = eb5b190badc5cd2a506a1b6ced3e92f948166974eef7d1abab61acc67aa379e6

Patch0001:      0001-skip-unsupported-tests-imports.patch

BuildArch:      noarch

# required by setup.py test
BuildRequires:  openssh
BuildRequires:  openssl

BuildRequires:  python3-cryptography
Requires:       python3-cryptography

%description
%{desc}

%package -n python3-asyncssh
Summary:        %{summary}
%{?python_provide:%python_provide python3-asyncssh}

%description -n python3-asyncssh
%{desc}

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build


%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-asyncssh
%license LICENSE COPYRIGHT
%doc README.rst examples
%{python3_sitelib}/*


%changelog
* Sat Jul 28 2018 Georg Sauthoff <mail@gms.tf> - 1.13.3-1
- initial packaging
