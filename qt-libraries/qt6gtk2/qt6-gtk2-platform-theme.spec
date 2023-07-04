%global _basename qt6gtk2

%global commit 2a21a8ad59a76e6928fae1699c830ca24fb2461c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20220520

Name:     qt6-gtk2-platform-theme
Version:  0.2%{?date:^git%{date}.%{shortcommit}}
Release:  1%{?dist}
Summary:  GTK+2.0 integration plugins for Qt6
License:  GPLv3
URL:      https://github.com/trialuser02/%{_basename}

%if 0%{?date}
Source0: %{url}/archive/%{commit}/%{_basename}-%{commit}.tar.gz
%else
Source0: %{url}/archive/v%{version}/%{_basename}-%{version}.tar.gz
%endif

BuildRequires: make

BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtbase-private-devel
BuildRequires: qt6-qtbase-static

BuildRequires: gtk2-devel
BuildRequires: libX11-devel

%description
Qt6Gtk2 - GTK+2.0 integration plugins for Qt6

%prep
%setup -qn %{_basename}-%{commit}

%build
%qmake_qt6 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_qt6_plugindir}/platformthemes/libqt6gtk2.so
%{_qt6_plugindir}/styles/libqt6gtk2-style.so

%changelog
* Sat May 6 2023 Dipta Biswas <dabiswas112@gmail.com> 0.0^git20220520
- Initial Package.
