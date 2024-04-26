Name:           kwin-effects-forceblur

%global forgeurl https://github.com/taj-ny/%{name}
Version:        1.2.0
%forgemeta

Release:        1%{?dist}
Summary:        Blur any window on Wayland and X11
License:        GPL-3.0
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6UiTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  cmake(KWin)
BuildRequires:  cmake(KWinDBusInterface)
BuildRequires:  cmake(KDecoration2)

BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)

Requires:       plasma-workspace
Requires:       kwin

%description
A fork of the KWin Blur effect for KDE Plasma 6 with the ability to blur any window on Wayland and X11.
Features
 - Wayland support
 - Draw image behind windows instead of blurring (can be used with a blurred image of the wallpaper in order to achieve a very similar effect to blur but with much lower GPU usage)
 - Rounded corners
 - Fix for artifacts when using a transparent color scheme


%files
%{_kf6_qtplugindir}/kwin/effects/configs/kwin_forceblur_config.so
%{_kf6_qtplugindir}/kwin/effects/plugins/forceblur.so

#------------------------------------------------------------------

%prep
%forgeautosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%changelog
* Fri Apr 26 2024 Dipta Biswas <dabiswas112@gmail.com> - 1.2.0-1
- initial package
