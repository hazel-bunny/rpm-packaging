%global _basename anoise
%global _suffix media
%global wheel_name %{_basename}_%{_suffix}

Name:           %{_basename}-%{_suffix}
Version:        0.0.17
Release:        2%{?dist}
Summary:        Ambient Noise Library
License:        GPLv3
URL:            https://costales.github.io/projects/anoise
Source:         https://launchpad.net/~costales/+archive/ubuntu/anoise/+sourcefiles/%{name}/%{version}/%{name}_%{version}.tar.gz

#------------------------------------------------------------------------------

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-installer
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel

Enhances:       anoise

#------------------------------------------------------------------------------

%description
Ambient Noise Library. Sounds and icons for Anoise Player

%files
%license COPYING.GPL3
%doc README

%dir %{_datadir}/%{_basename}/sounds/
%{_datadir}/%{_basename}/sounds/coffee_shop.{ogg,png}
%{_datadir}/%{_basename}/sounds/fire.{ogg,png}
%{_datadir}/%{_basename}/sounds/forest.{ogg,png}
%{_datadir}/%{_basename}/sounds/night.{ogg,png}
%{_datadir}/%{_basename}/sounds/rain.{ogg,png}
%{_datadir}/%{_basename}/sounds/sea.{ogg,png}
%{_datadir}/%{_basename}/sounds/storm.{ogg,png}
%{_datadir}/%{_basename}/sounds/wind.{ogg,png}

%{python3_sitelib}/%{wheel_name}-%{version}.dist-info/

#------------------------------------------------------------------------------

%prep
%setup -qn media

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
* Tue Jun 18 2024 Dipta Biswas <dabiswas112@gmail.com> - 0.0.17-2
- refactoring of spec file

* Thu Apr 11 2024 Dipta Biswas <dabiswas112@gmail.com> - 0.0.17-1
- initial package
