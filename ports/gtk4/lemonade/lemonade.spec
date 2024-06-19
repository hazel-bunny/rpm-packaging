Name:           lemonade
Version:        2024.04.22

%global forgeurl https://github.com/theycallhermax/%{name}
%global tag %{version}
%global date 20240422
%forgemeta

%global app_id ml.mdwalters.Lemonade

Release:        2%{?dist}
License:        GPL-3.0
Summary:        Follow discussions on Lemmy
URL:            %{forgeurl}
Source:         %{forgesource}

#------------------------------------------------------------------

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gtk-update-icon-cache
BuildRequires:  hicolor-icon-theme
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  ninja-build

BuildRequires:  python3-devel
BuildRequires:  python3-certifi
BuildRequires:  python3-charset-normalizer
BuildRequires:  python3-idna
BuildRequires:  python3-requests
BuildRequires:  python3-urllib3

Requires:       gtk4
Requires:       libadwaita
Requires:       python3-certifi
Requires:       python3-charset-normalizer
Requires:       python3-gobject
Requires:       python3-idna
Requires:       python3-requests
Requires:       python3-urllib3

BuildArch:      noarch

#------------------------------------------------------------------

%description
Lemonade is a sleek and modern Lemmy client that is designed to provide a
seamless browsing experience for Lemmy users. Built with the latest technology,
Lemonade utilizes the power of libadwaita and GTK 4 to deliver a beautiful and
intuitive user interface that is both easy to use and visually appealing.

With Lemonade, you can easily browse your favorite communities, discover new
content, and engage with other users. The client is optimized for speed and
performance, ensuring that you can quickly and efficiently navigate through
Lemmy without any lag or delays.

%files
%license LICENCE
%doc README.md

%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/appdata/%{app_id}.appdata.xml
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/icons/hicolor/{scalable,symbolic}/apps/%{app_id}*.svg

#------------------------------------------------------------------

%prep
%forgeautosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%__chmod 0755 %{buildroot}%{_bindir}/%{name}
%py_byte_compile %{python3} %{_datadir}/%{name}/%{name}/*.py

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{app_id}.appdata.xml

#------------------------------------------------------------------

%changelog
* Sat Jun 15 2024 Dipta Biswas <dabiswas112@gmail.com> - 2024.04.22-2
- Fix permissions

* Fri Jun 14 2024 Dipta Biswas <dabiswas112@gmail.com> - 2024.04.22-1
- initial package

