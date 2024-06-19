Name:          audio-recorder
Version:       3.3.4

%global app_id org.gnome.%{name}
%global ubuntu jammy

Release:       1%{?dist}
Summary:       Audio recorder application for the GNOME 3
License:       GPL-3.0
URL:           https://launchpad.net/%{name}
Source0:       https://launchpad.net/~%{name}/+archive/ubuntu/ppa/+sourcefiles/%{name}/%{version}~%{ubuntu}/%{name}_%{version}~%{ubuntu}.tar.gz

BuildRequires: gcc-c++
BuildRequires: gdk-pixbuf2
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
BuildRequires: pkgconfig(libpipewire-0.3)

Requires:      gstreamer1-plugins-base
Requires:      gstreamer1-plugins-good
Requires:      gstreamer1-plugins-bad-free
Requires:      libappindicator-gtk3

Recommends:    gstreamer1-plugins-bad-freeworld
Recommends:    gstreamer1-plugins-ugly
Recommends:    gstreamer1-plugin-libav

%description
Audio-recorder allows you to record your favourite music or audio to a file. It
can record audio from your system's soundcard, microphones, browsers, webcams &
more. Put simply: if it plays out of your loudspeakers you can record it.

%prep
%setup -qn %{name}-%{version} -c

%build
pushd trunk
%configure
%make_build
popd

%install
pushd trunk
%make_install
popd
%find_lang %{name}

%files -f %{name}.lang
%license trunk/COPYING
%doc trunk/{AUTHORS,ChangeLog,NEWS,README,TODO}

%{_bindir}/%{name}

%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/*/%{name}*.svg
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml

%{_mandir}/man1/%{name}.1.gz

%changelog
* Tue Jun 18 2024 Dipta Biswas <dabiswas112@gmail.com> - 3.3.4-1
- initial package
