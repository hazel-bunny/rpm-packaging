Name:           astronciaiptv
Version:        0.0.95
Release:        %autorelease
Group:          Video
License:        GPLv3
URL:            https://gitlab.com/muzena/iptv
Summary:        IPTV player with EPG support

Source0:        %{url}/-/archive/%{version}/iptv-%{version}.tar.bz2

BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-rpm-macros

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

%files
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_metainfodir}/%{name}.appdata.xml

#------------------------------------------------------------------

%prep
%autosetup -n iptv-%{version}
sed -i 's,/usr/lib/,%{_libdir}/,' usr/bin/%{name}
sed -i "s/__DEB_VERSION__/%{version}/g" usr/lib/%{name}/astroncia_iptv.py

%build
%make_build

%install
install -Dm 755 usr/bin/%{name} -t %{buildroot}%{_bindir}

cp -r usr/lib %{buildroot}%{_libdir}
cp -r usr/share %{buildroot}%{_datadir}

%py_byte_compile %{python3} usr/lib/%{name}/*/*.py
%py_byte_compile %{python3} usr/lib/%{name}/*.py

#------------------------------------------------------------------

%changelog
* Sun Jul 9 2023 Dipta Biswas <dabiswas112@gmail.com> 0.0.95-4
- Comply to fedora python packaging guidelines

* Sun Jun 25 2023 Dipta Biswas <dabiswas112@gmail.com> 0.0.95-3
- Tidy up spec

* Fri Jun 23 2023 Dipta Biswas <dabiswas112@gmail.com> 0.0.95-2
- Update sources
- Switch to make for installation

* Mon Jun 19 2023 Dipta Biswas <dabiswas112@gmail.com> 0.0.95-1
- Import from ROSA linux
