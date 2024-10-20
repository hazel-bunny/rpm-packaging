%global _basename Colloid
%global year 2024
%global month 06
%global day 18

Name:            colloid-gtk-theme

%global forgeurl https://github.com/vinceliuice/%{_basename}-gtk-theme
# %%global tag   %{year}-%{month}-%{day}
%global commit   8ebb9b1fb3827f8d78bb28217da918f10e874b30
%global date     %{year}1019
%forgemeta

Version:         %{year}.%{month}.%{day}
Release:         1%{?dist}
Summary:         Colloid gtk theme for linux
License:         GPL-3.0
URL:             %{forgeurl}
Source:          %{forgesource}

BuildArch:       noarch

BuildRequires:   sassc

Requires:        gtk2-engines
Requires:        gtk-murrine-engine
Requires:        gnome-themes-extra

%description
%summary.

%files
%{_datadir}/themes/%{_basename}*
%exclude %{_datadir}/themes/%{_basename}-Black*
%exclude %{_datadir}/themes/%{_basename}-*-Nord*
%exclude %{_datadir}/themes/%{_basename}-*-Dracula*

#------------------------------------------------------------------

%package    black
Summary:    Material Design theme for GNOME/GTK based desktop environments - Full black variant

%description black
Orchis is a Material Design theme for GNOME/GTK based desktop environments.

This package contains the full black variant.

%files      black
%{_datadir}/themes/%{_basename}-Black*

#------------------------------------------------------------------

%package    nord
Summary:    Material Design theme for GNOME/GTK based desktop environments - nord variant

%description nord
Orchis is a Material Design theme for GNOME/GTK based desktop environments.

This package contains the nord variant.

%files      nord
%{_datadir}/themes/%{_basename}-*-Nord*

#------------------------------------------------------------------

%package    dracula
Summary:    Material Design theme for GNOME/GTK based desktop environments - dracula variant

%description dracula
Orchis is a Material Design theme for GNOME/GTK based desktop environments.

This package contains the dracula variant.

%files      dracula
%{_datadir}/themes/%{_basename}-*-Dracula*

#------------------------------------------------------------------

%prep
%forgeautosetup -p1

%build
./parse-sass.sh

%install
mkdir -p %{buildroot}%{_datadir}/themes
./install.sh -i fedora -t all --shell 46 --tweaks primary dock -d %{buildroot}%{_datadir}/themes
./install.sh -n Orchis-Black -i fedora -t all --shell 46 --tweaks primary dock black -d %{buildroot}%{_datadir}/themes
./install.sh -i fedora -t all --shell 46 --tweaks primary dock nord -d %{buildroot}%{_datadir}/themes
./install.sh -i fedora -t all --shell 46 --tweaks primary dock dracula -d %{buildroot}%{_datadir}/themes

#------------------------------------------------------------------

%changelog
* Sun Oct 20 2024 Hazel Bunny <hazel_bunny@disroot.org> 2024.09.02-2
- Fix package names

* Fri Oct 18 2024 Hazel Bunny <hazel_bunny@disroot.org> 2024.09.02-1
- Initial Package.
