Name:           photoflare
Version:        1.6.9
Release:        1%{?dist}
Summary:        Quick, simple but powerful Cross Platform image editor.
License:        GPL3
Group:          Graphics
URL:            http://photoflare.io/
Source0:        https://github.com/PhotoFlare/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
#BuildRequires:  qt5-devel
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig(GraphicsMagick)
BuildRequires:  qt5-qttools
BuildRequires:  qt5-qttranslations
BuildRequires:  qt5-linguist
BuildRequires:	GraphicsMagick-c++-devel

%description
Quick, simple but powerful Cross Platform image editor.

%prep
%setup -q

%build
%qmake_qt5 PREFIX=/usr
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
%make_install INSTALL_ROOT=%{buildroot}

# We dont need this:
rm -rf %{buildroot}%{_datadir}/pixmaps/photoflare.png

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons//hicolor/*/apps/photoflare.png
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/metainfo/io.%{name}.%{name}.appdata.xml
%{_datadir}/%{name}/languages/*.qm
