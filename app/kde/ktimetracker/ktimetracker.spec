%global app_id org.kde.ktimetracker

Name:           ktimetracker
Version:        5.0.1
Release:        1
License:        GPLv2
Group:          Productivity/Other
URL:            https://apps.kde.org/%{name}
Summary:        Personal Time Tracker

Source0:        https://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  gettext
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  boost-devel
BuildRequires:  grantlee-qt5-devel >= 5.1.0
BuildRequires:  libassuan-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  sed
BuildRequires:  qca-qt5-devel
BuildRequires:  qjson-qt5-devel
BuildRequires:  zlib-devel

BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IdleTime)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5DBus) >= 5.10.0
BuildRequires:  cmake(Qt5Gui) >= 5.10.0
BuildRequires:  cmake(Qt5Widgets) >= 5.10.0
BuildRequires:  cmake(Qt5Xml) >= 5.10.0

BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(libxslt)

BuildRequires:  desktop-file-utils

Recommends:     %{name}-lang = %{version}

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

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
   touch --no-create %{_kf5_iconsdir}/hicolor &>/dev/null
   gtk-update-icon-cache %{_kf5_iconsdir}/hicolor &>/dev/null || :
   update-desktop-database -q &> /dev/null
fi

%posttrans
gtk-update-icon-cache %{_kf5_iconsdir}/hicolor &>/dev/null || :
update-desktop-database -q &> /dev/null

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
* Sun Jun 25 2023 Dipta Biswas <dabiswas112@gmail.com> - 5.0.1-1
- Initial package
