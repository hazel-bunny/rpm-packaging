%global app_id org.kde.ktimetracker

Name:           ktimetracker
Version:        5.0.1
Release:        2%{?dist}
License:        GFDL-1.2-only AND LGPL-3.0-only AND GPL-2.0-only
URL:            https://apps.kde.org/%{name}
Summary:        Personal Time Tracker

Source0:        https://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  appstream
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  kf5-rpm-macros

BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IdleTime)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)

BuildRequires:  cmake(Qt5DBus) >= 5.10.0
BuildRequires:  cmake(Qt5Gui) >= 5.10.0
BuildRequires:  cmake(Qt5Widgets) >= 5.10.0
BuildRequires:  cmake(Qt5Xml) >= 5.10.0

BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(Qca-qt5)
BuildRequires:  cmake(QJSON-qt5)

BuildRequires:  pkgconfig(libassuan)
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(zlib)

%description
KTimeTracker tracks time spent on various tasks.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake_kf5
%cmake_build

%install
%cmake_install

%find_lang %{name} --with-kde --with-html

%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/%{app_id}.appdata.xml

%files -f %{name}.lang
%license COPYING COPYING.DOC
%doc README ChangeLog.md
%doc %lang(en) %{_kf5_datadir}/doc/HTML/en/%{name}/
%{_kf5_bindir}/%{name}
%{_kf5_datadir}/applications/%{app_id}.desktop
%{_kf5_datadir}/dbus-1/interfaces/%{app_id}.%{name}.xml
%{_kf5_datadir}/icons/hicolor/*/apps/%{name}.png
%{_kf5_metainfodir}/%{app_id}.appdata.xml

%changelog
* Fri May 17 2024 Dipta Biswas <dabiswas112@gmail.com> - 5.0.1-2
- Fix license

* Sun Jun 25 2023 Dipta Biswas <dabiswas112@gmail.com> - 5.0.1-1
- Adapt OpenSUSE spec for Fedora
