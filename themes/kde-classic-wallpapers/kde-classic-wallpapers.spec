%global debug_package %{nil}

Name:    kde-classic-wallpapers
Version: 1.0

%global forgeurl https://github.com/MartinF99/%{name}
%global commit c04778741803f07c35d7b271fb7de07c68ceb815
%global date 20230926
%forgemeta

Release: 2%{?dist}
Summary: An archive of all classic kde wallpapers
License: GPL-3.0
URL:     %{forgeurl}
Source:  %{forgesource}

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: qt5-qtbase-devel
BuildRequires: kf5-kcoreaddons

%description
%summary

%prep
%forgeautosetup

%build
%cmake -DQT_MAJOR_VERSION=5
%cmake_build

%install
%cmake_install

for f in "%{buildroot}%{_datadir}/wallpapers/"*; do
  desktoptojson -i "${f}""/metadata.desktop" -o "${f}""/metadata.json"
done

%check

%files
%license LICENSE
%doc README.md
%{_datadir}/wallpapers/*

%changelog
%autochangelog
