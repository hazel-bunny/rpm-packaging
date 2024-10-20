%global debug_package %{nil}

Name:           yuki-iptv
%global forgeurl https://codeberg.org/liya/%{name}
Version:        0.0.14
%forgemeta

Release:        1%{?dist}
Summary:        IPTV player with EPG support
Group:          Multimedia
License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  hicolor-icon-theme
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-rpm-macros
BuildArch:      noarch

Requires:       mpv-libs
Requires:       python3-pyqt6
Requires:       python3-gobject
Requires:       python3-unidecode
Requires:       python3-chardet
Requires:       python3-requests
Requires:       python3-setproctitle
Requires:       python3-wand
Requires:       ffmpeg
Requires:       yt-dlp

Obsoletes:      astronciaiptv <= 0.0.95

%description
IPTV player with EPG support

%files
%{_bindir}/%{name}

%{_prefix}/lib/%{name}

%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_metainfodir}/%{name}.appdata.xml

#------------------------------------------------------------------

%prep
%forgeautosetup -p1
sed -i "s/QT_QPA_PLATFORM=xcb/QT_QPA_PLATFORM=wayland/g" usr/bin/%{name}
sed -i "s/__DEB_VERSION__/%{version}/g" usr/lib/%{name}/%{name}.py
# sed -i "s/"styleredefoff": True/"styleredefoff": False/g" usr/lib/%{name}/yuki_iptv/settings.py
# sed -i "s/setAppFusion = True/setAppFusion = False/g" usr/lib/%{name}/%{name}.py

%build
%make_build

%install
install -Dm 755 usr/bin/%{name} -t %{buildroot}%{_bindir}

cp -r usr/lib %{buildroot}%{_prefix}/lib
cp -r usr/share %{buildroot}%{_datadir}

%py_byte_compile %{python3} usr/lib/%{name}/*/*.py
%py_byte_compile %{python3} usr/lib/%{name}/*.py

%changelog
* Tue Oct 13 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.0.14-1
- Upgrade to 0.0.14

* Mon Sep 9 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.0.13-1
- Upgrade to 0.0.13

* Fri Apr 26 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.0.11-1
- Upgrade to 0.0.11

* Sun Apr 14 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.0.10-1
- initial package
