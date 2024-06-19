%global _basename qtutilities
%global forgeurl https://github.com/Martchus/%{_basename}
Version:        6.14.1
%forgemeta

%define soname 6
%define cfg qt6

Name:           %{_basename}-%{cfg}
Release:        1%{?dist}
Summary:        Common Qt related C++ classes and routines such as dialogs, widgets and models
License:        GPL-2.0-or-later

URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  cmake >= 3.17
BuildRequires:  gcc-c++
BuildRequires:  c++utilities-devel
BuildRequires:  pkgconfig

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)

%description
Common Qt related C++ classes and routines used by my applications such as dialogs, widgets and models.

#------------------------------------------------------------------

%package -n lib%{_basename}%{soname}-%{cfg}
Summary:        Common Qt related C++ classes and routines such as dialogs, widgets and models

%description -n lib%{_basename}%{soname}-%{cfg}
Common Qt related C++ classes and routines used by my applications such as dialogs, widgets and models.

%files -n lib%{_basename}%{soname}-%{cfg}
%license LICENSE
%{_libdir}/lib%{_basename}-%{cfg}.so.%{soname}*

#------------------------------------------------------------------

%package devel
Summary:        Devel files for %{_basename}
Requires:       c++utilities-devel
Requires:       lib%{_basename}%{soname}-%{cfg} = %{version}

%description devel
Development files for %{_basename}

%files devel
%doc README.md
%{_includedir}/%{_basename}-%{cfg}
%{_datadir}/%{_basename}-%{cfg}
%{_libdir}/pkgconfig/%{_basename}-%{cfg}.pc
%{_libdir}/lib%{_basename}-%{cfg}.so

#------------------------------------------------------------------

%prep
%forgeautosetup

%build
%cmake -DCONFIGURATION_NAME:STRING="%{cfg}" -DCONFIGURATION_DISPLAY_NAME="Qt 6" \
  -DCONFIGURATION_TARGET_SUFFIX:STRING="%{cfg}" -DQT_PACKAGE_PREFIX:STRING='Qt6' \
  -DBUILTIN_TRANSLATIONS:BOOL=ON
%cmake_build

%check
export QT_QPA_PLATFORM=offscreen
export LD_LIBRARY_PATH="$PWD/%{__cmake_builddir}:$LD_LIBRARY_PATH"
%cmake_build --target check

%install
%cmake_install

#------------------------------------------------------------------

%changelog
%autochangelog
