Name:           kommit
Version:        1.3.1
Release:        %autorelease
Summary:        Graphical Git Client

License:        GPL-3.0-or-later AND GPL-2.0-or-later AND BSD-3-Clause
URL:            https://apps.kde.org/kommit/
Source0:        https://invent.kde.org/sdk/kommit/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  qt6-rpm-macros
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6XmlGui)

BuildRequires:  pkgconfig(libgit2)
BuildRequires:  cmake(DolphinVcs)

Requires:       kf6-filesystem
Requires:       hicolor-icon-theme

Provides:       gitklient = %{version}-%{release}
Obsoletes:      gitklient < 1.0

%description
%{summary}.

%prep
%autosetup -n %{name}-v%{version}


%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build


%install
%cmake_install
%find_lang %{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml


%files -f %{name}.lang
%license COPYING LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}diff
%{_bindir}/%{name}merge
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.1.4.0
%{_libdir}/lib%{name}diff.so.0
%{_libdir}/lib%{name}diff.so.1.4.0
%{_libdir}/lib%{name}gui.so.0
%{_libdir}/lib%{name}gui.so.1.4.0
%{_qt6_plugindir}/dolphin/vcs/%{name}dolphinplugin.so
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/actions/*.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/qlogging-categories6/kommit.categories
%{_defaultdocdir}/HTML/en/%{name}


%changelog
* Wed Mar 6 2024 Dipta Biswas <dabiswas112@gmail.com> 1.3.1-1
- Update to 1.3.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 29 2023 Vasiliy Glazov <vascom2@gmail.com> 1.3.0-2
- Rebuild for new dolphin libs

* Mon Oct 30 2023 Vasiliy Glazov <vascom2@gmail.com> 1.3.0-1
- Update to 1.3.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 05 2023 Vasiliy Glazov <vascom2@gmail.com> 1.0.2-1
- Update to 1.0.2

* Thu Mar 30 2023 Vasiliy Glazov <vascom2@gmail.com> 1.0.1-1
- renaming of gitklient
