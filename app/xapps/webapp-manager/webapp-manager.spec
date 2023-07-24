Name:    webapp-manager
Version: 1.3.2
Release: %autorelease
License: GPLv3+
URL:     https://github.com/linuxmint/%{name}
Summary: Web Application Manager

Source0: %url/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gettext
BuildRequires: make
BuildRequires: python3-devel
BuildRequires: python3-rpm-macros

Requires: python3-beautifulsoup4
Requires: python3-configobj
Requires: python3-gobject
Requires: python3-pillow
Requires: python3-setproctitle
Requires: python3-tldextract
Requires: xapps

BuildArch: noarch

%description
Launch websites as if they were apps.

%files
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/kde4/%{name}.desktop
%{_datadir}/desktop-directories/webapps-webapps.directory
%{_datadir}/glib-2.0/schemas/org.x.%{name}.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/categories/applications-webapps.svg
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/%{name}/
%{_sysconfdir}/xdg/menus/applications-merged/webapps.menu

#------------------------------------------------------------------

%prep
%autosetup -p1
sed -i 's,/usr/lib/,%{_libdir}/,' usr/bin/%{name}
sed -i "s/__DEB_VERSION__/%{version}/g" usr/lib/%{name}/%{name}.py

%build
%make_build

%install
install -Dm 755 usr/bin/%{name} -t %{buildroot}%{_bindir}

cp -r etc %{buildroot}%{_sysconfdir}
cp -r usr/lib %{buildroot}%{_libdir}
cp -r usr/share %{buildroot}%{_datadir}

%py_byte_compile %{python3} %{buildroot}%{_libdir}/%{name}/*.py

#------------------------------------------------------------------

%changelog
* Sun Jul 9 2023 Dipta Biswas <dabiswas112@gmail.com> 1.3.2-2
- Comply to fedora python packaging guidelines

* Sun Jun 25 2023 Dipta Biswas <dabiswas112@gmail.com> 1.3.2-1
- Bump version
- Fix app version in about screen

* Thu Jun 15 2023 Dipta Biswas <dabiswas112@gmail.com> 1.3.0-2
- Bump version
- Fix app entry in kickoff

* Fri Jun 9 2023 Dipta Biswas <dabiswas112@gmail.com> 1.1.5-1
- Import from github:refi64/webapp-manager-fedora
