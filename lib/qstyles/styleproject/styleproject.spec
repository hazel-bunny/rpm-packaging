%global forgeurl https://sourceforge.net/projects/styleproject
%global scm git
%global commit 1f3a8e7a14562fe61980bdc53c7f41c6b4abc341/
%global date 20220128
%forgemeta

Name:    styleproject
Version: 2.0
Release: %autorelease
Summary: A maclike style for qt4/qt5/kde4/kde5.
License: None
URL:     %{forgeurl}
Source:  https://sourceforge.net/code-snapshots/git/s/st/styleproject/code.git/styleproject-code-1f3a8e7a14562fe61980bdc53c7f41c6b4abc341.zip

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(x11)

#Qt5
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(Qt5OpenGL)

#KF5
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KDecoration2)
BuildRequires: kf5-rpm-macros

#Qt4 and KDE4
BuildRequires: pkgconfig(Qt)
BuildRequires: kdelibs4-devel

%description
StyleProject is a style for qt4 and qt5 that requires kde for the window
decoration. Aim is to make a maclike experience, without making any 1:1 clone of
anything. Its highly experimental.

Features
- A very hackish CSD implementation (client side decorations)
- A very hackish implementation of content aware toolbars, like the one seen in mac os X yosemite
- Presets, different settings and palette for different applications
- Supports XBar (globalmenu implementation from the bespin style)
- Many different shadows for clickables, example: Raised, Sunken, Carved...
- Animated mouseovers for clickables
- Includes a KWin window decoration
- Text-file configuration
- User-defined gradients for many window-objects
- UNO: a apple-a-like combined head for mainwindows
- Translucency (requires a running compositing manager)
- Pretty configurable in general

%files
%license
%doc

%prep
%autosetup -n %{name}-code-%{commit}

%build
# Build for Qt 4
%global _vpath_builddir %{_target_platform}-qt4
%cmake -DQT5BUILD=OFF -DHASX11=0 -B %{_vpath_builddir}
%cmake_build
%undefine _vpath_builddir

# Build for Qt 5
%global _vpath_builddir %{_target_platform}-qt5
%cmake -DQT5BUILD=ON -B %{_vpath_builddir}
%cmake_build
%undefine _vpath_builddir

%install
%global _vpath_builddir %{_target_platform}-qt4
%cmake_install
%undefine _vpath_builddir

%global _vpath_builddir %{_target_platform}-qt5
%cmake_install
%undefine _vpath_builddir

%changelog
%autochangelog
