%global app_id org.kde.kup
%global forgeurl https://github.com/KDE/kup
%global commit 439195e275d030c88127871c03323ba58abf0bb7
%global date 20240321
%forgemeta

Name:           kup
Version:        0.9.1
Release:        %autorelease
Summary:        Backup scheduler for the Plasma desktop

License:        GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LicenseRef-KDE-Accepted-GPL
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  qt6-rpm-macros
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Plasma5Support)

BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pkgconfig(openssl)

Requires:       rsync
Requires:       bup

%description
Kup can help you remember to keep up-to-date backups of your personal files. It provides:
- Incremental backup archive with the use of "bup".
- Synchronized folders with the use of "rsync".
- Support for local filesystem or external usb storage.
- Monitor availability of backup destinations, like for example a mounted network storage.
- Integration into KDE's Plasma desktop.

%prep
%forgeautosetup -p1

%build
%cmake_kf6 -DBUILD_TESTING=OFF -DQT_MAJOR_VERSION=6
%cmake_build

%install
%cmake_install
%find_lang %{name}


%files -f %{name}.lang
%license LICENSES/*

/etc/xdg/autostart/kup-daemon.desktop

%{_bindir}/kup-daemon
%{_bindir}/kup-filedigger
%{_bindir}/kup-purger

%{_kf6_plugindir}/kio/kio_bup.so

%{_kf6_qtplugindir}/plasma/kcms/systemsettings_qwidgets/kcm_kup.so
%{_kf6_qtplugindir}/plasma5support/dataengine/plasma_engine_kup.so

%{_datadir}/applications/kcm_kup.desktop
%{_datadir}/icons/hicolor/scalable/apps/kup.svg
%{_datadir}/knotifications6/kupdaemon.notifyrc

%{_kf6_metainfodir}/%{app_id}.appdata.xml
%{_kf6_metainfodir}/%{app_id}applet.appdata.xml

%{_datadir}/plasma/plasmoids/%{app_id}applet/contents/ui/FullRepresentation.qml
%{_datadir}/plasma/plasmoids/%{app_id}applet/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/%{app_id}applet/metadata.json

%{_datadir}/plasma5support/services/kupdaemonservice.operations
%{_datadir}/plasma5support/services/kupservice.operations

%{_datadir}/qlogging-categories6/kup.categories


%changelog
* Sun Feb 25 2024 Dipta Biswas <dabiswas112@gmail.com> 0.9.1-1.git
- Switch to git snapshot

* Tue Mar 28 2023 Justin Zobel <justin@1707.io> - 0.9.1-1
- Initial package
