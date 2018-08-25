%global         srcname  asyncssh
%global         desc     Python 3 library for asynchronous client and\
server-side SSH communication. It uses the Python asyncio module and\
implements many SSH protocol features such as the various channels,\
SFTP, SCP, forwarding, session multiplexing over a connection and more.

Name:           python-%{srcname}
Version:        1.13.3
Release:        1%{?dist}
Summary:        Asynchronous SSH for Python

License:        EPL-1.0
URL:            https://github.com/ronf/asyncssh
Source0:        %pypi_source
#sha256(Source0) = eb5b190badc5cd2a506a1b6ced3e92f948166974eef7d1abab61acc67aa379e6

Patch0001:      0001-skip-unsupported-tests-imports.patch
Patch0002:      0002-Make-maximum-time_t-computation-more-portable.patch

BuildArch:      noarch

# required for py3_build macro
BuildRequires:  python3-devel

# required by setup.py test
BuildRequires:  openssh
BuildRequires:  openssl
BuildRequires:  python3-bcrypt
BuildRequires:  python3-gssapi
BuildRequires:  python3-libnacl
BuildRequires:  python3-pyOpenSSL

BuildRequires:  python3-cryptography
Requires:       python3-cryptography

# for ed25519 etc.
Recommends:     python3-libnacl

# for OpenSSH private key encryption
Suggests:       python3-bcrypt
# for GSSAPI key exchange/authentication
Suggests:       python3-gssapi
# for X.509 certificate authentication
Suggests:       python3-pyOpenSSL

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
sed -i '1,1s@^#!.*$@#!%{__python3}@' examples/*.py
%py3_build


%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE COPYRIGHT
%doc README.rst examples
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*-py*.egg-info/


%changelog
* Sat Jul 28 2018 Georg Sauthoff <mail@gms.tf> - 1.13.3-1
- initial packaging
