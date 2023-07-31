%global forgeurl https://github.com/atolstoy/skulpture
%global commit 725af7dd8cf7d573c36da698321760a1dfc84491
%global date 20230729
%forgemeta

Name:     skulpture
Version:  0
Release:  %autorelease
License:  GPLv3
Summary:  A classic style for Qt5 and Qt6 apps

URL:      %{forgeurl}
Source:   %{forgesource}
#Patch:   reverse-0d8d12f2.patch

BuildRequires: cmake
BuildRequires: extra-cmake-modules

#Qt5
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Gui)
BuildRequires: qt5-rpm-macros

#KF5
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: kf5-rpm-macros

#Qt6
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Gui)
BuildRequires: qt6-rpm-macros

Requires:      skulpture-common
Requires:      (qt5-style-skulpture if qt5-qtbase)
Requires:      (kde-style-skulpture if qt5-qtbase)
Requires:      (qt6-style-skulpture if qt6-qtbase)

%description
This is a re-worked and partially updated code of the original Skulpture style
that was once developed by Christoph Feck. Specifically, this repo is a
continuation of the skulpture-five (a Qt5/KF5 port) branch from 2016.

The purpose of this repo is to provide a working Qt6 port of Skulpture. Even
though it's not a pixel-perfect copy of its namesake for KDE4, it already
provides great consistency between Qt5 and Qt6 apps.

%files
#nothing

#-------------------------------------------------------------------------------

%package     common
Summary:     Common files for skulpture widget style

%description common
%{summary}

%files       common
%license     LICENSE COPYING
%doc         AUTHORS BUGS NEWS NOTES README.md VERSION

#-------------------------------------------------------------------------------

%package -n     kde-style-skulpture
Summary:        Tool to use the skulpture widget style with KDE Plasma
Requires:       skulpture-common
Requires:       qt5-style-skulpture

%description -n kde-style-skulpture
This package contains the kstyle, color scheme and configuration tool for
using the skulpture qstyle with KDE Plasma

%files -n       kde-style-skulpture
%{_datadir}/color-schemes/Skulpture*.colors
%{_datadir}/kstyle/themes/skulpture.themerc
%{_datadir}/kxmlgui5/skulpture

#-------------------------------------------------------------------------------

%package -n     qt5-style-skulpture
Summary:        Plastik widget style for Qt 5
Requires:       skulpture-common
Recommends:     skulpture-config

%description -n qt5-style-skulpture
%{summary}

%files -n       qt5-style-skulpture
%{_qt5_plugindir}/styles/skulpture.so
%{_qt5_plugindir}/kstyle_skulpture_config.so

#-------------------------------------------------------------------------------

%package -n     qt6-style-skulpture
Summary:        Plastik widget style for Qt 6
Requires:       skulpture-common

%description -n qt6-style-skulpture
%{summary}

%files -n       qt6-style-skulpture
%{_qt6_plugindir}/styles/skulpture.so

#-------------------------------------------------------------------------------

%prep
%forgeautosetup -p1

%build
# Build for Qt 5
%global _vpath_builddir %{_target_platform}-qt5
%cmake_kf5 -DUSE_QT6=OFF -DUSE_GUI_CONFIG=ON -B %{_vpath_builddir}
%cmake_build
%undefine _vpath_builddir

# Build for Qt 6
%global _vpath_builddir %{_target_platform}-qt6
%cmake -DUSE_QT6=ON -DUSE_GUI_CONFIG=OFF -B %{_vpath_builddir}
%cmake_build
%undefine _vpath_builddir

%install
%global _vpath_builddir %{_target_platform}-qt5
%cmake_install
%undefine _vpath_builddir

%global _vpath_builddir %{_target_platform}-qt6
%cmake_install
%undefine _vpath_builddir

mkdir -p %{buildroot}%{_datadir}
cp -r color-schemes %{buildroot}%{_datadir}/color-schemes
rm -rf %{buildroot}%{_datadir}/color-schemes/CMakeLists.txt

%changelog
%autochangelog
