Name:           kwin6-bismuth-decoration

%global forgeurl https://github.com/ivan-cukic/%{name}
%global commit 56541e21237a8a60438aa34de1aebc1ea52026c7
%global date 20240604
%forgemeta

Version:        0
Release:        1%{?dist}
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

%dir %{_kf6_qmldir}/org/kde/%{name}
%dir %{_kf6_qmldir}/org/kde/%{name}/core

%{_kf6_qmldir}/org/kde/%{name}/core/lib%{name}_core.so
%{_kf6_qmldir}/org/kde/%{name}/core/qmldir

%{_kf6_qtplugindir}/kcms/kcm_%{name}.so
%{_kf6_qtplugindir}/org.kde.kdecoration2/%{name}_kdecoration.so

%{_kf6_datadir}/kpackage/kcms/kcm_%{name}
%{_kf6_datadir}/kservices6/kcm_%{name}.desktop
%{_kf6_datadir}/kwin/scripts/%{name}
%{_kf6_datadir}/icons/hicolor/*/status/*
%{_kf6_datadir}/icons/hicolor/*/categories/*.svg
%{_kf6_datadir}/icons/hicolor/scalable/apps/*.svg
%{_kf6_datadir}/kconf_update/%{name}*
%{_kf6_datadir}/qlogging-categories6/%{name}.categories
%{_kf6_datadir}/config.kcfg/%{name}_config.kcfg

#------------------------------------------------------------------

%prep
%forgeautosetup -p1

%build
%cmake_kf6 -G Ninja -DUSE_NPM=OFF -DUSE_TSC=OFF -DBUILD_TESTING=false
%cmake_build

%install
%cmake_install

%changelog
* Fri Jun 7 2024 Dipta Biswas <dabiswas112@gmail.com> - 1.2.1-1
- Update to 1.2.1

* Sun May 26 2024 Dipta Biswas <dabiswas112@gmail.com> - 1.2.0-2
- rebuild for kwin 6.0.5

* Fri Apr 26 2024 Dipta Biswas <dabiswas112@gmail.com> - 1.2.0-1
- initial package
