%global _basename KDE-Rounded-Corners
%global forgeurl https://github.com/matinlotfali/%{_basename}
Version:        0.6.6
%forgemeta

Name:           kde-rounded-corners
Release:        1%{?dist}
Summary:        Rounds the corners of your windows
License:        GPL-3.0
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  qt6-qtbase-private-devel

BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KWin)
BuildRequires:  cmake(KWinDBusInterface)

BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xcb)

Requires:       kwin

%description
This effect rounds the corners of your windows and adds an outline around them without much affecting the performance of the KDE Plasma desktop

%files
%{_kf6_qtplugindir}/kwin/effects/configs/kwin_shapecorners_config.so
%{_kf6_qtplugindir}/kwin/effects/plugins/kwin4_effect_shapecorners.so
%{_kf6_datadir}/kwin/shaders/shapecorners_core.frag
%{_kf6_datadir}/kwin/shaders/shapecorners.frag

#------------------------------------------------------------------

%prep
%forgeautosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%changelog
* Sun May 26 2024 Dipta Biswas <dabiswas112@gmail.com> - 0.6.5-1
- update to 0.6.5

* Sat Apr 27 2024 Dipta Biswas <dabiswas112@gmail.com> - 0.6.2-1
- initial package

