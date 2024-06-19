%global _basename syncthingtray
%global forgeurl https://github.com/Martchus/%{_basename}
Version:        1.5.4
%forgemeta

%define soname 6
%define libver 15
%define cfg qt6

# Build web view only for specific architectures
%ifarch %{qt6_qtwebengine_arches}
%define webview_provider webengine
%else
%define webview_provider none
%endif

# disable KDE integrations (eg plasmoid, file item actions)
%define disable_kde_integrations OFF

# avoid dependency to qt5qmlimport(martchus.syncthingplasmoid.0) >= 6
# %%global __requires_exclude (martchus.syncthingplasmoid.0)
# %%global __provides_exclude (martchus.syncthingplasmoid.0)

Name:           %{_basename}-%{cfg}
Release:        1%{?dist}
Summary:        Tray application for Syncthing
License:        GPL-2.0-or-later

URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  cmake >= 3.17
BuildRequires:  cppunit-devel >= 1.14.0
BuildRequires:  gcc-c++
BuildRequires:  c++utilities-devel
BuildRequires:  boost-devel > 1.75
BuildRequires:  pkgconfig
BuildRequires:  syncthing

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
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
%endif

BuildRequires:  qtforkawesome-%{cfg}-devel
BuildRequires:  qtquickforkawesome-%{cfg}-devel
BuildRequires:  qtutilities-%{cfg}-devel

%description
Qt6-based tray application for Syncthing

%files
%doc README.md
%{_bindir}/%{_basename}-%{cfg}
%{_datadir}/applications/%{_basename}-%{cfg}.desktop
%{_metainfodir}/%{_basename}-%{cfg}.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/%{_basename}-%{cfg}.svg
%{_datadir}/bash-completion/completions/%{_basename}-%{cfg}

#------------------------------------------------------------------

%package -n syncthingctl-%{cfg}
Summary:        Simple command line application to control Syncthing

%description -n syncthingctl-%{cfg}
Simple command line application to control Syncthing (part of Syncthing Tray)

%files -n syncthingctl-%{cfg}
%{_bindir}/syncthingctl-%{cfg}
%{_datadir}/bash-completion/completions/syncthingctl-%{cfg}

#------------------------------------------------------------------

%package -n syncthingplasmoid-%{cfg}
Summary:        Widget for Plasma 6 desktop to control Syncthing

%description -n syncthingplasmoid-%{cfg}
Widget for Plasma 6 desktop to control Syncthing (part of Syncthing Tray)

%if "%{disable_kde_integrations}" == "OFF"
%files -n syncthingplasmoid-%{cfg}
%{_libdir}/pkgconfig/syncthingplasmoid-%{cfg}.pc
%{_qt6_plugindir}/plasma/applets/martchus.syncthingplasmoid-%{cfg}.so
%{_datadir}/syncthingplasmoid-%{cfg}
%{_metainfodir}/syncthingplasmoid-%{cfg}.metainfo.xml
%{_datadir}/plasma/plasmoids/martchus.syncthingplasmoid-%{cfg}/*
%endif

#------------------------------------------------------------------

%package -n syncthingfileitemaction-%{cfg}
Summary:        KIO file item action for Syncthing

%description -n syncthingfileitemaction-%{cfg}
KIO plugin to show Syncthing actions in Dolphin context menu

%if "%{disable_kde_integrations}" == "OFF"
%files -n syncthingfileitemaction-%{cfg}
%{_libdir}/pkgconfig/syncthingfileitemaction-%{cfg}.pc
%{_qt6_plugindir}/kf6/kfileitemaction/libsyncthingfileitemaction-%{cfg}.so
%{_datadir}/syncthingfileitemaction-%{cfg}
%{_metainfodir}/syncthingfileitemaction-%{cfg}.metainfo.xml
%endif

#------------------------------------------------------------------

%package -n libsyncthingconnector%{libver}-%{cfg}
Summary:        C++ library to access Syncthing
Provides:       libsyncthingconnector-%{cfg} = %{version}
Obsoletes:      libsyncthingconnector-%{cfg} < %{version}

%description -n libsyncthingconnector%{libver}-%{cfg}
C++ library to access Syncthing (backend library of Syncthing Tray)

%files -n libsyncthingconnector%{libver}-%{cfg}
%{_libdir}/libsyncthingconnector-%{cfg}.so.*

#------------------------------------------------------------------

%package -n syncthingconnector-%{cfg}-devel
Summary:        Devel files for libsyncthingconnector-%{cfg}
Requires:       c++utilities-devel
Requires:       libsyncthingconnector%{libver}-%{cfg} = %{version}
Requires:       qtutilities-%{cfg}-devel

%description -n syncthingconnector-%{cfg}-devel
C++ library to access Syncthing (backend library of Syncthing Tray) - development files

%files -n syncthingconnector-%{cfg}-devel
%{_includedir}/syncthingconnector-%{cfg}
%{_libdir}/libsyncthingconnector-%{cfg}.so
%{_libdir}/pkgconfig/syncthingconnector-%{cfg}.pc
%{_datadir}/syncthingconnector-%{cfg}/cmake

#------------------------------------------------------------------

%package -n libsyncthingmodel%{libver}-%{cfg}
Summary:        Qt6 models for Syncthing data
Requires:       qtforkawesomeiconengine-%{cfg}
Provides:       libsyncthingmodel-%{cfg} = %{version}
Obsoletes:      libsyncthingmodel-%{cfg} < %{version}

%description -n libsyncthingmodel%{libver}-%{cfg}
Qt models for Syncthing data (backend library of Syncthing Tray)

%files -n libsyncthingmodel%{libver}-%{cfg}
%{_libdir}/libsyncthingmodel-%{cfg}.so.*

#------------------------------------------------------------------

%package -n syncthingmodel-%{cfg}-devel
Summary:        Devel files for libsyncthingmodel-%{cfg}
Requires:       libsyncthingmodel%{libver}-%{cfg} = %{version}
Requires:       syncthingconnector-%{cfg}-devel

%description -n syncthingmodel-%{cfg}-devel
Qt models for Syncthing data (backend library of Syncthing Tray)  - development files

%files -n syncthingmodel-%{cfg}-devel
%{_includedir}/syncthingmodel-%{cfg}
%{_libdir}/libsyncthingmodel-%{cfg}.so
%{_libdir}/pkgconfig/syncthingmodel-%{cfg}.pc
%{_datadir}/syncthingmodel-%{cfg}/cmake

#------------------------------------------------------------------

%package -n libsyncthingwidgets%{libver}-%{cfg}
Summary:        Qt6 widgets for Syncthing tray
Requires:       qtforkawesomeiconengine-%{cfg}
Provides:       libsyncthingwidgets-%{cfg} = %{version}
Obsoletes:      libsyncthingwidgets-%{cfg} < %{version}

%description -n libsyncthingwidgets%{libver}-%{cfg}
Qt widgets for Syncthing tray (backend library of Syncthing Tray)

%files -n libsyncthingwidgets%{libver}-%{cfg}
%{_libdir}/libsyncthingwidgets-%{cfg}.so.*

#------------------------------------------------------------------

%package -n syncthingwidgets-%{cfg}-devel
Summary:        Devel files for libsyncthingmodel-%{cfg}
Requires:       libsyncthingwidgets%{libver}-%{cfg} = %{version}
Requires:       syncthingmodel-%{cfg}-devel

%description -n syncthingwidgets-%{cfg}-devel
Qt widgets for Syncthing tray (backend library of Syncthing Tray)  - development files

%files -n syncthingwidgets-%{cfg}-devel
%{_includedir}/syncthingwidgets-%{cfg}
%{_libdir}/libsyncthingwidgets-%{cfg}.so
%{_libdir}/pkgconfig/syncthingwidgets-%{cfg}.pc
%{_datadir}/syncthingwidgets-%{cfg}/cmake

#------------------------------------------------------------------

%prep
%forgeautosetup

%build
%cmake -DCONFIGURATION_NAME:STRING="%{cfg}" -DCONFIGURATION_DISPLAY_NAME="Qt 6" \
  -DCONFIGURATION_PACKAGE_SUFFIX_QTUTILITIES:STRING="-%{cfg}" \
  -DLIB_SYNCTHING_CONNECTOR_CONFIGURATION_TARGET_SUFFIX:STRING="%{cfg}" \
  -DSYNCTHINGFILEITEMACTION_CONFIGURATION_TARGET_SUFFIX:STRING="%{cfg}" \
  -DLIB_SYNCTHING_MODEL_CONFIGURATION_TARGET_SUFFIX:STRING="%{cfg}" \
  -DSYNCTHINGPLASMOID_CONFIGURATION_TARGET_SUFFIX:STRING="%{cfg}" \
  -DSYNCTHINGWIDGETS_CONFIGURATION_TARGET_SUFFIX:STRING="%{cfg}" \
  -DSYNCTHINGCTL_CONFIGURATION_TARGET_SUFFIX:STRING="%{cfg}" \
  -DSYNCTHINGTRAY_CONFIGURATION_TARGET_SUFFIX:STRING="%{cfg}" \
  -DQT_PACKAGE_PREFIX:STRING='Qt6' -DKF_PACKAGE_PREFIX:STRING='KF6' \
  -DQUICK_GUI:BOOL=NO -DBUILTIN_TRANSLATIONS:BOOL=ON \
  -DNO_PLASMOID:BOOL=%{disable_kde_integrations} \
  -DNO_FILE_ITEM_ACTION_PLUGIN:BOOL=%{disable_kde_integrations} \
  -DQT_PLUGIN_DIR=%{_qt6_plugindir} -DJS_PROVIDER:STRING=qml \
  -DWEBVIEW_PROVIDER:STRING=%{webview_provider}
%cmake_build

%check
export QT_QPA_PLATFORM=offscreen
export SYNCTHING_TEST_TIMEOUT_FACTOR=10
export SYNCTHINGTRAY_WIZARD_SETUP_DETECTION_TIMEOUT=5000
export LD_LIBRARY_PATH="$PWD/%{__cmake_builddir}/connector:$PWD/%{__cmake_builddir}/testhelper:$LD_LIBRARY_PATH"
%cmake_build --target check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{_basename}-%{cfg}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{_basename}-%{cfg}.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/syncthingplasmoid-%{cfg}.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/syncthingfileitemaction-%{cfg}.metainfo.xml

%install
%cmake_install

#------------------------------------------------------------------

%changelog
%autochangelog
