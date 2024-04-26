%global forgeurl https://github.com/vladimir-kraus/phantomstyle
%global branch modern-style
%global commit 3f43774c06fef1edfcec9b6d5d3b8e8247221a02
%global date 20230718
%forgemeta

Name:    phantom-modern-style
Version: 0
Release: %autorelease
Summary: Modern cross-platform QStyle
License: LGPLv2.1, MIT
URL:     %{forgeurl}
Source:  %{forgesource}

BuildRequires: pkgconfig

#Qt5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: qt5-rpm-macros

#Qt6
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: qt6-rpm-macros

Requires:      phantom-modern-style-common
Requires:      (qt5-style-phantom-modern if qt5-qtbase)
Requires:      (qt6-style-phantom-modern if qt6-qtbase)

%description
Phantom is a QStyle for Qt which began as an overhaul of QFusionStyle. Similar
to Fusion, it's designed to be a looks-the-same cross-platform style. It looks
native to nobody, but familiar to many. It has the visual appearance of a
traditional GUI, and does not adopt a "modern flat" style. Compared to Fusion,
it has many fixes, objective improvements, and subjective improvements.

%files
#nothing

#-------------------------------------------------------------------------------

%package     common
Summary:     Common files for modern phantom widget style

%description common
%{summary}

%files       common
%license     LICENSE
%doc         README.md

#-------------------------------------------------------------------------------

%package -n     qt5-style-phantom-modern
Summary:        Modern phantom widget style for Qt 5
Requires:       phantom-modernstyle-common

%description -n qt5-style-phantom-modern
%{summary}

%files -n qt5-style-phantom-modern
%{_qt5_plugindir}/styles/libphantommodernstyleplugin.so

#-------------------------------------------------------------------------------

%package -n     qt6-style-phantom-modern
Summary:        Modern phantom widget style for Qt 6
Requires:       phantom-modernstyle-common

%description -n qt6-style-phantom-modern
%{summary}

%files -n qt6-style-phantom-modern
%{_qt6_plugindir}/styles/libphantommodernstyleplugin.so

#-------------------------------------------------------------------------------

%prep
%forgeautosetup

%build
cd src/styleplugin

%global _vpath_builddir %{_target_platform}-qt5
mkdir %{_vpath_builddir} && pushd %{_vpath_builddir}
%qmake_qt5_wrapper ../phantomstyleplugin.pro
%make_build
popd
%undefine _vpath_builddir

rm -rf .qmake.stash

%global _vpath_builddir %{_target_platform}-qt6
mkdir %{_vpath_builddir} && pushd %{_vpath_builddir}
%qmake_qt6_wrapper ../phantomstyleplugin.pro
%make_build
popd
%undefine _vpath_builddir

rm -rf .qmake.stash

%install
mkdir -p %{buildroot}%{_qt5_plugindir}/styles/
mkdir -p %{buildroot}%{_qt6_plugindir}/styles/

cd src/styleplugin

%global _vpath_builddir %{_target_platform}-qt5
pushd %{_vpath_builddir}
install -Dm755 libphantommodernstyleplugin.so %{buildroot}%{_qt5_plugindir}/styles/
popd
%undefine _vpath_builddir

%global _vpath_builddir %{_target_platform}-qt6
pushd %{_vpath_builddir}
install -Dm755 libphantommodernstyleplugin.so %{buildroot}%{_qt6_plugindir}/styles/
popd
%undefine _vpath_builddir

%changelog
%autochangelog
