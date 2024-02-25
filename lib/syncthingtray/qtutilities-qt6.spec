#
# spec file for package qtutilities-qt6
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2018-2019 Martchus
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


%define reponame qtutilities
%define cfg qt6
%define soname 6

Name:           %{reponame}-%{cfg}
Version:        6.13.4
Release:        1.1
Summary:        Common Qt related C++ classes and routines such as dialogs, widgets and models
License:        GPL-2.0-or-later
Group:          System/Packages
URL:            https://github.com/Martchus/%{reponame}
Source:         https://github.com/Martchus/%{reponame}/archive/v%{version}/%{reponame}-%{version}.tar.gz
BuildRequires:  cmake >= 3.17
%if 0%{?fedora}
%else
BuildRequires:  ninja
%endif
%if 0%{?sle_version} && 0%{?sle_version} < 160000
BuildRequires:  gcc9-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  c++utilities-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Common Qt related C++ classes and routines used by my applications such as dialogs, widgets and models.

%package -n lib%{reponame}-%{cfg}%{soname}
Summary:        Common Qt related C++ classes and routines such as dialogs, widgets and models
Group:          System/Libraries

%description -n lib%{reponame}-%{cfg}%{soname}
Common Qt related C++ classes and routines used by my applications such as dialogs, widgets and models.

%package devel
Summary:        Devel files for %{reponame}
Group:          Development/Libraries/C and C++
Requires:       c++utilities-devel
Requires:       lib%{reponame}-%{cfg}%{soname} = %{version}

%description devel
Development files for %{reponame}

%prep
%setup -q -n %{reponame}-%{version}

%build
%if 0%{?sle_version} && 0%{?sle_version} < 160000
export CC=gcc-9
export CXX=g++-9
%endif
%if 0%{?fedora}
%else
%define __builder ninja
%endif
%cmake \
  -DBUILD_SHARED_LIBS:BOOL=ON \
  -DCONFIGURATION_NAME:STRING="%{cfg}" \
  -DCONFIGURATION_DISPLAY_NAME="Qt 6" \
  -DCONFIGURATION_TARGET_SUFFIX:STRING="%{cfg}" \
  -DQT_PACKAGE_PREFIX:STRING='Qt6' \
  -DBUILTIN_TRANSLATIONS:BOOL=ON
%if 0%{?fedora} && 0%{?fedora_version} < 33
make %{?_smp_mflags}
%else
%cmake_build
%endif

%check
export QT_QPA_PLATFORM=offscreen
%if 0%{?fedora}
%if 0%{?fedora_version} < 33
make %{?_smp_mflags} check
%else
export LD_LIBRARY_PATH="$PWD/%{__cmake_builddir}:$LD_LIBRARY_PATH"
%cmake_build --target check
%endif
%else
cd "%{__builddir}"
export LD_LIBRARY_PATH="$PWD:$LD_LIBRARY_PATH"
%cmake_build check
%endif

%install
%if 0%{?fedora} && 0%{?fedora_version} < 33
DESTDIR=%{buildroot} make %{?_smp_mflags} install
%else
%cmake_install
%endif

%post -n lib%{reponame}-%{cfg}%{soname} -p /sbin/ldconfig
%postun -n lib%{reponame}-%{cfg}%{soname} -p /sbin/ldconfig

%files -n lib%{reponame}-%{cfg}%{soname}
%license LICENSE
%{_libdir}/lib%{reponame}-%{cfg}.so.%{soname}*

%files devel
%doc README.md
%{_includedir}/%{reponame}-%{cfg}
%{_datadir}/%{reponame}-%{cfg}
%{_libdir}/pkgconfig/%{reponame}-%{cfg}.pc
%{_libdir}/lib%{reponame}-%{cfg}.so

%changelog
* Fri Feb 16 2024 Marius Kittler <marius.kittler@suse.com>
- Update to 6.13.4
* Sat Dec  9 2023 Marius Kittler <marius.kittler@suse.com>
- Initial import
