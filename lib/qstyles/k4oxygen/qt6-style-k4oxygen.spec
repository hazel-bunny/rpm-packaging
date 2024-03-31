%global style k4oxygen
%global dev 10110111

%global forgeurl https://github.com/%{dev}/%{style}
%global commit b0291eff019d4ccd498970d0c8323e49e74a2fec
%global date 20240329
%forgemeta

Name:       qt6-style-%{style}
Version:    0
Release:    %autorelease
Summary:    Variant of KDE4 Oxygen widget theme for Qt6
License:    LGPLv2.1
URL:        %{forgeurl}
Source:     %{forgesource}
Patch0:     6a60f887f76c714d9a2c0f4c1a4d2ec36fd47617.patch

BuildRequires: cmake
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(x11)

#Qt6
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6DBus)
BuildRequires: qt6-qtbase-private-devel
BuildRequires: qt6-rpm-macros

Requires:   k4oxygen-common

%description -n qt6-style-%{style}
K4Oxygen is a variant of KDE4 Oxygen widget theme, released from KDE
dependencies and supported for Qt4, Qt5, and Qt6.

This package contains the Qt6 style.

%files -n qt6-style-%{style}
%{_qt6_plugindir}/styles/%{style}.so

%prep
%forgeautosetup -p1

%build
# %%global _vpath_builddir %%{_target_platform}-qt6
%cmake -DQT_VERSION=6 # -B %%{_vpath_builddir}
%cmake_build
# %%undefine _vpath_builddir

%install
# %%global _vpath_builddir %%{_target_platform}-qt6
%cmake_install
# %%undefine _vpath_builddir

%changelog
%autochangelog
