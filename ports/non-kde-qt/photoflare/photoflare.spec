Name:           photoflare
Version:        1.6.13

%global forgeurl https://github.com/PhotoFlare/%{name}
%global tag v%{version}
%global date 20230809
%forgemeta

Release:        1%{?dist}
Summary:        Quick, simple but powerful Cross Platform image editor
License:        GPL-3.0

URL:            http://photoflare.io/
Source:         %{forgesource}

# Upstream patches
Patch0:         qt-6.diff

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig(GraphicsMagick)
BuildRequires:  pkgconfig(GraphicsMagick++)

BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-rpm-macros

Requires:       qt6-qtimageformats

%description
%summary

%prep
%forgeautosetup -p1
sed -i '/pixmaps \\/d' Photoflare.pro

%build
%qmake_qt6 PREFIX=/usr
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons//hicolor/*/apps/photoflare.png
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/metainfo/io.%{name}.%{name}.appdata.xml
%{_datadir}/%{name}/languages/*.qm

%changelog
* Tue Jun 18 2024 Hazel Bunny <hazel_bunny@disroot.org> - 1.6.13-1
- initial package
