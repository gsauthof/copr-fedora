# Generated from gist-6.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name gist

Name: rubygem-%{gem_name}
Version: 6.0.0
Release: 1%{?dist}
Summary: Upload code to gist.github.com
License: MIT
URL: https://github.com/defunkt/gist
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
%if 0%{?fedora} < 34
BuildRequires: rubygem(ronn)
%else
BuildRequires: rubygem(ronn-ng)
%endif
BuildRequires: rubygem(webmock)
BuildRequires: rubygem(rspec) > 3
BuildArch: noarch

%description
Upload source code, text files and similar content to gist.github.com
or a local GitHub Enterprise instance.

This package provides the gist command line utility and a single function
(Gist.gist) that uploads a gist.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

sed  's/\xe2\x80\x8c/\* /g' README.md > README.md.ron
ronn --roff --manual="Gist manual" README.md.ron

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

mkdir -p %{buildroot}%{_mandir}/man1
%if 0%{?fedora} < 34
cp README.1 %{buildroot}%{_mandir}/man1/%{gem_name}.1
%else
cp README.md.1 %{buildroot}%{_mandir}/man1/%{gem_name}.1
%endif


%check
pushd .%{gem_instdir}
rspec spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/gist
%license %{gem_instdir}/LICENSE.MIT
%{gem_instdir}/bin
%{gem_libdir}
%{gem_instdir}/vendor
%exclude %{gem_cache}
%{gem_spec}
%{_mandir}/man1/%{gem_name}.1*

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/gist.gemspec
%{gem_instdir}/spec

%changelog
* Sun Jul 04 2021 Georg Sauthoff <mail@gms.tf> - 6.0.0-1
- Initial package
