Name:           warehouse
Version:        1.6.5

%global forgeurl https://github.com/flattool/%{name}
%global tag %{version}
%global date 20240920
%forgemeta

%global app_id io.github.flattool.Warehouse

Release:        1%{?dist}
License:        GPL-3.0
Summary:        View flatpak info, manage user data, and batch manage installed flatpaks
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  blueprint-compiler
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection
BuildRequires:  gtk4-devel
BuildRequires:  gtk-update-icon-cache
BuildRequires:  hicolor-icon-theme
BuildRequires:  libadwaita-devel
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  python3-devel
BuildRequires:  python3-gobject

Requires:       flatpak-xdg-utils
Requires:       gtk4
Requires:       libadwaita
Requires:       python3-gobject

BuildArch:      noarch

%description
Warehouse is a versatile toolbox for managing flatpak user data, viewing flatpak
app info, and batch managing installed flatpaks.

🚀 Main Features:
 - Viewing Flatpak Info: 📋 Warehouse can display all the information provided
   by the flatpak list command in a user-friendly graphical window. Each item
   includes a button for easy copying.

 - Managing User Data: 🗑️ Flatpaks store user data in a specific system
   location, often left behind when an app is uninstalled. Warehouse can
   uninstall an app and delete its data, delete data without uninstalling, or
   simply show if an app has user data.

 - Batch Actions: ⚡ Warehouse features a batch mode for swift uninstallations,
   user data deletions, and app ID copying in bulk.

 - Leftover Data Management: 📁 Warehouse scans the user data folder to check
   for installed apps associated with the data. If none are found, it can delete
   the data or attempt to install a matching flatpak.

 - Manage Remotes: 📦 Installed and enabled Flatpak remotes can be deleted, and
   new remotes can be added.

%files
%license COPYING
%doc README.md

%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/icons/hicolor/{scalable,symbolic}/apps/%{app_id}*.svg
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo

%{_metainfodir}/%{app_id}.metainfo.xml

%prep
%forgeautosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%__chmod 0755 %{buildroot}%{_bindir}/%{name}
%py_byte_compile %{python3} %{_datadir}/%{name}/flattool_gui/*.py

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml

%changelog
* Fri Sep 20 2024 Hazel Bunny <hazel_bunny@disroot.org> - 1.6.5-1
- Update to 1.6.5

* Sun Jul 7 2024 Hazel Bunny <hazel_bunny@disroot.org> - 1.6.4-1
- Update to 1.6.4

* Sat Jun 15 2024 Hazel Bunny <hazel_bunny@disroot.org> - 1.6.2-2
- Fix permissions

* Fri Jun 14 2024 Hazel Bunny <hazel_bunny@disroot.org> - 1.6.2-1
- initial package


