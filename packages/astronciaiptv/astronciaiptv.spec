Name:           astronciaiptv
Version:        0.0.95
Release:        2%{?dist}
Group:          Video
License:        GPLv3
URL:            https://gitlab.com/muzena/iptv
Summary:        IPTV player with EPG support

Source0:        %{url}/-/archive/%{version}/iptv-%{version}.tar.bz2

BuildRequires:  make

Requires:       python3
Requires:       mpv
Requires:       python3-qt5
Requires:       python3-pillow
Requires:       python3-gobject
Requires:       python3-unidecode
Requires:       python3-requests
Requires:       python3-setproctitle
Requires:       ffmpeg

Recommends:     yt-dlp

BuildArch:      noarch

%description
%summary

%prep
%autosetup -n iptv-%{version}
sed -i "s/__DEB_VERSION__/%{version}/g" usr/lib/astronciaiptv/astroncia_iptv.py

%build
%make_build

%install
cp -af usr %{buildroot}

%files
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_metainfodir}/%{name}.appdata.xml

%changelog
* Fri Jun 23 2023 Dipta Biswas <dabiswas112@gmail.com> 0.0.95-2
- Update sources
- Switch to make for installation

* Mon Jun 19 2023 Dipta Biswas <dabiswas112@gmail.com> 0.0.95-1
- Import from ROSA linux