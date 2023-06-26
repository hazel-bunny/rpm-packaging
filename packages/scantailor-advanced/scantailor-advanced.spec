%define git 0

%global commit 85c3310cec0e6f4dd86333d140fb05d539cffaea
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20220423

%global _basename scantailor

Name:           %{_basename}-advanced
Version:        1.0.18
Release:        1%{?dist}
Summary:        An interactive post-processing tool for scanned pages
License:        GPLv3+ or LGPLv2.1
URL:            https://github.com/ScanTailor-Advanced/%{name}

Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  boost-devel
BuildRequires:  libXext-devel
BuildRequires:  libXrender-devel
BuildRequires:  libxcb-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  desktop-file-utils
BuildRequires:  glibc-static
# BuildRequires:  boost-test boost-thread
# BuildRequires:  cmake(Qt6OpenGLWidgets)

Provides:       scantailor
Obsoletes:      scantailor < 1.0.18

%description
Scan Tailor is an interactive post-processing tool for scanned pages. It
performs operations such as page splitting, deskewing, adding/removing borders,
and others. You give it raw scans, and you get pages ready to be printed or
assembled into a PDF or DJVU file. Scanning, optical character recognition, and
assembling multi-page documents are out of scope of this project.

ScanTailor Advanced is the ScanTailor version that merges the features of the
ScanTailor Featured and ScanTailor Enhanced versions, brings new ones and fixes.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
make tests
./tests/tests

%files
%doc COPYING resources/icons/COPYING-icons
%{_bindir}/scantailor
%{_bindir}/scantailor-cli
%{_datadir}/scantailor/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/scantailor.svg

%changelog
* Sat Jun 24 2023 Dipta Biswas <dabiswas112@gmail.com> - 1.0.18-1
- Initial release

