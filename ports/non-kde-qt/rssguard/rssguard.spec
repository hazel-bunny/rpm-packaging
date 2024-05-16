Name:           rssguard
Version:        4.7.0

%global forgeurl https://github.com/martinrotter/%{name}
%global tag %{version}
%global date 20240514
%forgemeta

%global app_id io.github.martinrotter.rssguard

Release:        1%{?dist}
Summary:        Simple yet powerful feed reader

# GPL-3.0-or-later: main program
# LGPL-3.0-or-later: src/librssguard/3rd-party/mimesis
# BSD-3-Clause: src/librssguard/network-web/googlesuggest.*
# BSD-4-Clause: src/librssguard/3rd-party/sc
# MIT: src/librssguard/3rd-party/boolinq
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND BSD-3-Clause AND BSD-4-Clause AND MIT

URL:            %{forgeurl}
Source:         %{forgesource}

# QtWebEngine is only available on those architectures
ExclusiveArch:  %{qt6_qtwebengine_arches}

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  cmake
BuildRequires:  make

BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Linguist)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)

BuildRequires:  pkgconfig(libsqlite3x)
BuildRequires:  pkgconfig(mpv)
BuildRequires:  pkgconfig(zlib)

Requires:       hicolor-icon-theme

Provides:       bundled(boolinq) = 3.0.1-1
Provides:       bundled(mimesis)
Provides:       bundled(simplecrypt) = 3.1-1

%description
RSS Guard is simple, light and easy-to-use RSS/ATOM feed aggregator developed
using Qt framework which supports online feed synchronization.

%prep
%forgeautosetup -p1
sed -i 's/\r$//' README.md

%build
%cmake -DNO_UPDATE_CHECK=ON -DENABLE_COMPRESSED_SITEMAP=ON
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml

%files
%doc README.md
%license LICENSE.md

%{_bindir}/%{name}

%{_includedir}/lib%{name}/

%{_libdir}/lib%{name}.so
%{_libdir}/%{name}/lib%{name}*.so

%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/icons/hicolor/*/apps/%{app_id}.png

%{_metainfodir}/%{app_id}.metainfo.xml

%changelog
%autochangelog
