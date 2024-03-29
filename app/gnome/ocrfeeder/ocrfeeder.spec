%global app_id org.gnome.OCRFeeder

%global forgeurl https://gitlab.gnome.org/GNOME/ocrfeeder
%global tag 0.8.5
# %%global commit edd666ac6f04720f3a8ec1bd9f082308d282491d
# %%global date 20220315
%forgemeta

Name:       ocrfeeder
Version:    %{tag}
Release:    %autorelease
License:    GPLv3+
Group:      Applications/Productivity
Summary:    Document layout analysis and optical character recognition system
URL:        %{forgeurl}
Source:     %{forgesource}

BuildArch:  noarch

BuildRequires:  intltool
BuildRequires:  gnome-doc-utils
# for glib-gettextize
BuildRequires:  glib2-devel
# for gnome-autogen.sh
BuildRequires:  gnome-common
# for GooCanvas-2.0.typelib
BuildRequires:  goocanvas2
# for Gtk-3.0.typelib
BuildRequires:  gtk3-devel
# for GtkSpell-3.0.typelib
BuildRequires:  gtkspell3
BuildRequires:  python3-devel
# for  pygobject3
BuildRequires:  python3-gobject
BuildRequires:  python3-enchant
BuildRequires:  python3-lxml
BuildRequires:  python3-pillow
BuildRequires:  python3-sane
BuildRequires:  python3-reportlab
BuildRequires:  python3-odfpy

# for rsvg-convert
BuildRequires:  librsvg2-tools
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:    gtk3
Requires:    goocanvas2
Requires:    gtkspell3
Requires:    python3
Requires:    python3-gobject
Requires:    python3-enchant
Requires:    python3-lxml
Requires:    python3-pillow
Requires:    python3-sane
Requires:    python3-reportlab
Requires:    python3-odfpy

Requires:    unpaper
Requires:    ghostscript
Requires:    GraphicsMagick
Requires:    yelp

Requires:    tesseract

Recommends:  gocr
Recommends:  ocrad
Recommends:  cuneiform

Requires(post):         coreutils
Requires(postun):       coreutils
Requires(posttrans):    coreutils
# gtk-update-icon-cache
Requires(postun):       gtk-update-icon-cache
Requires(posttrans):    gtk-update-icon-cache
# update-desktop-database
Requires(post):         desktop-file-utils
Requires(postun):       desktop-file-utils

%if "%{name}" != "%{app_id}"
Provides:       %{app_id} = %{version}-%{release}
%endif
Provides:       ocrfeeder-cli = %{version}-%{release}

%description
OCRFeeder is a document layout analysis and OCR system.
Given the images it will automatically outline its contents, distinguish between
what's graphics and text and perform OCR over the latter.
It generates multiple formats being its main one ODT.
It features a complete GTK graphical user interface that allows the users to
correct any unrecognized characters, defined or correct bounding boxes,
set paragraph styles, clean the input images, import PDFs,
save and load the project, export everything to multiple formats, etc.

%prep
%forgeautosetup

%build
./autogen.sh
%configure --enable-maintainer-mode
%{make_build}

%install
%{__make} install DESTDIR="%{buildroot}"
# fix shebang
for f in "%{buildroot}%{_bindir}/%{name}"*; do
  sed -i -re 's|^(#!/usr/bin/env python)$|\12|' "${f}"
done
# install icons
icon_in="resources/icons/%{app_id}.svg"
icon_out="%{app_id}.png"
for s in {16,22,24,32,48,64,72,96,128,192,256,512}; do
  [[ ! -f "%{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/${icon_out}" ]] || continue
  rsvg-convert "${icon_in}" -w "${s}" -h "${s}" -a -f png -o "${icon_out}"
  %{__install} -p -D -m 0644 "${icon_out}" "%{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/%{app_id}.png"
done
if [[ ! -f "%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{app_id}.svg" ]]; then
  %{__install} -p -D -m 0644 "${icon_in}" "%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{app_id}.svg"
fi

%find_lang "%{name}" --with-gnome

%check
desktop-file-validate "%{buildroot}/%{_datadir}/applications/%{app_id}.desktop"
appstream-util validate-relax --nonet "%{buildroot}%{_metainfodir}/%{app_id}.appdata.xml"

%post
touch --no-create "%{_datadir}/icons/hicolor" &> /dev/null || :
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :
if [[ "${1}" -eq "0" ]]; then
  touch --no-create "%{_datadir}/icons/hicolor" &> /dev/null || :
  gtk-update-icon-cache "%{_datadir}/icons/hicolor" &> /dev/null || :
fi

%posttrans
gtk-update-icon-cache "%{_datadir}/icons/hicolor" &> /dev/null || :

%files -f "%{name}.lang"
%doc AUTHORS NEWS README TRANSLATORS
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-cli
%{_datadir}/%{name}/
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/icons/hicolor/*/*/%{app_id}.*
%{_mandir}/man1/%{name}*
%{_metainfodir}/%{app_id}.appdata.xml
%{python3_sitelib}/%{name}/

%changelog
%autochangelog
