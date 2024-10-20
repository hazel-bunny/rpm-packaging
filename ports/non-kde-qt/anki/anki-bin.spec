%global _basename anki
%define _qt_lib aqt
%define _cpython cp39

Name:           %{_basename}-bin
Version:        24.06.3

%global forgeurl https://github.com/%{_basename}tects/%{_basename}
%global tag %{version}

%ifarch x86_64
%define _glibc 28
%define _wheel_source 51/5f/6f52b958fe38a36a0799c01fbd56a742ebdfcf41f89438dbee998b8ce692
%else
%ifarch aarch64
%define _glibc 31
%define _wheel_source df/bb/b0bfbc6a06a598b0b614d18dd8c4f40827828649f9742f1f44a4e44d6a2c
%endif
%endif

%define _pip_source https://files.pythonhosted.org/packages/
%define aqt_source 21/2a/d8e22a9521be04ef29a30d21a2c3008783ab03b6f07cc14696a040f747a4
%define anki_wheel %{_basename}-%{version}-%{_cpython}-abi3-manylinux_2_%{_glibc}_%{_arch}.whl
%define aqt_wheel %{_qt_lib}-%{version}-py3-none-any.whl

Release:        1%{?dist}
Summary:        Powerful, intelligent flash cards.
License:        AGPL-3.0-or-later AND GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT AND BSD-3-Clause AND CC-BY-SA-3.0 AND CC-BY-3.0 AND Apache-2.0 AND CC-BY-2.5
URL:            https://apps.ankiweb.net

Source0:        %{_pip_source}%{_wheel_source}/%{anki_wheel}
Source1:        %{_pip_source}%{aqt_source}/%{aqt_wheel}
Source2:        %{forgeurl}/raw/%{version}/qt/run%{_basename}.py
Source3:        %{forgeurl}/raw/%{version}/qt/bundle/lin/%{_basename}.desktop
Source4:        %{forgeurl}/raw/%{version}/qt/bundle/lin/%{_basename}.1
Source5:        %{forgeurl}/raw/%{version}/qt/bundle/lin/%{_basename}.xml
Source6:        %{forgeurl}/raw/%{version}/qt/bundle/lin/%{_basename}.png
Source7:        %{forgeurl}/raw/%{version}/qt/bundle/lin/%{_basename}.xpm
Source8:        %{forgeurl}/raw/%{version}/LICENSE
Source9:        %{forgeurl}/raw/%{version}/README.md

ExclusiveArch:  %{qt6_qtwebengine_arches}

BuildRequires:  desktop-file-utils
BuildRequires:  libxcrypt-compat
BuildRequires:  python3-devel
BuildRequires:  python3-installer
BuildRequires:  python3-pip

Requires:       python3-beautifulsoup4
Requires:       python3-decorator
Requires:       python3-distro
Requires:       python3-flask
Requires:       python3-flask-cors
Requires:       python3-jsonschema
Requires:       python3-markdown
Requires:       python3-orjson
Requires:       python3-pip-system-certs
Requires:       python3-protobuf
Requires:       python3-pyqt6-webengine
Requires:       python3-requests
Requires:       python3-send2trash
Requires:       python3-waitress

Requires:       hicolor-icon-theme
Requires:       qt6-qtsvg
Requires:       qt6-qtwebengine
Requires:       sox

Recommends:     lame
Recommends:     mplayer
Recommends:     mpv

Provides:       %{_basename} = %{version}
Provides:       python3-%{_basename} = %{version}
Provides:       python3-%{_qt_lib} = %{version}

%description
Anki is a program which makes remembering things easy. Because it's a lot more
efficient than traditional study methods, you can either greatly decrease your
time spent studying, or greatly increase the amount you learn.

Anyone who needs to remember things in their daily life can benefit from Anki.
Since it is content-agnostic and supports images, audio, videos and scientific
markup (via LaTeX), the possibilities are endless.

For example:
 - Learning a language
 - Studying for medical and law exams
 - Memorizing people's names and faces
 - Brushing up on geography
 - Mastering long poems
 - Even practicing guitar chords!

%prep
mkdir -p %{_pyproject_wheeldir}
cp -r %{SOURCE0} %{SOURCE1} %{_pyproject_wheeldir}

%build
#nothing

%install
%pyproject_install

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/{applications,pixmaps}
mkdir -p %{buildroot}%{_datadir}/man/man1
mkdir -p %{buildroot}%{_datadir}/mime/packages

install -Dm755 %{SOURCE2} %{buildroot}%{_bindir}/%{_basename}

install -Dm644 %{SOURCE3} %{buildroot}%{_datadir}/applications/%{_basename}.desktop
install -Dm644 %{SOURCE4} %{buildroot}%{_datadir}/man/man1/%{_basename}.1
install -Dm644 %{SOURCE5} %{buildroot}%{_datadir}/mime/packages/%{_basename}.xml
install -Dm644 %{SOURCE6} %{buildroot}%{_datadir}/pixmaps/%{_basename}.png
install -Dm644 %{SOURCE7} %{buildroot}%{_datadir}/pixmaps/%{_basename}.xpm
install -Dm644 %{SOURCE8} %{buildroot}%{_datadir}/licenses/%{name}/LICENSE
install -Dm644 %{SOURCE9} %{buildroot}%{_datadir}/doc/%{name}/README.md

%files
%license LICENSE
%doc README.md
%{_bindir}/%{_basename}
%{python3_sitearch}/%{_basename}/
%{python3_sitearch}/%{_basename}-%{version}.dist-info
%{python3_sitearch}/_%{_qt_lib}/
%{python3_sitearch}/%{_qt_lib}/
%{python3_sitearch}/%{_qt_lib}-%{version}.dist-info
%{_datadir}/applications/%{_basename}.desktop
%{_datadir}/man/man1/%{_basename}.*
%{_datadir}/mime/packages/%{_basename}.xml
%{_datadir}/pixmaps/%{_basename}.{png,xpm}

%changelog
* Fri Oct 18 2024 Hazel Bunny <hazel_bunny@disroot.org> - 24.06.3-1
- Initial package
