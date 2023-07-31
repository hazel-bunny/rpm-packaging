%global forgeurl https://github.com/themix-project/oomox-qt-styleplugin
%global commit e15cd47a127f898753b3fc9c6c4b3063f3506656
%global date 20230108
%forgemeta

Name:    oomox-qt
Version: 1.4.2
Release: %autorelease
Summary: Native style to bend Qt5/Qt6 applications to look with Themix colors
License: GPLv2+, LGPLv2+
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

#Qt6
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6DBus)
BuildRequires: qt6-rpm-macros

Requires: (qt5-style-oomox if qt5-qtbase)
Requires: (qt6-style-oomox if qt6-qtbase)

%description
A native style to bend Qt5/Qt6 applications to look with Themix colors.

This style is based on Qt Adwaita theme.

%files
# nothing

#-------------------------------------------------------------------------------

%package -n  liboomox-qt5
Summary:     Oomox Qt5 library

%description -n liboomox-qt5
%{summary}

%files -n liboomox-qt5
%{_libdir}/liboodwaitaqt.so.*
%{_libdir}/liboodwaitaqtpriv.so.*

#-------------------------------------------------------------------------------

%package -n  liboomox-qt5-devel
Summary:     Development files for oomox Qt5 library

%description -n liboomox-qt5-devel
This package contains libraries and header files for developing applications
that use liboomox-qt5.

%files -n liboomox-qt5-devel
%dir %{_includedir}/OodwaitaQt
%{_includedir}/OodwaitaQt/*.h
%dir %{_libdir}/cmake/OodwaitaQt
%{_libdir}/cmake/OodwaitaQt/*.cmake
%{_libdir}/pkgconfig/oodwaita-qt.pc
%{_libdir}/liboodwaitaqt.so
%{_libdir}/liboodwaitaqtpriv.so

#-----------------------------------------------------------------------------

%package -n qt5-style-oomox
Summary:    Native style to bend Qt5 applications to look with Themix colors
Requires:   liboomox-qt5
Enhances:   oomox-qt

%description -n qt5-style-oomox
%{summary}

%files -n qt5-style-oomox
%license LICENSE.GPL2 LICENSE.LGPL2
%doc AUTHORS README.md
%{_qt5_plugindir}/styles/oodwaita.so

#-------------------------------------------------------------------------------

%package -n  liboomox-qt6
Summary:     Oomox Qt6 library

%description -n liboomox-qt6
%{summary}

%files -n liboomox-qt6
%{_libdir}/liboodwaitaqt6.so.*
%{_libdir}/liboodwaitaqt6priv.so.*

#-------------------------------------------------------------------------------

%package -n  liboomox-qt6-devel
Summary:     Development files for oomox Qt5 library

%description -n liboomox-qt6-devel
This package contains libraries and header files for developing applications
that use liboomox-qt6.

%files -n liboomox-qt6-devel
%dir %{_includedir}/OodwaitaQt6
%{_includedir}/OodwaitaQt6/*.h
%dir %{_libdir}/cmake/OodwaitaQt6
%{_libdir}/cmake/OodwaitaQt6/*.cmake
%{_libdir}/pkgconfig/oodwaita-qt6.pc
%{_libdir}/liboodwaitaqt6.so
%{_libdir}/liboodwaitaqt6priv.so

#-----------------------------------------------------------------------------

%package -n qt6-style-oomox
Summary:    Native style to bend Qt6 applications to look with Themix colors
Requires:   liboomox-qt6
Enhances:   oomox-qt

%description -n qt6-style-oomox
%{summary}

%files -n qt6-style-oomox
%license LICENSE.GPL2 LICENSE.LGPL2
%doc AUTHORS README.md
%{_qt6_plugindir}/styles/oodwaita.so

#-----------------------------------------------------------------------------

%prep
%forgeautosetup

%build
# Build for Qt 6
%global _vpath_builddir %{_target_platform}-qt6
%cmake -DUSE_QT6=ON -B %{_vpath_builddir}
%cmake_build
%undefine _vpath_builddir

# Build for Qt 5
%global _vpath_builddir %{_target_platform}-qt5
%cmake -DUSE_QT6=OFF -B %{_vpath_builddir}
%cmake_build
%undefine _vpath_builddir

%install
%global _vpath_builddir %{_target_platform}-qt6
%cmake_install
%undefine _vpath_builddir

%global _vpath_builddir %{_target_platform}-qt5
%cmake_install
%undefine _vpath_builddir

%changelog
%autochangelog
