%global _basename qtforkawesome
%global forgeurl0 https://github.com/Martchus/%{_basename}
Version:        0.2.0

%global _base_lib Fork-Awesome
%global forgeurl1 https://github.com/ForkAwesome/%{_base_lib}
%global tag1 1.2.0
%global date1 20210827

%forgemeta -a

%define cfg qt6
%define soname 1

Name:           %{_basename}-%{cfg}
Release:        3%{?dist}
Summary:        Library that bundles ForkAwesome for use within Qt applications
License:        GPL-2.0-or-later
URL:            %{forgeurl0}

Source0:        %{forgesource0}
Source1:        %{forgesource1}

BuildRequires:  cmake >= 3.17
BuildRequires:  gcc-c++
BuildRequires:  c++utilities-devel
BuildRequires:  perl-YAML-LibYAML
BuildRequires:  pkgconfig
BuildRequires:  qtutilities-%{cfg}-devel

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Test)

%description
Library that bundles ForkAwesome for use within Qt applications.

%package -n lib%{_basename}-%{cfg}%{soname}
Summary:        Library that bundles ForkAwesome for use within Qt applications
Provides:       lib%{_basename} = %{version}
Obsoletes:      lib%{_basename} < %{version}

%description -n lib%{_basename}-%{cfg}%{soname}
Library that bundles ForkAwesome for use within Qt applications.

%package devel
Summary:        Devel files for %{_basename}-%{cfg}
Requires:       c++utilities-devel
Requires:       lib%{_basename}-%{cfg}%{soname} = %{version}
Requires:       qtforkawesomeiconengine-%{cfg} = %{version}
Requires:       qtutilities-%{cfg}-devel

%description devel
Development files for %{_basename}-%{cfg}

%package -n libqtquickforkawesome-%{cfg}%{soname}
Summary:        Library that bundles ForkAwesome for use within Qt Quick applications
Provides:       libqtquickforkawesome-%{cfg}%{_basename} = %{version}
Obsoletes:      libqtquickforkawesome-%{cfg}%{_basename} < %{version}

%description -n libqtquickforkawesome-%{cfg}%{soname}
Library that bundles ForkAwesome for use within Qt Quick applications.

%package -n qtquickforkawesome-%{cfg}-devel
Summary:        Devel files for qtquickforkawesome-%{cfg}
Requires:       %{_basename}-%{cfg}-devel
Requires:       libqtquickforkawesome-%{cfg}%{soname} = %{version}

%description -n qtquickforkawesome-%{cfg}-devel
Development files for qtquickforkawesome-%{cfg}

%package -n qtforkawesomeiconengine-%{cfg}
Summary:        Qt icon engine for %{_basename}-%{cfg}
Requires:       lib%{_basename}-%{cfg}%{soname} = %{version}

%description -n qtforkawesomeiconengine-%{cfg}
Qt icon engine plugin for %{_basename}-%{cfg}

%prep
%forgeautosetup -a

%build
%cmake \
  -DBUILD_SHARED_LIBS:BOOL=ON \
  -DCONFIGURATION_NAME:STRING="%{cfg}" \
  -DCONFIGURATION_DISPLAY_NAME="Qt 6" \
  -DCONFIGURATION_TARGET_SUFFIX:STRING="%{cfg}" \
  -DCONFIGURATION_PACKAGE_SUFFIX_QTUTILITIES:STRING="-%{cfg}" \
  -DQT_PACKAGE_PREFIX:STRING='Qt6' \
  -DBUILTIN_TRANSLATIONS:BOOL=ON \
  -DQT_PLUGIN_DIR=%{_qt6_plugindir} \
  -DFORK_AWESOME_FONT_FILE="%{_builddir}/%{_basename_forkawesome}-%{version_forkawesome}/fonts/forkawesome-webfont.ttf" \
  -DFORK_AWESOME_ICON_DEFINITIONS="%{_builddir}/%{_basename_forkawesome}-%{version_forkawesome}/src/icons/icons.yml"
%cmake_build

%check
export QT_QPA_PLATFORM=offscreen
export LD_LIBRARY_PATH="$PWD/%{__cmake_builddir}:$LD_LIBRARY_PATH"
%cmake_build --target check

%install
%cmake_install

%post -n lib%{_basename}-%{cfg}%{soname} -p /sbin/ldconfig
%postun -n lib%{_basename}-%{cfg}%{soname} -p /sbin/ldconfig

%post -n libqtquickforkawesome-%{cfg}%{soname} -p /sbin/ldconfig
%postun -n libqtquickforkawesome-%{cfg}%{soname} -p /sbin/ldconfig

%files -n lib%{_basename}-%{cfg}%{soname}
%license LICENSE
%{_libdir}/lib%{_basename}-%{cfg}.so.*

%files -n libqtquickforkawesome-%{cfg}%{soname}
%{_libdir}/libqtquickforkawesome-%{cfg}.so.*

%files devel
%doc README.md
%{_includedir}/%{_basename}-%{cfg}
%{_datadir}/%{_basename}-%{cfg}
%{_datadir}/%{_basename}iconengine-%{cfg}
%{_libdir}/pkgconfig/%{_basename}-%{cfg}.pc
%{_libdir}/pkgconfig/%{_basename}iconengine-%{cfg}.pc
%{_libdir}/lib%{_basename}-%{cfg}.so

%files -n qtquickforkawesome-%{cfg}-devel
%{_includedir}/qtquickforkawesome-%{cfg}
%{_datadir}/qtquickforkawesome-%{cfg}
%{_libdir}/pkgconfig/qtquickforkawesome-%{cfg}.pc
%{_libdir}/libqtquickforkawesome-%{cfg}.so

%files -n qtforkawesomeiconengine-%{cfg}
%dir %{_qt6_plugindir}/iconengines
%{_qt6_plugindir}/iconengines/lib%{_basename}iconengine-%{cfg}.so

%changelog
%autochangelog
