%global forgeurl https://github.com/10110111/k4oxygen
%global branch qt6x11
%global commit 6a60f887f76c714d9a2c0f4c1a4d2ec36fd47617
%global date 20230513
%forgemeta

Name:       qt6-style-k4oxygen
Version:    0
Release:    %autorelease
Summary:    Variant of KDE4 Oxygen widget theme for Qt6
License:    LGPLv2.1
URL:        %{forgeurl}
Source:     %{forgesource}

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

%description -n qt6-style-k4oxygen
K4Oxygen is a variant of KDE4 Oxygen widget theme, released from KDE
dependencies and supported for Qt4, Qt5, and Qt6.

This package contains the Qt6 style.

%files -n qt6-style-k4oxygen
%{_qt6_plugindir}/styles/k4oxygen.so

%prep
%forgeautosetup

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
