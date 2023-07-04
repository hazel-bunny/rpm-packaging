%define git 0

%global commit 6d3d4053bb5a081e60d11e2ddcba3dc59e1a777f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 230601

%global _basename goldendict
%global channel ChildrenDay
%global upstream_release %{channel}.%{date}.%{shortcommit}

Name: %{_basename}-ng
Version: 23.06.01%{?%git:^git%{date}.%{shortcommit}}
#https://github.com/xiaoyifang/goldendict-ng/tree/v23.06.01-ChildrenDay.230601.6d3d4053
#https://github.com/xiaoyifang/goldendict-ng/commit/6d3d4053bb5a081e60d11e2ddcba3dc59e1a777f
Release: %{channel}.%{date}.%{shortcommit}.%{?dist}

License: GPLv3+
Summary: A feature-rich dictionary lookup program, supporting multiple dictionary formats
URL: https://github.com/xiaoyifang/%{name}

%if 0%{?date}
Source0: %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
%else
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
%endif

BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Help)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5Network)
BuildRequires: qt5-qtspeech-devel
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5WebEngine)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5XmlPatterns)

BuildRequires: bzip2-devel
BuildRequires: eb-devel
BuildRequires: hunspell-devel
BuildRequires: libXtst-devel
BuildRequires: libtiff-devel
BuildRequires: libvorbis-devel
BuildRequires: libzstd-devel
BuildRequires: lzo-devel
BuildRequires: phonon-qt5-devel
BuildRequires: qtsingleapplication-qt5-devel

BuildRequires: ffmpeg-devel
#Comment out the previous line and uncomment the next line for avoiding RPMFusion
#BuildRequires: libavutil-free-devel
#BuildRequires: libavformat-free-devel

BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: make

BuildRequires: git
BuildRequires: libxkbcommon-devel
BuildRequires: opencc-devel
BuildRequires: pkg-config
BuildRequires: xapian-core-devel
BuildRequires: xz-devel
BuildRequires: xz-lzma-compat
BuildRequires: zlib-devel

Requires: eb
Requires: ffmpeg
Requires: hunspell
Requires: libvorbis
Requires: libXtst
Requires: lzo
Requires: opencc
Requires: qt5-qtbase%{?_isa}
Requires: qt5-qtmultimedia%{?_isa}
Requires: qt5-qtspeech%{?_isa}
Requires: qt5-qtsvg%{?_isa}
Requires: qt5-qttools%{?_isa}
Requires: qt5-qtwebengine%{?_isa}
Requires: xapian-core
Requires: xz
Requires: zlib

Recommends: %{name}-docs = %{?epoch:%{epoch}:}%{version}-%{release}

Provides:  %{_basename}-%{version}

Obsoletes: %{_basename} < 2

%description
Feature-rich dictionary lookup program.
    * Support of multiple dictionary file formats:
      * Babylon .BGL files
      * StarDict .ifo/.dict/.idx/.syn dictionaries
      * Dictd .index/.dict(.dz) dictionary files
      * ABBYY Lingvo .dsl source files
      * ABBYY Lingvo .lsa/.dat audio archives
    * Support for Wikipedia, Wiktionary or any other MediaWiki-based sites
    * Scan popup functionality. A small window pops up with translation of a
      word chosen from antoher application.
    * Full-text search.
    * And much more...

#%package docs
#Summary: Documentation for %{name}
#Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
#BuildArch: noarch

#%description docs
#Contain doc files of %{name}.

%package lang
Summary:  Translations for package %{name}
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description lang
This subpackage provides translations for Goldendict.

%prep
%autosetup -p1 %{?date:-n %{name}-%{commit}}
rm -rf {qtsingleapplication,maclibs,winlibs}
sed -e '/qtsingleapplication.pri/d' -i goldendict.pro

%build
%qmake_qt5 PREFIX=%{_prefix} CONFIG+=qtsingleapplication CONFIG+=use_xapian CONFIG+=use_iconv CONFIG+=zim_support goldendict.pro
%if 0%{?date}
echo "%{version}-%{channel}.%{date}.%{shortcommit}" > version.txt
%else
echo "%{version}" > version.txt
%endif
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

#%clean
#rm -rf %{buildroot}%{_datadir}/app-install

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/%{_basename}
%dir %{_datadir}/%{_basename}
#%{_datadir}/%{_basename}/locale
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{_basename}.png
%{_metainfodir}/*.metainfo.xml

#%files docs
#%{_datadir}/doc/%{name}/help

%files lang
%{_datadir}/%{_basename}/locale/

%changelog
* Fri Apr 28 2023 Dipta Biswas <dabiswas112@gmail.com> - 23.04.03-alpha.230427.becbe04d
- Initial Release
