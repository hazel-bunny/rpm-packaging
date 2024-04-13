%global debug_package %{nil}
%global forgeurl https://gitlab.com/divinae/focus-plasmoid
%global commit 09d8e4b73eff15ab42c79149cead255c191c72a5
%global date 20240326
%forgemeta

Name:          fokus-plasmoid
Version:       2.1.0
Release:       1%{?dist}
Summary:       Simple pomodoro de plasmoid
License:       GPLv3
URL:           %{forgeurl}
Source:        %{forgesource}

Requires:      plasma-workspace
Requires:      kf6-kirigami
Requires:      libplasma

%description
Fokus is simple pomodoro kde plasmoid.

%files
%license LICENSE
%doc README.md
%{_datadir}/plasma/plasmoids/com.dv.fokus

%prep
%forgeautosetup

%build
#nothing

%install
mkdir -p %{buildroot}%{_datadir}/plasma/plasmoids/com.dv.fokus/
cp -r package/* %{buildroot}%{_datadir}/plasma/plasmoids/com.dv.fokus/

%changelog
%autochangelog
