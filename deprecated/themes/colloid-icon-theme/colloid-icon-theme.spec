%global debug_package %{nil}
%global forgeurl https://github.com/vinceliuice/Colloid-icon-theme
%global tag 2023-07-01
%global date 20230701

%forgemeta

Name:           colloid-icon-theme
Version:        0.0
Release:        %autorelease
License:        GPLv3
Summary:        Colloid icon theme for linux desktops
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gtk-update-icon-cache

BuildArch:      noarch

%description
%{summary}

%prep
%forgeautosetup

%build
#nothing

%install
mkdir -p %{buildroot}%{_datadir}/icons
./install.sh -d %{buildroot}%{_datadir}/icons -t all -s all

%files
%{_datadir}/icons/Colloid*

%changelog
* Mon Oct 23 2023 Dipta Biswas <dabiswas112@gmail.com> 0.0-1.20230701
- Initial Package.
