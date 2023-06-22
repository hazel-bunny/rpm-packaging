Summary:	IPTV player
Name:		astronciaiptv
Version:	0.0.95
Release:	1%{?dist}
Group:		Video
License:	GPLv3
URL:		https://gitlab.com/muzena/iptv/
Source0:	https://gitlab.com/muzena/iptv/-/archive/%{version}/iptv-%{version}.tar.bz2
Requires:	python3
Requires:	mpv
Requires:	python3-qt5
Requires:	python3-pillow
Requires:	python3-gobject
Requires:	python3-unidecode
Requires:	python3-requests
Requires:	python3-setproctitle
Requires:	ffmpeg
BuildArch:	noarch

%description
IPTV player.

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/locale/*/*/astronciaiptv.mo
%{_prefix}/lib/%{name}
%{_datadir}/icons/hicolor/scalable/apps/astronciaiptv.svg
%{_metainfodir}/astronciaiptv.appdata.xml

%prep
%setup -q

%build
#nothing

%install
cp -af usr %{buildroot}

%changelog
* Mon Jun 19 2023 Dipta Biswas <dabiswas112@gmail.com> 0.0.95-1
- Import from ROSA linux