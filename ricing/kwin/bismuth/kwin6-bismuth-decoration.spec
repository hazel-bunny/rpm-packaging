Name:           kwin6-bismuth-decoration

%global forgeurl https://github.com/ivan-cukic/%{name}
%global commit 603f3cca4d9b1c383a352f6e570a2e56138ecedb
%global date 20240608
%forgemeta

Version:        0
Release:        2%{?dist}
Summary:        Tiling-WM-like window decorations for KWin
License:        BSD-3-Clause and CC-BY-4.0 and LGPL-3.0-or-later and MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules
BuildRequires:  golang-github-evanw-esbuild

BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-rpm-macros
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KDecoration2)

Requires:       kwin

%description
This is just a port of Bismuth decoration for Plasma/KWin 6

%files
%license LICENSES/MIT.txt
%license LICENSES/BSD-3-Clause.txt
%license LICENSES/CC-BY-4.0.txt
%license LICENSES/LGPL-3.0-or-later.txt
%doc README.md CHANGELOG.md CONTRIBUTING.md
%{_kf6_qtplugindir}/org.kde.kdecoration2/bismuth_kdecoration.so

#------------------------------------------------------------------

%prep
%forgeautosetup -p1

%build
%cmake_kf6 -G Ninja -DUSE_NPM=OFF -DUSE_TSC=OFF -DBUILD_TESTING=false
%cmake_build

%install
%cmake_install

%changelog
* Tue Oct 15 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0-2
- Fedora 41 Mass Rebuild

* Fri Jun 14 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0-1
- initial package
