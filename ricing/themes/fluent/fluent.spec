%global _basename Fluent
%global year 2024
%global month 06
%global day 12

Name:            fluent-gtk-theme

%global forgeurl https://github.com/vinceliuice/%{_basename}-gtk-theme
# %%global tag   %{year}-%{month}-%{day}
%global commit   1c7d2c97605c1fccc36a48c1c711ca5c19baec98
%global date     %{year}10%{day}
%forgemeta

Version:         %{year}.%{month}.%{day}
Release:         1%{?dist}
Summary:         Fluent design theme for GNOME/GTK based desktop environments
License:         GPL-3.0
URL:             %{forgeurl}
Source:          %{forgesource}

BuildArch:       noarch
BuildRequires:   sassc

Requires:        gtk2-engines
Requires:        gtk-murrine-engine
Requires:        gnome-themes-extra

%description
Fluent is a %summary.

%files
%{_datadir}/themes/%{_basename}*
%exclude %{_datadir}/themes/%{_basename}-round*

#------------------------------------------------------------------

%package    round
Summary:    Material Design theme for GNOME/GTK based desktop environments - Round variant

%description round
Orchis is a Material Design theme for GNOME/GTK based desktop environments.

This package contains the round variant.

%files      round
%{_datadir}/themes/%{_basename}-round*

#------------------------------------------------------------------

%prep
%forgeautosetup -p1

%build
./parse-sass.sh

%install
mkdir -p %{buildroot}%{_datadir}/themes
./install.sh -i fedora -t all -d %{buildroot}%{_datadir}/themes
./install.sh -i fedora -t all --tweaks round float -d %{buildroot}%{_datadir}/themes

#------------------------------------------------------------------

%changelog
* Sun Oct 20 2024 Hazel Bunny <hazel_bunny@disroot.org> 2024.06.12-1
- Initial Package
