Name:           plasma-custom-desktop-menu

%global forgeurl https://github.com/MatMoul/plasma-containmentactions-customdesktopmenu
%global commit bc699db15eee9f9784baeaccfbc693cd55023f57
%global date 20240309
%forgemeta

Version:        0.2.0
Release:        2%{?dist}
Summary:        Custom desktop menu for Plasma 6
License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source:         %{forgesource}

#------------------------------------------------------------------

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(Plasma)

Requires:       plasma-workspace

#------------------------------------------------------------------

%description
%summary

%files
%license LICENSE
%doc README.md
%{_kf6_qtplugindir}/plasma/containmentactions/matmoul-customdesktopmenu.so

#------------------------------------------------------------------

%prep
%forgeautosetup -p1

%build
mkdir %{_vpath_builddir}
pushd src
%cmake_kf6 -B ../%{_vpath_builddir}
popd
%cmake_build

%install
%cmake_install

#------------------------------------------------------------------

%changelog
* Mon Oct 14 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.2.0-2
- Fedora 41 Mass Rebuild

* Fri Jun 14 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.2.0-1
- initial package
