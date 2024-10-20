Name:           qcheckers
Version:        0.9.0

%global forgeurl https://github.com/portnov/%{name}
%global tag %{version}
%global date 20190314
%forgemeta

Release:        2%{?dist}
Summary:        Checkers board game
License:        GPL-2.0
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  hicolor-icon-theme
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  make

Obsoletes:      kcheckers

%description
The Qt version of the classic board game checkers. This game is also
known as draughts.

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog FAQ NEWS README.md TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}

#------------------------------------------------------------------

%prep
%forgeautosetup -p1

%build
%qmake_qt5 PREFIX=%{_prefix} INSTALL_ROOT=%{buildroot}
%make_build

%install
%make_install PREFIX=%{_prefix} INSTALL_ROOT=%{buildroot}
rm -rf %{buildroot}%{_datadir}/%{name}/{AUTHORS,COPYING,ChangeLog}
%find_lang %{name} --with-qt

#------------------------------------------------------------------

%changelog
* Thu Oct 17 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.9.0-2
- Fedora 41 mass rebuild

* Sun Jun 16 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.9.0-1
- Initial package
