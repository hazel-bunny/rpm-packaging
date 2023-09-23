%global _basename hamster
%global app_id org.gnome.Hamster

%global forgeurl https://github.com/project%{_basename}/%{_basename}
%global commit d10ae12cde0370233189574d255c831e3eb267ab
%global date 20230430
%forgemeta

%global debug_package %{nil}

Name:       %{_basename}-time-tracker
Version:    3.0.2
Release:    %autorelease
License:    GPLv3+
Summary:    The Linux time tracker
Group:      Applications/Productivity
URL:        %{forgeurl}
Source:     %{forgesource}

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
Project %{_basename} is time tracking for individuals. It helps you to keep track on
how much time you have spent during the day on activities you choose to track. 

Whenever you change from doing one task to other, you change your current
activity in %{_basename}. After a while you can see how many hours you have spent on
what. Maybe print it out, or export to some suitable format, if time reporting
is a request of your employee.

%prep
%setup -qn %{_basename}-%{commit}

%build
./waf configure -vv --prefix=%{_prefix} --datadir=%{_datadir} 
./waf build -vv %{?_smp_mflags}

%install
./waf install --destdir=%{buildroot}
rm -rf %{buildroot}%{_datadir}/glib-2.0/schemas/gschemas.compiled

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

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
%{_datadir}/help/*/%{_basename}
%{_datadir}/locale/*/LC_MESSAGES/%{_basename}.mo

%changelog
%autochangelog
