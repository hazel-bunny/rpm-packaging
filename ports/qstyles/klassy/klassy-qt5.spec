%global forgeurl https://github.com/paulmcauley/klassy
%global commit aee1befa285523b6f39398074b8cf1e5345f60c0
%global date 20240307
%forgemeta

Name:           klassy-qt5
Version:        5.0.breeze5.27.10
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

BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-filesystem

BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5X11Extras)

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
BuildRequires:  cmake(KDecoration2)

BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)

%description
A highly customizable binary Window Decoration and Application Style plugin for the KDE Plasma desktop. Install, and then enable in System Settings -> Appearance -> Window Decorations, and also in System Setings -> Appearance -> Application Style.


%prep
%forgeautosetup -p1

%build
%cmake_kf5 -DQT_MAJOR_VERSION=5
%cmake_build

%install
%cmake_install

%files
%license LICENSES/*.txt
%{_libdir}/libklassycommon5.so.*
%{_kf5_datadir}/applications/kcm_klassydecoration.desktop
%dir %{_kf5_qtplugindir}
%dir %{_kf5_qtplugindir}/plasma
%dir %{_kf5_qtplugindir}/plasma/kcms
%dir %{_kf5_qtplugindir}/plasma/kcms/klassy
%{_kf5_qtplugindir}/org.kde.kdecoration2/
%{_kf5_qtplugindir}/plasma/kcms/klassy/kcm_klassydecoration.so
%dir %{_kf5_qtplugindir}/plasma/kcms/systemsettings_qwidgets/
%{_kf5_qtplugindir}/plasma/kcms/systemsettings_qwidgets/klassystyleconfig.so
%{_kf5_qtplugindir}/styles/
%{_kf5_datadir}/kstyle/
%{_kf5_datadir}/applications/klassystyleconfig.desktop
%{_bindir}/klassy-settings
%{_datadir}/icons/hicolor/scalable
%{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/klassy-settings.*
%{_libdir}/cmake/Klassy/

%changelog
%autochangelog
