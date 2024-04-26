# build with HEIF support (needs RPMFusion free)
%bcond_with heif

# disable LTO (breaks gimp-2.99.15 build on F37)
# %%global _lto_cflags %%nil

%global lib_api_version 2.99
%global gettext_version 30

Name:       gimp
Version:    2.99.16
Release:    %autorelease
Summary:    GNU Image Manipulation Program

License:    GPLv3+ and GPLv3
URL:        https://www.%{name}.org/
	
Source0:    https://download.%{name}.org/%{name}/v%{lib_api_version}/%{name}-%{version}.tar.xz

# Try using the system monitor profile for color management by default.
# Fedora specific.
Patch1:         gimp-2.99-cm-system-monitor-profile-by-default.patch
# bz#1706653
Patch2:         gimp-2.99-default-font.patch

BuildRequires:  aalib-devel
BuildRequires:  curl
BuildRequires:  dbus-daemon
BuildRequires:  desktop-file-utils
BuildRequires:  enchant
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext >= 0.19
BuildRequires:  gjs
BuildRequires:  glib-networking
BuildRequires:  gtk-doc >= 1.0
BuildRequires:  icu
BuildRequires:  ImageMagick
BuildRequires:  intltool >= 0.40.1
BuildRequires:  appstream >= 0.15.3
BuildRequires:  libappstream-glib >= 0.7.7
BuildRequires:  libgs-devel
BuildRequires:  luajit
BuildRequires:  meson >= 0.56.0
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-lib
BuildRequires:  pkgconfig(alsa) >= 1.0.0
BuildRequires:  pkgconfig(appstream-glib) >= 0.7.7
BuildRequires:  pkgconfig(atk) >= 2.4.0
BuildRequires:  pkgconfig(babl) >= 0.1.98
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(cairo) >= 1.12.2
BuildRequires:  pkgconfig(cairo-pdf) >= 1.12.2
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(fontconfig) >= 2.12.4
BuildRequires:  pkgconfig(freetype2) >= 2.1.7
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.30.8
BuildRequires:  pkgconfig(gegl-0.4) >= 0.4.40
BuildRequires:  pkgconfig(gexiv2) >= 0.14.0
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.68.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.16.10
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(gutenprint)
BuildRequires:  pkgconfig(harfbuzz) >= 1.0.5
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.2.6
BuildRequires:  pkgconfig(lcms2) >= 2.8
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libart-2.0) >= 2.3.19
BuildRequires:  pkgconfig(libexif) >= 0.6.15
# RPMFusion free
%if %{with heif}
BuildRequires:  pkgconfig(libheif) >= 1.3.2
%endif
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(liblzma) >= 5.0.0
BuildRequires:  pkgconfig(libmng)
BuildRequires:  pkgconfig(libmypaint) >= 1.3.0
BuildRequires:  pkgconfig(libopenjp2) >= 2.1.0
BuildRequires:  pkgconfig(libjxl) >= 0.7.0
BuildRequires:  pkgconfig(libpng) >= 1.6.25
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.40.6
BuildRequires:  pkgconfig(libtiff-4) >= 4.0.0
BuildRequires:  pkgconfig(libunwind) >= 1.1.0
BuildRequires:  pkgconfig(libwebp) >= 0.6.0
BuildRequires:  pkgconfig(libwmf) >= 0.2.8
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(mypaint-brushes-1.0) >= 1.3.0
BuildRequires:  pkgconfig(OpenEXR) >= 1.6.1
BuildRequires:  pkgconfig(pangocairo) >= 1.44.0
BuildRequires:  pkgconfig(pangoft2) >= 1.29.4
BuildRequires:  pkgconfig(poppler-data) >= 0.4.9
BuildRequires:  pkgconfig(poppler-glib) >= 0.69.0
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(python3) >= 3.6.0
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.20.3
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  vala
BuildRequires:  xdg-utils
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  gi-docgen

Requires:       %{name}-libs = %{version}-%{release}
Requires:       %{name}-data = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       xdg-utils
Requires:       lua-lgi-compat

Recommends:     darktable
Recommends:     ghostscript
Recommends:     gjs
Recommends:     luajit
Recommends:     python3-gobject
Recommends:     rawtherapee
Recommends:     mypaint-brushes

Provides:       %{name} = %{version}

Obsoletes:      %{name} < %{version}

%description
GIMP (GNU Image Manipulation Program) is a powerful image composition and editing
program, which can be extremely useful for creating logos and other graphics for
web pages. GIMP has many of the tools and filters you would expect to find in similar
commercial offerings, and some interesting extras as well. GIMP provides a large
image manipulation toolbox, including channel operations and layers, effects, sub-pixel
imaging and anti-aliasing, and conversions, all with multi-level undo.

%package data
Summary:        GIMP data files
License:        LGPLv3+
Requires:       %{name}-data = %{version}-%{release}
BuildArch:      noarch

%description data
The %{name}-data package contains data files needed for the GNU Image
Manipulation Program (GIMP).

%package libs
Summary:        GIMP libraries
License:        LGPLv3+

%description libs
The %{name}-libs package contains shared libraries needed for the GNU Image
Manipulation Program (GIMP).

%package devel
Summary:        GIMP plugin and extension development kit
License:        LGPLv3+
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel-tools = %{version}-%{release}

%description devel
The %{name}-devel package contains the static libraries and header files for writing
GNU Image Manipulation Program (GIMP) plug-ins and extensions.

%package devel-doc
Summary:        GIMP plugin and extension development documentation
License:        LGPLv3+
Requires:       %{name}-devel = %{version}-%{release}
BuildArch:      noarch

%description devel-doc
The %{name}-devel-doc package contains documentation to build GNU Image
Manipulation Program (GIMP) plug-ins and extensions.

%package devel-tools
Summary:        GIMP plugin and extension development tools
License:        LGPLv3+
Requires:       %{name}-devel = %{version}-%{release}

%description devel-tools
The %{name}-devel-tools package contains gimptool, a helper program to
build GNU Image Manipulation Program (GIMP) plug-ins and extensions.



%prep
%autosetup -p1 -n %{name}-%{version}


%build
%meson %{!?with_heif:-Dheif=disabled}
%meson_build

%install
%meson_install

# Plugins and modules change often (grab the executeable ones)
find %{buildroot}%{_libdir}/gimp/%{lib_api_version} -type f | sed "s@^%{buildroot}@@g" | grep -v '\.a$' > gimp-plugin-files
find %{buildroot}%{_libdir}/gimp/%{lib_api_version}/* -type d | sed "s@^%{buildroot}@%%dir @g" >> gimp-plugin-files

# Auto detect the lang files
%find_lang gimp%{gettext_version}
%find_lang gimp%{gettext_version}-std-plug-ins
%find_lang gimp%{gettext_version}-script-fu
%find_lang gimp%{gettext_version}-libgimp
%find_lang gimp%{gettext_version}-python

cat gimp%{gettext_version}.lang gimp%{gettext_version}-std-plug-ins.lang gimp%{gettext_version}-script-fu.lang gimp%{gettext_version}-libgimp.lang gimp%{gettext_version}-python.lang > gimp-all.lang

# Build the master filelists generated from the above mess.
cat gimp-plugin-files gimp-all.lang > gimp.files

# desktop file -- mention version/unstable, use custom icon
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/gimp.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
#appstreamcli validate %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%files -f gimp.files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/gimp-%{binver}
%{_bindir}/gimp-console-%{binver}
%{_bindir}/gimp-test-clipboard-%{lib_api_version}
%{_bindir}/gimptool-%{lib_api_version}
%{_bindir}/gimp-script-fu-interpreter-3.0
%{_libexecdir}/gimp-debug-tool-%{lib_api_version}

%{_mandir}/man1/gimp-%{binver}.1*
%{_mandir}/man1/gimp-console-%{binver}.1*
%{_mandir}/man5/gimprc-%{binver}.5*

%dir %{_sysconfdir}/gimp
%dir %{_sysconfdir}/gimp/%{lib_api_version}
%config(noreplace) %{_sysconfdir}/gimp/%{lib_api_version}/controllerrc
%config(noreplace) %{_sysconfdir}/gimp/%{lib_api_version}/gimprc
%config(noreplace) %{_sysconfdir}/gimp/%{lib_api_version}/gimp.css
%config(noreplace) %{_sysconfdir}/gimp/%{lib_api_version}/unitrc
%config(noreplace) %{_sysconfdir}/gimp/%{lib_api_version}/sessionrc
%config(noreplace) %{_sysconfdir}/gimp/%{lib_api_version}/templaterc
%config(noreplace) %{_sysconfdir}/gimp/%{lib_api_version}/menurc
%config(noreplace) %{_sysconfdir}/gimp/%{lib_api_version}/toolrc

%dir %{_libdir}/gimp
%dir %{_libdir}/gimp/%{lib_api_version}
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Gimp-3.0.typelib
%{_libdir}/girepository-1.0/GimpUi-3.0.typelib

%{_datadir}/applications/*.desktop
# %%{_datadir}/metainfo/*.appdata.xml

%{_datadir}/icons/hicolor/*/apps/gimp.png

%{_datadir}/icons/hicolor/scalable/apps/gimp.svg

%files data
%dir %{_datadir}/gimp
%dir %{_datadir}/gimp/%{lib_api_version}
%{_datadir}/gimp/%{lib_api_version}/dynamics/
%{_datadir}/gimp/%{lib_api_version}/file-raw/
%{_datadir}/gimp/%{lib_api_version}/menus/
%{_datadir}/gimp/%{lib_api_version}/tags/
%{_datadir}/gimp/%{lib_api_version}/tips/
%{_datadir}/gimp/%{lib_api_version}/tool-presets/
%{_datadir}/gimp/%{lib_api_version}/ui/
%{_datadir}/gimp/%{lib_api_version}/brushes/
%{_datadir}/gimp/%{lib_api_version}/fractalexplorer/
%{_datadir}/gimp/%{lib_api_version}/gfig/
%{_datadir}/gimp/%{lib_api_version}/gflare/
%{_datadir}/gimp/%{lib_api_version}/gimpressionist/
%{_datadir}/gimp/%{lib_api_version}/gradients/
%{_datadir}/gimp/%{lib_api_version}/icons/
%{_datadir}/gimp/%{lib_api_version}/images/
%{_datadir}/gimp/%{lib_api_version}/palettes/
%{_datadir}/gimp/%{lib_api_version}/patterns/
%{_datadir}/gimp/%{lib_api_version}/scripts/
%{_datadir}/gimp/%{lib_api_version}/themes/
%{_datadir}/gimp/%{lib_api_version}/gimp-release

%files libs
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/libgimp-3.0.so.0*
%{_libdir}/libgimpbase-3.0.so.0*
%{_libdir}/libgimpcolor-3.0.so.0*
%{_libdir}/libgimpconfig-3.0.so.0*
%{_libdir}/libgimpmath-3.0.so.0*
%{_libdir}/libgimpmodule-3.0.so.0*
%{_libdir}/libgimpthumb-3.0.so.0*
%{_libdir}/libgimpui-3.0.so.0*
%{_libdir}/libgimpwidgets-3.0.so.0*
%{_libdir}/libgimp-scriptfu-3.0.so.0*

%files devel
%doc %{_datadir}/doc
%{_libdir}/*.so
%{_includedir}/gimp-3.0
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*.m4
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Gimp-3.0.gir
%{_datadir}/gir-1.0/GimpUi-3.0.gir
%{_datadir}/vala/vapi/gimp-3.0.*
%{_datadir}/vala/vapi/gimp-ui-3.0.*

%files devel-doc
%doc %{_datadir}/doc

%files devel-tools
%{_bindir}/gimptool-%{lib_api_version}
%{_mandir}/man1/gimptool-%{lib_api_version}.1*


%changelog
* Thu Nov 24 22:01:32 MSK 2022 Pavel Artsishevsky <polter.rnd@gmail.com> - 2.99.14-1
- Update to 2.99.14

* Sun Jul 3 21:25:11 MSK 2022 Pavel Artsishevsky <polter.rnd@gmail.com> - 2.99.10-2
- Update to 2.99.10

* Tue Apr 12 10:35:24 MSK 2022 Pavel Artsishevsky <polter.rnd@gmail.com> - 2.99.10-1
- Update to 2.99.10

* Tue Dec 7 11:36:41 MSK 2021 Pavel Artsishevsky <polter.rnd@gmail.com> - 2.99.8-2
- Rebuild with libjxl-0.6

* Wed Oct 27 17:56:55 MSK 2021 Pavel Artsishevsky <polter.rnd@gmail.com> - 2.99.8-1
- Update to 2.99.8

* Mon May 17 17:15:34 CET 2021 Pavel Artsishevsky <polter.rnd@gmail.com> - 2.99.7-3
- Add patch for running parent implementation of window_state_event
- Remove gimp30-tips.mo from package (issue #6852)
- Fix /etc/gimprc
- Add lua-lgi-compat to requirements

* Mon May 17 16:32:57 CET 2021 Pavel Artsishevsky <polter.rnd@gmail.com> - 2.99.7-2
- Update to 2.99.7

* Fri Dec 11 02:51:57 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.99.2-1
- Update to 2.99.2

* Sun Aug 23 15:51:38 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.99.2-0.2.20200823git56982e
- Bump to commit 56982e6ce96d34b0802f90b5dd0606565f6b3914

* Mon Jul 20 22:05:26 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.99.1-0.1.20200720git1a7a53d
- Initial package for GIMP 2.99
