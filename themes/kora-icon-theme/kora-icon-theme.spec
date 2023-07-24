%global _basename kora

Name:               %{_basename}-icon-theme
Version:            1.5.7
Release:            %autorelease
License:            GPL-3.0
URL:                https://github.com/bikass/%{_basename}
Summary:            Kora icon theme for GNU/Linux os

Source0:            %{url}/archive/v%{version}/%{_basename}-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      fdupes

Requires(post):     gtk-update-icon-cache

%description
Kora is an SVG icon theme with lots of new icons for GNU/Linux operating systems.

Different versions available:
kora - for dark themes with dark panel
kora-light - for light themes with dark panel (depends on Kora)
kora-light-panel - for light themes with light panel (depends on Kora and Kora-light)
kora-pgrey - theme with grey folder colors (depends on Kora)

%prep
%setup -q -n %{_basename}-%{version}

%build
# Nothing to do here

%install
%fdupes %{buildroot}
# Delete useless files from source folder
rm -f "%{_basename}/create-new-icon-theme.cache.sh"
rm -f "%{_basename}/icon-theme.cache"
rm -f "%{_basename}-light/create-new-icon-theme.cache.sh"
rm -f "%{_basename}-light/icon-theme.cache"
rm -f "%{_basename}-light-panel/create-new-icon-theme.cache.sh"
rm -f "%{_basename}-light-panel/icon-theme.cache"
rm -f "%{_basename}-pgrey/create-new-icon-theme.cache.sh"
rm -f "%{_basename}-pgrey/icon-theme.cache"

# Install icons
mkdir -p %{buildroot}%{_datadir}/icons
cp -dr --no-preserve=mode "%{_basename}" %{buildroot}%{_datadir}/icons/%{_basename}
cp -dr --no-preserve=mode "%{_basename}-light" %{buildroot}%{_datadir}/icons/%{_basename}-light
cp -dr --no-preserve=mode "%{_basename}-light-panel" %{buildroot}%{_datadir}/icons/%{_basename}-light-panel
cp -dr --no-preserve=mode "%{_basename}-pgrey" %{buildroot}%{_datadir}/icons/%{_basename}-pgrey

# Install license
mkdir -p %{buildroot}%{_datadir}/licenses/%{name}
cp -p "LICENSE" %{buildroot}%{_datadir}/licenses/%{name}

%files
%doc README.md
%license LICENSE
%{_datadir}/icons/%{_basename}
%{_datadir}/icons/%{_basename}-light
%{_datadir}/icons/%{_basename}-light-panel
%{_datadir}/icons/%{_basename}-pgrey

%changelog
%autochangelog
