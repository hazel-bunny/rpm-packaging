#
# spec file for package qtforkawesome-qt6
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2021 Martchus
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


%define reponame qtforkawesome
%define reponame_forkawesome Fork-Awesome
%define version_forkawesome 1.2.0
%define cfg qt6
%define soname 1

# define _libqt5_plugindir macro for Fedora
%if 0%{?fedora_version}
%define _qt6_pluginsdir %{_libdir}/qt6/plugins
%endif

Name:           %{reponame}-%{cfg}
Version:        0.1.0
Release:        %autorelease
Summary:        Library that bundles ForkAwesome for use within Qt applications
License:        GPL-2.0-or-later
Group:          System/Packages
URL:            https://github.com/Martchus/%{reponame}
Source0:        https://github.com/Martchus/%{reponame}/archive/v%{version}/%{reponame}-%{version}.tar.gz
Source1:        https://github.com/ForkAwesome/%{reponame_forkawesome}/archive/refs/tags/%{version_forkawesome}.tar.gz

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
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Library that bundles ForkAwesome for use within Qt applications.

%package -n lib%{reponame}-%{cfg}%{soname}
Summary:        Library that bundles ForkAwesome for use within Qt applications
Group:          System/Libraries
Provides:       lib%{reponame} = %{version}
Obsoletes:      lib%{reponame} < %{version}

%description -n lib%{reponame}-%{cfg}%{soname}
Library that bundles ForkAwesome for use within Qt applications.

%package devel
Summary:        Devel files for %{reponame}-%{cfg}
Group:          Development/Libraries/C and C++
Requires:       c++utilities-devel
Requires:       lib%{reponame}-%{cfg}%{soname} = %{version}
Requires:       qtforkawesomeiconengine-%{cfg} = %{version}
Requires:       qtutilities-%{cfg}-devel

%description devel
Development files for %{reponame}-%{cfg}

%package -n libqtquickforkawesome-%{cfg}%{soname}
Summary:        Library that bundles ForkAwesome for use within Qt Quick applications
Group:          System/Packages
Provides:       libqtquickforkawesome-%{cfg}%{reponame} = %{version}
Obsoletes:      libqtquickforkawesome-%{cfg}%{reponame} < %{version}

%description -n libqtquickforkawesome-%{cfg}%{soname}
Library that bundles ForkAwesome for use within Qt Quick applications.

%package -n qtquickforkawesome-%{cfg}-devel
Summary:        Devel files for qtquickforkawesome-%{cfg}
Group:          Development/Libraries/C and C++
Requires:       %{reponame}-%{cfg}-devel
Requires:       libqtquickforkawesome-%{cfg}%{soname} = %{version}

%description -n qtquickforkawesome-%{cfg}-devel
Development files for qtquickforkawesome-%{cfg}

%package -n qtforkawesomeiconengine-%{cfg}
Summary:        Qt icon engine for %{reponame}-%{cfg}
Group:          Development/Libraries/C and C++
Requires:       lib%{reponame}-%{cfg}%{soname} = %{version}

%description -n qtforkawesomeiconengine-%{cfg}
Qt icon engine plugin for %{reponame}-%{cfg}

%prep
%setup -q -D -b 1 -n %{reponame_forkawesome}-%{version_forkawesome}
%setup -q -n %{reponame}-%{version}

%build
%cmake \
  -DBUILD_SHARED_LIBS:BOOL=ON \
  -DCONFIGURATION_NAME:STRING="%{cfg}" \
  -DCONFIGURATION_DISPLAY_NAME="Qt 6" \
  -DCONFIGURATION_TARGET_SUFFIX:STRING="%{cfg}" \
  -DCONFIGURATION_PACKAGE_SUFFIX_QTUTILITIES:STRING="-%{cfg}" \
  -DQT_PACKAGE_PREFIX:STRING='Qt6' \
  -DBUILTIN_TRANSLATIONS:BOOL=ON \
  -DQT_PLUGIN_DIR=%{_qt6_pluginsdir} \
  -DFORK_AWESOME_FONT_FILE="%{_builddir}/%{reponame_forkawesome}-%{version_forkawesome}/fonts/forkawesome-webfont.ttf" \
  -DFORK_AWESOME_ICON_DEFINITIONS="%{_builddir}/%{reponame_forkawesome}-%{version_forkawesome}/src/icons/icons.yml"
%cmake_build

%check
export QT_QPA_PLATFORM=offscreen
export LD_LIBRARY_PATH="$PWD/%{__cmake_builddir}:$LD_LIBRARY_PATH"
%cmake_build --target check

%install
%cmake_install

%post -n lib%{reponame}-%{cfg}%{soname} -p /sbin/ldconfig
%postun -n lib%{reponame}-%{cfg}%{soname} -p /sbin/ldconfig

%post -n libqtquickforkawesome-%{cfg}%{soname} -p /sbin/ldconfig
%postun -n libqtquickforkawesome-%{cfg}%{soname} -p /sbin/ldconfig

%files -n lib%{reponame}-%{cfg}%{soname}
%license LICENSE
%{_libdir}/lib%{reponame}-%{cfg}.so.*

%files -n libqtquickforkawesome-%{cfg}%{soname}
%{_libdir}/libqtquickforkawesome-%{cfg}.so.*

%files devel
%doc README.md
%{_includedir}/%{reponame}-%{cfg}
%{_datadir}/%{reponame}-%{cfg}
%{_datadir}/%{reponame}iconengine-%{cfg}
%{_libdir}/pkgconfig/%{reponame}-%{cfg}.pc
%{_libdir}/pkgconfig/%{reponame}iconengine-%{cfg}.pc
%{_libdir}/lib%{reponame}-%{cfg}.so

%files -n qtquickforkawesome-%{cfg}-devel
%{_includedir}/qtquickforkawesome-%{cfg}
%{_datadir}/qtquickforkawesome-%{cfg}
%{_libdir}/pkgconfig/qtquickforkawesome-%{cfg}.pc
%{_libdir}/libqtquickforkawesome-%{cfg}.so

%files -n qtforkawesomeiconengine-%{cfg}
%dir %{_qt6_pluginsdir}/iconengines
%{_qt6_pluginsdir}/iconengines/lib%{reponame}iconengine-%{cfg}.so

%changelog
* Fri Feb 16 2024 Marius Kittler <marius.kittler@suse.com>
- Update to 0.1.0
* Sat Dec  9 2023 Marius Kittler <marius.kittler@suse.com>
- Initial import
