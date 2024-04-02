%global style plastik
%global dev MartinF99
%global _basename PlastikStyle

%global forgeurl https://github.com/%{dev}/%{_basename}
%global tag 1.0.4
%global date 20240319
%forgemeta

Name:     %{style}style
Version:  %tag
Release:  %autorelease
License:  LGPLv2.1
Summary:  QStyle imitating KDE 3's Plastik

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

Requires:      %{name}-common
Requires:      (%{name}-qt5 if qt5-qtbase)
Requires:      (%{name}-qt6 if qt6-qtbase)

%description
Plastikstyle is a qstyle for both qt5 and qt6 imitating the look and feel from
KDE3's plastikstyle. This is QPlastiqueStyle forked from qtstyleplugins.

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

%package qt5
Summary:        Plastik widget style for Qt 5
Requires:       %{name}-common

%description qt5
%{summary}

%files qt5
%{_qt5_plugindir}/styles/lib%{name}5.so

#-------------------------------------------------------------------------------

%package qt6
Summary:        Plastik widget style for Qt 6
Requires:       %{name}-common

%description qt6
%{summary}

%files qt6
%{_qt6_plugindir}/styles/lib%{name}6.so

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
