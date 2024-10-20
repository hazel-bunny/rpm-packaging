%global _basename anoise
%global _suffix 1
%global wheel_name %{_basename}_community_extension%{_suffix}

Name:           %{_basename}-community-extension%{_suffix}
Version:        0.0.1
Release:        3%{?dist}
Summary:        Ambient Noise Community Extension %{_suffix}
License:        GPLv3
URL:            https://costales.github.io/projects/%{_basename}
Source:         https://launchpad.net/~costales/+archive/ubuntu/%{_basename}/+sourcefiles/%{name}/%{version}/%{name}_%{version}.tar.gz

#------------------------------------------------------------------------------

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-installer
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel

Requires:       %{_basename}-media

Enhances:       %{_basename}

#------------------------------------------------------------------------------

%description
Ambient Noise Community Extension %{_suffix}. Sounds and icons for Anoise Player from users

%files
%license COPYING.GPL3
%{_datadir}/%{_basename}/sounds/river.{ogg,png}
%{python3_sitelib}/%{wheel_name}-%{version}.dist-info/

#------------------------------------------------------------------------------

%prep
%setup -qn community

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

cp -r %{buildroot}%{python3_sitelib}%{_datadir} %{buildroot}%{_prefix}/
mkdir -p %{buildroot}%{_datadir}/licenses/%{name}/
cp -r %{buildroot}%{python3_sitelib}/%{wheel_name}-%{version}.dist-info/COPYING.GPL3 %{buildroot}%{_datadir}/licenses/%{name}/
rm -rf %{buildroot}%{python3_sitelib}%{_prefix}/

%py_byte_compile %{python3} %{buildroot}%{_datadir}/%{_basename}/

#------------------------------------------------------------------------------

%changelog
* Sun Oct 13 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.0.1-3
- Fedora 41 Mass Rebuild

* Tue Jun 18 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.0.1-2
- refactoring of spec file

* Thu Apr 11 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.0.1-1
- initial package
