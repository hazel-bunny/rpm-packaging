Name: zuki-themes
Version: 4.0
Release: 1%{?dist}
License: GPLv3
Group: User Interface/X
URL: https://github.com/lassekongo83/%{name}
Summary: Themes for GTK, gnome-shell and more

Source0: %{url}/archive/v%{version}/%{_basename}-%{version}.tar.gz

BuildArch: noarch

Requires: gtk2-engines gtk-murrine-engine gtk2 gtk3

BuildRequires: meson ninja-build sassc

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}

%build
%meson_build

%install
%meson_install

%files
%{_datadir}/*

%changelog
* Mon Jun 19 2023 Dipta Biswas <dabiswas112@gmail.com> 4.0-1
- Initial Package.