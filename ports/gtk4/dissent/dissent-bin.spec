%global _basename dissent
%global app_id so.libdb.dissent
%global debug_package %{nil}

%ifarch x86_64
%define _suffix amd64
%else
%ifarch aarch64
%define _suffix arm64
%endif
%endif

Name:       %{_basename}-bin
Version:    0.0.27
Release:    1%{?dist}
License:    GPL-3.0
Summary:    Tiny Discord app
URL:        https://github.com/diamondburned/%{_basename}
Source:     %{url}/releases/download/v%{version}/%{_basename}-linux-%{_suffix}.tar.zst

BuildRequires:    gtk-update-icon-cache
BuildRequires:    desktop-file-utils

Requires:         gtk4 >= 4.10.3
Requires:         gobject-introspection
Requires:         libadwaita >= 1.3.2
Requires:         harfbuzz
Requires:         glib2
Requires:         graphene
Requires:         cairo
Requires:         hicolor-icon-theme
Requires:         pango
Requires:         glibc
Requires:         gdk-pixbuf2
Requires:         libgcc

Provides:         %{_basename}
Conflicts:        %{_basename}

ExclusiveArch:    x86_64 aarch64

%description
Dissent (previously gtkcord4) is a third-party Discord client designed for a
smooth, native experience on Linux desktops. Built with the GTK4 and libadwaita
for a modern look and feel, it delivers your favorite Discord app in a
lightweight and visually appealing package.

Dissent offers a streamlined Discord experience, prioritizing simplicity and
speed over feature completeness on par with the official client. Here's what
you can expect:
 - Text chat with complete Markdown and custom emoji support
 - Guild folders and channel categories
 - Tabbed chat interface
 - Quick switcher for channels and servers
 - Image and file uploads, previews, and downloads
 - User theming via custom CSS
 - Partial thread/forum support
 - Partial message reaction support
 - Partial AI summary support (provided by Discord)

It does not aim to support voice chat and other advanced features, as these are
best handled by the official client or the web app.

%prep
%setup -qn %{_basename}-%{version} -c

%build
#nothing

%install
install -Dm 755 bin/%{_basename} %{buildroot}%{_bindir}/%{_basename}
cp -r share %{buildroot}%{_datadir}
mv -f %{buildroot}%{_datadir}/icons/scalable/* %{buildroot}%{_datadir}/icons/hicolor/scalable
mv -f %{buildroot}%{_datadir}/icons/symbolic %{buildroot}%{_datadir}/icons/hicolor/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop

%files
%{_bindir}/%{_basename}

%{_datadir}/applications/%{app_id}.desktop

%{_datadir}/dbus-1/services/%{app_id}.service
%{_datadir}/dbus-1/services/%{app_id}.WindowServer.service
%{_datadir}/dbus-1/services/%{app_id}.GUI.service

%{_datadir}/icons/hicolor/{scalable,symbolic}/apps/%{app_id}.svg
%{_datadir}/icons/hicolor/scalable/actions/*.svg

%changelog
* Thu Aug 8 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.0.27-1
- initial package

