%define git 1

%global _basename hamster
%global app_id org.gnome.Hamster

%global commit d10ae12cde0370233189574d255c831e3eb267ab
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20230430

Name:       %{_basename}-time-tracker
Version:    3.0.2%{?git:^git%{date}.%{shortcommit}}
Release:    1%{?dist}
License:    GPLv3+
Group:      Applications/Productivity
URL:        https://github.com/project%{srcname}/%{srcname}
Summary:    The Linux time tracker

%if ! 0%{?git}
Source0: %{url}/archive/v%{version}/%{_basename}-%{version}.tar.gz
%else
Source0: %{url}/archive/%{commit}/%{_basename}-%{commit}.tar.gz
%endif

BuildRequires:    gettext
BuildRequires:    intltool
BuildRequires:    glib2-devel
BuildRequires:    dbus-glib
BuildRequires:    docbook-utils
BuildRequires:    gnome-doc-utils
BuildRequires:    libxslt
BuildRequires:    gtk-update-icon-cache
BuildRequires:    fdupes
BuildRequires:    gobject-introspection

BuildRequires:    desktop-file-utils
BuildRequires:    python3-devel
BuildRequires:    itstool

Requires:         dbus
Requires:         hicolor-icon-theme
Requires:         bash-completion

Requires:         python3-cairo
Requires:         python3-dbus
Requires:         python3-gobject
Requires:         python3-pyxdg

BuildRequires:    GConf2
Requires(pre):    GConf2
Requires(post):   GConf2
Requires(preun):  GConf2

%description
Project %{srcname} is time tracking for individuals. It helps you to keep track on
how much time you have spent during the day on activities you choose to track. 

Whenever you change from doing one task to other, you change your current
activity in %{srcname}. After a while you can see how many hours you have spent on
what. Maybe print it out, or export to some suitable format, if time reporting
is a request of your employee.

%prep
%autosetup -n %{srcname}-%{version}

%build
./waf configure -vv --prefix=%{_prefix} --datadir=%{_datadir} 
./waf build -vv %{?_smp_mflags}

%install
./waf install --destdir=%{buildroot}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop

%pre
%gconf_schema_prepare %{name}
%gconf_schema_obsolete %{name}

%post
%gconf_schema_upgrade %{name}

%preun
%gconf_schema_remove %{name}

%files
%license COPYING
%doc AUTHORS NEWS.md README.md MAINTAINERS
%{_bindir}/%{_basename}
%{_datadir}/applications/%{app_id}.GUI.desktop
%{_datadir}/dbus-1/services/%{app_id}.service
%{_datadir}/dbus-1/services/%{app_id}.WindowServer.service
%{_datadir}/dbus-1/services/%{app_id}.GUI.service
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/%{_basename}/
%{_libexecdir}/%{_basename}/
%{python3_sitelib}/%{_basename}/
%{_datadir}/bash-completion/completions/%{_basename}.bash
%{_datadir}/metainfo/%{app_id}.GUI.metainfo.xml
%{_datadir}/glib-2.0/schemas/org.gnome.%{_basename}.gschema.xml
%{_datadir}/help/C/%{_basename}
%{_datadir}/locale/*/LC_MESSAGES/%{srcname}.mo

%changelog
* Fri Jun 23 2023 Dipta Biswas <dabiswas112@gmail.com> - 3.0.2^git
- Switch to git snapshot
- Updated spec for newer versions of Fedora

* Mon Jun 15 2020 Markus Neteler <neteler@mundialis.de> - 3.0.2
- New upstream version
- updated SPEC to Python3 and new file locations

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.16.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.15.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0-0.14.rc1
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.13.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 09 2017 Iryna Shcherbina <ishcherb@redhat.com> - 2.0-0.12.rc1
- Add a build-time dependency on python2-devel (rhbz#1479813)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.11.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.10.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.9.rc1
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Mar 21 2016 Raphael Groner <projects.rg@smart.ms> - 2.0-0.8.rc1
- ugly workaround for different package name in f22 to satisfy depcheck

* Sat Mar 12 2016 Raphael Groner <projects.rg@smart.ms> - 2.0-0.7.rc1
- fix version warning and TargetFlags, rhbz#1317087
- consolidate patches to same patch level and use autosetup macro

* Sat Mar 12 2016 Raphael Groner <projects.rg@smart.ms> - 2.0-0.6.rc1
- add R: python-gobject, rhbz#1316230

* Thu Mar 03 2016 Raphael Groner <projects.rg@smart.ms> - 2.0-0.5.rc1
- apply patch against ZeroDivisionError, rhbz#1309613

* Mon Feb 15 2016 Raphael Groner <projects.rg@smart.ms> - 2.0-0.4.rc1
- readd lost build conditional for epel, rhbz#1046077

* Mon Feb 15 2016 Raphael Groner <projects.rg@smart.ms> - 2.0-0.3.rc1
- add upstream patches for GNOME 3.18, rhbz#1074967, rhbz#1307256

* Tue Feb 02 2016 Raphael Groner <projects.rg@smart.ms> - 2.0-0.2.rc1
- R: dbus-python, rhbz#1285405

* Mon Dec 21 2015 Raphael Groner <projects.rg@smart.ms> - 2.0-0.1.rc1
- bump to version 2.0-rc1
- small modernization

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Nov 23 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.04-4
- Patch for rhbz#1074967

* Tue Jul 15 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.04-3
- Add requires on pyxdg

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.04-1
- Update to latest upstream release. 

* Mon Dec 30 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.03.3-6
- Update desktop-file-validate command for F19

* Sat Dec 28 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.03.3-5
- Add patch for notification fix
- rhbz#1046991
- upstream issue #127
- upstream issue #117

* Tue Dec 24 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.03.3-4
- Add wnck dependency so users can use workspaces out of the box
- https://bugzilla.redhat.com/show_bug.cgi?id=1046077

* Tue Dec 17 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.03.3-3
- Add missing gnome-python2-gconf requirement
- https://bugzilla.redhat.com/show_bug.cgi?id=1043564

* Mon Dec 02 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.03.3-2
- Fixes as per rhbz#1036254
- Correct schame functions
- Own gnome help dir
- Own bash completion dir
- schema and bash completion files do not need to be %%config
- https://lists.fedoraproject.org/pipermail/packaging/2013-December/009834.html

* Sat Nov 30 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.03.3-1
- Initial rpm build