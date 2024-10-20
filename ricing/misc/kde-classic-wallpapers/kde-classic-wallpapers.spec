%global debug_package %{nil}

Name:            kde-classic-wallpapers
Version:         2.0

%global forgeurl https://github.com/MartinF99/%{name}
%global tag      v%{version}
%global date     20240314
%forgemeta

Release:         1%{?dist}
Summary:         An archive of all classic kde wallpapers
License:         GPL-3.0
URL:             %{forgeurl}
Source:          %{forgesource}

BuildRequires:   gcc-c++
BuildRequires:   cmake
BuildRequires:   extra-cmake-modules
BuildRequires:   kf6-rpm-macros

BuildArch:       noarch

%description
%summary

%files
%license LICENSE
%doc README.md
%{_datadir}/wallpapers/*

#------------------------------------------------------------------

%prep
%forgeautosetup

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

#------------------------------------------------------------------

%changelog
* Tue Oct 15 2024 Hazel Bunny <hazel_bunny@disroot.org> 2.0-1
- Initial Package.
