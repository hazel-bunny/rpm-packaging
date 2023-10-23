%global debug_package %{nil}
%global forgeurl https://github.com/vinceliuice/Colloid-kde
%global commit 0b79befdad9b442b5a8287342c4b7e47ff87d555
%global date 20230705

%forgemeta

Name:      colloid-kde
Version:   0.0
Release:   %autorelease
License:   GPLv3
Summary:   Colloid theme for KDE Plasma
URL:       %{forgeurl}
Source:    %{forgesource}

BuildArch: noarch

%description
Colloid kde theme is a clean and concise theme for KDE Plasma desktop

%prep
%forgeautosetup
sed -i 's,/usr/share,%{buildroot}%{_datadir},' install.sh
sed -i 's,$HOME/.local/share,%{buildroot}%{_datadir},' install.sh
sed -i 's,$HOME/.config,%{buildroot}%{_datadir},' install.sh

%build
#nothing

%install
mkdir -p %{buildroot}%{_datadir}
./install.sh

%files
%{_datadir}/aurorae/themes/Colloid*
%{_datadir}/color-schemes/Colloid*
%{_datadir}/plasma/desktoptheme/Colloid*
%{_datadir}/plasma/look-and-feel/com.github.vinceliuice.Colloid*
%{_datadir}/Kvantum/Colloid*
%{_datadir}/wallpapers/Colloid*

%changelog
* Mon Oct 23 2023 Dipta Biswas <dabiswas112@gmail.com> 0.0-1.20230812
- Initial Package.
