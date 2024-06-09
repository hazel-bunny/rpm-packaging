Name:          audio-recorder
Version:       2.2.3
Release:       1%{?dist}
Summary:       Audio recorder application for the GNOME 3
License:       GPLv3+
Group:         Sound/Utilities
URL:           https://launchpad.net/audio-recorder
Source0:       https://launchpad.net/%{name}/trunk/stable/+download/%{name}_%{version}.tar.xz
BuildRequires: intltool
BuildRequires: pkgconfig(appindicator3-0.1)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(dconf)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-pbutils-1.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libpulse)
BuildRequires: gcc-c++
Requires:      gstreamer1-plugins-bad-free
Requires:      gstreamer1-plugins-base
Requires:      gstreamer1-plugins-good

%description
Audio-recorder allows you to record your favourite music or audio to
a file. It can record audio from your system's soundcard,
microphones, browsers, webcams & more. Put simply: if it plays out of
your loudspeakers you can record it.

%prep
%setup -q -n %{name}

%build
%configure
make

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/*/%{name}*.svg
%{_datadir}/glib-2.0/schemas/org.gnome.audio-recorder.gschema.xml
%{_mandir}/man1/%{name}.1.gz

%changelog
2023-03-19 - Adrien_D <adriend@fedora.lan> 2.2.3-1.fc37
+ Revision: 2.2.3-1.fc37
- For FC37 et 38
