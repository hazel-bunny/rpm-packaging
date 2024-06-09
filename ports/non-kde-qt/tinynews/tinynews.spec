Name:           tinynews
Version:        0.9

%global forgeurl https://gitlab.com/communia/%{name}
%global tag %{version}
%global date 20210919
%forgemeta

%global app_id org.kde.%{name}

Release:        3%{?dist}
Summary:        Tiny tiny rss and pocket client application
License:        GPL-3.0

URL:            %{forgeurl}
Source:         %{forgesource}

# QtWebEngine is only available on those architectures
ExclusiveArch:  %{qt5_qtwebengine_arches}

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-rpm-macros
BuildRequires:  kf5-rpm-macros

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5WebEngineWidgets)
BuildRequires:  cmake(Qt5WebSockets)

BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5WidgetsAddons)

BuildRequires:  nodejs-devel
BuildRequires:  nodejs-npm

# QML module dependencies
Requires:       kf5-kirigami2
Requires:       kf5-kirigami2-addons
Requires:       kf5-plasma
Requires:       qt5-qtwebsockets-devel

Provides:       bundled(nodejs-readability)

%description
Tiny tiny rss and pocket client application.
Made with kirigami, the qml components from kde.

%prep
%forgeautosetup -p1
pushd src
npm install
popd

%build
%cmake_kf5
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
# appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.appdata.xml

%files
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_metainfodir}/%{app_id}.appdata.xml

%changelog
%autochangelog
