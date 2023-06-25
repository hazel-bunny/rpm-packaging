Name:             pdfchain
Version:          0.4.4.2
# Need epoch since upstream changed versioning style
Epoch:            1
Release:          1%{?dist}
Summary:          A GUI for pdftk
License:          GPLv3+
URL:              https://sourceforge.net/projects/pdfchain

Source0:          https://downloads.sourceforge.net/pdfchain/%{name}-%{version}.tar.gz
Source1:          pdfchain.appdata.xml
# Patch to make desktop file conform to standards
Patch0:           pdfchain-desktop.patch
# PATCH-FIX-UPSTREAM fix-crash-and-warnings.patch fcrozat@suse.com -- fix crash at startup
Patch1:           0003-Fix-crash-because-the-RadioButtonGroup-was-contructe.patch

BuildRequires:    gcc-c++
BuildRequires:    desktop-file-utils
BuildRequires:    gtkmm30-devel
BuildRequires:    intltool

# For dir ownership
Requires:         pdftk
Requires(post):   desktop-file-utils
Requires(postun): desktop-file-utils

%description
PDF Chain is a Graphical User Interface for the PDF Tool Kit.
It includes features designed to handle PDF files in a easy way.
Basicaly it can merge, split, add backgrounds or stamps and add attachments.
There are some tools for extended needs, too.

The GUI is written using GTKmm, a C++ library for GTK.
PDF Chain is released under the terms of the GNU Public License verion 3.
PDF Chain comes without any warranty.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
# Remove doc dir
rm -rf %{buildroot}%{_datadir}/doc/pdfchain

# Validate desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# Install metainfo
install -Dm0644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/pdfchain
%{_datadir}/applications/pdfchain.desktop
%{_datadir}/icons/hicolor/*/apps/pdfchain.png
%{_datadir}/pixmaps/pdfchain.png
%{_datadir}/metainfo/%{name}.appdata.xml

%changelog
* Sat Jun 24 2023 Dipta Biswas <dabiswas112@gmail.com> - 1:0.4.4.2-1
- Adopt and refactor old spec

* Tue Sep 07 2021 Sérgio Basto <sergio@serjux.com> - 1:0.4.4.2-1
- Update 0.4.4.2
- Add pdfchain.appdata.xml as a source and install it to the
  appdata dir; appdata file sent upstream.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.3-2
- Rebuilt for c++ ABI breakage

* Sun Jan 08 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1:0.3.3-1
- Update to 0.3.3.
- Fix BZ #772434.

* Sun Nov 13 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1:0.3.2-1
- Update to 0.3.2 (BZ #753593), based on Nicholas Kudriavtsev's patch.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.123-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.123-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.123-1
- Update to 0.123.

* Wed May 27 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.99-3
- Added missing BR: desktop-file-utils.
- Set license as GPLv3 for now.

* Wed May 27 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.99-2
- Clean up spec file for inclusion into Fedora.

* Wed May 6 2009  Leigh Scott <leigh123linux@googlemail.com> - 0.99-1
- Initial build
