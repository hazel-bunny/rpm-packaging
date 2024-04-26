%global debug_package %{nil}
%global forgeurl https://github.com/vinceliuice/Colloid-gtk-theme
%global tag 2023-08-12
%global date 20230812

%forgemeta

Name:      colloid-compact-gtk-theme
Version:   0.0
Release:   %autorelease
License:   GPLv3
Group:     User Interface/X
Summary:   Colloid compact gtk theme for linux
URL:       %{forgeurl}
Source:    %{forgesource}

BuildArch: noarch

Requires:  gtk2-engines gtk-murrine-engine gtk2 gtk3 gtk4

BuildRequires: sassc

%description
%{summary}

%files
%{_datadir}/themes/Colloid-*

#------------------------------------------------------------------

%package   black
Summary:   Colloid compact gtk theme for linux with blacker background

%description black
Colloid compact gtk theme for linux with blacker background

%files black
%{_datadir}/themes/ColloidBlack*

#------------------------------------------------------------------

%prep
%forgeautosetup

%build
#nothing

%install
mkdir -p %{buildroot}%{_datadir}/themes
./install.sh -d %{buildroot}%{_datadir}/themes -t all -s compact -n Colloid --tweaks all normal
./install.sh -d %{buildroot}%{_datadir}/themes -t all -s compact -n ColloidBlack --tweaks all normal black

%changelog
* Mon Oct 23 2023 Dipta Biswas <dabiswas112@gmail.com> 0.0-1.20230812
- Initial Package.
