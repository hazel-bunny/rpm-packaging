%global _basename ChatAI-Plasmoid
%global debug_package %{nil}

Name:           chatai-plasmoid

%global forgeurl https://github.com/DenysMb/%{_basename}
# %global tag %{version}
%global commit d3048fdd76f00e733c9f9fb298fc6338acb6a778
%global date 20240802
%forgemeta

Version:        1.8.0
Release:        2%{?dist}
Summary:        A range of chatbots as Plasmoid for your KDE Plasma desktop
License:        BSD-3-Clause
URL:            %{forgeurl}
Source:         %{forgesource}
BuildArch:      noarch
Requires:       plasma-workspace

%description
%summary

%files
%license LICENSE
%doc README.md
%{_datadir}/plasma/plasmoids/%{_basename}

%prep
%forgeautosetup

%build
#nothing

%install
mkdir -p %{buildroot}%{_datadir}/plasma/plasmoids/%{_basename}/
cp -r contents %{buildroot}%{_datadir}/plasma/plasmoids/%{_basename}/
install -Dm644 metadata.json %{buildroot}%{_datadir}/plasma/plasmoids/%{_basename}/

%changelog
* Mon Oct 14 2024 Hazel Bunny <hazel_bunny@disroot.org> - 1.8.0-2.git
- Switch to git snapshot

* Thu Aug 8 2024 Hazel Bunny <hazel_bunny@disroot.org> - 1.8.0-1
- Upgrade to version 1.8.0

* Sun Jul 14 2024 Hazel Bunny <hazel_bunny@disroot.org> - 1.6.0-1
- Upgrade to version 1.6.0

* Fri Jun 28 2024 Hazel Bunny <hazel_bunny@disroot.org> - 1.5.0-1
- Upgrade to version 1.5.0

* Wed Jun 19 2024 Hazel Bunny <hazel_bunny@disroot.org> - 1.4.0-1
- initial package
