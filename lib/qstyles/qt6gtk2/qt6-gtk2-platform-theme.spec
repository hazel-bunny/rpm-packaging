%global _basename qt6gtk2
%global forgeurl https://github.com/trialuser02/%{_basename}
%global commit 2a21a8ad59a76e6928fae1699c830ca24fb2461c
# %%global shortcommit %%(c=%%{commit}; echo ${c:0:7})
%global date 20220520
%forgemeta

Name:     qt6-gtk2-platform-theme
Version:  0.2
Release:  %autorelease
Summary:  GTK+2.0 integration plugins for Qt6
License:  GPLv2

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
* Thu Jul 27 2023 Dipta Biswas <dabiswas112@gmail.com> 0.2-1.20220520git2a21a8ad
- Fix license
- Add docs
- Rebuild for qt6-qtbase 6.5.2-1

* Mon Jul 17 2023 Dipta Biswas <dabiswas112@gmail.com> 0.0^git20220520-2
- Rebuild for qt6-qtbase 6.5.1-2

* Sat May 6 2023 Dipta Biswas <dabiswas112@gmail.com> 0.0^git20220520-1
- Initial Package.
