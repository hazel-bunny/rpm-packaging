Name:           anoise
Version:        0.0.36
Release:        2%{?dist}
Summary:        Ambient Noise Player
License:        GPLv3
URL:            https://costales.github.io/projects/%{name}
Source:         https://launchpad.net/~costales/+archive/ubuntu/%{name}/+sourcefiles/%{name}/%{version}/%{name}_%{version}.tar.gz
Patch0:         setup.patch

#------------------------------------------------------------------------------

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  libxcrypt-compat
BuildRequires:  python3-build
BuildRequires:  python3-devel
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-gstreamer1
BuildRequires:  python3-installer
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel

Requires:       gstreamer1
Requires:       gtk3
Requires:       libappindicator-gtk3
Requires:       python3-gstreamer1
Requires:       webkit2gtk4.0
Requires:       %{name}-media

Recommends:     %{name}-community-extension1
Recommends:     %{name}-community-extension2
Recommends:     %{name}-community-extension3
Recommends:     %{name}-community-extension4
Recommends:     %{name}-community-extension5
Recommends:     %{name}-gui

#------------------------------------------------------------------------------

%description
Ambient Noise Player. Relax or concentrate with a noise

%files
%license COPYING.GPL3
%doc README

%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/preferences.ui

%pycached %{_datadir}/%{name}/%{name}.py
%pycached %{_datadir}/%{name}/preferences.py
%pycached %{_datadir}/%{name}/sound_menu.py
%pycached %{_datadir}/%{name}/utils.py

%{python3_sitelib}/%{name}-%{version}.dist-info/

%{_datadir}/icons/hicolor/{16x16,48x48}/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo

#------------------------------------------------------------------------------

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
mkdir -p %{buildroot}%{_datadir}/licenses/%{name}/
cp -r %{buildroot}%{python3_sitelib}/%{name}-%{version}.dist-info/COPYING.GPL3 %{buildroot}%{_datadir}/licenses/%{name}/
rm -rf %{buildroot}%{python3_sitelib}%{_prefix}/

%py_byte_compile %{python3} %{buildroot}%{_datadir}/%{name}/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

#------------------------------------------------------------------------------

%changelog
* Tue Jun 18 2024 Dipta Biswas <dabiswas112@gmail.com> - 0.0.36-2
- refactoring of spec file

* Thu Apr 11 2024 Dipta Biswas <dabiswas112@gmail.com> - 0.0.36-1
- initial package
