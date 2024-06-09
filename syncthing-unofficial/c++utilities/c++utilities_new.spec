Name:           c++utilities

%global _basename cpp-utilities
%global forgeurl https://github.com/Martchus/%{_basename}
Version:        5.24.8
%forgemeta

%define soname 5

Release:        1%{?dist}
Summary:        Common C++ classes and routines
License:        GPL-2.0-or-later

URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  cmake >= 3.17
BuildRequires:  cppunit-devel >= 1.14.0
BuildRequires:  gcc-c++

%description
Common C++ classes and routines such as argument parser, IO and conversion utilities.

%package -n lib%{name}%{soname}
Summary:        Common C++ classes and routines

%description -n lib%{name}%{soname}
Common C++ classes and routines such as argument parser, IO and conversion utilities.

%package devel
Summary:        Devel files for %{name}
Requires:       cmake >= 3.9
Requires:       glibc-devel
Requires:       lib%{name}%{soname} = %{version}
Requires:       libstdc++-devel
Requires:       pkg-config

%description devel
Development files for %{name}

%prep
%forgeautosetup

%build
%cmake -DBUILD_SHARED_LIBS:BOOL=ON
%cmake_build

%check
export LD_LIBRARY_PATH="$PWD/%{__cmake_builddir}:$LD_LIBRARY_PATH"
%cmake_build --target check

%install
%cmake_install

%post -n lib%{name}%{soname} -p /sbin/ldconfig
%postun -n lib%{name}%{soname} -p /sbin/ldconfig

%files -n lib%{name}%{soname}
%license LICENSE
%{_libdir}/lib%{name}.so.%{soname}*

%files devel
%doc README.md
%{_includedir}/%{name}
%{_datadir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
