%global debug_package %{nil}
%global forgeurl https://gitlab.com/divinae/focus-plasmoid
%global commit ce21d7b1581b252ec6057151041d902ad6c63077
%global date 20231229
%forgemeta

Name:          fokus-plasmoid
Version:       1.5.5
Release:       %autorelease
Summary:       Simple pomodoro de plasmoid
License:       GPLv3
URL:           %{forgeurl}
Source:        %{forgesource}

BuildRequires: cmake
BuildRequires: extra-cmake-modules

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(Plasma)
BuildRequires: cmake(Plasma5Support)

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

%changelog
%autochangelog
