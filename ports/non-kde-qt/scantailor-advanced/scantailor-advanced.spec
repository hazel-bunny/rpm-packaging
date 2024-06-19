%global _basename scantailor
%global iconname ScanTailor
%global _qt_major_version 6

Name:           %{_basename}-advanced

%global forgeurl https://github.com/ScanTailor-Advanced/%{name}
%global commit 7601370ea92b2576907c5d8be98699bbd7b0a075
%global date 20230822

%forgemeta

Version:        1.0.19
Release:        3%{?dist}
Summary:        An interactive post-processing tool for scanned pages
License:        GPLv3+ or LGPLv2.1
URL:            %{forgeurl}
Source:         %{forgesource}

#------------------------------------------------------------------

BuildRequires:  glibc-static
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  desktop-file-utils

BuildRequires:  boost-devel
BuildRequires:  boost-test

BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(pthread-stubs)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xext)

BuildRequires:  cmake(Qt%{_qt_major_version}Core)
BuildRequires:  cmake(Qt%{_qt_major_version}Gui)
BuildRequires:  cmake(Qt%{_qt_major_version}Widgets)
BuildRequires:  cmake(Qt%{_qt_major_version}Xml)
BuildRequires:  cmake(Qt%{_qt_major_version}Network)
BuildRequires:  cmake(Qt%{_qt_major_version}LinguistTools)
BuildRequires:  cmake(Qt%{_qt_major_version}OpenGL)
BuildRequires:  cmake(Qt%{_qt_major_version}Svg)
BuildRequires:  cmake(Qt%{_qt_major_version}OpenGLWidgets)

Provides:       %{_basename} = %{version}
Obsoletes:      %{_basename} < %{version}

#------------------------------------------------------------------

%description
Scan Tailor is an interactive post-processing tool for scanned pages. It
performs operations such as page splitting, deskewing, adding/removing borders,
and others. You give it raw scans, and you get pages ready to be printed or
assembled into a PDF or DJVU file. Scanning, optical character recognition, and
assembling multi-page documents are out of scope of this project.

ScanTailor Advanced is the ScanTailor version that merges the features of the
ScanTailor Featured and ScanTailor Enhanced versions, brings new ones and fixes.

%files
%doc README.md
%{_bindir}/%{_basename}
%{_datadir}/%{name}
%{_datadir}/applications/%{_basename}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{iconname}.svg
%{_datadir}/mime/packages/%{_basename}-project.xml

#------------------------------------------------------------------

%prep
%forgeautosetup

%build
%cmake -GNinja -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

#------------------------------------------------------------------

%changelog
* Sun Jun 16 2024 Dipta Biswas <dabiswas112@gmail.com> - 1.0.19-3.git
- Fix build dependencies

* Sun Mar 31 2024 Dipta Biswas <dabiswas112@gmail.com> - 1.0.19-1.git
- Switch to git snapshot

* Sat Jun 24 2023 Dipta Biswas <dabiswas112@gmail.com> - 1.0.18-1
- Initial release
