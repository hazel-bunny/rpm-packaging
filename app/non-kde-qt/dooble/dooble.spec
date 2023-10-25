%global forgeurl https://github.com/textbrowser/dooble
%global tag 2023.08.30
%global date 20230830
%forgemeta

Name:          dooble
Version:       %{tag}
Release:       %autorelease
Summary:       Minimal, scientific, and stable Web browser
License:       BSD

URL:           %{forgeurl}
Source:        %{forgesource}

BuildRequires: make
BuildRequires: doxygen
BuildRequires: findutils
# BuildRequires: gendesk
BuildRequires: pkgconfig(gpgme)

BuildRequires: pkgconfig(Qt6Concurrent)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Network)
BuildRequires: pkgconfig(Qt6PrintSupport)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6Sql)
BuildRequires: pkgconfig(Qt6WebEngineWidgets)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6Xml)
BuildRequires: pkgconfig(Qt6Charts)

%description
Dooble is a minimal, scientific, and stable Web browser.
- A Web browser!
- Anonymous tab headers.
- Application lock.
- Basic themes.
- Compact. 40,000 lines of source! (Excluding UI files.)
- Cookie crusher.
- Custom search engines.
- Custom style sheets.
- Documented.
- Domain restrictions (blocker).
- Favorites.
- Floating digital clock.
- Floating minute history window.
- FreeBSD, Linux, MacOS, OS/2, OpenBSD, Windows.
- Gopher support.
- Great for older hardware!
- Many private windows.
- Multiple private instances, including downloads.
- Native graphing of data for scientific research.
- Original implementations of AES-256, Threefish-256.
- Peek-a-boo. Zero-script.
- Portable.
- Qt LTS!
- Qt-only dependency.
- WebEngine
- Windows portable.

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%prep
%forgeautosetup
sed -i 's|Categories=Web|Categories=Network;Qt;WebBrowser;|
        s|Exec=.*|Exec=dooble|
        s|Icon=.*|Icon=dooble|' %{name}.desktop
sed -i 's|QString path(QDir::currentPath());|QString path("/usr/share/dooble");|' Source/%{name}_settings.cc

%build
%qmake_qt6 ./%{name}.pro PREFIX=%{_prefix}
%make_build

%install
# %%make_install INSTALL_ROOT=%%{buildroot}
install -Dm755 Dooble %{buildroot}%{_bindir}/%{name}
install -Dm644 Icons/Logo/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -Dm644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 -t %{buildroot}%{_datadir}/%{name}/Translations Translations/%{name}_*.qm
install -Dm644 LICENSE %{buildroot}%{_datadir}/licenses/%{name}/LICENSE

%changelog
* Thu Oct 26 2023 Dipta Biswas <dabiswas112@gmail.com> 2023.08.30-1
- Initial Package.
