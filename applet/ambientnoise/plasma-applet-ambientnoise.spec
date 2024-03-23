%global debug_package %{nil}

Name:           plasma-applet-ambientnoise

%global forgeurl https://github.com/m-pilia/%{name}
%global date 20240311
%global tag 0.6.0
%forgemeta

%global orig_name org.kde.plasma.ambientnoise

Version:        %{tag}
Release:        %autorelease
Summary:        Ambient noise player applet (plasmoid) for KDE Plasma 6
License:        GPL-3.0
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Plasma5Support)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6Package)

Requires:       plasma-workspace
Requires:       kf6-kirigami2
Requires:       libplasma

Provides:       plasma6-applet-ambientnoise = %{version}-%{release}

Obsoletes:      plasma5-applet-ambientnoise <= %{version}-%{release}

%description
This applet for the KDE Plasma desktop allows to reproduce ambient noise. Multiple
noise components can be combined, controlling their individual volume. The applet
reads noise files and their icons from a given, customisable folder. The noise and
the icon must be in the same folder and share the same name, except for the file
extension.

The plasmoid remembers its state across reboots, including play/pause status, volume,
and active noise components. To prevent it from playing sound at start-up, even if
it was still playing at the time of the last shutdown, go to the plasmoid settings
and tick "Paused at start-up".

Free noises in a ready-to-use format for this plasmoid can be found in the anoise
project.

%prep
%forgeautosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{orig_name}.appdata.xml

%files
%license LICENSE
%doc README.md

%{_kf6_datadir}/icons/{breeze,breeze-dark}/apps/{16,22,32}/ambientnoise.svg
%{_kf6_datadir}/icons/hicolor/apps/scalable/ambientnoise.svg
%{_kf6_datadir}/plasma/plasmoids/%{orig_name}
%{_kf6_metainfodir}/%{orig_name}.appdata.xml

%changelog
%autochangelog
