%global _basename anoise
%global _suffix gui
%global wheel_name %{_basename}_%{_suffix}

Name:           %{_basename}-%{_suffix}
Version:        0.0.4
Release:        %autorelease
Summary:        Ambient Noise Player GUI
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

Requires:       gtk3
Requires:       webkit2gtk4.0
Requires:       anoise

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
mkdir -p %{buildroot}%{_datadir}/licenses/%{name}/
cp -r %{buildroot}%{python3_sitelib}/%{wheel_name}-%{version}.dist-info/COPYING.GPL3 %{buildroot}%{_datadir}/licenses/%{name}/
rm -rf %{buildroot}%{python3_sitelib}%{_prefix}/

%py_byte_compile %{python3} %{buildroot}%{_datadir}/%{_basename}/

%files
%license COPYING.GPL3
%{_datadir}/%{_basename}/%{_basename}.ui
%pycached %{_datadir}/%{_basename}/view.py
%{python3_sitelib}/%{wheel_name}-%{version}.dist-info/

%changelog
%autochangelog
