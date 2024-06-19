Name:           dconf-editor
Version:        3.20.3
Release:        1%{?dist}
Epoch:          1
Summary:        Configuration editor for dconf

License:        GPL-3.0-or-later AND CC0-1.0
URL:            https://wiki.gnome.org/Projects/dconf
Source0:        https://download.gnome.org/sources/%{name}/3.20/%{name}-%{version}.tar.xz

%global app_id ca.desrt.%{name}

BuildRequires:  /usr/bin/appstream-util
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  pkgconfig(dconf)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  vala

%description
Graphical tool for editing the dconf configuration database.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%find_lang dconf

%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/appdata/%{app_id}.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{app_id}.desktop

%files -f dconf.lang
%license COPYING
%{_bindir}/%{name}
%{_datadir}/appdata/%{app_id}.appdata.xml
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/dbus-1/services/%{app_id}.service
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}-symbolic.svg
%{_mandir}/man1/%{name}.1*

%changelog
* Thu Jun 30 2016 Kalev Lember <klember@redhat.com> - 3.20.3-1
- Update to 3.20.3

* Tue May 10 2016 Kalev Lember <klember@redhat.com> - 3.20.2-1
- Update to 3.20.2

* Thu Apr 14 2016 Kalev Lember <klember@redhat.com> - 3.20.1-1
- Update to 3.20.1

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Tue Mar 15 2016 Richard Hughes <rhughes@redhat.com> - 3.19.92-1
- Update to 3.19.92

* Tue Mar 01 2016 Richard Hughes <rhughes@redhat.com> - 3.19.91-1
- Update to 3.19.91

* Tue Feb 16 2016 Richard Hughes <rhughes@redhat.com> - 3.19.90-1
- Update to 3.19.90

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Kalev Lember <klember@redhat.com> - 3.19.3-1
- Update to 3.19.3

* Tue Nov 24 2015 Kalev Lember <klember@redhat.com> - 3.19.2-1
- Update to 3.19.2

* Fri Nov 13 2015 Kalev Lember <klember@redhat.com> - 3.18.2-1
- Update to 3.18.2

* Mon Oct 12 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Tue Sep 15 2015 Kalev Lember <klember@redhat.com> - 3.17.92-1
- Update to 3.17.92

* Tue Sep 01 2015 Kalev Lember <klember@redhat.com> - 3.17.91-1
- Update to 3.17.91

* Wed Aug 19 2015 Kalev Lember <klember@redhat.com> - 3.17.90-1
- Update to 3.17.90

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 01 2015 Kalev Lember <kalevlember@gmail.com> - 3.17.1-1
- Update to 3.17.1

* Tue Apr 14 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.1-1
- Update to 3.16.1

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-1
- Update to 3.15.92
- Ship the man page

* Tue Mar 03 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-3
- Fix unowned HighContrast icon theme directories (#1197898)

* Tue Mar 03 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-2
- Fix appdata screenshot URL
- Validate appdata during %%check

* Mon Mar 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-1
- Initial Fedora packaging
