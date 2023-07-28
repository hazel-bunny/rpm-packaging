%global forgeurl https://github.com/vladimir-kraus/phantomstyle
%global branch master
%global commit 95de707b855425e2639b37d6e9dd1ed65ee217e6
%global date 20210923
%forgemeta

Name:    phantomstyle
Version: 0
Release: %autorelease
Summary: Cross-platform QStyle for traditionalists
License: LGPLv2.1, MIT
URL:     %{forgeurl}
Source:  %{forgesource}

%description
Phantom is a QStyle for Qt which began as an overhaul of QFusionStyle. Similar
to Fusion, it's designed to be a looks-the-same cross-platform style. It looks
native to nobody, but familiar to many. It has the visual appearance of a
traditional GUI, and does not adopt a "modern flat" style. Compared to Fusion,
it has many fixes, objective improvements, and subjective improvements.

%files
%license LICENSE
%doc README.md

%prep
%forgeautosetup

%build
cd src/styleplugin

%global _vpath_builddir %{_target_platform}-qt5
%qmake_qt5
%make_build
%undefine _vpath_builddir

rm -rf .qmake.stash

# Build for Qt 6
%global _vpath_builddir %{_target_platform}-qt6
%qmake_qt6
%make_build
%undefine _vpath_builddir

%install
cd src/styleplugin

%global _vpath_builddir %{_target_platform}-qt5
%make_install INSTALL_ROOT=%{buildroot}
%undefine _vpath_builddir

%global _vpath_builddir %{_target_platform}-qt6
%make_install INSTALL_ROOT=%{buildroot}
%undefine _vpath_builddir

%changelog
%autochangelog
