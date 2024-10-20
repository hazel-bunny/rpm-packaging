%global app_id org.gnome.OCRFeeder

Name:       ocrfeeder
Version:    0.8.5

%global forgeurl https://gitlab.gnome.org/GNOME/%{name}
%global tag %{version}
# %%global commit edd666ac6f04720f3a8ec1bd9f082308d282491d
# %%global date 20220315
%forgemeta

Release:    4%{?dist}
License:    GPL-3.0
Summary:    Document layout analysis and optical character recognition system
URL:        %{forgeurl}
Source:     %{forgesource}

# Upstream merge requests
# Fix gocr parameters
Patch0:     11.patch
# Port to GooCanvas 3.0
Patch1:     12.patch
# Convert README to MD
# Patch2:   14.patch
# Specify Gtk version
Patch2:     22.patch
# Fix typos in help
Patch3:     15.patch
# Fix Tesseract abbreviation for Czech
Patch4:     16.patch
# Avoid deprecated imghdr module
Patch5:     17.patch
# Avoid deprecated imp module
Patch6:     18.patch
# Set default window size instead of size request
Patch7:     19.patch
# Set program name to application ID
Patch8:     20.patch
# Add URLs for translate and vcs-browser to appdata
Patch9:     21.patch


BuildArch:  noarch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  glib2-devel
BuildRequires:  gnome-doc-utils
BuildRequires:  gnome-common
BuildRequires:  goocanvas3
BuildRequires:  gtk3-devel
BuildRequires:  gtkspell3
BuildRequires:  libappstream-glib
BuildRequires:  librsvg2-tools

BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-enchant
BuildRequires:  python3-lxml
BuildRequires:  python3-pillow
BuildRequires:  python3-sane
BuildRequires:  python3-reportlab
BuildRequires:  python3-odfpy

Requires:    GraphicsMagick
Requires:    ghostscript
Requires:    gtk3
Requires:    goocanvas3
Requires:    gtkspell3
Requires:    python3-gobject
Requires:    python3-enchant
Requires:    python3-lxml
Requires:    python3-pillow
Requires:    python3-sane
Requires:    python3-reportlab
Requires:    python3-odfpy
Requires:    tesseract
Requires:    unpaper

Recommends:  gocr
Recommends:  ocrad
Recommends:  cuneiform

%if "%{name}" != "%{app_id}"
Provides:       %{app_id} = %{version}-%{release}
%endif
Provides:       ocrfeeder-cli = %{version}-%{release}

%description
OCRFeeder is a document layout analysis and OCR system. Given the images it will
automatically outline its contents, distinguish between what's graphics and text
and perform OCR over the latter. It generates multiple formats being its main
one ODT. It features a complete GTK graphical user interface that allows the
users to correct any unrecognized characters, defined or correct bounding boxes,
set paragraph styles, clean the input images, import PDFs, save and load the
project, export everything to multiple formats, etc.

%prep
%forgeautosetup -p1
# Fix build with Python 3.12
# sed -e 's|import imp; imp.find_module|import importlib; importlib.import_module|' -i m4/m4_ax_python_module.m4

%build
./autogen.sh
%configure
%make_build

%install
%make_install DESTDIR="%{buildroot}"

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
* Tue Aug 27 2024 Hazel Bunny <hazel_bunny@disroot.org> 0.8.5-4
- Rebuild for Fedora 41

* Mon Jun 17 2024 Hazel Bunny <hazel_bunny@disroot.org> 0.8.5-3
- Fix build for python 3.12
- Fix gocr parameters
- Port to goocanvas-3.0

* Wed Apr 26 2023 Hazel Bunny <hazel_bunny@disroot.org> 0.8.5-2
- Switch to forge macros

* Wed Apr 26 2023 Hazel Bunny <hazel_bunny@disroot.org> 0.8.5-1
- Update to version 0.8.5
- Update spec for python3
- Remove patches and use upstream source

* Sun Feb 09 2020 Tomasz Tomasik <scx.mail@gmail.com> 0.8.1-4.20200107git1160f3d
- Fix PDF import

* Thu Jan 23 2020 Tomasz Tomasik <scx.mail@gmail.com> 0.8.1-3.20200107git1160f3d
- Update to the latest Python2-based version with built-in odfpy

* Tue Feb 05 2019 Tomasz Tomasik <scx.mail@gmail.com> 0.8.1-2.20181218git51483c4
- Update patches
  https://gitlab.gnome.org/GNOME/ocrfeeder/merge_requests/1

* Wed Jan 23 2019 Tomasz Tomasik <scx.mail@gmail.com> 0.8.1-1.20181218git51483c4
- Update to the latest version

* Wed Jan 23 2019 Tomasz Tomasik <scx.mail@gmail.com> 0.8.1-1
- Initial packaging
