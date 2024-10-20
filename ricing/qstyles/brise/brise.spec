%global _basename brise

%global forgeurl https://invent.kde.org/carlschwan/%{_basename}
%global commit_full 54c2ea70b42aacfc6a30560429a058e87b7a0013
%global commit %%(c=%%{commit_full}; echo ${c:0:7})
%global date 20240205

Name:           plasma-%{_basename}
Version:        6.0.80^%{date}.%{commit}
Release:        1%{?dist}
Summary:        Artwork, styles and assets for the Brise visual style for the Plasma Desktop
License:        BSD-3-Clause AND GPL-2.0-or-later AND MIT
URL:            %{forgeurl}
Source:         %{forgeurl}/-/archive/%{commit_full}/%{_basename}-%{commit_full}.tar.bz2

BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules >= 5.102.0

BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-filesystem

BuildRequires:  kf6-rpm-macros
BuildRequires:  kf6-filesystem

BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5X11Extras)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Xml)

BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5FrameworkIntegration)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5Package)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  cmake(KF5WindowSystem)

BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6FrameworkIntegration)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  cmake(KDecoration2)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Plasma5Support)

BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)

%description
Brise is a style for Plasma. This is a fork of Breeze and the name is a
translations of Breeze to French and German. This repository contains some
parts of Breeze such as the window decorations and the application style.

This repository contains many parts of Brise, such as:
 - Color schemes, located under /colors.
 - Window decorations, located under /kdecoration.
 - Application style, located under /kstyle.

%prep
%autosetup -p1 -n %{_basename}-%{commit_full}
sed -i 's/#build_Qt5()/build_Qt5()/g' CMakeLists.txt

%build
%cmake -DBUILD_QT5=ON -DBUILD_QT6=ON
%cmake_build

%install
%cmake_install

# Remove locales as they conflict with breeze
rm -rf %{buildroot}%{_kf6_datadir}/locale

%files
%license LICENSES/*.txt

%{_bindir}/%{_basename}-settings6
%{_libdir}/cmake/Brise/

%{_kf5_qtplugindir}/styles/%{_basename}5.so
%{_kf6_qtplugindir}/styles/%{_basename}6.so
%{_kf6_qtplugindir}/kstyle_config/%{_basename}styleconfig.so
%{_kf6_qtplugindir}/org.kde.kdecoration2/org.kde.%{_basename}.so
%{_kf6_qtplugindir}/org.kde.kdecoration2.kcm/kcm_%{_basename}decoration.so

%{_kf6_datadir}/applications/kcm_%{_basename}decoration.desktop
%{_kf6_datadir}/applications/%{_basename}styleconfig.desktop
%{_kf6_datadir}/color-schemes/Brise*.colors
%{_kf6_datadir}/icons/hicolor/scalable/apps/%{_basename}-settings.svgz
%{_kf6_datadir}/kstyle/themes/%{_basename}.themerc
%{_kf6_datadir}/QtCurve/Brise.qtcurve

%changelog
* Sat Oct 19 2024 Hazel Bunny <hazel_bunny@disroot.org> - 6.0.80^20240205.54c2ea70-1
- Initial package

