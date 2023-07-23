%define git 0

%global commit 6d3d4053bb5a081e60d11e2ddcba3dc59e1a777f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 230601

%global _basename goldendict
%global app_id org.xiaoyifang.GoldenDict_NG

%global forgeurl https://github.com/xiaoyifang/%{_basename}-ng

Version:        23.06.01
%forgemeta

Name:           %{_basename}-ng
Release:        %autorelease
Summary:        The Next Generation GoldenDict

# The program is licensed under the GPL-3.0-or-later, except some files:
# src/{dictzip.hh,dictzip.c} are under GPL-1.0-or-later license
# src/dict/{bgl_babylon.hh,bgl_babylon.cc} are under GPL-2.0-or-later license
# src/dict/{ripemd.hh,ripemd.cc,mdictparser.hh,mdictparser.cc} are under GPL-3.0-only license
# files of JavaScript libraries:
# src/scripts/darkreader.js - MIT license
# src/scripts/{iframeResizer.contentWindow.min.js,iframeResizer.min.js} - MIT license
# src/scripts/jquery-3.6.0.slim.min.js - MIT license
License:        GPL-3.0-or-later AND GPL-1.0-or-later AND GPL-2.0-or-later AND GPL-3.0-only AND MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

# https://src.fedoraproject.org/rpms/qt6-qtwebengine/blob/rawhide/f/qt6-qtwebengine.spec#_90
ExclusiveArch:  aarch64 x86_64

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6TextToSpeech)

BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(opencc)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xapian-core)
BuildRequires:  pkgconfig(libzim)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(tomlplusplus)
# ffmpeg
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswresample)
# xz-devel
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  eb-devel

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Provides:       bundled(qtsingleapplication)
Provides:       bundled(js-darkreader)
Provides:       bundled(js-iframe-resizer)
Provides:       bundled(js-jquery)

Conflicts:      %{_basename}

%description
Feature-rich dictionary lookup program.
* Support of multiple dictionary file formats:
  * Babylon .BGL files
  * StarDict .ifo/.dict/.idx/.syn dictionaries
  * Dictd .index/.dict(.dz) dictionary files
  * ABBYY Lingvo .dsl source files
  * ABBYY Lingvo .lsa/.dat audio archives
* Support for Wikipedia, Wiktionary or any other MediaWiki-based sites
* Scan popup functionality. A small window pops up with translation of a word
  chosen from antoher application.
* Full-text search.
* And much more...

%prep
%forgeautosetup -p1

# remove unneeded third-party libraries
rm -r thirdparty/{fmt,qwebengine_ts,tomlplusplus}
rm -r winlibs

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DUSE_SYSTEM_FMT=ON \
    -DUSE_SYSTEM_TOML=ON \
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/%{_basename}
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/pixmaps/%{_basename}.png
%{_metainfodir}/%{app_id}.metainfo.xml
%dir %{_datadir}/%{_basename}
%dir %{_datadir}/%{_basename}/locale
%{_datadir}/%{_basename}/locale/*.qm

%changelog
%autochangelog
