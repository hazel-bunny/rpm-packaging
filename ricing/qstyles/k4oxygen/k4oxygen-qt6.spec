%global style k4oxygen
%global qt 6
%global dev 10110111

%global forgeurl https://github.com/%{dev}/%{style}
%global commit b0291eff019d4ccd498970d0c8323e49e74a2fec
%global date 20240329
%forgemeta

Name:    %{style}-qt%{qt}
Version: 0
Release: 3%{?dist}
Summary: Variant of KDE4 Oxygen widget theme for Qt%{qt}
License: LGPL-2.1
URL:     %{forgeurl}
Source:  %{forgesource}
Patch0:  oxygenconfig.patch

BuildRequires: cmake
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6DBus)
# BuildRequires: qt6-qtbase-private-devel
BuildRequires: qt%{qt}-rpm-macros

%description
K4Oxygen is a variant of KDE4 Oxygen widget theme, released from KDE
dependencies and supported for Qt4, Qt5, and Qt6. It is based on
oxygen-transparent for KDE4, but currently has some **limitations**:

- no window decorations implementation
- no configuration utility
- translucency in Qt5 version is in experimental stage, and unchecked
  completely in Qt6 version

The theme does read Oxygen and global KDE settings similarly to how
oxygen-gtk does it.

This package contains the Qt%{qt} style.

%files
%license COPYING
%doc README.md
%{_qt6_plugindir}/styles/%{style}.so

%prep
%forgeautosetup -p1
sed -i 's/set(X11_FOUND TRUE)/set(X11_FOUND FALSE)/g' CMakeLists.txt

%build
%cmake -DQT_VERSION=%{qt}
%cmake_build

%install
%cmake_install

%changelog
* Sat Oct 19 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0-3
- Initial split package
