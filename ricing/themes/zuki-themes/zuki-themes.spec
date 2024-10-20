Name:            zuki-themes

%global forgeurl https://github.com/lassekongo83/zuki-themes
%global commit   3267bd71ea9dd2001ff4797c48662f8385bf1517
%global date     20220407
%forgemeta

Version:         4.0
Release:         2%{?dist}
Summary:         Themes for GTK, gnome-shell and more
License:         GPL-3.0-or-later
URL:             %{forgeurl}
Source:          %{forgesource}

BuildArch:       noarch

BuildRequires:   meson
BuildRequires:   ninja-build
BuildRequires:   sassc

Requires:        gtk2-engines
Requires:        gtk-murrine-engine
Requires:        gtk2
Requires:        gtk3
Requires:        gtk4

%description
%{summary}

%files
%{_datadir}/themes/Zukitre
%{_datadir}/themes/Zukitre-dark
%{_datadir}/themes/Zukitwo
%{_datadir}/themes/Zukitwo-dark

#------------------------------------------------------------------

%prep
%forgeautosetup -p1

%build
%meson
%meson_build

%install
%meson_install

#------------------------------------------------------------------

%changelog
* Tue Oct 15 2024 Hazel Bunny <hazel_bunny@disroot.org> 4.0-2.git
- Switch to git snapshot

* Mon Jun 19 2023 Hazel Bunny <hazel_bunny@disroot.org> 4.0-1
- Initial Package.
