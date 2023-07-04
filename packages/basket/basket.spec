%define git 0

%global app_id org.kde.basket

%global commit a801db18d2487e5b26b2bec548a0763df70ac8b8
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20190228

%global upstreamversion 2.49b

Name:          basket
Version:       2.49%{?%git:^git%{date}.%{shortcommit}}
Release:       3%{?dist}
License:       GPLv2+
Group:         Applications/Productivity
URL:           https://invent.kde.org/utilities/%{name}
Summary:       A multi-purpose note-taking application

Source0:       %{url}/-/archive/v%{upstreamversion}/%{name}-v%{upstreamversion}.tar.bz2

# %%if 0%%{?git}
# Source0: https://github.com/KDE/%%{name}/archive/%%{commit}/%%{name}-%%{commit}.tar.gz
# %%else
# Source0: https://github.com/KDE/%%{name}/archive/v%%{version}/%%{name}-%%{version}.tar.gz
# %%endif

Patch0:        090ac469.patch
#Patch0:       %%{url}/-/commit/090ac469.patch
#BuildRoot:    %%{_tmppath}/%%{name}-%%{version}-root-%%(%%{__id_u} -n)

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: pkgconfig(libgit2)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(phonon4qt5)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5FileMetaData)
BuildRequires: cmake(KF5GlobalAccel)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(Qt5Concurrent)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Xml)
BuildRequires: kf5-kdelibs4support
BuildRequires: shared-mime-info
BuildRequires: gpgme-devel

# requirements for %%check
BuildRequires: desktop-file-utils

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

Recommends:     %{name}-lang = %{version}

Provides:       basket5 = %{version}

Obsoletes:      basket5 < %{version}

%description
This multi-purpose note-taking application can helps you to:

- Easily take all sort of notes
- Collect research results and share them
- Centralize your project data and re-use them
- Quickly organize your toughts in idea boxes
- Keep track of your information in a smart way
- Make intelligent To Do lists
- And a lot more...

This application provides several baskets where to drop every sort of notes:
rich text, links, images, sounds, files, colors, application launcher...
Objects can be edited, copied, dragged... So, you can arrange them as you want!
This application can be used to quickly drop web objects (link, text, images...)
or notes, as well as to free your clutered desktop (if any).
It is also useful to collect informations for a report. Those data can be shared
with co-workers by exporting baskets to HTML.

%package libs
Summary:        Basket libraries
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description libs
Basket libraries

%prep
%setup -q -n %{name}-v%{upstreamversion}
%patch 0 -p1

%build
%cmake_kf5
%cmake_build

%install
%cmake_install

%find_lang %{name} --with-kde --with-html

%check
desktop-file-validate \
        %{buildroot}%{_kf5_datadir}/applications/%{name}.desktop

%post libs -p /sbin/ldconfig

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database &> /dev/null || :

%postun libs -p /sbin/ldconfig

%postun
if [ $1 -eq 0 ] ; then
   touch --no-create %{_kf5_iconsdir}/hicolor &>/dev/null
   gtk-update-icon-cache %{_kf5_iconsdir}/hicolor &>/dev/null || :
   update-desktop-database -q &> /dev/null
fi

%posttrans
gtk-update-icon-cache %{_kf5_iconsdir}/hicolor &>/dev/null || :
update-desktop-database -q &> /dev/null

%files -f %{name}.lang
%doc README.md AUTHORS
%{_kf5_bindir}/%{name}
%{_kf5_datadir}/%{name}/
%{_kf5_datadir}/applications/%{name}.desktop
%{_kf5_datadir}/kxmlgui5/%{name}/
%{_kf5_datadir}/icons/hicolor/*/actions/likeback_*
%{_kf5_datadir}/icons/hicolor/*/actions/tag_*
%{_kf5_datadir}/icons/hicolor/*/apps/%{name}.png
%{_kf5_datadir}/kservices5/%{name}*.desktop

%files libs
%{_kf5_libdir}/lib%{name}common*
%{_kf5_qtplugindir}/%{name}thumbcreator.so
%{_kf5_qtplugindir}/kcm_%{name}.so

%changelog
* Tue Jul 4 2023 Dipta Biswas <dabiswas112@gmail.com> - 2.49-3
- add patch for libgit2
- refactor spec
- fix files

* Fri Aug 05 2022 Luigi Toscano <luigi.toscano@tiscali.it> - 2.49-2
- adapt to the new cmake, make it compile again

* Thu Jun 27 2019 Luigi Toscano <luigi.toscano@tiscali.it> - 2.49-1
- new release (basket 2.49 + fixes)

* Wed Jan 30 2019 Luigi Toscano <luigi.toscano@tiscali.it> - 2.11-0.20180715git058ce7a
- new git snapshot (basket 2.11beta + fixes)

* Wed Apr 27 2016 Luigi Toscano <luigi.toscano@tiscali.it> - 2.10-0.20160425gitb77687f
- new git snapshot (basket 2.10beta + fixes)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.81-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 15 2010 Thomas Janssen <thomasj@fedoraproject.org> 1.81-1
- basket 1.81

* Tue May 11 2010 Rex Dieter <rdieter@fedoraproject.org> 1.80-2
- dfi usage: drop --vendor=fedora
- various .spec cosmetics

* Sun Apr 11 2010 Thomas Janssen <thomasj@fedoraproject.org> 1.80-1
- basket-1.80

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 04 2008 Rex Dieter <rdieter@fedoraproject.org> 1.0.3.1-4
- fix ->F-10+ upgrade path
- Cannot configure basket, kcm_basket.la missing (#474425)
- drop needless Requires: hicolor-icon-theme

* Sat Nov 15 2008 Christopher D. Stover <quantumburnz@hotmail.com> 1.0.3.1-3
- resolved kontact broken dependency

* Mon Nov 10 2008 Christopher D. Stover <quantumburnz@hotmail.com> 1.0.3.1-2
- added a requires for hicolor-icon-theme
- removed -p from the main package /sbin/ldconfig

* Sat Oct 25 2008 Christopher D. Stover <quantumburnz@hotmail.com> 1.0.3.1-1
- version 1.0.3.1
- gcc43 patch is no longer needed

* Sat Jun 07 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 1.0.2-7
- disable -kontact for F10+ (can't integrate KDE 3 app into KDE 4 Kontact)

* Sun Jun 01 2008 Aurelien Bompard <abompard@fedoraproject.org> 1.0.2-6
- rebuild

* Wed Mar 02 2008 Rex Dieter <rdieter@fedoraproject.org> 1.0.2-5
- fix rawhide build (#433960)
- summary: s/for KDE//

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> 1.0.2-4
- Autorebuild for GCC 4.3

* Sat Oct 27 2007 Aurelien Bompard <abompard@fedoraproject.org> 1.0.2-3
- fix kontact plugin for kdepim-enterprise (bug 354771)

* Sat Aug 25 2007 Aurelien Bompard <abompard@fedoraproject.org> 1.0.2-2
- rebuild for BuildID
- fix license tag

* Tue Apr 24 2007 Aurelien Bompard <abompard@fedoraproject.org> 1.0.2-1
- version 1.0.2 (bug 237660)

* Sun Mar 18 2007 Aurelien Bompard <abompard@fedoraproject.org> 1.0.1-1
- version 1.0.1

* Sat Feb 17 2007 Aurelien Bompard <abompard@fedoraproject.org> 1.0-2
- split off the kontact plugin, patch by Laurent Rineau (see bug 228966)

* Mon Feb 12 2007 Aurelien Bompard <abompard@fedoraproject.org> 1.0-1
- version 1.0

* Wed Oct 25 2006 Aurelien Bompard <abompard@fedoraproject.org> 0.6.0-1
- version 0.6.0

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.5.0-10
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 19 2006 Aurelien Bompard <abompard@fedoraproject.org> 0.5.0-9
- add explicit linking to libfam

* Tue Sep 19 2006 Aurelien Bompard <abompard@fedoraproject.org> 0.5.0-8
- rebuild

* Wed Aug 30 2006 Aurelien Bompard <abompard@fedoraproject.org> 0.5.0-7
- BR: gamin-devel

* Wed Aug 30 2006 Aurelien Bompard <abompard@fedoraproject.org> 0.5.0-6
- rebuild

* Tue Feb 21 2006 Aurelien Bompard <gauret[AT]free.fr> 0.5.0-5
- rebuild for FC5

* Mon Oct 17 2005 Aurelien Bompard <gauret[AT]free.fr> 0.5.0-4
- add patch for 64 bits

* Fri Oct 14 2005 Aurelien Bompard <gauret[AT]free.fr> 0.5.0-3
- don't add the extension to the icon, it's useless
- touch the icon dir in post and postun

* Fri Oct 14 2005 Aurelien Bompard <gauret[AT]free.fr> 0.5.0-2
- own the doc dir
- use hicolor instead of crystalsvg as icon theme
- add extension to the icon in the desktop file

* Wed Oct 12 2005 Aurelien Bompard <gauret[AT]free.fr> 0.5.0-1
- port to Fedora from Mandriva (release 3)

* Wed Jul 13 2005 Nicolas Lécureuil <neoclust@mandrake.org> 0.5.0-3mdk
- Fix File section

* Fri May 06 2005 Nicolas Lécureuil <neoclust@mandrake.org> 0.5.0-2mdk
- Fix BuildRequires
- Fix Build For amd64

* Wed Apr 06 2005 Nicolas Lécureuil <neoclust@mandrake.org> 0.5.0-1mdk
- First release
