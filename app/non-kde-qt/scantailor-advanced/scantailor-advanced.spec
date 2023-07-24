%global git 0

%global commit 85c3310cec0e6f4dd86333d140fb05d539cffaea
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20220423

%global _basename scantailor

%global __cmake_in_source_build 1

Name:           %{_basename}-advanced
Version:        1.0.18%{?%git:^git%{date}.%{shortcommit}}
Release:        %autorelease
Summary:        An interactive post-processing tool for scanned pages
License:        GPLv3+ or LGPLv2.1
URL:            https://github.com/ScanTailor-Advanced/%{name}

Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

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

Provides:       scantailor = 1.0.18
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
mkdir build
pushd build
%cmake .. -DEXTRA_LIBS=Xrender -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo -DCMAKE_INSTALL_PREFIX="/usr"
popd
make %{?_smp_mflags} -C build

%install
make install DESTDIR=%{buildroot} -C build

%check
cd build
make test

%files
%doc README.md
%{_bindir}/%{_basename}
%{_datadir}/%{name}
%{_datadir}/applications/%{_basename}.desktop
%{_datadir}/icons/hicolor/scalable/apps/ScanTailor.svg
%{_datadir}/mime/packages/%{_basename}-project.xml

%changelog
* Sat Jun 24 2023 Dipta Biswas <dabiswas112@gmail.com> - 1.0.18-1
- Initial release
