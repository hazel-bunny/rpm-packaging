%global _basename PlastikStyle
%global forgeurl https://github.com/MartinF99/%{_basename}
%global tag 1.0.2
%global date 20230619
# %%global commit 15db58b0c85663f2d3d43a531c0f865234e5f9bf
# %%global shortcommit %%(c=%%{commit}; echo ${c:0:7})
%forgemeta

Name:     plastikstyle
Version:  %tag
Release:  %autorelease
License:  LGPLv2.1
Summary:  Fork of QPlastiqueStyle from qt5-styleplugins and a port to qt6

URL:      %{forgeurl}
Source:   %{forgesource}

BuildRequires: cmake

#Qt5
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Gui)
BuildRequires: qt5-rpm-macros

#Qt6
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Gui)
BuildRequires: qt6-rpm-macros

Requires:      plastikstyle-common
Requires:      (qt5-style-plastik if qt5-qtbase)
Requires:      (qt6-style-plastik if qt6-qtbase)

%description
Plastik style - used by default for KDE3.4 and KDE3.5
This is a fork of QPlastiqueStyle from qt5-styleplugins and a port to qt6.

%files
#nothing

#-------------------------------------------------------------------------------

%package     common
Summary:     Common files for plastik widget style

%description common
%{summary}

%files       common
%license     LICENSE
%doc         README.md

#-------------------------------------------------------------------------------

%package -n     qt5-style-plastik
Summary:        Plastik widget style for Qt 5
Requires:       plastikstyle-common

%description -n qt5-style-plastik
%{summary}

%files -n qt5-style-plastik
%{_qt5_plugindir}/styles/libplastikstyle5.so

#-------------------------------------------------------------------------------

%package -n     qt6-style-plastik
Summary:        Plastik widget style for Qt 6
Requires:       plastikstyle-common

%description -n qt6-style-plastik
%{summary}

%files -n qt6-style-plastik
%{_qt6_plugindir}/styles/libplastikstyle6.so

#-------------------------------------------------------------------------------

%prep
%forgeautosetup

%build
%cmake -DENABLE_ALL=on
%cmake_build

%install
%cmake_install

%changelog
%autochangelog
