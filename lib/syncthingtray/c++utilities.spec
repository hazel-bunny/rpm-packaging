#
# spec file for package c++utilities
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2018 Martchus
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


%define reponame c++utilities
%define soname 5

Name:           %{reponame}
Version:        5.24.6
Release:        1
Summary:        Common C++ classes and routines
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/Martchus/cpp-utilities
Source:         https://github.com/Martchus/cpp-utilities/archive/v%{version}/cpp-utilities-%{version}.tar.gz
BuildRequires:  cmake >= 3.17
%if 0%{?fedora}
%else
BuildRequires:  ninja
%endif
BuildRequires:  cppunit-devel >= 1.14.0
%if 0%{?sle_version} && 0%{?sle_version} < 160000
BuildRequires:  gcc9-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Common C++ classes and routines such as argument parser, IO and conversion utilities.

%package -n lib%{reponame}%{soname}
Summary:        Common C++ classes and routines
Group:          System/Libraries

%description -n lib%{reponame}%{soname}
Common C++ classes and routines such as argument parser, IO and conversion utilities.

%package devel
Summary:        Devel files for %{reponame}
Group:          Development/Libraries/C and C++
Requires:       cmake >= 3.9
Requires:       glibc-devel
Requires:       lib%{reponame}%{soname} = %{version}
Requires:       libstdc++-devel
Requires:       pkg-config

%description devel
Development files for %{reponame}

%prep
%setup -q -n cpp-utilities-%{version}

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
  -DBUILD_SHARED_LIBS:BOOL=ON
%if 0%{?fedora} && 0%{?fedora_version} < 33
make %{?_smp_mflags}
%else
%cmake_build
%endif

%check
%if 0%{?fedora}
%if 0%{?fedora_version} < 33
make %{?_smp_mflags} check
%else
export LD_LIBRARY_PATH="$PWD/%{__cmake_builddir}:$LD_LIBRARY_PATH"
%cmake_build --target check
%endif
%else
%if (0%{?sle_version} == 150200 || 0%{?sle_version} == 150300) && 0%{?is_opensuse}
# FIXME: fix tests under Leap 15.2 which fail at some point with "1/1 Test #1: ...........***Exception: SegFault  0.02 sec"
%else
cd "%{__builddir}"
export LD_LIBRARY_PATH="$PWD:$LD_LIBRARY_PATH"
%cmake_build check
%endif
%endif

%install
%if 0%{?fedora} && 0%{?fedora_version} < 33
DESTDIR=%{buildroot} make %{?_smp_mflags} install
%else
%cmake_install
%endif

%post -n lib%{reponame}%{soname} -p /sbin/ldconfig
%postun -n lib%{reponame}%{soname} -p /sbin/ldconfig

%files -n lib%{reponame}%{soname}
%license LICENSE
%{_libdir}/lib%{reponame}.so.%{soname}*

%files devel
%doc README.md
%{_includedir}/%{reponame}
%{_datadir}/%{reponame}
%{_libdir}/pkgconfig/%{reponame}.pc
%{_libdir}/lib%{reponame}.so

%changelog
* Fri Feb 16 2024 Marius Kittler <marius.kittler@suse.com>
- Update to 5.24.6
* Fri Feb 16 2024 Marius Kittler <marius.kittler@suse.com>
- Update to 5.24.7
* Mon Dec 11 2023 Marius Kittler <marius.kittler@suse.com>
- Update to 5.24.4
* Tue Dec  5 2023 Marius Kittler <marius.kittler@suse.com>
- Update to 5.24.3
* Wed Nov 22 2023 Marius Kittler <marius.kittler@suse.com>
- Update to 5.24.2
* Fri Sep  8 2023 Marius Kittler <marius.kittler@suse.com>
- Update to 5.24.1
* Fri Jul  7 2023 Marius Kittler <marius.kittler@suse.com>
- Update to 5.24.0
* Wed Jun  7 2023 Marius Kittler <marius.kittler@suse.com>
- Update to 5.23.0
* Thu Apr  6 2023 Marius Kittler <marius.kittler@suse.com>
- Update to 5.22.0
* Tue Mar  7 2023 Marius Kittler <marius.kittler@suse.com>
- Update to 5.21.0
* Fri Nov  4 2022 Marius Kittler <marius.kittler@suse.com>
- Update to 5.20.0
* Wed Sep  7 2022 Marius Kittler <marius.kittler@suse.com>
- Update to 5.19.0
* Wed Aug  3 2022 Marius Kittler <marius.kittler@suse.com>
- Update to 5.18.0
* Wed Jul  6 2022 Marius Kittler <marius.kittler@suse.com>
- Update to 5.17.0
* Thu Jun  9 2022 Marius Kittler <marius.kittler@suse.com>
- Update to 5.16.0
* Tue May 24 2022 Marius Kittler <marius.kittler@suse.com>
- Update to 5.15.0
* Tue Apr  5 2022 Marius Kittler <marius.kittler@suse.com>
- Update to 5.14.0
* Wed Feb 16 2022 Marius Kittler <marius.kittler@suse.com>
- Update to 5.13.0
* Tue Jan 11 2022 Marius Kittler <marius.kittler@suse.com>
- Update to 5.12.0
* Wed Nov  3 2021 Marius Kittler <marius.kittler@suse.com>
- Update to 5.11.3
* Wed Oct  6 2021 Marius Kittler <marius.kittler@suse.com>
- Update to 5.11.2
* Tue Sep  7 2021 Marius Kittler <marius.kittler@suse.com>
- Update to 5.11.1
* Mon Aug  9 2021 Marius Kittler <marius.kittler@suse.com>
- Update to 5.11.0
* Wed Jul  7 2021 Marius Kittler <marius.kittler@suse.com>
- Update to 5.10.5
* Wed Jun  9 2021 Marius Kittler <marius.kittler@suse.com>
- Update to 5.10.4
* Fri May 14 2021 Marius Kittler <marius.kittler@suse.com>
- Update to 5.10.3
* Wed Apr  7 2021 Marius Kittler <marius.kittler@suse.com>
- Update to 5.10.2
* Wed Feb  3 2021 Marius Kittler <marius.kittler@suse.com>
- Update to 5.10.1
* Thu Dec  3 2020 Marius Kittler <marius.kittler@suse.com>
- Update to 5.9.0
* Wed Nov  4 2020 Marius Kittler <marius.kittler@suse.com>
- Update to 5.8.0
* Mon Oct 12 2020 Marius Kittler <marius.kittler@suse.com>
- Update to 5.7.0
* Wed Aug 12 2020 Marius Kittler <marius.kittler@suse.com>
- Update to 5.6.0
* Fri Jul 10 2020 Marius Kittler <marius.kittler@suse.com>
- Update to 5.5.0
* Thu May  7 2020 Marius Kittler <marius.kittler@suse.com>
- Update to 5.4.0
* Wed Mar 18 2020 Marius Kittler <marius.kittler@suse.com>
- Update to 5.3.0
* Wed Mar 18 2020 Marius Kittler <marius.kittler@suse.com>
- Update to 5.3.0
* Wed Feb  5 2020 Marius Kittler <marius.kittler@suse.com>
- Update to 5.2.0
* Thu Jan  9 2020 Marius Kittler <marius.kittler@suse.com>
- Update to 5.1.0
* Wed Oct  2 2019 Marius Kittler <marius.kittler@suse.com>
- Update to 5.0.1
* Mon Aug 26 2019 Marius Kittler <marius.kittler@suse.com>
- Update to 5.0.0
* Mon Apr 29 2019 Marius Kittler <marius.kittler@suse.com>
- Update to 4.17.1
* Fri Mar  8 2019 Marius Kittler <marius.kittler@suse.com>
- Update to 4.17.0
* Tue Feb 19 2019 Marius Kittler <marius.kittler@suse.com>
- Update to 4.17.0
* Mon Nov  5 2018 Marius Kittler <marius.kittler@suse.com>
- Update to 4.16.0
* Wed Sep 26 2018 Marius Kittler <marius.kittler@suse.com>
- Update to 4.15.0
* Mon Jun  4 2018 marius.kittler@suse.com
- Update to 4.14.2
* Thu May 17 2018 marius.kittler@suse.com
- Update to 4.14.1
* Thu Mar 29 2018 marius.kittler@suse.com
- Update to 4.13.0
* Thu Feb  8 2018 marius.kittler@suse.com
- Fix running tests
* Thu Feb  8 2018 marius.kittler@suse.com
- Support Fedora
* Thu Feb  8 2018 marius.kittler@suse.com
- Allow build under Leap 42.2
* Thu Feb  8 2018 marius.kittler@suse.com
- Fix build dir
* Thu Feb  8 2018 marius.kittler@suse.com
- Update to 4.12.1
* Tue Jan 30 2018 marius.kittler@suse.com
- Update to 4.12.0
* Thu Nov 16 2017 marius.kittler@suse.com
- Fix file conflicts
* Tue Nov  7 2017 marius.kittler@suse.com
- Update to 4.11.0
* Mon Oct  9 2017 marius.kittler@suse.com
- Update to 4.10.0
