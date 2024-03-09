%global debug_package %{nil}
%global forgeurl https://gitlab.com/divinae/focus-plasmoid
%global commit ce21d7b1581b252ec6057151041d902ad6c63077
%global date 20231229
%forgemeta

Name:          fokus-plasmoid
Version:       2.0.1
Release:       %autorelease
Summary:       Simple pomodoro de plasmoid
License:       GPLv3
URL:           %{forgeurl}
Source:        %{forgesource}

Requires:      kf6-kirigami2
Requires:      libplasma
Requires:      plasma5support

%description
Fokus is simple pomodoro kde plasmoid.

%files
%license LICENSE
%doc README.md
%dir %{_datadir}/plasma/plasmoids/com.dv.fokus

%prep
%forgeautosetup

%build
#nothing

%install
mkdir -p %{buildroot}%{_datadir}/plasma/plasmoids/com.dv.fokus/
cp -r package/* %{buildroot}%{_datadir}/plasma/plasmoids/com.dv.fokus/

%changelog
%autochangelog
