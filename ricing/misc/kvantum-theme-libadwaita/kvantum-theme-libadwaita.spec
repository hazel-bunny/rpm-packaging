%global _basename KvLibadwaita
%global forgeurl https://github.com/GabePoel/%{_basename}
%global commit 87c1ef9f44ec48855fd09ddab041007277e30e37
%global date 20240316
%forgemeta

Name:      kvantum-theme-libadwaita
Version:   0.0
Release:   2%{?dist}
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
%{_datadir}/color-schemes/Libadwaita*
%{_datadir}/Kvantum/%{_basename}
%{_datadir}/Kvantum/%{_basename}Dark

%prep
%forgeautosetup

%build
# Nothing to do here

%install
mkdir -p %{buildroot}%{_datadir}/color-schemes
mkdir -p %{buildroot}%{_datadir}/Kvantum/%{_basename}Dark
mkdir -p %{buildroot}%{_datadir}/Kvantum/%{_basename}
cd src
cp -r Colors/* %{buildroot}%{_datadir}/color-schemes/
cp -r %{_basename}/%{_basename}Dark.* %{buildroot}%{_datadir}/Kvantum/%{_basename}Dark/
cp -r %{_basename}/%{_basename}.* %{buildroot}%{_datadir}/Kvantum/%{_basename}/

%changelog
* Tue Oct 15 2024 Hazel Bunny <hazel_bunny@disroot.org> 0.0-2
- Update git snapshot

* Thu Oct 26 2023 Hazel Bunny <hazel_bunny@disroot.org> 0.0-1
- Initial Package.
