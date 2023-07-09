%global commit d10ae12cde0370233189574d255c831e3eb267ab
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20230430

Name:           warpinator
Version:        1.6.3
Release:        0
License:        GPLv3
URL:            https://github.com/linuxmint/warpinator
Summary:        Share files across the LAN

Source:         https://github.com/linuxmint/warpinator/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  glib2-tools
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  polkit-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-grpcio
BuildRequires:  python3-protobuf
BuildRequires:  python3-setuptools
BuildRequires:  python3-zeroconf
BuildRequires:  update-desktop-files

Requires:       python3-PyNaCl
Requires:       python3-cryptography
Requires:       python3-gobject-Gdk
Requires:       python3-grpcio
Requires:       python3-netifaces
Requires:       python3-protobuf
Requires:       python3-setproctitle
Requires:       python3-xapp
Requires:       python3-zeroconf

BuildArch:      noarch

%lang_package

%description
Warpinator is a simple app that allows users to share files across the LAN.

%package -n nemo-extension-%{name}
Summary:        Warpinator extension for nemo
Requires:       nemo
Requires:       warpinator = %{version}
Supplements:    (nemo and warpinator)
BuildArch:      noarch

%description -n nemo-extension-%{name}
Warpinator is a simple app that allows users to share files across the LAN.

This package provides an extension to use warpinator from nemo file browser.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

# Files missing hashbangs
for f in config warp_pb2 warp_pb2_grpc
do
  sed -i "1i#!%{_bindir}/python3" %{buildroot}%{_libexecdir}/warpinator/${f}.py
done

chmod +x %{buildroot}%{_libexecdir}/warpinator/*.py

%suse_update_desktop_file -r org.x.Warpinator Network FileTransfer
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc README.md
%if 0%{?suse_version} >= 1550
%{_distconfdir}/xdg/autostart/warpinator-autostart.desktop
%else
%{_sysconfdir}/xdg/autostart/warpinator-autostart.desktop
%endif
%{_bindir}/warpinator
%{_bindir}/warpinator-send
%{_libexecdir}/warpinator/
%{_datadir}/applications/org.x.Warpinator.desktop
%{_datadir}/glib-2.0/schemas/org.x.Warpinator.gschema.xml
%dir %{_datadir}/icons/hicolor/*@2
%dir %{_datadir}/icons/hicolor/*@2/apps
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/metainfo/org.x.Warpinator.appdata.xml
%{_datadir}/warpinator/

%files -n nemo-extension-%{name}
%dir %{_datadir}/nemo
%dir %{_datadir}/nemo/actions
%{_datadir}/nemo/actions/warpinator*

%files lang -f %{name}.lang

%changelog
