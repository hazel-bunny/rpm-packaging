%global _basename plasma6-window-title-applet
%global debug_package %{nil}

%global forgeurl https://github.com/dhruv8sh/%{_basename}
Version:        0.9.0
# %%global commit 6d6b939bb8138a8b1640cf2f6d395a3030d7bbaa
# %%global date 20240411
%forgemeta

%global applet_id org.kde.windowtitle

Name:           applet-window-title
Release:        2%{?dist}
Summary:        Plasma 6 applet that shows the application title and icon for active window
License:        GPL-2.0-or-later

URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch
BuildRequires:  desktop-file-utils
Requires:       plasma-workspace

%description
This is a Plasma 6 applet that shows the current window title and icon in your
panels. This plasmoid is coming from Latte land but it can also support Plasma
panels.

%files
%license LICENSE
%doc README.md
%{_datadir}/plasma/plasmoids/%{applet_id}/

%prep
%forgeautosetup

%build
#nothing

%install
mkdir -p %{buildroot}%{_datadir}/plasma/plasmoids/%{applet_id}/
cp -r contents %{buildroot}%{_datadir}/plasma/plasmoids/%{applet_id}/
install -Dm644 metadata.json %{buildroot}%{_datadir}/plasma/plasmoids/%{applet_id}/

%changelog
* Mon Oct 14 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.9.0-2
- Fedora 41 Mass Rebuild

* Tue Jul 30 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.9.0-1
- Update to 0.9.0

* Wed Jun 19 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.5-1
- initial package
