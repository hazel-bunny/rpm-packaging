#
# spec file for package syncthingtray-qt6
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Martchus
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define reponame syncthingtray
%define cfg qt6
%define libver 12

# disable web view under PowerPC and s390x (Qt WebEngine not available)
%ifnarch ppc ppc64 ppc64le s390x i386 i486 i586 i686
%define webview_provider webengine
%else
%define webview_provider none
%endif

# disable KDE integrations for now
%define disable_kde_integrations OFF

# define _qt6_pluginsdir macro for Fedora
%if 0%{?fedora_version}
%define _qt6_pluginsdir %{_libdir}/qt6/plugins
%endif

# avoid dependency to qt5qmlimport(martchus.syncthingplasmoid.0) >= 6
%global __requires_exclude (martchus.syncthingplasmoid.0)
%global __provides_exclude (martchus.syncthingplasmoid.0)

Name:           %{reponame}-%{cfg}
Version:        1.4.13
Release:        %autorelease
Summary:        Tray application for Syncthing
License:        GPL-2.0-or-later
Group:          System/Packages
URL:            https://github.com/Martchus/%{reponame}
Source:         https://github.com/Martchus/%{reponame}/archive/v%{version}/%{reponame}-%{version}.tar.gz

BuildRequires:  cmake >= 3.17
BuildRequires:  cppunit-devel >= 1.14.0
BuildRequires:  gcc-c++
BuildRequires:  c++utilities-devel
BuildRequires:  boost-devel > 1.75

BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
%if "%{webview_provider}" == "webengine"
BuildRequires:  cmake(Qt6WebEngineWidgets)
%endif
%if "%{disable_kde_integrations}" == "OFF"
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigCore)
BuildRequires:  cmake(KF6IO)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
%endif
BuildRequires:  pkgconfig
BuildRequires:  qtforkawesome-%{cfg}-devel
BuildRequires:  qtquickforkawesome-%{cfg}-devel
BuildRequires:  qtutilities-%{cfg}-devel
BuildRequires:  syncthing
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Qt6-based tray application for Syncthing

%package -n syncthingctl-%{cfg}
Summary:        Simple command line application to control Syncthing
Group:          System/Packages

%description -n syncthingctl-%{cfg}
Simple command line application to control Syncthing (part of Syncthing Tray)

%package -n syncthingplasmoid-%{cfg}
Summary:        Widget for Plasma 6 desktop to control Syncthing
Group:          System/Packages

%description -n syncthingplasmoid-%{cfg}
Widget for Plasma 6 desktop to control Syncthing (part of Syncthing Tray)

%package -n libsyncthingconnector-%{cfg}%{libver}
Summary:        C++ library to access Syncthing
Group:          System/Packages
Provides:       libsyncthingconnector-%{cfg} = %{version}
Obsoletes:      libsyncthingconnector-%{cfg} < %{version}

%description -n libsyncthingconnector-%{cfg}%{libver}
C++ library to access Syncthing (backend library of Syncthing Tray)

%package -n syncthingconnector-%{cfg}-devel
Summary:        Devel files for libsyncthingconnector-%{cfg}
Group:          Development/Libraries/C and C++
Requires:       c++utilities-devel
Requires:       libsyncthingconnector-%{cfg}%{libver} = %{version}
Requires:       qtutilities-%{cfg}-devel

%description -n syncthingconnector-%{cfg}-devel
C++ library to access Syncthing (backend library of Syncthing Tray) - development files

%package -n libsyncthingmodel-%{cfg}%{libver}
Summary:        Qt6 models for Syncthing data
Group:          System/Packages
Requires:       qtforkawesomeiconengine-%{cfg}
Provides:       libsyncthingmodel-%{cfg} = %{version}
Obsoletes:      libsyncthingmodel-%{cfg} < %{version}

%description -n libsyncthingmodel-%{cfg}%{libver}
Qt models for Syncthing data (backend library of Syncthing Tray)

%package -n syncthingmodel-%{cfg}-devel
Summary:        Devel files for libsyncthingmodel-%{cfg}
Group:          Development/Libraries/C and C++
Requires:       libsyncthingmodel-%{cfg}%{libver} = %{version}
Requires:       syncthingconnector-%{cfg}-devel

%description -n syncthingmodel-%{cfg}-devel
Qt models for Syncthing data (backend library of Syncthing Tray)  - development files

%package -n libsyncthingwidgets-%{cfg}%{libver}
Summary:        Qt6 widgets for Syncthing tray
Group:          System/Packages
Requires:       qtforkawesomeiconengine-%{cfg}
Provides:       libsyncthingwidgets-%{cfg} = %{version}
Obsoletes:      libsyncthingwidgets-%{cfg} < %{version}

%description -n libsyncthingwidgets-%{cfg}%{libver}
Qt widgets for Syncthing tray (backend library of Syncthing Tray)

%package -n syncthingwidgets-%{cfg}-devel
Summary:        Devel files for libsyncthingmodel-%{cfg}
Group:          Development/Libraries/C and C++
Requires:       libsyncthingwidgets-%{cfg}%{libver} = %{version}
Requires:       syncthingmodel-%{cfg}-devel

%description -n syncthingwidgets-%{cfg}-devel
Qt widgets for Syncthing tray (backend library of Syncthing Tray)  - development files

%package -n syncthingfileitemaction-%{cfg}
Summary:        KIO file item action for Syncthing
Group:          System/Packages

%description -n syncthingfileitemaction-%{cfg}
KIO plugin to show Syncthing actions in Dolphin context menu

%prep
%setup -q -n %{reponame}-%{version}

%build
%cmake \
  -DCONFIGURATION_NAME:STRING="%{cfg}" \
  -DCONFIGURATION_DISPLAY_NAME="Qt 6" \
  -DCONFIGURATION_PACKAGE_SUFFIX_QTUTILITIES:STRING="-%{cfg}" \
  -DLIB_SYNCTHING_CONNECTOR_CONFIGURATION_TARGET_SUFFIX:STRING="%{cfg}" \
  -DSYNCTHINGFILEITEMACTION_CONFIGURATION_TARGET_SUFFIX:STRING="%{cfg}" \
  -DLIB_SYNCTHING_MODEL_CONFIGURATION_TARGET_SUFFIX:STRING="%{cfg}" \
  -DSYNCTHINGPLASMOID_CONFIGURATION_TARGET_SUFFIX:STRING="%{cfg}" \
  -DSYNCTHINGWIDGETS_CONFIGURATION_TARGET_SUFFIX:STRING="%{cfg}" \
  -DSYNCTHINGCTL_CONFIGURATION_TARGET_SUFFIX:STRING="%{cfg}" \
  -DSYNCTHINGTRAY_CONFIGURATION_TARGET_SUFFIX:STRING="%{cfg}" \
  -DQT_PACKAGE_PREFIX:STRING='Qt6' \
  -DKF_PACKAGE_PREFIX:STRING='KF6' \
  -DQUICK_GUI:BOOL=NO \
  -DBUILTIN_TRANSLATIONS:BOOL=ON \
  -DBUILD_SHARED_LIBS:BOOL=ON \
  -DNO_PLASMOID:BOOL=%{disable_kde_integrations} \
  -DNO_FILE_ITEM_ACTION_PLUGIN:BOOL=%{disable_kde_integrations} \
  -DQT_PLUGIN_DIR=%{_qt6_pluginsdir} \
  -DWEBVIEW_PROVIDER:STRING=%{webview_provider} \
  -DJS_PROVIDER:STRING=qml
%cmake_build

%check
export QT_QPA_PLATFORM=offscreen
export SYNCTHING_TEST_TIMEOUT_FACTOR=10
export SYNCTHINGTRAY_WIZARD_SETUP_DETECTION_TIMEOUT=5000
export LD_LIBRARY_PATH="$PWD/%{__cmake_builddir}/connector:$PWD/%{__cmake_builddir}/testhelper:$LD_LIBRARY_PATH"
%cmake_build --target check

%install
%cmake_install

# remove devel files for plugins
%if "%{disable_kde_integrations}" == "OFF"
rm -r %{buildroot}/%{_libdir}/pkgconfig/syncthingfileitemaction-%{cfg}.pc
rm -r %{buildroot}/%{_libdir}/pkgconfig/syncthingplasmoid-%{cfg}.pc
rm -r %{buildroot}/%{_datadir}/syncthingfileitemaction-%{cfg}
rm -r %{buildroot}/%{_datadir}/syncthingplasmoid-%{cfg}
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post -n libsyncthingconnector-%{cfg}%{libver} -p /sbin/ldconfig
%postun -n libsyncthingconnector-%{cfg}%{libver} -p /sbin/ldconfig

%post -n libsyncthingmodel-%{cfg}%{libver} -p /sbin/ldconfig
%postun -n libsyncthingmodel-%{cfg}%{libver} -p /sbin/ldconfig

%post -n libsyncthingwidgets-%{cfg}%{libver} -p /sbin/ldconfig
%postun -n libsyncthingwidgets-%{cfg}%{libver} -p /sbin/ldconfig

%post -n syncthingctl-%{cfg} -p /sbin/ldconfig
%postun -n syncthingctl-%{cfg} -p /sbin/ldconfig

%if "%{disable_kde_integrations}" == "OFF"
%post -n syncthingplasmoid-%{cfg} -p /sbin/ldconfig
%postun -n syncthingplasmoid-%{cfg} -p /sbin/ldconfig

%post -n syncthingfileitemaction-%{cfg} -p /sbin/ldconfig
%postun -n syncthingfileitemaction-%{cfg} -p /sbin/ldconfig
%endif

%files
%doc README.md
%{_bindir}/syncthingtray-%{cfg}
%{_datadir}/applications/syncthingtray-%{cfg}.desktop
%if 0%{?sle_version} && 0%{?sle_version} <= 120400
%else
%{_datadir}/metainfo/syncthingtray-%{cfg}.appdata.xml
%endif
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/syncthingtray-%{cfg}.svg
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/syncthingtray-%{cfg}

%files -n syncthingctl-%{cfg}
%{_bindir}/syncthingctl-%{cfg}
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/syncthingctl-%{cfg}

%files -n libsyncthingconnector-%{cfg}%{libver}
%{_libdir}/libsyncthingconnector-%{cfg}.so.*

%files -n syncthingconnector-%{cfg}-devel
%{_includedir}/syncthingconnector-%{cfg}
%{_libdir}/libsyncthingconnector-%{cfg}.so
%{_libdir}/pkgconfig/syncthingconnector-%{cfg}.pc
%dir %{_datadir}/syncthingconnector-%{cfg}
%{_datadir}/syncthingconnector-%{cfg}/cmake

%files -n libsyncthingmodel-%{cfg}%{libver}
%{_libdir}/libsyncthingmodel-%{cfg}.so.*

%files -n syncthingmodel-%{cfg}-devel
%{_includedir}/syncthingmodel-%{cfg}
%{_libdir}/libsyncthingmodel-%{cfg}.so
%{_libdir}/pkgconfig/syncthingmodel-%{cfg}.pc
%dir %{_datadir}/syncthingmodel-%{cfg}
%{_datadir}/syncthingmodel-%{cfg}/cmake

%files -n libsyncthingwidgets-%{cfg}%{libver}
%{_libdir}/libsyncthingwidgets-%{cfg}.so.*

%files -n syncthingwidgets-%{cfg}-devel
%{_includedir}/syncthingwidgets-%{cfg}
%{_libdir}/libsyncthingwidgets-%{cfg}.so
%{_libdir}/pkgconfig/syncthingwidgets-%{cfg}.pc
%dir %{_datadir}/syncthingwidgets-%{cfg}
%{_datadir}/syncthingwidgets-%{cfg}/cmake

%if "%{disable_kde_integrations}" == "OFF"
%files -n syncthingfileitemaction-%{cfg}
%dir %{_qt6_pluginsdir}/kf6/kfileitemaction
%{_qt6_pluginsdir}/kf6/kfileitemaction/libsyncthingfileitemaction-%{cfg}.so
%{_datadir}/metainfo/syncthingfileitemaction-%{cfg}.appdata.xml

%files -n syncthingplasmoid-%{cfg}
%dir %{_qt6_pluginsdir}/plasma/applets
%{_qt6_pluginsdir}/plasma/applets/martchus.syncthingplasmoid-%{cfg}.so
%{_datadir}/metainfo/syncthingplasmoid-%{cfg}.appdata.xml
%dir %{_datadir}/plasma
%dir %{_datadir}/plasma/plasmoids
%dir %{_datadir}/plasma/plasmoids/martchus.syncthingplasmoid-%{cfg}
%{_datadir}/plasma/plasmoids/martchus.syncthingplasmoid-%{cfg}/*
%endif

%changelog
* Sun Feb 25 2024 Dipta Biswas <dabiswas112@gmail.com>
- Build with plasma support
* Fri Feb 16 2024 Marius Kittler <marius.kittler@suse.com>
- Update to 1.4.13
* Fri Feb 16 2024 Marius Kittler <marius.kittler@suse.com>
- Initial import
