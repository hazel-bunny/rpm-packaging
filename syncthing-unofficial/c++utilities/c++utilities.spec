Name:           c++utilities

%global _basename cpp-utilities
%global forgeurl https://github.com/Martchus/%{_basename}
Version:        5.24.9
%forgemeta

%define soversion 5

Release:        1%{?dist}
Summary:        Common C++ classes and routines
License:        GPL-2.0-or-later

URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  cmake >= 3.17
BuildRequires:  pkgconfig(cppunit) >= 1.14.0
BuildRequires:  gcc-c++

%description
Common C++ classes and routines such as argument parser, IO and conversion utilities.

%package -n lib%{name}%{soversion}
Summary:        Common C++ classes and routines

%description -n lib%{name}%{soversion}
Common C++ classes and routines such as argument parser, IO and conversion utilities.

%package devel
Summary:        Devel files for %{name}
Requires:       cmake >= 3.9
Requires:       glibc-devel
Requires:       lib%{name}%{soversion} = %{version}
Requires:       libstdc++-devel

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

%post -n lib%{name}%{soversion} -p /sbin/ldconfig
%postun -n lib%{name}%{soversion} -p /sbin/ldconfig

%files -n lib%{name}%{soversion}
%license LICENSE
%{_libdir}/lib%{name}.so.%{soversion}*

%files devel
%doc README.md
%{_includedir}/%{name}
%{_datadir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
