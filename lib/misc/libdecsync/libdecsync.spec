%global forgeurl https://github.com/39aldo39/libdecsync
%global commit a512d924345a33c52a3f7f2719ed001777ca6350
%global date 20220914
%forgemeta

Name:    libdecsync
Version: 2.2.1
Release: %autorelease
Summary: Library for DecSync
License: GPLv2+
URL:     %{forgeurl}
Source:  %{forgesource}

BuildRequires:  make
BuildRequires:  java-17-openjdk-headless
BuildRequires:  ncurses-compat-libs

%description
libdecsync is a multiplatform library for synchronizing using DecSync

%files
%license LICENSE.txt
%doc README.md
%_libdir/libdecsync.so
%_datadir/pkgconfig/decsync.pc

#-----------------------------------------------------------------------

%package devel
Summary:  Development files for libdecsync
Requires: libdecsync

%description devel
This package includes the header files you will need to compile
applications supporting DecSync

%files devel
%_includedir/libdecsync.h
%_includedir/libdecsync_api.h

#-----------------------------------------------------------------------

%prep
%forgeautosetup -p1

%build
mkdir -p build/bin/linuxX64/releaseShared
touch build/bin/linuxX64/releaseShared/decsync.pc
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%changelog
%autochangelog
