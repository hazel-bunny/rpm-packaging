%global _basename kup
%global app_id org.kde.%{_basename}

Name:           kde-%{_basename}
Version:        0.10.0

%global forgeurl https://github.com/KDE/%{_basename}
%global tag %{_basename}-%{version}
%global date 20240526
%forgemeta

Release:        1%{?dist}
Summary:        Backup scheduler for the Plasma desktop
License:        GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LicenseRef-KDE-Accepted-GPL
URL:            %{forgeurl}
Source:         %{forgesource}

#------------------------------------------------------------------

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  libappstream-glib
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
Requires:       hicolor-icon-theme
Requires:       plasma-workspace

Recommends:     bup

#------------------------------------------------------------------

%description
Kup can help you remember to keep up-to-date backups of your personal files. It provides:
- Incremental backup archive with the use of "bup".
- Synchronized folders with the use of "rsync".
- Support for local filesystem or external usb storage.
- Monitor availability of backup destinations, like for example a mounted network storage.
- Integration into KDE's Plasma desktop.

%files -f %{_basename}.lang
%license LICENSES/*

%{_qt6_sysconfdir}/autostart/%{_basename}-daemon.desktop

%{_kf6_bindir}/%{_basename}-daemon
%{_kf6_bindir}/%{_basename}-filedigger
%{_kf6_bindir}/%{_basename}-purger

%{_kf6_plugindir}/kio/kio_bup.so

%{_kf6_qtplugindir}/plasma/kcms/systemsettings_qwidgets/kcm_%{_basename}.so
%{_kf6_qtplugindir}/plasma5support/dataengine/plasma_engine_%{_basename}.so

%{_kf6_datadir}/applications/kcm_%{_basename}.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/%{_basename}.svg
%{_kf6_datadir}/knotifications6/%{_basename}daemon.notifyrc

%{_kf6_metainfodir}/%{app_id}.appdata.xml
%{_kf6_metainfodir}/%{app_id}applet.appdata.xml

%{_kf6_datadir}/plasma/plasmoids/%{app_id}applet/contents/ui/FullRepresentation.qml
%{_kf6_datadir}/plasma/plasmoids/%{app_id}applet/contents/ui/main.qml
%{_kf6_datadir}/plasma/plasmoids/%{app_id}applet/metadata.json

%{_kf6_datadir}/plasma5support/services/%{_basename}daemonservice.operations
%{_kf6_datadir}/plasma5support/services/%{_basename}service.operations

%{_kf6_datadir}/qlogging-categories6/%{_basename}.categories

#------------------------------------------------------------------

%prep
%forgeautosetup -p1

%build
%cmake_kf6 -DBUILD_TESTING=OFF -DQT_MAJOR_VERSION=6
%cmake_build

%install
%cmake_install

# Bad icon name
sed -i "/<icon type=\"stock\">/d" %{buildroot}%{_kf6_metainfodir}/%{app_id}.appdata.xml
sed -i "/<icon type=\"stock\">/d" %{buildroot}%{_kf6_metainfodir}/%{app_id}applet.appdata.xml

%find_lang %{_basename}

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/kcm_%{_basename}.desktop
desktop-file-validate %{buildroot}%{_qt6_sysconfdir}/autostart/%{_basename}-daemon.desktop

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/%{app_id}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/%{app_id}applet.appdata.xml

#------------------------------------------------------------------

%changelog
* Mon May 27 2024 Dipta Biswas <dabiswas112@gmail.com> - 0.10.0-1
- Update to 0.10.0

* Fri May 17 2024 Dipta Biswas <dabiswas112@gmail.com> - 0.9.1-3.git
- Add check

* Sun Feb 25 2024 Dipta Biswas <dabiswas112@gmail.com> 0.9.1-1.git
- Switch to git snapshot

* Tue Mar 28 2023 Justin Zobel <justin@1707.io> - 0.9.1-1
- Initial package
