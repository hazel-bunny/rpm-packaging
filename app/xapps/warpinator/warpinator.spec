%global app_id org.x.Warpinator

%global commit d10ae12cde0370233189574d255c831e3eb267ab
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20230430

Name:           warpinator
Version:        1.6.3
Release:        0
License:        GPLv3
URL:            https://github.com/linuxmint/%{name}
Summary:        Share files across the LAN

Source:         https://github.com/linuxmint/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  polkit-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-grpcio
BuildRequires:  python3-protobuf
BuildRequires:  python3-setuptools
BuildRequires:  python3-zeroconf
BuildRequires:  desktop-file-utils

Requires:       python3-cryptography
Requires:       python3-gobject
Requires:       python3-grpcio
Requires:       python3-netifaces
Requires:       python3-protobuf
Requires:       python3-pynacl
Requires:       python3-setproctitle
Requires:       python3-xapp
Requires:       python3-zeroconf

BuildArch:      noarch

%description
Warpinator is a simple app that allows users to share files across the LAN.

%package -n nemo-extension-%{name}
Summary:        Warpinator extension for nemo
Requires:       nemo
Requires:       %{name} = %{version}
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
  sed -i "1i#!%{_bindir}/python3" %{buildroot}%{_libexecdir}/%{name}/${f}.py
done

chmod +x %{buildroot}%{_libexecdir}/%{name}/*.py

%suse_update_desktop_file -r %{app_id} Network FileTransfer
%find_lang %{name} %{?no_lang_C}

%files -f %{name}.lang
%license COPYING
%doc README.md
%if 0%{?suse_version} >= 1550
%{_distconfdir}/xdg/autostart/%{name}-autostart.desktop
%else
%{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop
%endif
%{_bindir}/%{name}
%{_bindir}/%{name}-send
%{_libexecdir}/%{name}/
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/icons/hicolor/*@2
%{_datadir}/icons/hicolor/*@2/apps
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/metainfo/%{app_id}.appdata.xml
%{_datadir}/%{name}/

%files -n nemo-extension-%{name}
%dir %{_datadir}/nemo
%dir %{_datadir}/nemo/actions
%{_datadir}/nemo/actions/%{name}*

%changelog
