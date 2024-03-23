%global forgeurl https://github.com/moodyhunter/applet-window-buttons6
%global date 20240308
%global commit a7b95da32717b90a1d9478db429d6fa8a6c4605f
%forgemeta

%global orig_name org.kde.windowbuttons

Name:           applet-window-buttons
Version:        0.12.0
Release:        %autorelease
Summary:        Plasma 6 applet to show window buttons in panels
License:        GPL-2.0-or-later
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(KDecoration2)

Requires:       plasma-workspace

Provides:       applet-window-buttons6 = %{version}-%{release}

%description
This is a Plasma 6 applet that shows the current window appmenu in
one's panels. This plasmoid is coming from Latte land, but it can also
support Plasma panels.

%prep
%forgeautosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

# Bad icon name
sed -i "/<icon type=\"stock\">/d" %{buildroot}%{_datadir}/metainfo/%{orig_name}.appdata.xml


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{orig_name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/plasma/plasmoids/%{orig_name}/metadata.desktop

%files
%license LICENSE
%{_kf6_datadir}/plasma/plasmoids/%{orig_name}
%{_qt6_qmldir}/org/kde/appletdecoration
%{_kf6_metainfodir}/%{orig_name}.appdata.xml


%changelog
* Fri Mar 15 2024 Dipta Biswas <dabiswas112@gmail.com> - 0.12.0-1.git
- Switch to a git snapshot to fix metadata.json

* Fri Mar 8 2024 Dipta Biswas <dabiswas112@gmail.com> - 0.12.0-1
- Update to version 0.12.0

* Wed Feb 21 2024 Alessandro Astone <ales.astone@gmail.com> - 0.11.1^20240221.3047ed7-1
- Switch to a fork compatible with Plasma 6

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 0.11.1-6
- Cosmetic changes to the spec file.
- Add patch from PR 191 locally.

* Tue Jan 31 2023 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0.11.1-5
- Rebuilt for kde 5.26.90 library changes

* Tue Jan 31 2023 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0.11.1-4
- Rebuilt for libkdecorations2private.so

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 31 2022  Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0.11.1-1
- Update to version 0.11.1

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 7 2021  Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0.10.1-1
- 0.10.1

* Tue Dec 7 2021  Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0.9.0-5
- 00-fix-update-override.patch add into git source for fix build problem (#2024145)
- cosmetic fixes

* Wed Oct 13 2021 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0.9.0-4
- rawhide-fixing build attempt #1
- 00-fix-update-override.patch added.

* Thu Jul 29 2021 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0.9.0-3
- BR : appstream added fix build errors

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 12 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 0.9.0-1
- initial package
