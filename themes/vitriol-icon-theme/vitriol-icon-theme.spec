%global forgeurl https://github.com/hazel-bunny/vitriol-icon-theme
%global commit 223a68559b12a7ddcb8f66628480e9e1f63cd831
%global date 20240228
%forgemeta

Name:    vitriol-icon-theme
Summary: Vitriol icon theme
Version: 6.0.0
Release: %autorelease

# http://techbase.kde.org/Policies/Licensing_Policy
License: LGPL-3.0-or-later

URL:	 %{forgeurl}
Source:  %{forgesource}

# must come *after* patches or %%autosetup sometimes doesn't work right -- rex
BuildArch: noarch

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel

# icon optimizations
BuildRequires: hardlink
# for optimizegraphics
#BuildRequires: kde-dev-scripts
BuildRequires: time
# for generate-24px-versions.py
BuildRequires: python3-lxml

# inheritance, though could consider Recommends: if needed -- rex
Requires: hicolor-icon-theme

# Needed for proper Fedora logo
Requires: system-logos

# upstream name
Provides:       breeze-icons = %{version}-%{release}
Provides:       kf6-breeze-icons = %{version}-%{release}
Replaces:       breeze-icon-theme

%description
%{summary}.

%package rcc
Summary: breeze Qt resource files
# when split out
#Conflicts: breeze-icon-theme < 5.33.0-2
Requires: %{name} = %{version}-%{release}
%description rcc
%{summary}.

%package     devel
Summary:     Breeze icon theme development files
Requires:    %{name} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%forgeautosetup -n %{framework}-%{version} -p1

# Fix FTI for -devel package
sed -e 's|\${KDE_INSTALL_CMAKEPACKAGEDIR}|%{_datadir}/cmake|g' -i CMakeLists.txt


%build
%cmake_kf6 -DBINARY_ICONS_RESOURCE=ON
%cmake_build


%install
%cmake_install

# Do not use Fedora logo from upstream
rm -rf %{buildroot}%{_datadir}/icons/breeze-dark/apps/48/org.fedoraproject.AnacondaInstaller.svg
rm -rf %{buildroot}%{_datadir}/icons/breeze/apps/48/org.fedoraproject.AnacondaInstaller.svg
# Use copy found in fedora-logos
pushd %{buildroot}%{_datadir}/icons/breeze-dark/apps/48/
ln -s ../../../hicolor/48x48/apps/org.fedoraproject.AnacondaInstaller.svg org.fedoraproject.AnacondaInstaller.svg
popd
pushd %{buildroot}%{_datadir}/icons/breeze/apps/48/
ln -s ../../../hicolor/48x48/apps/org.fedoraproject.AnacondaInstaller.svg org.fedoraproject.AnacondaInstaller.svg
popd

## icon optimizations
# Note: we don't do optimizegraphics because breeze is exclusively SVG
#du -s  .
#time optimizegraphics ||:
du -s .
hardlink -c -v %{buildroot}%{_datadir}/icons/
du -s .

# %%ghost icon.cache
touch  %{buildroot}%{_kf6_datadir}/icons/{breeze,breeze-dark}/icon-theme.cache


## trigger-based scriptlets
%transfiletriggerin -- %{_datadir}/icons/breeze
gtk-update-icon-cache --force %{_datadir}/icons/breeze &>/dev/null || :

%transfiletriggerin -- %{_datadir}/icons/breeze-dark
gtk-update-icon-cache --force %{_datadir}/icons/breeze-dark &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/breeze
gtk-update-icon-cache --force %{_datadir}/icons/breeze &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/breeze-dark
gtk-update-icon-cache --force %{_datadir}/icons/breeze-dark &>/dev/null || :


%files
%license COPYING-ICONS
%doc README.md
%ghost %{_datadir}/icons/breeze/icon-theme.cache
%ghost %{_datadir}/icons/breeze-dark/icon-theme.cache
%{_datadir}/icons/breeze/
%{_datadir}/icons/breeze-dark/
%exclude %{_datadir}/icons/breeze/breeze-icons.rcc
%exclude %{_datadir}/icons/breeze-dark/breeze-icons-dark.rcc

%files devel
%{_datadir}/cmake/KF6BreezeIcons/

%files rcc
%{_datadir}/icons/breeze/breeze-icons.rcc
%{_datadir}/icons/breeze-dark/breeze-icons-dark.rcc


%changelog
%autochangelog
