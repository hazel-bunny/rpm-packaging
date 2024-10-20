Name:           savedesktop
Version:        3.4.1

%global forgeurl https://github.com/vikdevelop/SaveDesktop
%global tag %{version}
%global date 20240923
%forgemeta

%global app_id io.github.vikdevelop.SaveDesktop

Release:        1%{?dist}
License:        GPL-3.0
Summary:        Save your desktop configuration
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  desktop-file-utils
BuildRequires:  gtk-update-icon-cache
BuildRequires:  hicolor-icon-theme
BuildRequires:  libappstream-glib

BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-dbus

Requires:       gtk4
Requires:       libadwaita
Requires:       python3-gobject
Requires:       python3-dbus

BuildArch:      noarch

%description
Save and load KDE Plasma, Xfce and GNOME-based DE configuration

Supported environments:
 -  GNOME
 -  Xfce
 -  Cinnamon
 -  Budgie
 -  COSMIC (Pop!_OS)
 -  Pantheon
 -  MATE
 -  KDE Plasma

SaveDesktop can save:
 -  your icons, fonts, and themes
 -  your settings
 -  your backgrounds (including dynamic wallpapers, provided that the same username is retained)
 -  your GNOME and Nautilus extensions
 -  your installed Flatpak apps and its data
 -  your Desktop folder in the home directory
 -  other items related to your desktop environment (e.g., Cinnamon extensions and applets, KDE Plasma widgets, etc.)

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/icons/hicolor/{scalable,symbolic}/apps/%{app_id}*.svg
%{_datadir}/icons/hicolor/symbolic/actions/*.{svg,png}
%{_metainfodir}/%{app_id}.metainfo.xml

#------------------------------------------------------------------------------

%prep
%forgeautosetup -p1

# Use system directories
sed -i 's|{home}/.local/share/savedesktop/translations|/usr/share/savedesktop/translations|g' src/localization.py

%build
#nothing

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/{applications,glib-2.0,icons,metainfo}

install -Dm755 %{name} %{buildroot}%{_datadir}/%{name}/src/%{name}

sed -i "s\Exec=%{name}\Exec=python %{_datadir}/%{name}/src/%{name}\ " flatpak/%{app_id}.desktop
install -Dm644 -t %{buildroot}%{_datadir}/applications flatpak/%{app_id}.desktop
install -Dm644 -t %{buildroot}%{_metainfodir} flatpak/%{app_id}.metainfo.xml
install -Dm644 -t %{buildroot}%{_datadir}/glib-2.0/schemas flatpak/%{app_id}.gschema.xml

ln -s %{_datadir}/%{name}/src/%{name} %{buildroot}%{_bindir}/%{name}

cp -R src translations %{buildroot}%{_datadir}/%{name}/

# Install app icons
install -Dm644 -t %{buildroot}%{_datadir}/icons/hicolor/scalable/apps flatpak/icons/%{app_id}.svg
install -Dm644 -t %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps flatpak/icons/%{app_id}-symbolic.svg
install -Dm644 -t %{buildroot}%{_datadir}/icons/hicolor/symbolic/actions flatpak/symbolic-icons/*.{svg,png}

%py_byte_compile %{python3} %{_datadir}/%{name}/src/*.py

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml

#------------------------------------------------------------------------------

%changelog
* Mon Sep 9 2024 Hazel Bunny <hazel_bunny@disroot.org> - 3.4-1
- Update to version 3.4

* Sun Jul 14 2024 Hazel Bunny <hazel_bunny@disroot.org> - 3.3.2-1
- Update to version 3.3.2

* Sat Jul 6 2024 Hazel Bunny <hazel_bunny@disroot.org> - 3.3.1-1
- Update to version 3.3.1

* Mon Jun 17 2024 Hazel Bunny <hazel_bunny@disroot.org> - 3.2.4-1
- initial package


