%global _basename feedreader
%global app_id org.gnome.FeedReader

%global forgeurl https://github.com/39aldo39/%{_basename}

Version:        2.12.0
%forgemeta

Name:           %{_basename}-decsync
Release:        %autorelease
Summary:        RSS desktop client

# Some of the source files are GPLv3+ and some are LGPLv3+, which makes the
# combined work GPLv3+.
License:        GPLv3+
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gumbo)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(rest-0.7)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  libdecsync-devel
BuildRequires:  vala
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate

Requires:       dbus
Requires:       libdecsync
Requires:       hicolor-icon-theme

Conflicts:      %{_basename}

%description
FeedReader is a modern desktop application designed to complement existing
web-based RSS accounts. It combines all the advantages of web based services
like synchronization across all your devices with everything you expect from a
modern desktop application.

%prep
%setup -qn FeedReader-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{_basename}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop

%files -f %{_basename}.lang
%license LICENSE
%{_bindir}/%{_basename}
%{_libdir}/%{_basename}/
%{_libdir}/libFeedReader.so
%{_datadir}/%{_basename}/
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.%{_basename}*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{app_id}.svg
%{_datadir}/icons/hicolor/scalable/apps/%{app_id}-symbolic.svg
%{_metainfodir}/%{app_id}.appdata.xml

%changelog
%autochangelog
