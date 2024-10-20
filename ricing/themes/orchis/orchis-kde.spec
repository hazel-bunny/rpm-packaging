%global _basename Orchis
%global dev vinceliuice
%global theme_id com.github.%{dev}.%{_basename}

Name:            orchis-kde

%global forgeurl https://github.com/%{dev}/%{_basename}-kde
%global commit   036e831f545de829a7eaa65f0128322663d406e4
%global date     20241012
%forgemeta

Version:         0
Release:         1%{?dist}
Summary:         %{_basename} themes for kde plasma
License:         GPL-3.0-only
URL:             %{forgeurl}
Source:          %{forgesource}

BuildArch:       noarch

Recommends:      %{name}-kvantum
Recommends:      %{name}-decorations
Recommends:      %{name}-konsole
Recommends:      %{name}-wallpapers
Recommends:      %{name}-yakuake

Suggests:        orchis-gtk-theme
Suggests:        papirus-icon-theme

%description
%{_basename} kde is a materia Design theme for KDE Plasma desktop.

In this repository you'll find:
 - Aurorae Themes
 - Kvantum Themes
 - Plasma Color Schemes
 - Plasma Desktop Themes
 - Plasma Look-and-Feel Themes

%files
%license LICENSE
%doc README.md
%{_datadir}/color-schemes/%{_basename}*.colors
%{_datadir}/plasma/desktoptheme/%{_basename}
%{_datadir}/plasma/desktoptheme/%{_basename}-dark
%{_datadir}/plasma/look-and-feel/%{theme_id}
%{_datadir}/plasma/look-and-feel/%{theme_id}-dark

#------------------------------------------------------------------

%package decorations
Summary:    %{_basename}-KDE Aurorae theme

%description decorations
%{_basename} kde is a materia Design theme for KDE Plasma desktop.

This package contains the Aurorae window decorations.

%files decorations
%license LICENSE
%{_datadir}/aurorae/themes/%{_basename}*

#------------------------------------------------------------------

%package kvantum
Summary:    %{_basename}-KDE Kvantum theme
Requires:   kvantum
Requires:   (kvantum-qt5 if qt5-qtbase)

%description kvantum
%{_basename} kde is a materia Design theme for KDE Plasma desktop.

This package contains the %{_basename}Dark and %{_basename}Light Kvantum theme.

%files kvantum
%license LICENSE
%{_datadir}/Kvantum/%{_basename}
%{_datadir}/Kvantum/%{_basename}-solid

#------------------------------------------------------------------

%package sddm
Summary:    %{_basename}-KDE SDDM theme
Requires:   sddm

%description sddm
%{_basename} kde is a materia Design theme for KDE Plasma desktop.

This package contains the %{_basename}Dark and %{_basename} SDDM theme.

%files sddm
%license LICENSE
%{_datadir}/sddm/themes/%{_basename}

#------------------------------------------------------------------

%package wallpapers
Summary:    %{_basename}-KDE wallpapers

%description wallpapers
%{_basename} kde is a materia Design theme for KDE Plasma desktop.

This package contains the %{_basename} wallpapers.

%files wallpapers
%license LICENSE
%{_datadir}/wallpapers/%{_basename}

#------------------------------------------------------------------

%prep
%forgeautosetup -p1

%build
# Nothing to build

%install
# make folders
mkdir -p %{buildroot}%{_datadir}/aurorae/themes
mkdir -p %{buildroot}%{_datadir}/color-schemes
mkdir -p %{buildroot}%{_datadir}/plasma
mkdir -p %{buildroot}%{_datadir}/Kvantum
mkdir -p %{buildroot}%{_datadir}/sddm/themes
mkdir -p %{buildroot}%{_datadir}/wallpapers

# aurorae theme
cp -r aurorae/* %{buildroot}%{_datadir}/aurorae/themes/
# kvantum theme
cp -r Kvantum/* %{buildroot}%{_datadir}/Kvantum/
# color scheme
cp -r color-schemes/* %{buildroot}%{_datadir}/color-schemes/
# desktop theme
cp -r plasma/* %{buildroot}%{_datadir}/plasma/
# look and feel
cp -r wallpaper/* %{buildroot}%{_datadir}/wallpapers/
# sddm
cp -r sddm/6.0/%{_basename} %{buildroot}%{_datadir}/sddm/themes/

rm -rf %{buildroot}%{_datadir}/plasma/desktoptheme/icons

#------------------------------------------------------------------

%changelog
* Fri Oct 18 2024 Hazel Bunny <hazel_bunny@disroot.org> 0-1
- Initial Package.
