%global app_id org.kde.basket
%global forgeurl https://invent.kde.org/utilities/basket
%global tag v2.49b
# %%global commit a801db18d2487e5b26b2bec548a0763df70ac8b8
# %%global date 20190228
%forgemeta

Name:          basket
Version:       2.49
Release:       %autorelease
License:       GPLv2+
Group:         Applications/Productivity
Summary:       A multi-purpose note-taking application
URL:           %{forgeurl}
Source:        %{forgesource}

Patch:         090ac469.patch

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
%forgeautosetup -p1

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
%autochangelog
