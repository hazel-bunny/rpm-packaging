Name:           warpinator
Version:        1.8.6

%global forgeurl https://github.com/linuxmint/%{name}
%global commit 34413b665559c96f8ccc4bff5856d180e02777f6
%global date 20240721
%forgemeta

%global app_id org.x.Warpinator

Release:        2%{?dist}
License:        GPLv3
Summary:        Send and Receive Files across the Network
URL:            %{forgeurl}
Source:         %{forgesource}

#------------------------------------------------------------------

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  polkit-devel
BuildRequires:  python3-devel

BuildRequires:  python3-gobject
BuildRequires:  python3-grpcio
BuildRequires:  python3-protobuf
BuildRequires:  python3-setuptools
BuildRequires:  python3-zeroconf

Requires:       python3-cryptography
Requires:       python3-gobject
Requires:       python3-grpcio
Requires:       python3-ifaddr
Requires:       python3-netaddr
Requires:       python3-netifaces
Requires:       python3-packaging
Requires:       python3-protobuf
Requires:       python3-pynacl
Requires:       python3-qrcode
Requires:       python3-setproctitle
Requires:       python3-xapp
Requires:       python3-zeroconf

BuildArch:      noarch

#------------------------------------------------------------------

%description
Warpinator allows you to easily connect multiple computers on a
local area network and share files quickly and securely.

%files -f %{name}.lang
%license COPYING
%doc README.md

%{_bindir}/%{name}
%{_bindir}/%{name}-send

%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{app_id}.png
%{_datadir}/icons/hicolor/scalable/apps/%{app_id}*.svg
# %{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/polkit-1/actions/org.x.%{name}.policy
%{_datadir}/%{name}/

%{_libexecdir}/%{name}/
%{_metainfodir}/%{app_id}.appdata.xml
%{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop

#------------------------------------------------------------------

%package -n nemo-extension-%{name}
Summary:        Warpinator extension for nemo
Requires:       nemo
Requires:       %{name} = %{version}
Supplements:    (nemo and warpinator)
BuildArch:      noarch

%description -n nemo-extension-%{name}
Warpinator allows you to easily connect multiple computers on a local
area network and share files quickly and securely. This package
provides an extension to use warpinator from nemo file browser.

%files -n nemo-extension-%{name}
%{_datadir}/nemo/actions/%{name}*

#------------------------------------------------------------------

%prep
%forgeautosetup -p1

%build
%meson -Dbundle-zeroconf=false -Dbundle-landlock=false -Dbundle-grpc=false
%meson_build

%install
%meson_install

# Files missing hashbangs
for f in config warp_pb2 warp_pb2_grpc
do
  sed -i "1i#!%{_bindir}/python3" %{buildroot}%{_libexecdir}/%{name}/${f}.py
done

%py_byte_compile %{python3} %{buildroot}%{_libexecdir}/%{name}/*.py
chmod +x %{buildroot}%{_libexecdir}/%{name}/*.py

%find_lang %{name} %{?no_lang_C}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/warpinator-autostart.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.appdata.xml

#------------------------------------------------------------------

%changelog
* Wed Oct 16 2024 Hazel Bunny <hazel_bunny@disroot.org> - 1.8.6-2
- Fedora 41 Mass Rebuild

* Tue Jul 30 2024 Hazel Bunny <hazel_bunny@disroot.org> - 1.8.6-1
- initial package
