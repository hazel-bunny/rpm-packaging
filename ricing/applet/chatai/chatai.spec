%global _basename ChatAI-Plasmoid
%global debug_package %{nil}

Name:           chatai-plasmoid
Version:        1.4.0

%global forgeurl https://github.com/DenysMb/%{_basename}
%global tag %{version}
%global date 20240614
%forgemeta

Release:        1%{?dist}
Summary:        A range of chatbots as Plasmoid for your KDE Plasma desktop
License:        Unlicense
URL:            %{forgeurl}
Source:         %{forgesource}
BuildArch:      noarch
Requires:       plasma-workspace

%description
%summary

%files
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
* Wed Jun 19 2024 Dipta Biswas <dabiswas112@gmail.com> - 1.4.0-1
- initial package
