%global         srcname  img2pdf

Name:		python3-img2pdf
Version:	0.2.4
Release:	1%{?dist}
Summary:	Lossless images to PDF conversion library and command

License:	GPLv3+
URL:		https://pypi.org/project/img2pdf
Source0:	https://files.pythonhosted.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:	python3-devel
BuildRequires:	python3-pillow
BuildRequires:	python3-pdfrw
Requires:	python3-pillow

%{?python_provide:%python_provide python3-img2pdf}

%description
Python 3 library and command line utility img2pdf for losslessly converting
a bunch of image files into a PDF file. That means that the images
are either inserted into the PDF as-is or they are recompressed using
lossless compression. Thus, img2pdf usually runs faster and may yield
smaller PDF files than an ImageMagick convert command.

The img2pdf command complements the pdfimages command.

%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install

%check
%{__python3} setup.py test

%files
%{_bindir}/%{srcname}
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/jp2.py
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{srcname}-%{version}*.egg-info
%doc README.md


%changelog
* Tue May 1 2018 Georg Sauthoff <mail@gms.tf> - 0.2.4-1
- initial packaging
