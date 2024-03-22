Name:    systemdgenie

%global forgeurl https://github.com/KDE/%{name}
%global commit 45ce5d742d2c0f6a3fa8cb1b6f81e526ccdcfc2d
%global date 20240317
%forgemeta

Summary: Systemd managment utility
Version: 0.99.0
Release: %autorelease

License: GPLv2+
URL:     %{forgeurl}
Source:  %{forgesource}

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: desktop-file-utils
BuildRequires: kf6-rpm-macros

BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(systemd)

BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6XmlGui)

%description
SystemdGenie is a systemd management utility based on KDE technologies. It provides a graphical frontend for the systemd daemon, which allows for viewing and controlling systemd units, logind sessions as well as easy modification of configuration and unit files.

%prep
%forgeautosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-html

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.systemdgenie.desktop

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/%{name}
%{_kf6_libexecdir}/kauth/systemdgeniehelper
%{_kf6_datadir}/applications/org.kde.systemdgenie.desktop
%{_kf6_datadir}/dbus-1/system-services/org.kde.kcontrol.systemdgenie.service
%{_kf6_datadir}/dbus-1/system.d/org.kde.kcontrol.systemdgenie.conf
%{_kf6_datadir}/kxmlgui5/%{name}/
%{_kf6_datadir}/polkit-1/actions/org.kde.kcontrol.systemdgenie.policy

%changelog
* Wed Mar 6 2024 Dipta Biswas <dabiswas112@gmail.com> 0.99.0-1.git
- Initial packaging
