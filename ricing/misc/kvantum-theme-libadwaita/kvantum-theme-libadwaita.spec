%global _basename KvLibadwaita
%global forgeurl https://github.com/GabePoel/%{_basename}
%global commit 61f2e0b04937b6d31f0f4641c9c9f1cc3600a723
%global date 20220806
%forgemeta

Name:      kvantum-theme-libadwaita
Version:   0.0
Release:   %{autorelease}
Summary:   Libadwaita theme for Kvantum
License:   GPLv3
URL:       %{forgeurl}
Source:    %{forgesource}
BuildArch: noarch
Requires:  kvantum

%description
%summary

%files
%license LICENSE
%doc README.md
%{_datadir}/Kvantum/%{_basename}

%prep
%forgeautosetup

%build
# Nothing to do here

%install
mkdir -p %{buildroot}%{_datadir}/Kvantum
cd src
cp -r %{_basename} %{buildroot}%{_datadir}/Kvantum/

%changelog
* Thu Oct 26 2023 Dipta Biswas <dabiswas112@gmail.com> 0.0-1
- Initial Package.
