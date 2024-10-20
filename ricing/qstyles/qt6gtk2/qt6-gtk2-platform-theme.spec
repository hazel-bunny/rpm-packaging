%global _basename qt6gtk2
%global forgeurl https://github.com/trialuser02/%{_basename}
%global commit b574ba5b59edf5ce220ca304e1d07d75c94d03a2
# %%global shortcommit %%(c=%%{commit}; echo ${c:0:7})
%global date 20240814
%forgemeta

Name:     qt6-gtk2-platform-theme
Version:  0.2
Release:  1%{?dist}
Summary:  GTK+2.0 integration plugins for Qt6
License:  GPL-2.0

URL:      %{forgeurl}
Source:   %{forgesource}

BuildRequires: make

BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtbase-private-devel
BuildRequires: qt6-qtbase-static

BuildRequires: gtk2-devel
BuildRequires: libX11-devel

%description
Qt6Gtk2 - GTK+2.0 integration plugins for Qt6

%prep
%forgeautosetup

%build
%qmake_qt6 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%license COPYING
%doc README.md ChangeLog AUTHORS
%{_qt6_plugindir}/platformthemes/libqt6gtk2.so
%{_qt6_plugindir}/styles/libqt6gtk2-style.so

%changelog
* Wed Oct 16 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.2-1.20240814gitb574ba5b
- Fedora 41 Mass Rebuild

* Mon Jul 8 2024 Hazel Bunny <hazel_bunny@disroot.org> 0.2-1.20240623git2e872948
- Rebuild for Qt 6.7.2

* Wed Jun 19 2024 Hazel Bunny <hazel_bunny@disroot.org> 0.2-1.20240120git5df96819
- Fix license
- Rebuild for Qt 6.7.0

* Thu Jul 27 2023 Hazel Bunny <hazel_bunny@disroot.org> 0.2-1.20220520git2a21a8ad
- Fix license
- Add docs
- Rebuild for Qt 6.5.2

* Mon Jul 17 2023 Hazel Bunny <hazel_bunny@disroot.org> 0.0^git20220520-2
- Rebuild for Qt 6.5.1

* Sat May 6 2023 Hazel Bunny <hazel_bunny@disroot.org> 0.0^git20220520-1
- Initial Package.
