%global style k4oxygen
%global dev 10110111

%global forgeurl https://github.com/%{dev}/%{style}
%global commit 9a65c1ebe90ba0169a3ea73441d89291bee19d71
%global date 20240603
%forgemeta

Name:    %{style}
Version: 0
Release: 3%{?dist}
Summary: Variant of KDE4 Oxygen widget theme
License: LGPL-2.1
URL:     %{forgeurl}
Source:  %{forgesource}

BuildRequires: cmake

#Qt6
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6DBus)
BuildRequires: qt6-qtbase-private-devel
BuildRequires: qt6-rpm-macros

# Qt5
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5DBus)
BuildRequires: qt5-rpm-macros

# Qt4
BuildRequires: pkgconfig(Qt)

Requires: %{style}-common
Requires: (%{style}-qt4 if qt)
Requires: (%{style}-qt5 if qt5-qtbase)
Requires: (%{style}-qt6 if qt6-qtbase)

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

%files
#nothing

#-------------------------------------------------------------------------------

%package  common
Summary:  Common files for k4oxygen widget style
Enhances: %{style}

%description common
%{summary}

%files common
%license COPYING
%doc README.md

#-----------------------------------------------------------------------------

%package  qt4
Summary:  Variant of KDE4 Oxygen widget theme for Qt4
Requires: %{style}-common
Enhances: %{style}

%description qt4
K4Oxygen is a variant of KDE4 Oxygen widget theme, released from KDE
dependencies and supported for Qt4, Qt5, and Qt6.

This package contains the Qt4 style.

%files qt4
%{_qt4_plugindir}/styles/%{style}.so

#-----------------------------------------------------------------------------

%package  qt5
Summary:  Variant of KDE4 Oxygen widget theme for Qt5
Requires: %{style}-common
Enhances: %{style}

%description qt5
K4Oxygen is a variant of KDE4 Oxygen widget theme, released from KDE
dependencies and supported for Qt4, Qt5, and Qt6.

This package contains the Qt5 style.

%files qt5
%{_qt5_plugindir}/styles/%{style}.so

#-----------------------------------------------------------------------------

%package  qt6
Summary:  Variant of KDE4 Oxygen widget theme for Qt6
Requires: %{style}-common
Enhances: %{style}

%description qt6
K4Oxygen is a variant of KDE4 Oxygen widget theme, released from KDE
dependencies and supported for Qt4, Qt5, and Qt6.

This package contains the Qt6 style.

%files qt6
%{_qt6_plugindir}/styles/%{style}.so

#-----------------------------------------------------------------------------

%prep
%forgesetup
sed -i 's/set(X11_FOUND TRUE)/set(X11_FOUND FALSE)/g' CMakeLists.txt

%build
# Build for Qt 4
%global _vpath_builddir %{_target_platform}-qt4
%cmake -DQT_VERSION=4 -B %{_vpath_builddir}
%cmake_build
%undefine _vpath_builddir

# Build for Qt 5
%global _vpath_builddir %{_target_platform}-qt5
%cmake -DQT_VERSION=5 -B %{_vpath_builddir}
%cmake_build
%undefine _vpath_builddir

# Build for Qt 6
/usr/bin/patch -p1 -s < %{_sourcedir}/qt6x11_wayland.patch
%global _vpath_builddir %{_target_platform}-qt6
%cmake -DQT_VERSION=6 -B %{_vpath_builddir}
%cmake_build
%undefine _vpath_builddir

%install
%global _vpath_builddir %{_target_platform}-qt4
%cmake_install
%undefine _vpath_builddir

%global _vpath_builddir %{_target_platform}-qt5
%cmake_install
%undefine _vpath_builddir

%global _vpath_builddir %{_target_platform}-qt6
%cmake_install
%undefine _vpath_builddir

%changelog
%autochangelog
