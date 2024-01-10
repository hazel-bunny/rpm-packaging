Name:           anoise-media
Version:        0.0.17
Release:        %autorelease
Summary:        Ambient Noise Library
License:        GPLv3
URL:            https://costales.github.io/projects/anoise
Source:         https://launchpad.net/~costales/+archive/ubuntu/anoise/+sourcefiles/%{name}/%{version}/%{name}_%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-installer
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel

Enhances:       anoise

%description
Ambient Noise Library. Sounds and icons for Anoise Player

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# This file is included in anoise-gui
rm %{buildroot}%{_datadir}/%{name}/%{name}.ui

cp -r %{buildroot}%{python3_sitelib}%{_datadir} %{buildroot}%{_prefix}/
cp -r %{buildroot}%{python3_sitelib}/%{name}-%{version}.dist-info/COPYING.GPL3 %{buildroot}%{_datadir}/licenses/%{name}/
rm -rf %{buildroot}%{python3_sitelib}/

%py_byte_compile %{python3} %{buildroot}%{_libdir}/%{name}/*.py

%files
%license COPYING.GPL3
%doc README changelog.gz copyright
%{_datadir}/anoise/sounds/
%{python3_sitelib}/%{name}-%{version}.dist-info/

%changelog
%autochangelog
