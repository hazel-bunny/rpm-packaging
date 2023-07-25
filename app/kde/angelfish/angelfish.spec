Name:           angelfish
Version:        23.04.3
Epoch:          1
Release:        %autorelease
Summary:        Plasma Mobile minimal web browser

License:        MIT and GPLv2+ and LGPLv2 and LGPLv2+
# For a breakdown of the licensing, see PACKAGE-LICENSING
URL:            https://invent.kde.org/plasma-mobile/%{name}
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz

%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  kf5-rpm-macros
BuildRequires:  libappstream-glib
 
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5KirigamiAddons)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Purpose)
BuildRequires:  cmake(KF5QQC2DesktopStyle)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Feedback)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5WebSockets)
BuildRequires:  cmake(Qt5Widgets)

BuildRequires:  cargo-rpm-macros
BuildRequires:  rust-cxx-devel
BuildRequires:  rust-cxx-build-devel
BuildRequires:  corrosion

Requires:       hicolor-icon-theme
# QML module dependencies
Requires:       kf5-kirigami2%{?_isa} 
Requires:       kf5-kirigami2-addons%{?_isa}
Requires:       kf5-purpose%{?_isa}
Requires:       qt5-qtfeedback%{?_isa} 
Requires:       qt5-qtgraphicaleffects%{?_isa}
Requires:       qt5-qtquickcontrols2%{?_isa}
Requires:       qt5-qtwayland%{?_isa} 
Requires:       qt5-qtwebengine%{?_isa}

%description
Web browser for mobile devices with Plasma integration

%prep
%autosetup -n %{name}-%{version}
%cargo_prep

%generate_buildrequires
cd src/rs/adblock
%cargo_generate_buildrequires

%build
%cmake_kf5 -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.%{name}.metainfo.xml


%files -f %{name}.lang
%license LICENSES/{MIT,GPL-2.0-or-later,LGPL-2.0-only,LGPL-2.0-or-later}.txt
%doc README.md

%{_kf5_bindir}/%{name}
%{_kf5_bindir}/%{name}-webapp

%{_kf5_datadir}/applications/org.kde.%{name}.desktop
%{_kf5_datadir}/config.kcfg/%{name}settings.kcfg
%{_kf5_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg
%{_kf5_datadir}/knotifications5/%{name}.notifyrc

%{_kf5_metainfodir}/org.kde.%{name}.metainfo.xml

%changelog
%autochangelog
