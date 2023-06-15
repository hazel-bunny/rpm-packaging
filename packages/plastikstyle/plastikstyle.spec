%define git 1

%global _basename PlastikStyle

%global commit 15db58b0c85663f2d3d43a531c0f865234e5f9bf
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20230615

Name:     plastikstyle
%if ! 0%{?git}
Version:  1.0.1
%else
Version:  1.0.1%{?date:^git%{date}.%{shortcommit}}
%endif
Release:  1%{?dist}
URL:      https://github.com/MartinF99/%{_basename}
Summary:  Fork of QPlastiqueStyle from qt5-styleplugins

%if ! 0%{?git}
Source0: %{url}/archive/v%{version}/%{_basename}-%{version}.tar.gz
%else
Source0: %{url}/archive/%{commit}/%{_basename}-%{commit}.tar.gz
%endif

BuildRequires: cmake

#Qt5
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Gui)
BuildRequires: qt5-rpm-macros

#Qt6
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Gui)
BuildRequires: qt6-rpm-macros

%description
Plastik style - This is a fork of QPlastiqueStyle from qt5-styleplugins and a port to qt6.
a port of the Plastik style, used by default for KDE3.4 and KDE3.5

%package -n     qt5-style-plastik
Summary:        Plastik widget style for Qt 5
%description -n qt5-style-plastik
%{summary}.

%package -n     qt6-style-plastik
Summary:        Plastik widget style for Qt 6
%description -n qt6-style-plastik
%{summary}.

%prep
%setup -qn %{_basename}-%{commit}

%build
%cmake -DENABLE_ALL=on
%cmake_build

%install
%cmake_install

%files -n qt5-style-plastik
%{_qt5_plugindir}/styles/libplastikstyle5.so

%files -n qt6-style-plastik
%{_qt6_plugindir}/styles/libplastikstyle6.so

%changelog
* Thu Jun 15 2023 Dipta Biswas <dabiswas112@gmail.com> 1.0.1^git20230615
- Bump to version 1.0.1

* Fri May 5 2023 Dipta Biswas <dabiswas112@gmail.com> 0.0^git20230317
- Initial Package.