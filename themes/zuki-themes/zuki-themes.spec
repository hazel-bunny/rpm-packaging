Name: zuki-themes
Version: 4.0
Release: %autorelease
License: GPLv3
Group: User Interface/X
URL: https://github.com/lassekongo83/%{name}
Summary: Themes for GTK, gnome-shell and more

Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

Requires: gtk2-engines gtk-murrine-engine gtk2 gtk3

BuildRequires: meson ninja-build sassc

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%{_datadir}/themes/Zukitre
%{_datadir}/themes/Zukitre-dark
%{_datadir}/themes/Zukitwo
%{_datadir}/themes/Zukitwo-dark
%{_datadir}/themes/Zuki-shell

%changelog
* Mon Jun 19 2023 Dipta Biswas <dabiswas112@gmail.com> 4.0-1
- Initial Package.
