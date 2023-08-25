%global debug_package %{nil}
%global forgeurl https://gitlab.com/divinae/focus-plasmoid
Version:       1.5.5
%global tag v%{version}
%global date 20221001
%forgemeta

Name:          fokus-plasmoid
Release:       %autorelease
Summary:       Simple pomodoro de plasmoid
License:       GPLv3
URL:           %{forgeurl}
Source:        %{forgesource}

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: cmake(KF5Plasma)

%description
Fokus is simple pomodoro kde plasmoid.

%files
%license LICENSE
%doc README.md
%{_datadir}/plasma/plasmoids/fokus

%prep
%forgeautosetup

%build
#nothing

%install
mkdir -p %{buildroot}%{_datadir}/plasma/plasmoids/fokus/
cp -r package/* %{buildroot}%{_datadir}/plasma/plasmoids/fokus/
rm -rf %{buildroot}%{_datadir}/plasma/plasmoids/fokus/CMakeLists.txt

%changelog
%autochangelog
