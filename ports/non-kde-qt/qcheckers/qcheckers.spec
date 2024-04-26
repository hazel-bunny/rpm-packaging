Name:           qcheckers

%global forgeurl https://github.com/portnov/%{name}
%global tag 0.9.0
%global date 20190314
%forgemeta

Version:        %{tag}
Release:        %{autorelease}
Summary:        Checkers board game

License:        GPLv2+
URL:            %{forgeurl}
Source:         %{forgesource}

Requires:       hicolor-icon-theme
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  desktop-file-utils
BuildRequires:  make

%description
The Qt version of the classic board game checkers. This game is also
known as draughts.

%prep
%forgeautosetup -p1

%build
%qmake_qt5  PREFIX=/usr INSTALL_ROOT=%{buildroot}
%make_build

%install
mkdir -p %{buildroot}%{_prefix}/{bin,lib,lib64,share}
install -Dp -m 755 %{name} %{buildroot}%{_bindir}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
install -Dp -m 644 icons/biglogo.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

mkdir -p %{buildroot}/%{_datadir}/%{name}/
install -p -m 644 i18n/*.qm %{buildroot}/%{_datadir}/%{name}/
cp -p -r themes %{buildroot}/%{_datadir}/%{name}/
%find_lang %{name} --with-qt

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog FAQ README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/themes

%changelog
%autochangelog
