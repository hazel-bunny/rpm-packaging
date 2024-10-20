Name:             ibus-avro

%global app_id com.github.sarim.ibus.avro
%global schema com.omicronlab.avro
%global debug_package %{nil}

%global forgeurl https://github.com/sarim/%{name}
%global commit 4da8b056752288dc81224c0aa4bc81a67ae0625c
%global date 20230914
%forgemeta

Version:          1.2
Release:          3%{?dist}
Summary:          Avro phonetic bangla typing layout for ibus
License:          MPL-2.0
URL:              %{forgeurl}
Source0:          %{forgesource}

BuildRequires:    automake
BuildRequires:    gjs
BuildRequires:    ibus-devel
BuildRequires:    intltool
BuildRequires:    libappstream-glib
BuildRequires:    make

Requires:         gjs
Requires:         ibus

%description
%summary

%files
%license LICENSE
%doc README.md
%{_datadir}/applications/ibus-setup-%{name}.desktop
%{_datadir}/glib-2.0/schemas/%{schema}.gschema.xml
%{_datadir}/ibus/component/%{name}.xml
%{_datadir}/%{name}
%{_metainfodir}/%{app_id}.metainfo.xml

%prep
%forgeautosetup -p1

%build
aclocal && autoconf && automake --add-missing
%configure
%make_build

%install
make DESTDIR=%{buildroot} INSTALL="%{__install} -p" installdeb
rm -rf %{buildroot}%{_libexecdir}
chmod +x %{buildroot}%{_datadir}/%{name}/main-gjs.js
sed -i 's|<layout>bn</layout>|<layout>us</layout>|' "%{buildroot}%{_datadir}/ibus/component/%{name}.xml"

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml

%changelog
* Thu Oct 17 2024 Hazel Bunny <hazel_bunny@disroot.org> - 1.2-3
- Fedora 41 Mass Rebuild

* Sun Aug 11 2024 Hazel Bunny <hazel_bunny@disroot.org> - 1.2-2.git
- Rebuild for ibus 1.5.30

* Sat Jun 22 2024 Hazel Bunny <hazel_bunny@disroot.org> - 1.2-1.git
- Initial build
