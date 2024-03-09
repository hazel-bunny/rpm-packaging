%global forgeurl https://github.com/paulmcauley/klassy
%global commit 14713a510b0b89b084b9c0b3713ad35f15b9e8f2
%global date 20240308
%forgemeta

Name:           klassy-qt6
Version:        5.101.breeze6.0.80
Release:        %autorelease
Summary:        Window Decoration and Application Style plugin for the KDE Plasma desktop
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            %{forgeurl}
Source:         %{forgesource}

Obsoletes:      classikstyles
Obsoletes:      classik

BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules >= 5.98.0

BuildRequires:  kf6-rpm-macros
BuildRequires:  kf6-filesystem

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Xml)

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
A highly customizable binary Window Decoration and Application Style plugin for the KDE Plasma desktop. Install, and then enable in System Settings -> Appearance -> Window Decorations, and also in System Setings -> Appearance -> Application Style.


%prep
%forgeautosetup -p1

%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build

%install
%cmake_install

%files
%license LICENSES/*.txt
%{_libdir}/libklassycommon6.so.*
%{_kf6_datadir}/applications/kcm_klassydecoration.desktop
%dir %{_kf6_qtplugindir}
%dir %{_kf6_qtplugindir}/plasma
%dir %{_kf6_qtplugindir}/plasma/kcms
%dir %{_kf6_qtplugindir}/plasma/kcms/klassy
%{_kf6_qtplugindir}/org.kde.kdecoration2/
%{_kf6_qtplugindir}/plasma/kcms/klassy/kcm_klassydecoration.so
%dir %{_kf6_qtplugindir}/plasma/kcms/systemsettings_qwidgets/
%{_kf6_qtplugindir}/plasma/kcms/systemsettings_qwidgets/klassystyleconfig.so
%{_kf6_qtplugindir}/styles/
%{_kf6_datadir}/kstyle/
%{_kf6_datadir}/applications/klassystyleconfig.desktop
%{_bindir}/klassy-settings
%{_datadir}/icons/hicolor/scalable
%{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/klassy-settings.*
%{_libdir}/cmake/Klassy/

%changelog
%autochangelog
