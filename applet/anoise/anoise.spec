Name:           anoise
Version:        0.0.36
Release:        %autorelease
Summary:        Ambient Noise Player
License:        GPLv3
URL:            https://costales.github.io/projects/anoise
Source:         https://launchpad.net/~costales/+archive/ubuntu/%{name}/+sourcefiles/%{name}/%{version}/%{name}_%{version}.tar.gz
Patch0:         setup.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-gstreamer1
BuildRequires:  python3-installer
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  libxcrypt-compat

Requires:       webkit2gtk4.0
Requires:       anoise-media
Requires:       libappindicator-gtk3

Recommends:     anoise-community-extension1
Recommends:     anoise-community-extension2
Recommends:     anoise-community-extension3
Recommends:     anoise-community-extension4
Recommends:     anoise-community-extension5
Recommends:     anoise-gui

%description
Ambient Noise Player. Relax or concentrate with a noise

%prep
rm -rf %{name}_%{version}
tar -xzf %{SOURCE0}
mv -f "%{name} " %{name}_%{version}
cd %{name}_%{version}
sed -i 's/anoise.desktop.in/Ambient Noise/g' "%{name}.desktop.in"
%patch 0 -p1

%generate_buildrequires
cd %{name}_%{version}
%pyproject_buildrequires

%build
cd %{name}_%{version}
%pyproject_wheel

%install
cd %{name}_%{version}
%pyproject_install

# This file is included in anoise-gui
rm %{buildroot}%{_datadir}/%{name}/%{name}.ui

cp -r %{buildroot}%{python3_sitelib}%{_datadir} %{buildroot}%{_prefix}/
cp -r %{buildroot}%{python3_sitelib}/%{name}-%{version}.dist-info/COPYING.GPL3 %{buildroot}%{_datadir}/licenses/%{name}/
rm -rf %{buildroot}%{python3_sitelib}%{_prefix}/

%py_byte_compile %{python3} %{buildroot}%{_libdir}/%{name}/*.py

%files
%license COPYING.GPL3
%doc README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{python3_sitelib}/%{name}-%{version}.dist-info/

%changelog
%autochangelog
