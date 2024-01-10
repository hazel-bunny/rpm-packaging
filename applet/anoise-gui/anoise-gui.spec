%global _basename anoise
%global wheel_name %{_basename}_gui

Name:           %{_basename}-gui
Version:        0.0.4
Release:        %autorelease
Summary:        Ambient Noise Player
License:        GPLv3
URL:            https://costales.github.io/projects/%{_basename}
Source:         https://launchpad.net/~costales/+archive/ubuntu/%{_basename}/+sourcefiles/%{name}/%{version}/%{name}_%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-installer
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  gtk3-devel

Requires:       python3
Requires:       anoise
Requires:       gtk3

Enhances:       anoise

%description
GUI for Ambient Noise Player

%prep
%autosetup -p1 -n %{name}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

cp -r %{buildroot}%{python3_sitelib}%{_datadir} %{buildroot}%{_prefix}/
rm -rf %{buildroot}%{python3_sitelib}/

%py_byte_compile %{python3} %{buildroot}%{_libdir}/%{name}/*.py

%files
%doc changelog.gz copyright
%{_datadir}/%{_basename}/%{_basename}.ui
%{_datadir}/%{_basename}/view.py
%{python3_sitelib}/%{wheel_name}-%{version}.dist-info/

%changelog
%autochangelog
