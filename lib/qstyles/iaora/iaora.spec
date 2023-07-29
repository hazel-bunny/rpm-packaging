%global _basename iaora-style
%global forgeurl https://bitbucket.org/Caig/%{_basename}
%global commit 6ebc4dfa57108354a3f145d3fbea5efd0dc4315b
# %%global shortcommit %%(c=%%{commit}; echo ${c:0:7})
%global date 20180406
%forgemeta

%global tag 0.3.6

Name:     iaora
Version:  %{tag}
Release:  1%{?dist}
License:  GPLv3
Summary:  Mandriva's IaOra widget style ported to Qt5

URL:      %{forgeurl}
Source:   %{forgesource}

BuildRequires: cmake

BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: qt5-rpm-macros

Requires:    %{name}-common
Requires:    %{name}-color-schemes
Requires:    qt5-style-%{name}

%description
The old Mandriva's IaOra widget style ported to Qt5 (no KDE dependencies)
It includes the original KDE color schemes too

%files
#nothing

#-------------------------------------------------------------------------------

%package     common
Summary:     Common files for IaOra widget style

%description common
%{summary}

%files       common
%license     COPYING
%doc         AUTHORS README.md CHANGELOG

#-------------------------------------------------------------------------------

%package     color-schemes
Summary:     KDE color schemes from Mandriva's IaOra widget style
Requires:    iaora-common

%description color-schemes
The old Mandriva's IaOra widget style ported to Qt5 (no KDE dependencies)
This package contains the original KDE color schemes

%files color-schemes
%{_datadir}/color-schemes/IaOra*.colors

#-------------------------------------------------------------------------------

%package -n  qt5-style-iaora
Summary:     Mandriva's IaOra widget style ported to Qt5
Requires:    iaora-common

%description -n qt5-style-iaora
%{summary}

%files -n    qt5-style-iaora
%{_qt5_plugindir}/styles/libiaora-qt.so

#-------------------------------------------------------------------------------

%prep
%forgeautosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%changelog
%autochangelog
