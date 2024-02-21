%global forgeurl https://github.com/10110111/k4oxygen
%global commit d6190f579c34148b32fd8ecd64d9bbb270a6900a
%global date 20230916
%forgemeta

Name:    k4oxygen
Version: 0
Release: %autorelease
Summary: Variant of KDE4 Oxygen widget theme
License: LGPLv2.1
URL:     %{forgeurl}
Source:  %{forgesource}

BuildRequires: cmake
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(x11)

#Qt5
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: qt5-rpm-macros

#Qt4
BuildRequires: pkgconfig(Qt)

Requires: %{name}-common
Requires: (qt4-style-%{name} if qt)
Requires: (qt5-style-%{name} if qt5-qtbase)
Requires: (qt6-style-%{name} if qt6-qtbase)

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

%package     common
Summary:     Common files for k4oxygen widget style
Enhances:    k4oxygen

%description common
%{summary}

%files       common
%license COPYING
%doc README.md

#-----------------------------------------------------------------------------

%package -n qt4-style-k4oxygen
Summary:    Variant of KDE4 Oxygen widget theme for Qt4
Requires:   k4oxygen-common
Enhances:   k4oxygen

%description -n qt4-style-k4oxygen
K4Oxygen is a variant of KDE4 Oxygen widget theme, released from KDE
dependencies and supported for Qt4, Qt5, and Qt6.

This package contains the Qt4 style.

%files -n qt4-style-k4oxygen
%{_qt4_plugindir}/styles/k4oxygen.so

#-----------------------------------------------------------------------------

%package -n qt5-style-k4oxygen
Summary:    Variant of KDE4 Oxygen widget theme for Qt5
Requires:   k4oxygen-common
Enhances:   k4oxygen

%description -n qt5-style-k4oxygen
K4Oxygen is a variant of KDE4 Oxygen widget theme, released from KDE
dependencies and supported for Qt4, Qt5, and Qt6.

This package contains the Qt5 style.

%files -n qt5-style-k4oxygen
%{_qt5_plugindir}/styles/k4oxygen.so

#-----------------------------------------------------------------------------

# %%package -n qt6-style-k4oxygen
# Summary:    Variant of KDE4 Oxygen widget theme for Qt6
# Enhances:   k4oxygen
# Requires:   k4oxygen-common
#
# %%description -n qt6-style-k4oxygen
# K4Oxygen is a variant of KDE4 Oxygen widget theme, released from KDE
# dependencies and supported for Qt4, Qt5, and Qt6.
#
# This package contains the Qt6 style.
#
# %%files -n qt6-style-k4oxygen
# %%{_qt6_plugindir}/styles/k4oxygen.so

#-----------------------------------------------------------------------------

%prep
%forgeautosetup

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
# %%global _vpath_builddir %%{_target_platform}-qt6
# %%cmake -DQT_VERSION=6 -B %%{_vpath_builddir}
# %%cmake_build
# %%undefine _vpath_builddir

%install
%global _vpath_builddir %{_target_platform}-qt4
%cmake_install
%undefine _vpath_builddir

%global _vpath_builddir %{_target_platform}-qt5
%cmake_install
%undefine _vpath_builddir

# %%global _vpath_builddir %%{_target_platform}-qt6
# %%cmake_install
# %%undefine _vpath_builddir

%changelog
%autochangelog
