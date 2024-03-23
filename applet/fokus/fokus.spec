%global debug_package %{nil}
%global forgeurl https://gitlab.com/divinae/focus-plasmoid
%global commit 27129140956645d8ab17eb2ca847cdb7d97d7496
%global date 20240315
%forgemeta

Name:          fokus-plasmoid
Version:       2.1.0
Release:       %autorelease
Summary:       Simple pomodoro de plasmoid
License:       GPLv3
URL:           %{forgeurl}
Source:        %{forgesource}

Requires:      plasma-workspace
Requires:      kf6-kirigami2
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
