%global _basename Kvantum

%global _vpath_srcdir %{_basename}

Name:           kvantum
Version:        1.0.10
Release:        %autorelease
Epoch:          1
Summary:        SVG-based theme engine for Qt, KDE and LXQt
License:        GPLv3
URL:            https://github.com/tsujan/%{_basename}
Source:         %url/archive/V%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  desktop-file-utils

#Qt4
BuildRequires:  pkgconfig(Qt)
BuildRequires:  kdelibs-devel

#Qt5
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  qt5-rpm-macros

#KF5
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  kde-filesystem
BuildRequires:  kf5-rpm-macros

#Qt6
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Designer)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  qt6-rpm-macros

Requires:       %{name}-data
Requires:       %{name}-manager

Requires:       (qt4-style-%{name} if qt)
Requires:       (qt5-style-%{name} if qt5-qtbase)
Requires:       (qt6-style-%{name} if qt6-qtbase)

Requires:       hicolor-icon-theme

%description
Kvantum is an SVG-based theme engine for Qt, KDE and LXQt, with an emphasis on
elegance, usability and practicality.

Kvantum has a default dark theme, which is inspired by the default theme of
Enlightenment. Creation of realistic themes like that for KDE was the first
reason to make Kvantum but it goes far beyond its default theme: you could make
themes with very different looks and feels for it, whether they be
photorealistic or cartoonish, 3D or flat, embellished or minimalistic, or
something in between, and Kvantum will let you control almost every aspect of Qt
widgets.

Kvantum also comes with extra themes that are installed as root with Qt5
installation and can be selected and activated by using Kvantum Manager.

%files
#nothing

#-----------------------------------------------------------------------------

%package manager
Summary:    Application for using and tweaking Kvantum themes

Requires:   kvantum-data
Requires:   qt5-style-kvantum

Recommends: (qt4-style-kvantum if qt)
Recommends: (qt6-style-kvantum if qt6-qtbase)

Enhances:   kvantum

%description manager
Kvantum is an SVG-based theme engine for Qt, KDE and LXQt, with an emphasis on
elegance, usability and practicality.

This package contains Kvantum manager.

%files manager -f %{name}.lang
%{_bindir}/kvantummanager
%{_bindir}/kvantumpreview
%{_datadir}/applications/kvantummanager.desktop
%dir %{_datadir}/kvantumpreview
%dir %{_datadir}/kvantumpreview/translations
%dir %{_datadir}/kvantummanager
%dir %{_datadir}/kvantummanager/translations

#-----------------------------------------------------------------------------

%package data
Summary:    Common data for Kvantum

BuildArch:  noarch

Enhances:   kvantum

%description data
Kvantum is an SVG-based theme engine for Qt, KDE and LXQt, with an emphasis on
elegance, usability and practicality.

This package contains the data needed by Kvantum.

%files data
%license Kvantum/COPYING
%doc Kvantum/ChangeLog
%doc Kvantum/NEWS
%doc Kvantum/README.md
%doc Kvantum/doc/*
%{_datadir}/Kvantum/
%{_datadir}/icons/hicolor/scalable/apps/kvantum.svg

#-----------------------------------------------------------------------------

%package    color-schemes
Summary:    Color schemes provided by Kvantum

BuildArch:  noarch

Enhances:   kvantum

%description color-schemes
Kvantum is an SVG-based theme engine for Qt, KDE and LXQt, with an emphasis on
elegance, usability and practicality.

This package contains the KDE color schemes provided by Kvantum.

%files color-schemes
%{_kde4_appsdir}/color-schemes/Kv*.colors
%{_kf5_datadir}/color-schemes/Kv*.colors

#-----------------------------------------------------------------------------

%package -n qt4-style-kvantum
Summary:    SVG-based theme engine for Qt4, KDE and LXQt

Requires:   kvantum-data

Recommends: kvantum-manager

Enhances:   kvantum

%description -n qt4-style-kvantum
Kvantum is an SVG-based theme engine for Qt, KDE and LXQt, with an emphasis on
elegance, usability and practicality.

This package contains the Qt4 style.

%files -n qt4-style-kvantum
%{_qt4_plugindir}/styles/libkvantum.so

#-----------------------------------------------------------------------------

%package -n qt5-style-kvantum
Summary:    SVG-based theme engine for Qt5, KDE and LXQt

Requires:   kvantum-data

Recommends: kvantum-manager

Enhances:   kvantum

%description -n qt5-style-kvantum
Kvantum is an SVG-based theme engine for Qt, KDE and LXQt, with an emphasis on
elegance, usability and practicality.

This package contains the Qt5 style.

%files -n qt5-style-kvantum
%{_qt5_plugindir}/styles/libkvantum.so

#-----------------------------------------------------------------------------

%package -n qt6-style-kvantum
Summary:    SVG-based theme engine for Qt6, KDE and LXQt

Requires:   kvantum-data

Recommends: kvantum-manager

Enhances:   kvantum

%description -n qt6-style-kvantum
Kvantum is an SVG-based theme engine for Qt, KDE and LXQt, with an emphasis on
elegance, usability and practicality.

This package contains the Qt6 style.

%files -n qt6-style-kvantum
%{_qt6_plugindir}/styles/libkvantum.so

#-----------------------------------------------------------------------------

%prep
%autosetup -n Kvantum-%{version}

%build
# Build for Qt 4
%global _vpath_builddir %{_vpath_srcdir}/%{_target_platform}-qt4
%cmake -DENABLE_QT4=ON -DENABLE_QT5=OFF -B %{_vpath_builddir}
%cmake_build
%undefine _vpath_builddir

# Build for Qt 5
%global _vpath_builddir %{_vpath_srcdir}/%{_target_platform}-qt5
%cmake -DENABLE_QT4=OFF -DENABLE_QT5=ON -B %{_vpath_builddir}
%cmake_build
%undefine _vpath_builddir

# Build for Qt 6
%global _vpath_builddir %{_vpath_srcdir}/%{_target_platform}-qt6
%cmake -DENABLE_QT4=OFF -DENABLE_QT5=OFF -B %{_vpath_builddir}
%cmake_build
%undefine _vpath_builddir

%install
%global _vpath_builddir %{_vpath_srcdir}/%{_target_platform}-qt4
%cmake_install
%undefine _vpath_builddir

%global _vpath_builddir %{_vpath_srcdir}/%{_target_platform}-qt5
%cmake_install
%undefine _vpath_builddir

%global _vpath_builddir %{_vpath_srcdir}/%{_target_platform}-qt6
%cmake_install
%undefine _vpath_builddir

mkdir -p %{buildroot}%{_datadir}/doc
cp -r Kvantum/doc %{buildroot}%{_datadir}/doc/kvantum-data

# desktop-file-validate doesn't recognize LXQt
sed -i "s|LXQt|X-LXQt|" %{buildroot}%{_datadir}/applications/kvantummanager.desktop

%find_lang %{name} --all-name --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/kvantummanager.desktop

%changelog
%autochangelog
