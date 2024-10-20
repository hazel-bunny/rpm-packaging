%global _basename qtforkawesome
%global forgeurl0 https://github.com/Martchus/%{_basename}
Version:        0.2.2

%global _base_lib Fork-Awesome
%global forgeurl1 https://github.com/ForkAwesome/%{_base_lib}
%global tag1 1.2.0
%global date1 20210827

%forgemeta -a

%define cfg qt6
%define soname 1

Name:           %{_basename}-%{cfg}
Release:        1%{?dist}
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

#------------------------------------------------------------------

%package -n lib%{_basename}%{soname}-%{cfg}
Summary:        Library that bundles ForkAwesome for use within Qt applications
Provides:       lib%{_basename} = %{version}
Obsoletes:      lib%{_basename} < %{version}

%description -n lib%{_basename}%{soname}-%{cfg}
Library that bundles ForkAwesome for use within Qt applications.

%files -n lib%{_basename}%{soname}-%{cfg}
%license LICENSE
%{_libdir}/lib%{_basename}-%{cfg}.so.*

#------------------------------------------------------------------

%package devel
Summary:        Devel files for %{_basename}-%{cfg}
Requires:       c++utilities-devel
Requires:       lib%{_basename}%{soname}-%{cfg} = %{version}
Requires:       qtforkawesomeiconengine-%{cfg} = %{version}
Requires:       qtutilities-%{cfg}-devel

%description devel
Development files for %{_basename}-%{cfg}

%files devel
%doc README.md
%{_includedir}/%{_basename}-%{cfg}
%{_datadir}/%{_basename}-%{cfg}
%{_datadir}/%{_basename}iconengine-%{cfg}
%{_libdir}/pkgconfig/%{_basename}-%{cfg}.pc
%{_libdir}/pkgconfig/%{_basename}iconengine-%{cfg}.pc
%{_libdir}/lib%{_basename}-%{cfg}.so

#------------------------------------------------------------------

%package -n libqtquickforkawesome%{soname}-%{cfg}
Summary:        Library that bundles ForkAwesome for use within Qt Quick applications
Provides:       libqtquickforkawesome-%{cfg}%{_basename} = %{version}
Obsoletes:      libqtquickforkawesome-%{cfg}%{_basename} < %{version}

%description -n libqtquickforkawesome%{soname}-%{cfg}
Library that bundles ForkAwesome for use within Qt Quick applications.

%files -n libqtquickforkawesome%{soname}-%{cfg}
%{_libdir}/libqtquickforkawesome-%{cfg}.so.*

#------------------------------------------------------------------

%package -n qtquickforkawesome-%{cfg}-devel
Summary:        Devel files for qtquickforkawesome-%{cfg}
Requires:       %{_basename}-%{cfg}-devel
Requires:       libqtquickforkawesome%{soname}-%{cfg} = %{version}

%description -n qtquickforkawesome-%{cfg}-devel
Development files for qtquickforkawesome-%{cfg}

%files -n qtquickforkawesome-%{cfg}-devel
%{_includedir}/qtquickforkawesome-%{cfg}
%{_datadir}/qtquickforkawesome-%{cfg}
%{_libdir}/pkgconfig/qtquickforkawesome-%{cfg}.pc
%{_libdir}/libqtquickforkawesome-%{cfg}.so

#------------------------------------------------------------------

%package -n qtforkawesomeiconengine-%{cfg}
Summary:        Qt icon engine for %{_basename}-%{cfg}
Requires:       lib%{_basename}%{soname}-%{cfg} = %{version}

%description -n qtforkawesomeiconengine-%{cfg}
Qt icon engine plugin for %{_basename}-%{cfg}

%files -n qtforkawesomeiconengine-%{cfg}
%{_qt6_plugindir}/iconengines/lib%{_basename}iconengine-%{cfg}.so

#------------------------------------------------------------------

%prep
# %%forgesetup -a

%setup -q -D -b 1 -n %{_base_lib}-%{tag1}
%setup -q -n %{_basename}-%{version}

%build
%cmake -DCONFIGURATION_NAME:STRING="%{cfg}" -DCONFIGURATION_DISPLAY_NAME="Qt 6" \
  -DBUILTIN_TRANSLATIONS:BOOL=ON -DCONFIGURATION_TARGET_SUFFIX:STRING="%{cfg}" \
  -DCONFIGURATION_PACKAGE_SUFFIX_QTUTILITIES:STRING="-%{cfg}" \
  -DQT_PACKAGE_PREFIX:STRING='Qt6' -DQT_PLUGIN_DIR=%{_qt6_plugindir} \
  -DFORK_AWESOME_FONT_FILE="%{_builddir}/%{_base_lib}-%{tag1}/fonts/forkawesome-webfont.ttf" \
  -DFORK_AWESOME_ICON_DEFINITIONS="%{_builddir}/%{_base_lib}-%{tag1}/src/icons/icons.yml"
%cmake_build

%check
export QT_QPA_PLATFORM=offscreen
export LD_LIBRARY_PATH="$PWD/%{__cmake_builddir}:$LD_LIBRARY_PATH"
%cmake_build --target check

%install
%cmake_install

#------------------------------------------------------------------

%changelog
* Thu Oct 17 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.2.2-1
- Update to version 0.2.2

* Fri Sep 20 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.2.1-1
- Update to version 0.2.1

* Mon Aug 12 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.2.0-4
- Rebuild for qtutilities 6.14.2-1

* Sat Jul 6 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.2.0-3
- Adopt from obs://home:mkittler
