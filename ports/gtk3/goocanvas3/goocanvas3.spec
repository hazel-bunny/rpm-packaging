%global _basename goocanvas
%global apiver  3.0

Name:           %{_basename}3
Version:        3.0.0

%global forgeurl https://gitlab.gnome.org/Archive/%{_basename}
%global tag %{version}
%global date 20210116
%forgemeta

Release:        1%{?dist}
Summary:        A new canvas widget for GTK+ that uses cairo for drawing

License:        LGPLv2+
URL:            %forgeurl
Source:         %forgesource
# Source0:      https://download.gnome.org/sources/%{_basename}/%{apiver}/%{_basename}-%{version}.tar.xz

# Upstream merge requests
Patch0:         15.patch

BuildRequires:  gettext-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo) >= 1.10.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0.0

%description
GooCanvas is a new canvas widget for GTK+ that uses the cairo 2D library for
drawing. It has a model/view split, and uses interfaces for canvas items and
views, so you can easily turn any application object into canvas items.

%files  -f %{name}.lang
%license COPYING
%doc README ChangeLog AUTHORS NEWS TODO
%{_libdir}/lib%{_basename}-%{apiver}.so*
%{_libdir}/girepository-1.0/GooCanvas-%{apiver}.typelib

#------------------------------------------------------------------------------

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files devel
%{_includedir}/%{_basename}-%{apiver}
%{_libdir}/pkgconfig/%{_basename}-%{apiver}.pc
%{_datadir}/gir-1.0/GooCanvas-%{apiver}.gir

#------------------------------------------------------------------------------

%prep
%forgeautosetup -p1

%build
./autogen.sh
# python GI wrapper is not enabled yet until i figure a proper way to package it
%configure --disable-static \
           --enable-python=no
%make_build

%install
%make_install DESTDIR=%buildroot
find %buildroot -name '*.la' -exec rm -f {} ';'
%find_lang %{name}

%ldconfig_scriptlets

#------------------------------------------------------------------------------

%changelog
* Mon Jun 17 2024 Dipta Biswas <dabiswas112@gmail.com> - 3.0.0-1
- initial package
