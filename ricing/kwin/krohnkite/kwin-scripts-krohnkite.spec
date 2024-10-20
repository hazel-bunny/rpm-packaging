%global _basename krohnkite

Name:            kwin-scripts-%{_basename}
Version:         0.9.8.2

%global forgeurl https://github.com/anametologin/%{_basename}
%global commit 56df0da265aa248a4fa7a0133a7b208bdc4f3dbd
%global date 20241008
%forgemeta

Release:         1%{?dist}
Summary:         A dynamic tiling extension for KWin
License:         MIT
URL:             %{forgeurl}
Source:          %{forgesource}

BuildArch:       noarch

BuildRequires:   make
BuildRequires:   typescript
BuildRequires:   p7zip
BuildRequires:   desktop-file-utils

Requires:        kwin

#------------------------------------------------------------------

%description
A dynamic tiling extension for KWin 6. Kröhnkite is mainly inspired by dwm from
suckless folks, and aims to provide rock solid stability while fully integrating
into KWin. The name of the script is from mineral Kröhnkite; it starts with K
and looks cool.

Features
 - DWM-like window tiling
    - Dynamically tile windows, rather than manually placing each.
    - Floating windows
 - Fully integrates into KWin features, including:
    - Multi-screen
    - Activities & Virtual desktop
    - Basic window management (minimize, fullscreen, switching, etc)
 - Multiple Layout Support
    - Tiling layout
    - Monocle layout
    - Desktop-friendly layouts (Spread, Stair)

%files
%license LICENSE
%doc README.md
%{_datadir}/kwin/scripts/%{_basename}
%{_datadir}/kservices6/%{_basename}.desktop

#------------------------------------------------------------------

%prep
%forgeautosetup

%build
tsc

%install
mkdir -p %{buildroot}%{_datadir}/kwin/scripts/%{_basename}/contents/{code,config,ui}

# krohnkite.js
install -Dm644 krohnkite.js %{buildroot}%{_datadir}/kwin/scripts/%{_basename}/contents/code/script.js

# metadata.json
install -Dm644 res/metadata.json %{buildroot}%{_datadir}/kwin/scripts/%{_basename}/metadata.json
sed -E -e 's&\$VER&'%{version}'&' -e 's&\$REV&'%{commit}'&' \
    -i %{buildroot}%{_datadir}/kwin/scripts/%{_basename}/metadata.json

# other files
install -Dm644 res/main.js %{buildroot}%{_datadir}/kwin/scripts/%{_basename}/contents/code/main.js
install -Dm644 res/config.xml %{buildroot}%{_datadir}/kwin/scripts/%{_basename}/contents/config/main.xml
install -Dm644 res/config.ui %{buildroot}%{_datadir}/kwin/scripts/%{_basename}/contents/ui/config.ui
install -Dm644 res/main.qml %{buildroot}%{_datadir}/kwin/scripts/%{_basename}/contents/ui/main.qml
install -Dm644 res/popup.qml %{buildroot}%{_datadir}/kwin/scripts/%{_basename}/contents/ui/popup.qml
install -Dm644 res/shortcuts.qml %{buildroot}%{_datadir}/kwin/scripts/%{_basename}/contents/ui/shortcuts.qml

install -Dm644 res/metadata.desktop %{buildroot}%{_datadir}/kservices6/%{_basename}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/kservices6/%{_basename}.desktop

#------------------------------------------------------------------

%changelog
* Thu Oct 10 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.9.8.2-1
- Update to 0.9.8.2

* Wed Jun 19 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.9.6-1
- initial package

