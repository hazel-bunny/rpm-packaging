Name:           httraqt
Version:        1.4.11
Release:        %autorelease
License:        GPLv3
URL:            https://%{name}.sourceforge.net/
Summary:        HTTrack Qt GUI

Source0:        https://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  httrack-devel
BuildRequires:  qt6-rpm-macros

BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6DBus)

Requires:       hicolor-icon-theme
Requires:       httrack

%description
HTTraQt is the clone from WinHTTrack, software for downloading of internet 
sites or/and content of their: multimedia files, documents, images, etc.

Features:
* Possible to easy switch the language of GUI.
* Easy to add the language files without to change the program code.
* Selection of browser little bit changed: possible to select browser and 
system of "User Agent".
* Extended the selectiing of file extensions under "Rulez" settings.

%prep
%setup -qn %{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%doc README
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
* Wed Apr 26 2023 Dipta Biswas <dabiswas112@gmail.com> 1.4.11-1
- Update to 1.4.11
- Update spec for qt6

* Sun Oct 11 2015 Christopher Meng <rpm@cicku.me> - 1.4.6-1
- Update to 1.4.6

* Mon Aug 31 2015 Christopher Meng <rpm@cicku.me> - 1.4.5-1
- Update to 1.4.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.4.4-3
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 08 2014 Christopher Meng <rpm@cicku.me> - 1.4.4-2
- Update the license
- SPEC cleanup

* Mon Jul 21 2014 Christopher Meng <rpm@cicku.me> - 1.4.4-1
- Update to 1.4.4

* Sat Jun 14 2014 Christopher Meng <rpm@cicku.me> - 1.4.3-1
- Update to 1.4.3

* Wed May 28 2014 Christopher Meng <rpm@cicku.me> - 1.3.4-1
- Update to 1.3.4

* Fri Jan 31 2014 Christopher Meng <rpm@cicku.me> - 1.3.0-1
- Initial Package.
