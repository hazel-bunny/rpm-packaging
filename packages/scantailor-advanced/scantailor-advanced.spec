%define git 1

%global app_id org.kde.basket

%global commit e016f3e99a7dec3cc317ecc83fcba30f614ca32d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20230612

%global __cmake_in_source_build 1

Name:           scantailor-advanced
Version:        0.9.11.1
Release:        34%{?dist}
Summary:        An interactive post-processing tool for scanned pages

License:        GPLv3+ or LGPLv2.1
URL:            http://scantailor.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
# Don't override CFLAGS and CXXFLAGS: https://github.com/scantailor/scantailor/pull/160
Patch0:         0001-respect-CFLAGS-and-CXXFLAGS.patch
Patch1:         boost1.6.patch
Patch2:         gcc6-build-patch.patch
Patch3:         f30-buildfailures.patch

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  libXext-devel
BuildRequires:  qt-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  libjpeg-devel
BuildRequires:  zlib-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libXrender-devel
BuildRequires:  desktop-file-utils
BuildRequires:  glibc-static

%description
Scan Tailor is an interactive post-processing tool for scanned pages.
It performs operations such as page splitting, deskewing, adding/removing
borders, and others. You give it raw scans, and you get pages ready to be
printed or assembled into a PDF or DJVU file. Scanning, optical character
recognition, and assembling multi-page documents are out of scope of this
project.

%prep
%setup -q
%patch0 -p1
%patch1 -p1 -z .boost
%patch2 -p1 -b .gcc6-build
%patch3 -p1 -b .f30-buildfaulures

%build
%cmake . -DEXTRA_LIBS=Xrender -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo -DCMAKE_INSTALL_PREFIX="/usr" 
make %{?_smp_mflags}
mv resources/icons/COPYING resources/icons/COPYING-icons

%install
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/scalable/apps
cp -p resources/appicon.svg \
        ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/scalable/apps/scantailor.svg

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
* Sat Jun 24 2023 Dipta Biswas <dabiswas112@gmail.com> - 1.0.18^git-1
- Initial release

