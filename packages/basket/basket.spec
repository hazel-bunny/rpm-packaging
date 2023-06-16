%global upstreamversion 2.49b
Name:          basket
Version:       2.49
Release:       2%{?dist}
Summary:       Taking care of your ideas

Group:         Applications/Productivity
License:       GPLv2+
URL:           https://launchpad.net/basket
Source0:       %{name}-%{version}.tar.gz
Patch0:        01-fix-mimetype-installation.patch
BuildRoot:     %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(Phonon4Qt5)
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
BuildRequires: shared-mime-info
BuildRequires: gpgme-devel

# requirements for %check
BuildRequires: desktop-file-utils

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
A multi-purpose note-taking application that makes it easy to write down ideas
as you think, and quickly find them later.  You can collect, import or share
any data, tag your notes and secure it some or all of it with passwords and/or
encryption.

%package libs
Summary:        Basket libraries
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description libs
Basket libraries

%prep
%setup -q -n %{name}-%{upstreamversion}
%patch0 -p1

%build
%cmake_kf5

%cmake_build

%install
%cmake_install

# Menu
desktop-file-validate \
        %{buildroot}%{_kf5_datadir}/applications/%{name}.desktop

%find_lang %{name} --with-kde --with-html

%clean
rm -rf %{buildroot}

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
%defattr(-,root,root,-)
%doc README.md AUTHORS COPYING
%{_kf5_bindir}/basket
%{_kf5_datadir}/applications/*.desktop
%{_kf5_datadir}/basket/
%{_kf5_datadir}/kxmlgui5/
%{_kf5_datadir}/kservices5/
%{_kf5_datadir}/icons/hicolor/
%{_kf5_datadir}/mime/packages/basket.xml

%files libs
%defattr(-,root,root,-)
%{_kf5_libdir}/*.so*
%{_kf5_libdir}/qt5/plugins/*.so

%changelog
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
