%global _basename KDE-Rounded-Corners
%global forgeurl https://github.com/matinlotfali/%{_basename}
%global commit 8b1ac40425120cd5f8b14cf8ded1f53ac7f9b6f5
%global date 20240918
%forgemeta

Name:           kde-rounded-corners
Version:        0.6.7
Release:        7%{?dist}
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
* Sat Oct 19 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.6.7-7
- Rebuild for KWin 6.2.1

* Thu Oct 10 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.6.7-6.git
- Rebuild for kwin 6.2.0

* Fri Sep 20 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.6.7-5.git
- Rebuild for kwin 6.1.5

* Sun Aug 11 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.6.7-4
- Rebuild for kwin 6.1.4

* Sun Jul 28 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.6.7-3
- Rebuild for kwin 6.1.3

* Sat Jul 13 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.6.7-2
- Rebuild for kwin 6.1.2

* Thu Jun 27 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.6.7-1
- update to 0.6.7

* Sun May 26 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.6.5-1
- update to 0.6.5

* Sat Apr 27 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.6.2-1
- initial package

